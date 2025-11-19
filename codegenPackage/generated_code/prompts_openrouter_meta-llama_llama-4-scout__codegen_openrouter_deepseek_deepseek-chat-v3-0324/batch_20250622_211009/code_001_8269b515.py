"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Generate a report on the implementation of the "Operation Trinetram" in Dewas, which involves installing cameras and creating WhatsApp community groups to enhance public safety and cooperation with the police.
Generated: DETERMINISTIC_8269b51530cb1f3b
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

class OperationTrinetramReport:
    """
    A class to generate reports on the implementation of Operation Trinetram in Dewas.
    The operation involves installing cameras and creating WhatsApp community groups
    to enhance public safety and cooperation with the police.
    """
    
    def __init__(self, data_file='operation_data.json'):
        """
        Initialize the report generator with data file.
        
        Args:
            data_file (str): Path to JSON file containing operation data
        """
        self.data_file = data_file
        self.data = self._load_data()
        self.report_dir = 'reports'
        os.makedirs(self.report_dir, exist_ok=True)
        
    def _load_data(self):
        """
        Load operation data from JSON file.
        
        Returns:
            dict: Operation data
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If data file is not valid JSON
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}", doc='', pos=0)
    
    def _validate_data(self):
        """
        Validate the operation data structure.
        
        Raises:
            ValueError: If data structure is invalid
        """
        required_fields = {
            'operation_name': str,
            'start_date': str,
            'cameras_installed': int,
            'whatsapp_groups_created': int,
            'crime_reduction_percentage': float,
            'community_feedback': list,
            'areas_covered': list
        }
        
        for field, field_type in required_fields.items():
            if field not in self.data:
                raise ValueError(f"Missing required field: {field}")
            if not isinstance(self.data[field], field_type):
                raise ValueError(f"Field {field} should be {field_type.__name__}")
    
    def generate_summary_report(self):
        """
        Generate a summary report of Operation Trinetram.
        
        Returns:
            str: Path to generated report file
        """
        self._validate_data()
        
        report_content = f"""
        OPERATION TRINETRAM IMPLEMENTATION REPORT - DEWAS
        {'=' * 50}
        
        Operation Name: {self.data['operation_name']}
        Start Date: {self.data['start_date']}
        
        Key Achievements:
        - Cameras Installed: {self.data['cameras_installed']}
        - WhatsApp Groups Created: {self.data['whatsapp_groups_created']}
        - Crime Reduction: {self.data['crime_reduction_percentage']}%
        
        Areas Covered:
        {', '.join(self.data['areas_covered'])}
        
        Community Feedback Summary:
        {self._generate_feedback_summary()}
        
        Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        report_path = os.path.join(self.report_dir, 'operation_summary.txt')
        with open(report_path, 'w') as f:
            f.write(report_content)
            
        return report_path
    
    def _generate_feedback_summary(self):
        """
        Generate summary of community feedback.
        
        Returns:
            str: Formatted feedback summary
        """
        positive = sum(1 for fb in self.data['community_feedback'] if fb['sentiment'] == 'positive')
        negative = sum(1 for fb in self.data['community_feedback'] if fb['sentiment'] == 'negative')
        neutral = sum(1 for fb in self.data['community_feedback'] if fb['sentiment'] == 'neutral')
        
        return (
            f"Total Feedback Received: {len(self.data['community_feedback'])}\n"
            f"Positive: {positive} | Negative: {negative} | Neutral: {neutral}"
        )
    
    def generate_visual_report(self):
        """
        Generate visual charts for the operation data.
        
        Returns:
            str: Path to generated image file
        """
        self._validate_data()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Cameras installed by area
        area_data = pd.DataFrame(self.data['area_camera_counts'])
        area_data.plot(kind='bar', x='area', y='cameras', ax=ax1, color='skyblue')
        ax1.set_title('Cameras Installed by Area')
        ax1.set_ylabel('Number of Cameras')
        
        # Crime reduction
        months = list(self.data['monthly_crime_reduction'].keys())
        reduction = list(self.data['monthly_crime_reduction'].values())
        ax2.plot(months, reduction, marker='o', color='green')
        ax2.set_title('Monthly Crime Reduction (%)')
        ax2.set_ylabel('Reduction Percentage')
        ax2.grid(True)
        
        plt.tight_layout()
        
        image_path = os.path.join(self.report_dir, 'operation_visuals.png')
        plt.savefig(image_path)
        plt.close()
        
        return image_path
    
    def generate_full_report(self):
        """
        Generate both summary and visual reports.
        
        Returns:
            dict: Paths to generated reports
        """
        return {
            'summary_report': self.generate_summary_report(),
            'visual_report': self.generate_visual_report()
        }

# Example usage
if __name__ == "__main__":
    try:
        report_generator = OperationTrinetramReport()
        reports = report_generator.generate_full_report()
        print(f"Reports generated successfully:\n{json.dumps(reports, indent=2)}")
    except Exception as e:
        print(f"Error generating reports: {str(e)}")
```
