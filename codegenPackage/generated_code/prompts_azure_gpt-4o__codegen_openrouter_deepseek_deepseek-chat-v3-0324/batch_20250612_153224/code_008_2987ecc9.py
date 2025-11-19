"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Write code to implement a reporting system for tracking the efficiency of administrative processes in public institutions, inspired by Licitare's "Gestão de Processos e Procedimentos Administrativos."
Generated: DETERMINISTIC_2987ecc95ac613bf
Batch ID: 20250612_153224
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
import os
from typing import Dict, List, Optional, Tuple
from enum import Enum
import csv
from dataclasses import dataclass, asdict


class ProcessStatus(Enum):
    """Enum representing the status of an administrative process."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class AdministrativeProcess:
    """Data class representing an administrative process."""
    process_id: str
    title: str
    description: str
    department: str
    responsible_person: str
    start_date: datetime.date
    end_date: Optional[datetime.date] = None
    status: ProcessStatus = ProcessStatus.PENDING
    efficiency_score: Optional[float] = None
    comments: Optional[str] = None


class ProcessTracker:
    """Class for tracking and reporting on administrative processes."""
    
    def __init__(self, data_file: str = "processes.json"):
        """Initialize the ProcessTracker with a data file."""
        self.data_file = data_file
        self.processes: Dict[str, AdministrativeProcess] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load process data from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for process_id, process_data in data.items():
                        process_data['start_date'] = datetime.datetime.strptime(
                            process_data['start_date'], '%Y-%m-%d').date()
                        if process_data['end_date']:
                            process_data['end_date'] = datetime.datetime.strptime(
                                process_data['end_date'], '%Y-%m-%d').date()
                        process_data['status'] = ProcessStatus(process_data['status'])
                        self.processes[process_id] = AdministrativeProcess(**process_data)
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}")
    
    def _save_data(self) -> None:
        """Save process data to the data file."""
        try:
            data = {
                process_id: asdict(process)
                for process_id, process in self.processes.items()
            }
            for process_id in data:
                data[process_id]['start_date'] = data[process_id]['start_date'].isoformat()
                if data[process_id]['end_date']:
                    data[process_id]['end_date'] = data[process_id]['end_date'].isoformat()
                data[process_id]['status'] = data[process_id]['status'].value
            
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving data: {str(e)}")
    
    def add_process(self, process: AdministrativeProcess) -> None:
        """Add a new administrative process."""
        if process.process_id in self.processes:
            raise ValueError(f"Process with ID {process.process_id} already exists.")
        self.processes[process.process_id] = process
        self._save_data()
    
    def update_process(
        self,
        process_id: str,
        status: Optional[ProcessStatus] = None,
        end_date: Optional[datetime.date] = None,
        efficiency_score: Optional[float] = None,
        comments: Optional[str] = None
    ) -> None:
        """Update an existing administrative process."""
        if process_id not in self.processes:
            raise ValueError(f"Process with ID {process_id} does not exist.")
        
        process = self.processes[process_id]
        if status:
            process.status = status
        if end_date:
            process.end_date = end_date
        if efficiency_score is not None:
            process.efficiency_score = efficiency_score
        if comments is not None:
            process.comments = comments
        
        self._save_data()
    
    def get_process(self, process_id: str) -> AdministrativeProcess:
        """Retrieve a process by its ID."""
        if process_id not in self.processes:
            raise ValueError(f"Process with ID {process_id} does not exist.")
        return self.processes[process_id]
    
    def list_processes(
        self,
        department: Optional[str] = None,
        status: Optional[ProcessStatus] = None,
        date_range: Optional[Tuple[datetime.date, datetime.date]] = None
    ) -> List[AdministrativeProcess]:
        """List processes with optional filters."""
        filtered = list(self.processes.values())
        
        if department:
            filtered = [p for p in filtered if p.department == department]
        
        if status:
            filtered = [p for p in filtered if p.status == status]
        
        if date_range:
            start_date, end_date = date_range
            filtered = [
                p for p in filtered
                if start_date <= p.start_date <= end_date
            ]
        
        return filtered
    
    def calculate_efficiency_metrics(self) -> Dict[str, float]:
        """Calculate efficiency metrics across all processes."""
        completed = [
            p for p in self.processes.values()
            if p.status == ProcessStatus.COMPLETED and p.efficiency_score is not None
        ]
        
        if not completed:
            return {}
        
        avg_score = sum(p.efficiency_score for p in completed) / len(completed)
        min_score = min(p.efficiency_score for p in completed)
        max_score = max(p.efficiency_score for p in completed)
        
        return {
            "average_efficiency": avg_score,
            "min_efficiency": min_score,
            "max_efficiency": max_score
        }
    
    def generate_report(self, report_file: str, format: str = 'csv') -> None:
        """Generate a report of processes in the specified format."""
        if format not in ['csv', 'json']:
            raise ValueError("Unsupported report format. Use 'csv' or 'json'.")
        
        processes = list(self.processes.values())
        
        try:
            if format == 'csv':
                with open(report_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=[
                        'process_id', 'title', 'description', 'department',
                        'responsible_person', 'start_date', 'end_date',
                        'status', 'efficiency_score', 'comments'
                    ])
                    writer.writeheader()
                    for process in processes:
                        row = asdict(process)
                        row['status'] = row['status'].value
                        row['start_date'] = row['start_date'].isoformat()
                        if row['end_date']:
                            row['end_date'] = row['end_date'].isoformat()
                        writer.writerow(row)
            else:  # json
                report_data = {
                    p.process_id: asdict(p) for p in processes
                }
                for process_id in report_data:
                    report_data[process_id]['status'] = report_data[process_id]['status'].value
                    report_data[process_id]['start_date'] = report_data[process_id]['start_date'].isoformat()
                    if report_data[process_id]['end_date']:
                        report_data[process_id]['end_date'] = report_data[process_id]['end_date'].isoformat()
                
                with open(report_file, 'w') as f:
                    json.dump(report_data, f, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")


# Example usage
if __name__ == "__main__":
    tracker = ProcessTracker()
    
    # Add a new process
    new_process = AdministrativeProcess(
        process_id="PRC-2023-001",
        title="Budget Approval",
        description="Annual budget approval process",
        department="Finance",
        responsible_person="John Doe",
        start_date=datetime.date(2023, 1, 1)
    )
    tracker.add_process(new_process)
    
    # Update a process
    tracker.update_process(
        process_id="PRC-2023-001",
        status=ProcessStatus.COMPLETED,
        end_date=datetime.date(2023, 1, 31),
        efficiency_score=8.5,
        comments="Completed ahead of schedule"
    )
    
    # Generate a report
    tracker.generate_report("process_report.csv", format="csv")
    
    # Calculate metrics
    metrics = tracker.calculate_efficiency_metrics()
    print(f"Efficiency Metrics: {metrics}")
```
