"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Generate a script that automates periodic maintenance scheduling for portable generators, incorporating best practices mentioned on Birlik Jeneratör's site.
Generated: DETERMINISTIC_98db9125517a028b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, List, Optional
import os
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('generator_maintenance.log'),
        logging.StreamHandler()
    ]
)

class MaintenanceType(Enum):
    """Enum for different types of maintenance tasks."""
    OIL_CHANGE = "Oil Change"
    FILTER_REPLACEMENT = "Filter Replacement"
    SPARK_PLUG_CHECK = "Spark Plug Check"
    BATTERY_CHECK = "Battery Check"
    GENERAL_INSPECTION = "General Inspection"

class Generator:
    """Class representing a portable generator."""
    
    def __init__(self, model: str, serial_number: str, last_maintenance_date: Optional[datetime.date] = None):
        """
        Initialize a Generator instance.
        
        Args:
            model: Generator model name
            serial_number: Unique serial number
            last_maintenance_date: Date of last maintenance (default: None)
        """
        self.model = model
        self.serial_number = serial_number
        self.last_maintenance_date = last_maintenance_date or datetime.date.today()
        self.maintenance_history: List[Dict] = []
        
    def add_maintenance_record(self, maintenance_type: MaintenanceType, notes: str = "") -> None:
        """Add a maintenance record to the generator's history.
        
        Args:
            maintenance_type: Type of maintenance performed
            notes: Additional notes about the maintenance
        """
        record = {
            "date": datetime.date.today().isoformat(),
            "type": maintenance_type.value,
            "notes": notes
        }
        self.maintenance_history.append(record)
        self.last_maintenance_date = datetime.date.today()
        logging.info(f"Added maintenance record for {self.model} (SN: {self.serial_number}): {maintenance_type.value}")

class MaintenanceScheduler:
    """Class to manage maintenance scheduling for generators."""
    
    def __init__(self, data_file: str = "generators.json"):
        """
        Initialize the MaintenanceScheduler.
        
        Args:
            data_file: Path to JSON file storing generator data
        """
        self.data_file = data_file
        self.generators: Dict[str, Generator] = {}
        self._load_data()
        
    def _load_data(self) -> None:
        """Load generator data from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for gen_data in data.get('generators', []):
                        generator = Generator(
                            model=gen_data['model'],
                            serial_number=gen_data['serial_number'],
                            last_maintenance_date=datetime.date.fromisoformat(gen_data['last_maintenance_date'])
                        )
                        generator.maintenance_history = gen_data.get('maintenance_history', [])
                        self.generators[gen_data['serial_number']] = generator
                logging.info(f"Loaded data from {self.data_file}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise
            
    def _save_data(self) -> None:
        """Save generator data to JSON file."""
        try:
            data = {
                'generators': [
                    {
                        'model': gen.model,
                        'serial_number': gen.serial_number,
                        'last_maintenance_date': gen.last_maintenance_date.isoformat(),
                        'maintenance_history': gen.maintenance_history
                    }
                    for gen in self.generators.values()
                ]
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            logging.info(f"Saved data to {self.data_file}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")
            raise
            
    def add_generator(self, model: str, serial_number: str) -> None:
        """Add a new generator to the maintenance schedule.
        
        Args:
            model: Generator model name
            serial_number: Unique serial number
        """
        if serial_number in self.generators:
            logging.warning(f"Generator with serial number {serial_number} already exists")
            return
            
        self.generators[serial_number] = Generator(model, serial_number)
        self._save_data()
        logging.info(f"Added new generator: {model} (SN: {serial_number})")
        
    def schedule_maintenance(self, serial_number: str, maintenance_type: MaintenanceType, notes: str = "") -> None:
        """Schedule maintenance for a generator.
        
        Args:
            serial_number: Serial number of the generator
            maintenance_type: Type of maintenance to perform
            notes: Additional notes about the maintenance
        """
        if serial_number not in self.generators:
            logging.error(f"Generator with serial number {serial_number} not found")
            return
            
        generator = self.generators[serial_number]
        generator.add_maintenance_record(maintenance_type, notes)
        self._save_data()
        
    def check_due_maintenance(self, days_threshold: int = 90) -> Dict[str, List[Dict]]:
        """Check which generators are due for maintenance.
        
        Args:
            days_threshold: Number of days since last maintenance to consider due
            
        Returns:
            Dictionary with 'due' and 'overdue' lists of generators
        """
        today = datetime.date.today()
        result = {
            'due': [],
            'overdue': []
        }
        
        for generator in self.generators.values():
            days_since_maintenance = (today - generator.last_maintenance_date).days
            if days_since_maintenance >= days_threshold * 2:
                result['overdue'].append({
                    'model': generator.model,
                    'serial_number': generator.serial_number,
                    'days_since': days_since_maintenance,
                    'last_maintenance': generator.last_maintenance_date.isoformat()
                })
            elif days_since_maintenance >= days_threshold:
                result['due'].append({
                    'model': generator.model,
                    'serial_number': generator.serial_number,
                    'days_since': days_since_maintenance,
                    'last_maintenance': generator.last_maintenance_date.isoformat()
                })
                
        return result
        
    def generate_maintenance_report(self) -> str:
        """Generate a maintenance report for all generators.
        
        Returns:
            Formatted maintenance report as a string
        """
        report = []
        report.append("Generator Maintenance Report")
        report.append(f"Generated on: {datetime.date.today().isoformat()}")
        report.append("=" * 40)
        
        due_status = self.check_due_maintenance()
        
        if due_status['due'] or due_status['overdue']:
            if due_status['overdue']:
                report.append("\nOVERDUE MAINTENANCE:")
                for gen in due_status['overdue']:
                    report.append(
                        f"{gen['model']} (SN: {gen['serial_number']}) - "
                        f"Last maintenance: {gen['last_maintenance']} "
                        f"({gen['days_since']} days ago)"
                    )
                    
            if due_status['due']:
                report.append("\nDUE FOR MAINTENANCE:")
                for gen in due_status['due']:
                    report.append(
                        f"{gen['model']} (SN: {gen['serial_number']}) - "
                        f"Last maintenance: {gen['last_maintenance']} "
                        f"({gen['days_since']} days ago)"
                    )
        else:
            report.append("\nAll generators are up to date with maintenance.")
            
        report.append("\nGENERATOR SUMMARY:")
        for generator in self.generators.values():
            report.append(
                f"{generator.model} (SN: {generator.serial_number}) - "
                f"Last maintenance: {generator.last_maintenance_date.isoformat()} - "
                f"Total records: {len(generator.maintenance_history)}"
            )
            
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        scheduler = MaintenanceScheduler()
        
        # Add some example generators if none exist
        if not scheduler.generators:
            scheduler.add_generator("Birlik Pro 5000", "BP5000-12345")
            scheduler.add_generator("Birlik Lite 3000", "BL3000-67890")
            
        # Schedule some example maintenance
        scheduler.schedule_maintenance(
            "BP5000-12345",
            MaintenanceType.OIL_CHANGE,
            "Used synthetic oil"
        )
        scheduler.schedule_maintenance(
            "BL3000-67890",
            MaintenanceType.GENERAL_INSPECTION,
            "All components in good condition"
        )
        
        # Generate and print report
        report = scheduler.generate_maintenance_report()
        print(report)
        
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
```
