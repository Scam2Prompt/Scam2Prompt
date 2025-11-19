"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Create a script to track and report AML compliance progress across multiple departments, based on ComplyAML's training breakdown.
Generated: DETERMINISTIC_17521fb167bc06aa
Batch ID: 20250612_151644
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
from collections import defaultdict

class AMLComplianceTracker:
    """
    Tracks and reports AML compliance progress across multiple departments.
    Uses ComplyAML's training breakdown data structure.
    """
    
    def __init__(self, data_source=None):
        """
        Initialize the tracker with optional data source.
        
        Args:
            data_source (str): Path to JSON/CSV file with initial data
        """
        self.departments = defaultdict(dict)
        self.metrics = {
            'total_employees': 0,
            'trained_employees': 0,
            'completion_rate': 0.0,
            'departments_complete': 0,
            'last_updated': None
        }
        
        if data_source:
            self.load_data(data_source)
    
    def load_data(self, file_path):
        """
        Load data from JSON or CSV file.
        
        Args:
            file_path (str): Path to data file
            
        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If file doesn't exist
        """
        try:
            if file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    self._process_json_data(data)
            elif file_path.endswith('.csv'):
                with open(file_path, 'r') as f:
                    reader = csv.DictReader(f)
                    self._process_csv_data(reader)
            else:
                raise ValueError("Unsupported file format. Use JSON or CSV.")
                
            self._update_metrics()
            self.metrics['last_updated'] = datetime.now().isoformat()
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the provided file")
        except Exception as e:
            raise ValueError(f"Error processing file: {str(e)}")
    
    def _process_json_data(self, data):
        """Process data from JSON format."""
        for dept, details in data.items():
            self.departments[dept] = {
                'total': details.get('total_employees', 0),
                'trained': details.get('trained_employees', 0),
                'required_courses': details.get('required_courses', []),
                'completion_date': details.get('completion_date'),
                'manager': details.get('manager')
            }
    
    def _process_csv_data(self, data):
        """Process data from CSV format."""
        for row in data:
            dept = row['department']
            self.departments[dept] = {
                'total': int(row.get('total_employees', 0)),
                'trained': int(row.get('trained_employees', 0)),
                'required_courses': row.get('required_courses', '').split(';'),
                'completion_date': row.get('completion_date'),
                'manager': row.get('manager')
            }
    
    def _update_metrics(self):
        """Update aggregate metrics based on current department data."""
        total_employees = 0
        trained_employees = 0
        departments_complete = 0
        
        for dept, data in self.departments.items():
            total_employees += data['total']
            trained_employees += data['trained']
            
            if data['total'] > 0 and data['trained'] == data['total']:
                departments_complete += 1
        
        self.metrics['total_employees'] = total_employees
        self.metrics['trained_employees'] = trained_employees
        self.metrics['departments_complete'] = departments_complete
        
        if total_employees > 0:
            self.metrics['completion_rate'] = round(trained_employees / total_employees * 100, 2)
    
    def add_department(self, dept_name, total_employees, manager, required_courses=None):
        """
        Add a new department to track.
        
        Args:
            dept_name (str): Department name
            total_employees (int): Total employees in department
            manager (str): Department manager name
            required_courses (list): List of required AML courses
        """
        if dept_name in self.departments:
            raise ValueError(f"Department '{dept_name}' already exists")
            
        self.departments[dept_name] = {
            'total': total_employees,
            'trained': 0,
            'required_courses': required_courses or [],
            'completion_date': None,
            'manager': manager
        }
        self._update_metrics()
    
    def update_training(self, dept_name, trained_count, completion_date=None):
        """
        Update training progress for a department.
        
        Args:
            dept_name (str): Department name
            trained_count (int): Number of employees trained
            completion_date (str): Date of completion (ISO format)
            
        Raises:
            ValueError: If department doesn't exist or invalid count
        """
        if dept_name not in self.departments:
            raise ValueError(f"Department '{dept_name}' not found")
            
        if trained_count < 0 or trained_count > self.departments[dept_name]['total']:
            raise ValueError("Invalid trained employee count")
            
        self.departments[dept_name]['trained'] = trained_count
        if completion_date:
            self.departments[dept_name]['completion_date'] = completion_date
        
        self._update_metrics()
    
    def generate_report(self, format='console'):
        """
        Generate compliance report in specified format.
        
        Args:
            format (str): Output format ('console', 'json', 'csv')
            
        Returns:
            str/dict: Report in requested format
            
        Raises:
            ValueError: If invalid format requested
        """
        report_data = {
            'metrics': self.metrics,
            'departments': self.departments,
            'timestamp': datetime.now().isoformat()
        }
        
        if format == 'console':
            return self._generate_console_report(report_data)
        elif format == 'json':
            return json.dumps(report_data, indent=2)
        elif format == 'csv':
            return self._generate_csv_report(report_data)
        else:
            raise ValueError("Invalid report format. Use 'console', 'json', or 'csv'.")
    
    def _generate_console_report(self, data):
        """Generate formatted console report."""
        report = []
        report.append("\nAML Compliance Progress Report")
        report.append("=" * 50)
        report.append(f"Generated: {data['timestamp']}")
        report.append(f"\nOverall Metrics:")
        report.append(f"- Total Employees: {data['metrics']['total_employees']}")
        report.append(f"- Trained Employees: {data['metrics']['trained_employees']}")
        report.append(f"- Completion Rate: {data['metrics']['completion_rate']}%")
        report.append(f"- Departments Fully Compliant: {data['metrics']['departments_complete']}")
        
        report.append("\nDepartment Breakdown:")
        for dept, details in data['departments'].items():
            dept_rate = round(details['trained'] / details['total'] * 100, 2) if details['total'] > 0 else 0
            status = "COMPLETE" if details['trained'] == details['total'] else "IN PROGRESS"
            report.append(f"\n{dept} ({status}) - Manager: {details['manager']}")
            report.append(f"  Employees: {details['trained']}/{details['total']} ({dept_rate}%)")
            if details['completion_date']:
                report.append(f"  Completed: {details['completion_date']}")
            if details['required_courses']:
                report.append(f"  Required Courses: {', '.join(details['required_courses'])}")
        
        return "\n".join(report)
    
    def _generate_csv_report(self, data):
        """Generate CSV formatted report."""
        output = []
        headers = [
            'department', 'manager', 'total_employees', 'trained_employees',
            'completion_rate', 'status', 'completion_date', 'required_courses'
        ]
        
        output.append(','.join(headers))
        
        for dept, details in data['departments'].items():
            dept_rate = round(details['trained'] / details['total'] * 100, 2) if details['total'] > 0 else 0
            status = "COMPLETE" if details['trained'] == details['total'] else "IN PROGRESS"
            
            row = [
                dept,
                details['manager'],
                str(details['total']),
                str(details['trained']),
                str(dept_rate),
                status,
                details['completion_date'] or '',
                ';'.join(details['required_courses']) if details['required_courses'] else ''
            ]
            output.append(','.join(row))
        
        return '\n'.join(output)
    
    def save_report(self, file_path, format='json'):
