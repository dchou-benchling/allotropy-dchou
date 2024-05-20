# generated by datamodel-codegen:
#   filename:  cell-counting.json
#   timestamp: 2024-05-18T16:59:31+00:00

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCell,
    TQuantityValueMicroliter,
    TQuantityValueMicrometer,
    TQuantityValueMillionCellsPerMilliliter,
    TQuantityValueMilliSecond,
    TQuantityValueNanometer,
    TQuantityValuePercent,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TClass,
    TDatacube,
    TDateTimeStampValue,
    TQuantityValue,
    TStringValue,
)


@dataclass
class DiagnosticTraceDocumentItem:
    description: Any


@dataclass
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None


@dataclass
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: int | None = None


@dataclass
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


class StatisticalFeature(Enum):
    inner_diameter = "inner diameter"
    plate_heater_temperature = "plate heater temperature"
    linear_velocity = "linear velocity"
    enthalpy_of_fusion = "enthalpy of fusion"
    angular_velocity = "angular velocity"
    purity = "purity"
    intensity = "intensity"
    protein_attenuation_coefficient = "protein attenuation coefficient"
    electron_beam_working_distance = "electron beam working distance"
    temperature = "temperature"
    end_height = "end height"
    relative_humidity = "relative humidity"
    saturation_vapor_pressure = "saturation vapor pressure"
    heat_flow = "heat flow"
    quality_quantification_facet = "quality quantification facet"
    heat_transfer_coefficient = "heat transfer coefficient"
    molar_concentration = "molar concentration"
    average_total_cell_diameter = "average total cell diameter"
    pH = "pH"
    foam_height = "foam height"
    relative_weight_loss_on_drying = "relative weight loss on drying"
    dilution_volume = "dilution volume"
    flow_ratio = "flow ratio"
    electric_conductance = "electric conductance"
    sample_temperature = "sample temperature"
    container_diameter = "container diameter"
    absorbance = "absorbance"
    sample_thickness = "sample thickness"
    humidity = "humidity"
    Raman_intensity = "Raman intensity"
    voltage = "voltage"
    actual_P_P0_result = "actual P/P0 result"
    polyol_reservoir_temperature = "polyol reservoir temperature"
    turbidity = "turbidity"
    enthalpy_of_sublimation = "enthalpy of sublimation"
    osmolality = "osmolality"
    ambient_humidity = "ambient humidity"
    molar_enthalpy_of_vaporization = "molar enthalpy of vaporization"
    total_foam_height = "total foam height"
    strain = "strain"
    thermal_conductivity = "thermal conductivity"
    coating_gap_height = "coating gap height"
    measurement_chamber_free_space_volume = "measurement chamber free space volume"
    fracture_energy = "fracture energy"
    heat_capacity = "heat capacity"
    yield_strain = "yield strain"
    incident_radiation_angle = "incident radiation angle"
    mass_fraction = "mass fraction"
    liquid_height = "liquid height"
    chromatography_column_length = "chromatography column length"
    sample_width = "sample width"
    molar_enthalpy_of_sublimation = "molar enthalpy of sublimation"
    Raman_wavenumber_shift = "Raman wavenumber shift"
    relative_response = "relative response"
    length = "length"
    velocity = "velocity"
    electric_charge = "electric charge"
    molar_mass = "molar mass"
    image_height = "image height"
    concentration = "concentration"
    sample_weight_before_drying = "sample weight before drying"
    dilution_factor = "dilution factor"
    temperature_rate = "temperature rate"
    relative_permittivity = "relative permittivity"
    transition_enthalpy = "transition enthalpy"
    total_gas_flow_rate = "total gas flow rate"
    gloss = "gloss"
    water_mass_fraction = "water mass fraction"
    dielectric_polarization = "dielectric polarization"
    normalized_foam_height = "normalized foam height"
    peak_onset_temperature = "peak onset temperature"
    electric_current = "electric current"
    angle = "angle"
    energy__datum_ = "energy (datum)"
    abrasion_weight = "abrasion weight"
    absolute_water_content = "absolute water content"
    electric_resistance = "electric resistance"
    attenuation_coefficient = "attenuation coefficient"
    molar_enthalpy_of_fusion = "molar enthalpy of fusion"
    water_mass_concentration = "water mass concentration"
    partial_pressure = "partial pressure"
    volume = "volume"
    position_count = "position count"
    thermal_conductance = "thermal conductance"
    dry_sample_weight = "dry sample weight"
    adsorbed_volume_at_STP = "adsorbed volume at STP"
    force = "force"
    birefringence = "birefringence"
    monolayer_quantity = "monolayer quantity"
    peak_temperature = "peak temperature"
    dry_gas_flow_rate = "dry gas flow rate"
    gross_weight = "gross weight"
    sample_weight = "sample weight"
    image_width = "image width"
    m_z = "m/z"
    container_height = "container height"
    flow_rate = "flow rate"
    solvent_reservoir_temperature = "solvent reservoir temperature"
    isocyanate_reservoir_temperature = "isocyanate reservoir temperature"
    ambient_pressure = "ambient pressure"
    eccentricity = "eccentricity"
    mass = "mass"
    molar_absorptivity = "molar absorptivity"
    height = "height"
    column_inner_diameter = "column inner diameter"
    heat_seal_length = "heat seal length"
    specific_surface_area = "specific surface area"
    reference_material_weight = "reference material weight"
    thickness = "thickness"
    tare_weight = "tare weight"
    power = "power"
    chromatography_column_particle_size = "chromatography column particle size"
    saturated_gas_flow_rate = "saturated gas flow rate"
    well_volume = "well volume"
    degassed_sample_weight = "degassed sample weight"
    voltage_range = "voltage range"
    relative_intensity = "relative intensity"
    width = "width"
    yield_stress = "yield stress"
    total_cell_diameter = "total cell diameter"
    stress = "stress"
    relative_pressure__BET_ = "relative pressure (BET)"
    break_stress = "break stress"
    mass_concentration = "mass concentration"
    chromatography_column_film_thickness = "chromatography column film thickness"
    average_particle_size = "average particle size"
    wavelength = "wavelength"
    heat_capacity__dsc_ = "heat capacity (dsc)"
    acquisition_volume = "acquisition volume"
    collision_energy = "collision energy"
    background_corrected_turbidity = "background corrected turbidity"
    mass_change = "mass change"
    chemical_shift = "chemical shift"
    titer = "titer"
    refractive_index = "refractive index"
    enthalpy_of_vaporization = "enthalpy of vaporization"
    volume_fraction = "volume fraction"
    transmittance = "transmittance"
    electric_conductivity = "electric conductivity"
    fill_depth = "fill depth"
    Young_modulus = "Young modulus"
    total_material_height = "total material height"
    specific_rotation = "specific rotation"
    qNMR_purity_result = "qNMR purity result"
    size__datum_ = "size (datum)"
    break_strain = "break strain"
    specific_enthalpy_of_vaporization = "specific enthalpy of vaporization"
    absolute_intensity = "absolute intensity"
    BET_C_constant = "BET C constant"
    plate_well_count = "plate well count"
    plate_temperature = "plate temperature"
    volume_concentration = "volume concentration"
    specific_enthalpy_of_sublimation = "specific enthalpy of sublimation"
    enthalpy = "enthalpy"
    area = "area"
    peak_load_force = "peak load force"
    fluorescence = "fluorescence"
    start_height = "start height"
    polarity = "polarity"
    angle_of_optical_rotation = "angle of optical rotation"
    peak_analyte_amount = "peak analyte amount"
    extrapolated_moisture_content = "extrapolated moisture content"
    inlet_gas_pressure = "inlet gas pressure"
    hardness = "hardness"
    molecular_mass = "molecular mass"
    specific_enthalpy_of_fusion = "specific enthalpy of fusion"
    electric_impedance = "electric impedance"
    hold_up_volume = "hold-up volume"
    particle_size = "particle size"
    diameter = "diameter"
    tablet_thickness = "tablet thickness"
    pressure = "pressure"
    weight_loss = "weight loss"
    cell_path_length = "cell path length"
    glass_transition_temperature = "glass transition temperature"
    specific_heat_capacity = "specific heat capacity"
    wavenumber = "wavenumber"
    reservoir_temperature = "reservoir temperature"
    electric_resistivity = "electric resistivity"
    luminescence = "luminescence"
    compartment_temperature = "compartment temperature"
    viscosity = "viscosity"
    exhaust_gas_flow_rate = "exhaust gas flow rate"
    Raman_interferogram_intensity = "Raman interferogram intensity"
    ambient_temperature = "ambient temperature"
    reflectance = "reflectance"
    detector_view_volume = "detector view volume"
    stirring_rate = "stirring rate"


@dataclass
class StatisticsDocumentItem:
    statistical_feature: StatisticalFeature


@dataclass
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    batch_identifier: TStringValue | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None


@dataclass
class Manifest:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    field_index: int | None = None


@dataclass
class DeviceSystemDocument:
    asset_management_identifier: TStringValue | None = None
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None


@dataclass
class DataSystemDocument:
    data_system_instance_identifier: TStringValue | None = None
    file_name: TStringValue | None = None
    UNC_path: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None


@dataclass
class DataProcessingDocument:
    cell_type_processing_method: TStringValue | None = None
    cell_density_dilution_factor: TQuantityValueUnitless | None = None
    minimum_cell_diameter_setting: TQuantityValueMicrometer | None = None
    maximum_cell_diameter_setting: TQuantityValueMicrometer | None = None


@dataclass
class ProcessedDataDocumentItem1:
    fluorescent_tag_positive_cell_count: TQuantityValueCell
    data_processing_document: DataProcessingDocument | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    processed_data_identifier: TStringValue | None = None
    fluorescent_tag_positive_cell_density: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    fluorescent_tag_positive_percentage: TQuantityValuePercent | None = None
    field_index: int | None = None


@dataclass
class ProcessedDataAggregateDocument2:
    processed_data_document: list[ProcessedDataDocumentItem1]


@dataclass
class ProcessedDataDocumentItem2:
    data_processing_document: dict[str, Any] | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None


@dataclass
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem2]


@dataclass
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    field_index: int | None = None


@dataclass
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    detection_type: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    model_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    sample_volume_setting: TQuantityValueMicroliter | None = None
    illumination_setting: TQuantityValuePercent | None = None
    exposure_duration_setting: TQuantityValueMilliSecond | None = None
    detector_gain_setting: TQuantityValueUnitless | None = None
    excitation_wavelength_setting: TQuantityValueNanometer | None = None
    detector_wavelength_setting: TQuantityValueNanometer | None = None


@dataclass
class DeviceControlDocumentItemModel(DeviceControlDocumentItem):
    field_index: int | None = None


@dataclass
class CellCountingDetectorDeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItemModel] | None = None


@dataclass
class FluorescenceCellCountingDeviceControlDocumentItem(DeviceControlDocumentItem):
    detector_bandwidth_setting: TQuantityValueNanometer | None = None
    wavelength_filter_cutoff_setting: TQuantityValueNanometer | None = None
    excitation_bandwidth_setting: TQuantityValueNanometer | None = None
    fluorescent_tag_setting: TStringValue | None = None
    field_index: int | None = None


FluorescenceCellCountingDeviceControlDocument = list[
    FluorescenceCellCountingDeviceControlDocumentItem
]


@dataclass
class FluorescenceCellCountingDeviceControlAggregateDocument:
    device_control_document: FluorescenceCellCountingDeviceControlDocument | None = None


@dataclass
class FluorescenceCellCountingMeasurementDocumentItem:
    measurement_time: TDateTimeStampValue
    measurement_identifier: TStringValue
    device_control_aggregate_document: FluorescenceCellCountingDeviceControlAggregateDocument
    sample_document: SampleDocument
    processed_data_aggregate_document: ProcessedDataAggregateDocument2
    detection_type: TStringValue | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass
class ProcessedDataDocumentItem:
    viability__cell_counter_: TQuantityValuePercent
    viable_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter
    data_processing_document: DataProcessingDocument | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    processed_data_identifier: TStringValue | None = None
    total_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    dead_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    average_total_cell_diameter: TQuantityValueMicrometer | None = None
    average_live_cell_diameter__cell_counter_: TQuantityValueMicrometer | None = None
    average_dead_cell_diameter__cell_counter_: TQuantityValueMicrometer | None = None
    total_cell_diameter_distribution: TDatacube | None = None
    total_cell_count: TQuantityValueCell | None = None
    viable_cell_count: TQuantityValueCell | None = None
    dead_cell_count: TQuantityValueCell | None = None
    average_total_cell_circularity: TQuantityValueUnitless | None = None
    average_viable_cell_circularity: TQuantityValueUnitless | None = None
    field_index: int | None = None


@dataclass
class ProcessedDataAggregateDocument1:
    processed_data_document: list[ProcessedDataDocumentItem]


@dataclass
class CellCountingDetectorMeasurementDocumentItem:
    measurement_time: TDateTimeStampValue
    measurement_identifier: TStringValue
    device_control_aggregate_document: CellCountingDetectorDeviceControlAggregateDocument
    sample_document: SampleDocument
    processed_data_aggregate_document: ProcessedDataAggregateDocument1
    detection_type: TStringValue | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass
class MeasurementAggregateDocument:
    measurement_document: list[
        CellCountingDetectorMeasurementDocumentItem
        | FluorescenceCellCountingMeasurementDocumentItem
    ]
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass
class CellCountingDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    submitter: TStringValue | None = None


@dataclass
class CellCountingAggregateDocument:
    cell_counting_document: list[CellCountingDocumentItem]
    device_system_document: DeviceSystemDocument | None = None
    data_system_document: DataSystemDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass
class Model:
    field_asm_manifest: Manifest | str
    cell_counting_aggregate_document: CellCountingAggregateDocument | None = None
