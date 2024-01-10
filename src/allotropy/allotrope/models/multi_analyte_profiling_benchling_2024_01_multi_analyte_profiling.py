# generated by datamodel-codegen:
#   filename:  multi-analyte-profiling.json
#   timestamp: 2024-01-09T19:16:56+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Union

from allotropy.allotrope.models.shared.components.plate_reader import (
    SampleRoleType,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueNumber,
    TQuantityValueUnitless,
    TRelativeFluorescenceUnit,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDateTimeStampValue,
    TQuantityValue,
    TStringValue,
)


@dataclass
class DeviceControlAggregateDocument:
    device_control_document: list[Any]


@dataclass
class Manifest:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: Optional[str] = None
    field_type: Optional[str] = None
    shapes: Optional[list[str]] = None


@dataclass
class Asm:
    field_asm_manifest: Optional[Union[str, Manifest]] = None


@dataclass
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: Optional[int] = None


@dataclass
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass
class DeviceDocumentItem:
    device_identifier: Optional[TStringValue] = None
    device_type: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    brand_name: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class ReferenceMaterialDocument:
    reference_material_identifier: Optional[TStringValue] = None
    batch_identifier: Optional[TStringValue] = None
    expiry_time_prescription: Optional[TDateTimeStampValue] = None


@dataclass
class CalibrationResultDocumentItem:
    calibration_result_name: Optional[TStringValue] = None
    calibration_result: Optional[TQuantityValueUnitless] = None


@dataclass
class CalibrationResultAggregateDocument:
    calibration_result_document: Optional[list[CalibrationResultDocumentItem]] = None


@dataclass
class CalibrationDocumentItem:
    calibration_name: Optional[TStringValue] = None
    calibration_description: Optional[TStringValue] = None
    calibration_time: Optional[TDateTimeStampValue] = None
    expiry_time_prescription: Optional[TDateTimeStampValue] = None
    calibration_report: Optional[TStringValue] = None
    reference_material_document: Optional[ReferenceMaterialDocument] = None
    calibration_result_aggregate_document: Optional[
        CalibrationResultAggregateDocument
    ] = None


@dataclass
class CalibrationAggregateDocument:
    calibration_document: Optional[list[CalibrationDocumentItem]] = None


@dataclass
class DeviceSystemDocument:
    asset_management_identifier: Optional[TStringValue] = None
    description: Optional[Any] = None
    brand_name: Optional[TStringValue] = None
    product_manufacturer: Optional[TStringValue] = None
    device_identifier: Optional[TStringValue] = None
    model_number: Optional[TStringValue] = None
    equipment_serial_number: Optional[TStringValue] = None
    firmware_version: Optional[TStringValue] = None
    device_document: Optional[list[DeviceDocumentItem]] = None
    calibration_aggregate_document: Optional[CalibrationAggregateDocument] = None


@dataclass
class DataSystemDocument:
    data_system_instance_identifier: Optional[TStringValue] = None
    file_name: Optional[TStringValue] = None
    UNC_path: Optional[TStringValue] = None
    software_name: Optional[TStringValue] = None
    software_version: Optional[TStringValue] = None
    ASM_converter_name: Optional[TStringValue] = None
    ASM_converter_version: Optional[TStringValue] = None


@dataclass
class SampleDocument:
    sample_identifier: TStringValue
    description: Optional[Any] = None
    batch_identifier: Optional[TStringValue] = None
    group_identifier: Optional[TStringValue] = None
    sample_role_type: Optional[SampleRoleType] = None
    written_name: Optional[TStringValue] = None
    location_identifier: Optional[TStringValue] = None
    well_plate_identifier: Optional[TStringValue] = None


@dataclass
class ErrorDocumentItem:
    error: TStringValue
    error_feature: Optional[TStringValue] = None


@dataclass
class ErrorAggregateDocument:
    error_document: Optional[list[ErrorDocumentItem]] = None


@dataclass
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: Optional[DataSourceAggregateDocument] = None
    calculated_data_identifier: Optional[TStringValue] = None
    calculation_description: Optional[TStringValue] = None
    field_index: Optional[int] = None


@dataclass
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass
class AnalyteDocumentItem:
    analyte_identifier: TStringValue
    analyte_name: TStringValue
    assay_bead_identifier: TStringValue
    assay_bead_count: TQuantityValueNumber
    fluorescence: TRelativeFluorescenceUnit


@dataclass
class AnalyteAggregateDocument:
    analyte_document: list[AnalyteDocumentItem]


@dataclass
class MeasurementDocumentItem:
    measurement_identifier: TStringValue
    measurement_time: TDateTimeStampValue
    sample_document: SampleDocument
    device_control_aggregate_document: DeviceControlAggregateDocument
    assay_bead_count: TQuantityValueNumber
    analyte_aggregate_document: AnalyteAggregateDocument
    error_aggregate_document: Optional[ErrorAggregateDocument] = None


@dataclass
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocumentItem]
    analytical_method_identifier: Optional[TStringValue] = None
    method_version: Optional[TStringValue] = None
    experimental_data_identifier: Optional[TStringValue] = None
    experiment_type: Optional[TStringValue] = None
    container_type: Optional[TStringValue] = None
    plate_well_count: Optional[TQuantityValueNumber] = None


@dataclass
class MultiAnalyteProfilingDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: Optional[TStringValue] = None
    submitter: Optional[TStringValue] = None


@dataclass
class MultiAnalyteProfilingAggregateDocument:
    device_system_document: DeviceSystemDocument
    multi_analyte_profiling_document: list[MultiAnalyteProfilingDocumentItem]
    data_system_document: Optional[DataSystemDocument] = None
    calculated_data_aggregate_document: Optional[CalculatedDataAggregateDocument] = None


@dataclass
class Model(Asm):
    field_asm_manifest: Union[str, Manifest]
    multi_analyte_profiling_aggregate_document: Optional[
        MultiAnalyteProfilingAggregateDocument
    ] = None
