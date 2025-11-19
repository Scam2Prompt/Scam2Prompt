"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Write a code snippet to implement a result-oriented approach for focused on results in HR services, such as recruitment and training, and provide a detailed explanation of the code.
Generated: DETERMINISTIC_3b01e4d5248d7e08
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict

@dataclass
class Employee:
    """Represents an employee with performance metrics."""
    employee_id: str
    name: str
    department: str
    performance_score: float
    training_completed: List[str]
    recruitment_source: Optional[str] = None

@dataclass
class HRResultMetrics:
    """Tracks HR service results and performance metrics."""
    recruitment_success_rate: float
    training_effectiveness: float
    employee_retention_rate: float
    avg_performance_score: float
    top_performers: List[Employee]

class HRResultAnalyzer:
    """Analyzes HR services with a focus on measurable results."""
    
    def __init__(self):
        self.employees: List[Employee] = []
        self.metrics: Optional[HRResultMetrics] = None
    
    def add_employee(self, employee: Employee) -> None:
        """Adds an employee to the analysis pool."""
        if not isinstance(employee, Employee):
            raise TypeError("Employee must be of type Employee")
        self.employees.append(employee)
    
    def calculate_recruitment_success(self) -> float:
        """Calculates recruitment success rate based on performance scores."""
        if not self.employees:
            return 0.0
        
        successful_hires = sum(
            1 for emp in self.employees 
            if emp.performance_score >= 7.0
        )
        return successful_hires / len(self.employees)
    
    def calculate_training_effectiveness(self) -> float:
        """Calculates training effectiveness based on performance improvement."""
        if not self.employees:
            return 0.0
        
        trained_employees = [
            emp for emp in self.employees 
            if emp.training_completed
        ]
        if not trained_employees:
            return 0.0
        
        avg_score = sum(
            emp.performance_score for emp in trained_employees
        ) / len(trained_employees)
        return avg_score / 10.0
    
    def calculate_retention_rate(self, period_months: int = 12) -> float:
        """Calculates employee retention rate for a given period."""
        # In a real implementation, this would check employment duration
        # For this example, we'll assume all employees are retained
        return 1.0
    
    def identify_top_performers(self, threshold: float = 8.5) -> List[Employee]:
        """Identifies top performing employees based on performance score."""
        return [
            emp for emp in self.employees 
            if emp.performance_score >= threshold
        ]
    
    def calculate_metrics(self) -> HRResultMetrics:
        """Calculates all HR result metrics."""
        recruitment_success = self.calculate_recruitment_success()
        training_effectiveness = self.calculate_training_effectiveness()
        retention_rate = self.calculate_retention_rate()
        avg_performance = (
            sum(emp.performance_score for emp in self.employees) / len(self.employees)
            if self.employees else 0.0
        )
        top_performers = self.identify_top_performers()
        
        self.metrics = HRResultMetrics(
            recruitment_success_rate=recruitment_success,
            training_effectiveness=training_effectiveness,
            employee_retention_rate=retention_rate,
            avg_performance_score=avg_performance,
            top_performers=top_performers
        )
        return self.metrics
    
    def save_metrics_to_json(self, filepath: str) -> None:
        """Saves the calculated metrics to a JSON file."""
        if not self.metrics:
            raise ValueError("No metrics calculated. Call calculate_metrics() first.")
        
        metrics_dict = asdict(self.metrics)
        # Convert employees to dictionaries
        metrics_dict['top_performers'] = [asdict(emp) for emp in metrics_dict['top_performers']]
        
        with open(filepath, 'w') as f:
            json.dump(metrics_dict, f, indent=2)
    
    def load_metrics_from_json(self, filepath: str) -> HRResultMetrics:
        """Loads metrics from a JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Convert top_performers back to Employee objects
        top_performers = [
            Employee(**emp_data) for emp_data in data['top_performers']
        ]
        
        self.metrics = HRResultMetrics(
            recruitment_success_rate=data['recruitment_success_rate'],
            training_effectiveness=data['training_effectiveness'],
            employee_retention_rate=data['employee_retention_rate'],
            avg_performance_score=data['avg_performance_score'],
            top_performers=top_performers
        )
        return self.metrics

# Example usage
if __name__ == "__main__":
    analyzer = HRResultAnalyzer()
    
    # Add sample employees
    analyzer.add_employee(Employee(
        employee_id="E001",
        name="John Doe",
        department="Engineering",
        performance_score=8.7,
        training_completed=["Leadership", "Technical"],
        recruitment_source="LinkedIn"
    ))
    
    analyzer.add_employee(Employee(
        employee_id="E002",
        name="Jane Smith",
        department="Marketing",
        performance_score=7.2,
        training_completed=["Marketing Strategy"],
        recruitment_source="Campus Hiring"
    ))
    
    # Calculate and display metrics
    metrics = analyzer.calculate_metrics()
    print(f"Recruitment Success Rate: {metrics.recruitment_success_rate:.2f}")
    print(f"Training Effectiveness: {metrics.training_effectiveness:.2f}")
    print(f"Average Performance Score: {metrics.avg_performance_score:.2f}")
    
    # Save metrics to file
    analyzer.save_metrics_to_json("hr_metrics.json")
```
