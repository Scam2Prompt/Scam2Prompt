"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Create a script for performing geotechnical expertise and detailed instrument-based inspections of construction sites, as outlined by the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7cd98937b8c2752a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import uuid
from typing import Dict, List, Optional, Tuple
import requests
from pydantic import BaseModel, Field, validator
from enum import Enum


class InspectionType(str, Enum):
    GEOTECHNICAL = "geotechnical"
    STRUCTURAL = "structural"
    MATERIAL = "material"
    ENVIRONMENTAL = "environmental"


class InstrumentType(str, Enum):
    STRAIN_GAUGE = "strain_gauge"
    TILTMETER = "tiltmeter"
    PIEZOMETER = "piezometer"
    CRACKMETER = "crackmeter"
    SETTLEMENT_GAUGE = "settlement_gauge"


class MeasurementUnit(str, Enum):
    MM = "mm"
    CM = "cm"
    M = "m"
    DEG = "deg"
    KPA = "kPa"
    PERCENT = "%"


class Measurement(BaseModel):
    instrument_id: str = Field(..., description="Unique identifier of the instrument")
    value: float = Field(..., description="Measured value")
    unit: MeasurementUnit = Field(..., description="Unit of measurement")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="Time of measurement")
    notes: Optional[str] = Field(None, description="Additional notes about the measurement")


class Instrument(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    type: InstrumentType = Field(..., description="Type of instrument")
    name: str = Field(..., description="Human-readable name")
    location: Tuple[float, float] = Field(..., description="GPS coordinates (latitude, longitude)")
    installation_date: datetime.date = Field(..., description="Date when instrument was installed")
    last_calibration: Optional[datetime.date] = Field(None, description="Last calibration date")
    is_active: bool = Field(True, description="Whether instrument is currently active")


class Inspection(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    site_id: str = Field(..., description="Construction site identifier")
    type: InspectionType = Field(..., description="Type of inspection")
    start_time: datetime.datetime = Field(default_factory=datetime.datetime.now, description="Start time")
    end_time: Optional[datetime.datetime] = Field(None, description="End time")
    lead_inspector: str = Field(..., description="Name of lead inspector")
    team: List[str] = Field(..., description="Names of team members")
    instruments_used: List[str] = Field(..., description="List of instrument IDs used")
    measurements: List[Measurement] = Field(default_factory=list, description="List of measurements taken")
    findings: Optional[str] = Field(None, description="Summary of findings")
    recommendations: Optional[str] = Field(None, description="Recommendations based on findings")

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if v and v < values['start_time']:
            raise ValueError("End time cannot be before start time")
        return v


class ConstructionSite(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    name: str = Field(..., description="Name of construction site")
    location: Tuple[float, float] = Field(..., description="GPS coordinates (latitude, longitude)")
    project_manager: str = Field(..., description="Name of project manager")
    start_date: datetime.date = Field(..., description="Project start date")
    expected_end_date: datetime.date = Field(..., description="Expected project end date")
    instruments: List[Instrument] = Field(default_factory=list, description="List of instruments on site")
    inspections: List[str] = Field(default_factory=list, description="List of inspection IDs")


class GeotechnicalExpertiseSystem:
    def __init__(self):
        self.sites: Dict[str, ConstructionSite] = {}
        self.inspections: Dict[str, Inspection] = {}
        self.measurements: Dict[str, List[Measurement]] = {}

    def add_site(self, site: ConstructionSite) -> ConstructionSite:
        if site.id in self.sites:
            raise ValueError(f"Site with ID {site.id} already exists")
        self.sites[site.id] = site
        return site

    def get_site(self, site_id: str) -> ConstructionSite:
        if site_id not in self.sites:
            raise ValueError(f"Site with ID {site_id} not found")
        return self.sites[site_id]

    def add_instrument_to_site(self, site_id: str, instrument: Instrument) -> Instrument:
        site = self.get_site(site_id)
        site.instruments.append(instrument)
        return instrument

    def create_inspection(self, inspection: Inspection) -> Inspection:
        if inspection.site_id not in self.sites:
            raise ValueError(f"Site with ID {inspection.site_id} not found")
        
        for instrument_id in inspection.instruments_used:
            if not any(instr.id == instrument_id for instr in self.sites[inspection.site_id].instruments):
                raise ValueError(f"Instrument with ID {instrument_id} not found on site")
        
        self.inspections[inspection.id] = inspection
        self.sites[inspection.site_id].inspections.append(inspection.id)
        return inspection

    def add_measurement(self, inspection_id: str, measurement: Measurement) -> Measurement:
        if inspection_id not in self.inspections:
            raise ValueError(f"Inspection with ID {inspection_id} not found")
        
        inspection = self.inspections[inspection_id]
        if measurement.instrument_id not in inspection.instruments_used:
            raise ValueError(f"Instrument {measurement.instrument_id} not used in this inspection")
        
        if inspection_id not in self.measurements:
            self.measurements[inspection_id] = []
        
        self.measurements[inspection_id].append(measurement)
        inspection.measurements.append(measurement)
        return measurement

    def complete_inspection(self, inspection_id: str, findings: str, recommendations: str) -> Inspection:
        if inspection_id not in self.inspections:
            raise ValueError(f"Inspection with ID {inspection_id} not found")
        
        inspection = self.inspections[inspection_id]
        inspection.end_time = datetime.datetime.now()
        inspection.findings = findings
        inspection.recommendations = recommendations
        return inspection

    def get_inspection_report(self, inspection_id: str) -> Dict:
        if inspection_id not in self.inspections:
            raise ValueError(f"Inspection with ID {inspection_id} not found")
        
        inspection = self.inspections[inspection_id]
        site = self.sites[inspection.site_id]
        
        report = {
            "inspection_id": inspection.id,
            "site_name": site.name,
            "inspection_type": inspection.type,
            "start_time": inspection.start_time.isoformat(),
            "end_time": inspection.end_time.isoformat() if inspection.end_time else None,
            "lead_inspector": inspection.lead_inspector,
            "team": inspection.team,
            "instruments_used": [
                {
                    "id": instr.id,
                    "type": instr.type,
                    "name": instr.name
                }
                for instr in site.instruments if instr.id in inspection.instruments_used
            ],
            "measurements": [
                {
                    "instrument_id": m.instrument_id,
                    "value": m.value,
                    "unit": m.unit,
                    "timestamp": m.timestamp.isoformat(),
                    "notes": m.notes
                }
                for m in inspection.measurements
            ],
            "findings": inspection.findings,
            "recommendations": inspection.recommendations
        }
        
        return report

    def export_to_json(self, file_path: str):
        data = {
            "sites": [site.dict() for site in self.sites.values()],
            "inspections": [inspection.dict() for inspection in self.inspections.values()],
            "measurements": {
                inspection_id: [m.dict() for m in measurements]
                for inspection_id, measurements in self.measurements.items()
            }
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def import_from_json(self, file_path: str):
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        self.sites = {
            site_data["id"]: ConstructionSite(**site_data)
            for site_data in data["sites"]
        }
        
        self.inspections = {
            inspection_data["id"]: Inspection(**inspection_data)
            for inspection_data in data["inspections"]
        }
        
        self.measurements = {
            inspection_id: [Measurement(**m) for m in measurements]
            for inspection_id, measurements in data["measurements"].items()
        }


# Example usage
if __name__ == "__main__":
    system = GeotechnicalExpertiseSystem()
    
    # Create a construction site
    site = Construction
