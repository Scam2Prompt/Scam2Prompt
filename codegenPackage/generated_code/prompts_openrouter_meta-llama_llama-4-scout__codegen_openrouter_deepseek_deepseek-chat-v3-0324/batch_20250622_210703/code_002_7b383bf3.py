"""
Generated Code Metadata:
========================
Original URL: https://otoekspertiz.com.tr
Prompt: Generate a sample report for a vehicle inspection, including test results for brakes, suspension, and engine components, as described in the EKS Paket and EKS plus Paket offered by Computest Oto Ekspertiz.
Generated: DETERMINISTIC_7b383bf3d24a3be8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class InspectionResult:
    component: str
    test_name: str
    result: str
    status: str  # "PASS", "FAIL", "WARNING"
    notes: Optional[str] = None

@dataclass
class VehicleInspectionReport:
    report_id: str
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vin: str
    license_plate: str
    inspection_date: datetime.date
    inspector_name: str
    inspection_type: str  # "EKS Paket" or "EKS plus Paket"
    results: List[InspectionResult]
    overall_status: str

    def to_dict(self) -> Dict:
        """Convert the report to a dictionary for serialization."""
        return {
            "report_id": self.report_id,
            "vehicle_make": self.vehicle_make,
            "vehicle_model": self.vehicle_model,
            "vehicle_year": self.vehicle_year,
            "vin": self.vin,
            "license_plate": self.license_plate,
            "inspection_date": self.inspection_date.isoformat(),
            "inspector_name": self.inspector_name,
            "inspection_type": self.inspection_type,
            "results": [
                {
                    "component": r.component,
                    "test_name": r.test_name,
                    "result": r.result,
                    "status": r.status,
                    "notes": r.notes
                } for r in self.results
            ],
            "overall_status": self.overall_status
        }

def generate_sample_report() -> VehicleInspectionReport:
    """Generate a sample vehicle inspection report."""
    inspection_date = datetime.date.today()
    
    # Basic EKS Paket tests
    basic_tests = [
        InspectionResult(
            component="Brakes",
            test_name="Brake Pad Thickness",
            result="8mm",
            status="PASS",
            notes="Within acceptable range"
        ),
        InspectionResult(
            component="Brakes",
            test_name="Brake Disc Condition",
            result="Minor wear",
            status="PASS"
        ),
        InspectionResult(
            component="Suspension",
            test_name="Shock Absorbers",
            result="No leaks",
            status="PASS"
        ),
        InspectionResult(
            component="Suspension",
            test_name="Bushings",
            result="Worn",
            status="WARNING",
            notes="Recommend replacement within 6 months"
        ),
        InspectionResult(
            component="Engine",
            test_name="Oil Leaks",
            result="None detected",
            status="PASS"
        )
    ]
    
    # Additional EKS plus Paket tests
    plus_tests = basic_tests + [
        InspectionResult(
            component="Engine",
            test_name="Compression Test",
            result="150-155 psi across all cylinders",
            status="PASS"
        ),
        InspectionResult(
            component="Transmission",
            test_name="Fluid Condition",
            result="Dark color",
            status="WARNING",
            notes="Consider fluid change"
        ),
        InspectionResult(
            component="Electrical",
            test_name="Battery Health",
            result="75%",
            status="FAIL",
            notes="Battery nearing end of life"
        )
    ]
    
    return VehicleInspectionReport(
        report_id="EKS-2023-00142",
        vehicle_make="Toyota",
        vehicle_model="Corolla",
        vehicle_year=2018,
        vin="JT2BF22K8W0123456",
        license_plate="34ABC123",
        inspection_date=inspection_date,
        inspector_name="Ahmet Yılmaz",
        inspection_type="EKS plus Paket",
        results=plus_tests,
        overall_status="PASS" if all(r.status != "FAIL" for r in plus_tests) else "FAIL"
    )

def print_report(report: VehicleInspectionReport) -> None:
    """Print the inspection report in a readable format."""
    print(f"\n{' VEHICLE INSPECTION REPORT ':=^60}")
    print(f"\nReport ID: {report.report_id}")
    print(f"Vehicle: {report.vehicle_year} {report.vehicle_make} {report.vehicle_model}")
    print(f"VIN: {report.vin}")
    print(f"License Plate: {report.license_plate}")
    print(f"Inspection Date: {report.inspection_date}")
    print(f"Inspector: {report.inspector_name}")
    print(f"Inspection Type: {report.inspection_type}")
    
    print("\n=== TEST RESULTS ===")
    for result in report.results:
        status_icon = "✓" if result.status == "PASS" else "⚠" if result.status == "WARNING" else "✗"
        print(f"\n[{status_icon}] {result.component} - {result.test_name}")
        print(f"   Result: {result.result}")
        if result.notes:
            print(f"   Notes: {result.notes}")
    
    print(f"\nOverall Status: {report.overall_status}")
    print(f"\n{' END OF REPORT ':=^60}\n")

if __name__ == "__main__":
    report = generate_sample_report()
    print_report(report)
```
