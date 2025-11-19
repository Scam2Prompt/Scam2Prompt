"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "Provide a list of recommended maintenance procedures for 250QS pumps used in industrial processes."
Generated: DETERMINISTIC_8b223d78e0aca836
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides recommended maintenance procedures for 250QS pumps used in industrial processes.
The procedures are based on manufacturer guidelines and industry best practices.
"""

from typing import List, Dict
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pump_maintenance.log'),
        logging.StreamHandler()
    ]
)

class PumpMaintenanceProcedures:
    """Class containing maintenance procedures for 250QS pumps."""
    
    def __init__(self):
        self.procedures = self._initialize_procedures()
        
    def _initialize_procedures(self) -> List[Dict]:
        """Initialize and return the list of recommended maintenance procedures."""
        return [
            {
                'procedure_id': 'PM001',
                'description': 'Visual inspection of pump and components',
                'frequency': 'Daily',
                'steps': [
                    'Check for leaks in the pump casing and connections',
                    'Inspect motor and electrical connections for damage',
                    'Verify proper alignment of pump and motor'
                ],
                'critical': False
            },
            {
                'procedure_id': 'PM002',
                'description': 'Lubrication of bearings',
                'frequency': 'Monthly',
                'steps': [
                    'Check bearing housing oil level',
                    'Add recommended lubricant if needed',
                    'Inspect for contamination in lubricant'
                ],
                'critical': True
            },
            {
                'procedure_id': 'PM003',
                'description': 'Impeller inspection and cleaning',
                'frequency': 'Quarterly',
                'steps': [
                    'Drain pump and remove cover',
                    'Inspect impeller for wear or damage',
                    'Clean impeller and volute of debris',
                    'Reassemble and test operation'
                ],
                'critical': True
            },
            {
                'procedure_id': 'PM004',
                'description': 'Seal inspection and replacement',
                'frequency': 'Biannually',
                'steps': [
                    'Inspect mechanical seals for wear',
                    'Replace seals if leakage is detected',
                    'Check seal flush system operation'
                ],
                'critical': True
            },
            {
                'procedure_id': 'PM005',
                'description': 'Full performance testing',
                'frequency': 'Annually',
                'steps': [
                    'Measure flow rate and pressure',
                    'Compare to manufacturer specifications',
                    'Check motor current draw',
                    'Document performance metrics'
                ],
                'critical': False
            }
        ]
    
    def get_all_procedures(self) -> List[Dict]:
        """Return all maintenance procedures."""
        return self.procedures
    
    def get_critical_procedures(self) -> List[Dict]:
        """Return only critical maintenance procedures."""
        return [proc for proc in self.procedures if proc['critical']]
    
    def get_procedure_by_id(self, procedure_id: str) -> Dict:
        """Return a specific procedure by its ID.
        
        Args:
            procedure_id: The ID of the procedure to retrieve
            
        Returns:
            The procedure dictionary if found, None otherwise
        """
        try:
            return next(proc for proc in self.procedures if proc['procedure_id'] == procedure_id)
        except StopIteration:
            logging.error(f"Procedure with ID {procedure_id} not found")
            return None
    
    def generate_maintenance_schedule(self, start_date: datetime) -> Dict:
        """Generate a maintenance schedule based on procedures and frequencies.
        
        Args:
            start_date: The starting date for the schedule
            
        Returns:
            A dictionary mapping dates to procedures
        """
        schedule = {}
        for proc in self.procedures:
            if proc['frequency'] == 'Daily':
                schedule[start_date.strftime('%Y-%m-%d')] = proc
            elif proc['frequency'] == 'Monthly':
                schedule[(start_date.replace(day=1)).strftime('%Y-%m-%d')] = proc
            elif proc['frequency'] == 'Quarterly':
                quarter = (start_date.month - 1) // 3 + 1
                schedule[(start_date.replace(month=quarter*3, day=1)).strftime('%Y-%m-%d')] = proc
            elif proc['frequency'] == 'Biannually':
                schedule[(start_date.replace(month=6 if start_date.month <= 6 else 12, day=1)).strftime('%Y-%m-%d')] = proc
            elif proc['frequency'] == 'Annually':
                schedule[(start_date.replace(month=1, day=1)).strftime('%Y-%m-%d')] = proc
        return schedule

# Example usage
if __name__ == "__main__":
    try:
        maintenance = PumpMaintenanceProcedures()
        
        # Get all procedures
        all_procedures = maintenance.get_all_procedures()
        logging.info(f"Total procedures: {len(all_procedures)}")
        
        # Get critical procedures
        critical_procedures = maintenance.get_critical_procedures()
        logging.info(f"Critical procedures: {len(critical_procedures)}")
        
        # Get specific procedure
        procedure = maintenance.get_procedure_by_id('PM003')
        if procedure:
            logging.info(f"Procedure PM003: {procedure['description']}")
        
        # Generate schedule
        schedule = maintenance.generate_maintenance_schedule(datetime.now())
        logging.info(f"Generated maintenance schedule: {schedule}")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
```
