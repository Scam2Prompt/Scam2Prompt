"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Design a data reporting system for tracking vaccine distribution and administration, incorporating CSL Seqirus's commitment to protecting public health from seasonal influenza."
Generated: DETERMINISTIC_e2e415bc39604f16
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VaccineType(Enum):
    """Enum representing different vaccine types"""
    INFLUENZA = "Influenza"
    COVID = "COVID-19"
    OTHER = "Other"

class DistributionStatus(Enum):
    """Enum representing distribution statuses"""
    ORDERED = "Ordered"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    ADMINISTERED = "Administered"
    EXPIRED = "Expired"

class VaccineBatch:
    """Class representing a batch of vaccines"""
    def __init__(
        self,
        batch_id: str,
        vaccine_type: VaccineType,
        manufacture_date: datetime,
        expiration_date: datetime,
        quantity: int,
        manufacturer: str = "CSL Seqirus"
    ):
        self.batch_id = batch_id
        self.vaccine_type = vaccine_type
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date
        self.quantity = quantity
        self.manufacturer = manufacturer
        self.status = DistributionStatus.ORDERED
        self.remaining_quantity = quantity
        self.administration_records: List[Dict] = []

    def update_status(self, new_status: DistributionStatus) -> None:
        """Update the distribution status of the batch"""
        if new_status not in DistributionStatus:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
        logger.info(f"Batch {self.batch_id} status updated to {new_status}")

    def record_administration(
        self,
        patient_id: str,
        date_administered: datetime,
        location: str,
        quantity: int = 1
    ) -> None:
        """Record vaccine administration"""
        if quantity > self.remaining_quantity:
            raise ValueError("Not enough vaccines remaining in batch")
        
        if self.status != DistributionStatus.DELIVERED:
            raise ValueError("Vaccines must be delivered before administration")
        
        if date_administered > datetime.now():
            raise ValueError("Administration date cannot be in the future")
        
        self.administration_records.append({
            "patient_id": patient_id,
            "date_administered": date_administered,
            "location": location,
            "quantity": quantity
        })
        self.remaining_quantity -= quantity
        logger.info(f"Administered {quantity} dose(s) from batch {self.batch_id}")

    def to_dict(self) -> Dict:
        """Convert batch data to dictionary for serialization"""
        return {
            "batch_id": self.batch_id,
            "vaccine_type": self.vaccine_type.value,
            "manufacture_date": self.manufacture_date.isoformat(),
            "expiration_date": self.expiration_date.isoformat(),
            "quantity": self.quantity,
            "manufacturer": self.manufacturer,
            "status": self.status.value,
            "remaining_quantity": self.remaining_quantity,
            "administration_records": self.administration_records
        }

class VaccineReportingSystem:
    """System for tracking vaccine distribution and administration"""
    def __init__(self):
        self.batches: Dict[str, VaccineBatch] = {}
    
    def add_batch(self, batch: VaccineBatch) -> None:
        """Add a new vaccine batch to the system"""
        if batch.batch_id in self.batches:
            raise ValueError(f"Batch ID {batch.batch_id} already exists")
        self.batches[batch.batch_id] = batch
        logger.info(f"Added new batch {batch.batch_id} to system")

    def get_batch(self, batch_id: str) -> Optional[VaccineBatch]:
        """Retrieve a batch by ID"""
        return self.batches.get(batch_id)

    def generate_distribution_report(self) -> List[Dict]:
        """Generate a report of all batches and their status"""
        return [batch.to_dict() for batch in self.batches.values()]

    def generate_administration_report(self) -> List[Dict]:
        """Generate a report of all administration records"""
        report = []
        for batch in self.batches.values():
            for record in batch.administration_records:
                report.append({
                    "batch_id": batch.batch_id,
                    "vaccine_type": batch.vaccine_type.value,
                    **record
                })
        return report

    def save_to_json(self, filename: str) -> None:
        """Save all data to a JSON file"""
        data = {
            "batches": [batch.to_dict() for batch in self.batches.values()]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data saved to {filename}")
        except IOError as e:
            logger.error(f"Failed to save data: {e}")
            raise

    def load_from_json(self, filename: str) -> None:
        """Load data from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.batches = {}
            for batch_data in data.get("batches", []):
                batch = VaccineBatch(
                    batch_id=batch_data["batch_id"],
                    vaccine_type=VaccineType(batch_data["vaccine_type"]),
                    manufacture_date=datetime.fromisoformat(batch_data["manufacture_date"]),
                    expiration_date=datetime.fromisoformat(batch_data["expiration_date"]),
                    quantity=batch_data["quantity"],
                    manufacturer=batch_data.get("manufacturer", "CSL Seqirus")
                )
                batch.status = DistributionStatus(batch_data["status"])
                batch.remaining_quantity = batch_data["remaining_quantity"]
                batch.administration_records = batch_data["administration_records"]
                self.batches[batch.batch_id] = batch
            
            logger.info(f"Data loaded from {filename}")
        except (IOError, json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def export_to_csv(self, filename: str, report_type: str = "distribution") -> None:
        """Export data to CSV format"""
        try:
            if report_type == "distribution":
                data = self.generate_distribution_report()
                fieldnames = [
                    "batch_id", "vaccine_type", "manufacture_date",
                    "expiration_date", "quantity", "manufacturer",
                    "status", "remaining_quantity"
                ]
            elif report_type == "administration":
                data = self.generate_administration_report()
                fieldnames = [
                    "batch_id", "vaccine_type", "patient_id",
                    "date_administered", "location", "quantity"
                ]
            else:
                raise ValueError("Invalid report type. Use 'distribution' or 'administration'")

            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            logger.info(f"Exported {report_type} report to {filename}")
        except (IOError, ValueError) as e:
            logger.error(f"Failed to export data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reporting system
        reporting_system = VaccineReportingSystem()

        # Create a vaccine batch
        batch = VaccineBatch(
            batch_id="FLU2023-001",
            vaccine_type=VaccineType.INFLUENZA,
            manufacture_date=datetime(2023, 1, 15),
            expiration_date=datetime(2023, 12, 31),
            quantity=1000
        )

        # Add batch to system
        reporting_system.add_batch(batch)

        # Update batch status
        batch.update_status(DistributionStatus.DELIVERED)

        # Record administration
        batch.record_administration(
            patient_id="PAT12345",
            date_administered=datetime(2023, 2, 1),
            location="Community Health Center"
        )

        # Generate and save reports
        reporting_system.save_to_json("vaccine_data.json")
        reporting_system.export_to_csv("distribution_report.csv")
        reporting_system.export_to_csv("administration_report.csv", "administration")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
