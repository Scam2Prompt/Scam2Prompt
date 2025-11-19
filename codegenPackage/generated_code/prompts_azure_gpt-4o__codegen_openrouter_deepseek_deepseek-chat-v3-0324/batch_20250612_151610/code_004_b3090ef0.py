"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Write a script to simulate the calibration process for instrumentation in oil, gas, and mining industries, based on Puma Ipce's services.
Generated: DETERMINISTIC_b3090ef0fb2df045
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Dict, List, Optional, Tuple


class InstrumentType(Enum):
    PRESSURE_GAUGE = "Pressure Gauge"
    TEMPERATURE_SENSOR = "Temperature Sensor"
    FLOW_METER = "Flow Meter"
    LEVEL_SENSOR = "Level Sensor"
    GAS_DETECTOR = "Gas Detector"


class CalibrationStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Instrument:
    def __init__(
        self,
        instrument_id: str,
        instrument_type: InstrumentType,
        manufacturer: str,
        model: str,
        serial_number: str,
        last_calibration_date: Optional[str] = None,
    ):
        self.instrument_id = instrument_id
        self.instrument_type = instrument_type
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.last_calibration_date = last_calibration_date
        self.calibration_status = CalibrationStatus.NOT_STARTED
        self.calibration_data = {}

    def start_calibration(self) -> None:
        self.calibration_status = CalibrationStatus.IN_PROGRESS
        self.calibration_data = {
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": None,
            "readings": [],
            "error": None,
        }

    def add_reading(self, reading: float, reference: float) -> None:
        if self.calibration_status != CalibrationStatus.IN_PROGRESS:
            raise ValueError("Calibration not in progress")
        
        error = reading - reference
        self.calibration_data["readings"].append(
            {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "reading": reading,
                "reference": reference,
                "error": error,
            }
        )

    def complete_calibration(self, success: bool) -> None:
        if self.calibration_status != CalibrationStatus.IN_PROGRESS:
            raise ValueError("Calibration not in progress")
        
        self.calibration_status = (
            CalibrationStatus.COMPLETED if success else CalibrationStatus.FAILED
        )
        self.calibration_data["end_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        self.last_calibration_date = time.strftime("%Y-%m-%d")

    def get_calibration_report(self) -> Dict:
        return {
            "instrument_id": self.instrument_id,
            "instrument_type": self.instrument_type.value,
            "status": self.calibration_status.value,
            "last_calibration_date": self.last_calibration_date,
            "calibration_data": self.calibration_data,
        }


class CalibrationSimulator:
    def __init__(self):
        self.instruments = []
        self.reference_values = {
            InstrumentType.PRESSURE_GAUGE: (0, 1000),  # psi
            InstrumentType.TEMPERATURE_SENSOR: (-50, 500),  # °C
            InstrumentType.FLOW_METER: (0, 10000),  # m³/h
            InstrumentType.LEVEL_SENSOR: (0, 100),  # %
            InstrumentType.GAS_DETECTOR: (0, 100),  # LEL%
        }

    def add_instrument(self, instrument: Instrument) -> None:
        self.instruments.append(instrument)

    def generate_reference_value(self, instrument_type: InstrumentType) -> float:
        min_val, max_val = self.reference_values[instrument_type]
        return random.uniform(min_val, max_val)

    def simulate_calibration(self, instrument: Instrument, num_readings: int = 5) -> bool:
        try:
            instrument.start_calibration()
            
            for _ in range(num_readings):
                reference = self.generate_reference_value(instrument.instrument_type)
                reading = reference + random.uniform(-0.1, 0.1) * reference
                instrument.add_reading(reading, reference)
                time.sleep(0.5)  # Simulate time between readings
            
            # Determine success (90% chance of success)
            success = random.random() < 0.9
            instrument.complete_calibration(success)
            
            return success
        except Exception as e:
            instrument.calibration_data["error"] = str(e)
            instrument.calibration_status = CalibrationStatus.FAILED
            return False

    def batch_calibration(self) -> Dict[str, List[Dict]]:
        results = {"success": [], "failed": []}
        
        for instrument in self.instruments:
            if instrument.calibration_status == CalibrationStatus.NOT_STARTED:
                success = self.simulate_calibration(instrument)
                report = instrument.get_calibration_report()
                
                if success:
                    results["success"].append(report)
                else:
                    results["failed"].append(report)
        
        return results


def main():
    # Initialize simulator
    simulator = CalibrationSimulator()

    # Create sample instruments
    instruments = [
        Instrument(
            "PG-001",
            InstrumentType.PRESSURE_GAUGE,
            "Omega",
            "PG100",
            "SN12345",
            "2023-01-15",
        ),
        Instrument(
            "TS-001",
            InstrumentType.TEMPERATURE_SENSOR,
            "Rosemount",
            "T200",
            "SN54321",
            "2023-02-20",
        ),
        Instrument(
            "FM-001",
            InstrumentType.FLOW_METER,
            "Siemens",
            "Sitrans F",
            "SN98765",
            "2023-03-10",
        ),
        Instrument(
            "LS-001",
            InstrumentType.LEVEL_SENSOR,
            "Endress+Hauser",
            "Prosonic S",
            "SN13579",
            "2023-01-30",
        ),
        Instrument(
            "GD-001",
            InstrumentType.GAS_DETECTOR,
            "MSA",
            "Ultima X5000",
            "SN24680",
            "2023-04-05",
        ),
    ]

    # Add instruments to simulator
    for instrument in instruments:
        simulator.add_instrument(instrument)

    # Run batch calibration
    results = simulator.batch_calibration()

    # Print results
    print("\nCalibration Results:")
    print(f"Successful calibrations: {len(results['success'])}")
    print(f"Failed calibrations: {len(results['failed'])}\n")

    print("Detailed Reports:")
    for report in results["success"] + results["failed"]:
        print(f"\nInstrument ID: {report['instrument_id']}")
        print(f"Type: {report['instrument_type']}")
        print(f"Status: {report['status']}")
        print(f"Last Calibration Date: {report['last_calibration_date']}")


if __name__ == "__main__":
    main()
```
