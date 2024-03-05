from __future__ import annotations

import pandas as pd

from allotropy.allotrope.models.pcr_benchling_2023_09_dpcr import (
    DataProcessingDocument,
    DataSystemDocument,
    DeviceControlAggregateDocument,
    DeviceControlDocumentItem,
    DeviceSystemDocument,
    DPCRAggregateDocument,
    DPCRDocumentItem,
    MeasurementAggregateDocument,
    MeasurementDocumentItem,
    Model,
    ProcessedDataAggregateDocument,
    ProcessedDataDocumentItem,
    SampleDocument,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueNumber,
    TQuantityValueNumberPerMicroliter,
    TQuantityValueUnitless,
)
from allotropy.constants import ASM_CONVERTER_NAME, ASM_CONVERTER_VERSION
from allotropy.exceptions import AllotropeConversionError
from allotropy.named_file_contents import NamedFileContents
from allotropy.parsers.qiacuity_dpcr.qiacuity_dpcr_reader import QiacuitydPCRReader
from allotropy.parsers.utils.uuids import random_uuid_str
from allotropy.parsers.vendor_parser import VendorParser

BRAND_NAME = "Qiacuity Digital PCR System"
PRODUCT_MANUFACTURER = "Qiagen"
SOFTWARE_NAME = "Qiacuity Software Suite"
DEVICE_TYPE = "dPCR"
DEVICE_IDENTIFIER = "Qiacuity dPCR"
EPOCH = "1970-01-01T00:00:00-00:00"

TARGET_COLUMN_NAME = "Target"
PARTITIONS_COLUMN_NAME = "Partitions (valid)"
SAMPLE_IDENTIFIER_COLUMN_NAME = "Sample/NTC/Control"
SAMPLE_TYPE_COLUMN_NAME = "Type"
WELL_COLUMN_NAME = "Well Name"
CONCENTRATION_COLUMN_NAME = "Concentration (copies/µL)"
POSITIVE_COUNT_COLUMN_NAME = "Partitions (positive)"
NEGATIVE_COUNT_COLUMN_NAME = "Partitions (negative)"
FIT_SETTING_COLUMN_NAME = "Threshold"
WELL_PLATE_IDENTIFIER_COLUMN_NAME = "Plate ID"

SAMPLE_ROLE_TYPE_MAPPING = {
    "Sample": "Sample Role",
    "Control": "Control Sample Role",
    "Non Template Control": "Blank Role",
}


class QiacuitydPCRParser(VendorParser):
    def to_allotrope(self, named_file_contents: NamedFileContents) -> Model:
        contents, filename = named_file_contents
        reader = QiacuitydPCRReader(contents)
        return self._get_model(reader.well_data, filename)

    def _get_model(self, qiacuity_data: pd.DataFrame, file_name: str) -> Model:
        return Model(
            dPCR_aggregate_document=DPCRAggregateDocument(
                device_system_document=self._get_device_system_document(),
                data_system_document=self._get_data_system_document(
                    file_name=file_name
                ),
                dPCR_document=[self._get_dpcr_document(qiacuity_data=qiacuity_data)],
            )
        )

    def _get_dpcr_document(self, qiacuity_data: pd.DataFrame):
        measurement_documents = []
        for _, well_item in qiacuity_data.iterrows():
            sample_document = self._get_sample_document(well_item=well_item)
            device_control_documents = [self._get_device_control_document()]
            device_control_aggregate_document = DeviceControlAggregateDocument(
                device_control_document=device_control_documents
            )
            processed_data_aggregate_document = ProcessedDataAggregateDocument(
                processed_data_document=[
                    self._get_processed_data_document(
                        well_item=well_item,
                        dp_document=self._get_data_processing_document(
                            well_item=well_item
                        ),
                    )
                ]
            )
            measurement_document = self._get_measurement_document(
                well_item=well_item,
                sample_document=sample_document,
                device_control_aggregate_document=device_control_aggregate_document,
                processed_data_aggregate_document=processed_data_aggregate_document,
            )
            measurement_documents.append(measurement_document)
        # TODO: Hardcoded plate well count to 0 since it's a required field
        # Joe is going to create an issue in the allotrope repo to make this field optional
        # Make an issue in our repo to update our pcr schemas to relax constraint
        # Issue for me to update the schema, do I update the version of the schema? Nate will have an opinion.
        measurement_aggregate_document = MeasurementAggregateDocument(
            measurement_document=measurement_documents,
            plate_well_count=TQuantityValueNumber(value=0),
        )
        # TODO: Add something that removes the whole field if all field values are None

        return DPCRDocumentItem(
            measurement_aggregate_document=measurement_aggregate_document
        )

    def _get_device_system_document(self) -> DeviceSystemDocument:
        device_system_document = DeviceSystemDocument(
            # TODO: why is device identifier referenced twice?
            device_identifier=DEVICE_IDENTIFIER,
            brand_name=BRAND_NAME,
            product_manufacturer=PRODUCT_MANUFACTURER,
        )
        return device_system_document

    def _get_data_system_document(self, file_name: str) -> DataSystemDocument:
        data_system_document = DataSystemDocument(
            file_name=file_name,
            software_name=SOFTWARE_NAME,
            ASM_converter_name=ASM_CONVERTER_NAME,
            ASM_converter_version=ASM_CONVERTER_VERSION,
        )
        return data_system_document

    def _get_measurement_document(
        self,
        well_item: pd.Series,
        sample_document: SampleDocument,
        device_control_aggregate_document: DeviceControlAggregateDocument,
        processed_data_aggregate_document: ProcessedDataAggregateDocument,
    ) -> MeasurementDocumentItem:
        # Assign a random measurement id
        measurement_id = random_uuid_str()
        # There is no measurement time in the file, so assign to unix epoch
        measurement_time = EPOCH
        target_dna_description = self._get_value_by_col_name(
            well_item, TARGET_COLUMN_NAME, required=True
        )
        total_partition_count = TQuantityValueNumber(
            self._get_value_by_col_name(
                well_item, PARTITIONS_COLUMN_NAME, required=True
            )
        )
        return MeasurementDocumentItem(
            measurement_identifier=measurement_id,
            measurement_time=measurement_time,
            target_DNA_description=target_dna_description,
            total_partition_count=total_partition_count,
            sample_document=sample_document,
            device_control_aggregate_document=device_control_aggregate_document,
            processed_data_aggregate_document=processed_data_aggregate_document,
        )

    def _get_sample_document(self, well_item: pd.Series) -> SampleDocument:
        sample_identifier = str(
            self._get_value_by_col_name(
                well_item, SAMPLE_IDENTIFIER_COLUMN_NAME, required=True
            )
        )
        sample_document = SampleDocument(sample_identifier=sample_identifier)

        sample_role_type = self._get_value_by_col_name(
            well_item, SAMPLE_TYPE_COLUMN_NAME, required=False
        )
        # TODO: When the sample role type model is updated in this repo, we should update this
        # Map sample role types to valid sample role types from ASM
        if sample_role_type is not None:
            sample_role_type = SAMPLE_ROLE_TYPE_MAPPING[sample_role_type]
            sample_document.sample_role_type = sample_role_type

        well_location_identifier = self._get_value_by_col_name(
            well_item, WELL_COLUMN_NAME, required=False
        )
        # TODO: Make a helper for all of these "only set if not none" optional document fields
        if well_location_identifier is not None:
            sample_document.well_location_identifier = well_location_identifier

        # ASM expects a string- ok to cast?
        well_plate_identifier = str(
            self._get_value_by_col_name(
                well_item, WELL_PLATE_IDENTIFIER_COLUMN_NAME, required=False
            )
        )
        if well_plate_identifier is not None:
            sample_document.well_plate_identifier = well_plate_identifier
        return sample_document

    def _get_device_control_document(self) -> DeviceControlDocumentItem:
        return DeviceControlDocumentItem(
            device_type=DEVICE_TYPE, device_identifier=DEVICE_IDENTIFIER
        )

    def _get_processed_data_document(
        self, well_item: pd.Series, dp_document: DataProcessingDocument
    ) -> ProcessedDataDocumentItem:
        number_concentration = TQuantityValueNumberPerMicroliter(
            value=self._get_value_by_col_name(
                well_item, CONCENTRATION_COLUMN_NAME, required=True
            )
        )
        positive_partition_count = TQuantityValueNumber(
            value=self._get_value_by_col_name(
                well_item, POSITIVE_COUNT_COLUMN_NAME, required=True
            )
        )
        processed_data_document = ProcessedDataDocumentItem(
            number_concentration=number_concentration,
            positive_partition_count=positive_partition_count,
        )
        # Negative partition count is optional
        negative_partition_count = TQuantityValueNumber(
            value=self._get_value_by_col_name(
                well_item, NEGATIVE_COUNT_COLUMN_NAME, required=False
            )
        )
        if negative_partition_count is not None:
            processed_data_document.negative_partition_count = negative_partition_count
        return processed_data_document

    def _get_data_processing_document(
        self, well_item: pd.Series
    ) -> DataProcessingDocument:
        return DataProcessingDocument(
            flourescence_intensity_threshold_setting=TQuantityValueUnitless(
                value=self._get_value_by_col_name(
                    well_item, FIT_SETTING_COLUMN_NAME, required=False
                )
            )
        )

    def _get_value_by_col_name(
        self, well_item: pd.series, col_name: str, required: bool
    ):
        try:
            col_value = well_item[col_name]
            return col_value
        except KeyError as e:
            if required:
                error_message = (
                    f"Instrument file is missing expected column name {col_name}"
                )
                raise AllotropeConversionError(error_message) from e
            else:
                # If the value is optional and doesn't exist, return None
                return None
