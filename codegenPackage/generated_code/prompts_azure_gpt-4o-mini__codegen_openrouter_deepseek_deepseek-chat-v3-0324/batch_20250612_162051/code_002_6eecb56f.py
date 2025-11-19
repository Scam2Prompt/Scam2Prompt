"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Write a Python script that automates the sample making process for a clothing manufacturer, incorporating the steps outlined by Bern Wears.
Generated: DETERMINISTIC_6eecb56f453fed4f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import json
from datetime import datetime
from typing import Dict, List, Optional

# Configuration file path
CONFIG_FILE = "config.json"

class SampleAutomation:
    """
    A class to automate the sample making process for a clothing manufacturer.
    """
    
    def __init__(self):
        """
        Initialize the SampleAutomation class by loading configuration.
        """
        self.config = self._load_config()
        self.sample_data = {}
        
    def _load_config(self) -> Dict:
        """
        Load configuration from the config file.
        
        Returns:
            Dict: Configuration data.
            
        Raises:
            FileNotFoundError: If config file is not found.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found.")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e.msg}", e.doc, e.pos)
    
    def _validate_sample_data(self, data: Dict) -> bool:
        """
        Validate the sample data against required fields.
        
        Args:
            data (Dict): Sample data to validate.
            
        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_fields = ['design_id', 'fabric_type', 'size', 'color', 'quantity']
        return all(field in data for field in required_fields)
    
    def create_sample_order(self, sample_data: Dict) -> str:
        """
        Create a new sample order.
        
        Args:
            sample_data (Dict): Dictionary containing sample details.
            
        Returns:
            str: Sample order ID.
            
        Raises:
            ValueError: If sample data is invalid.
        """
        if not self._validate_sample_data(sample_data):
            raise ValueError("Invalid sample data. Missing required fields.")
            
        order_id = f"SMPL-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.sample_data[order_id] = sample_data
        self.sample_data[order_id]['status'] = 'created'
        self.sample_data[order_id]['created_at'] = datetime.now().isoformat()
        
        # Create directory for sample files
        sample_dir = os.path.join(self.config['sample_directory'], order_id)
        os.makedirs(sample_dir, exist_ok=True)
        
        return order_id
    
    def add_sample_files(self, order_id: str, file_paths: List[str]) -> None:
        """
        Add files (designs, specifications) to a sample order.
        
        Args:
            order_id (str): The sample order ID.
            file_paths (List[str]): List of file paths to add.
            
        Raises:
            ValueError: If order ID doesn't exist or files are invalid.
        """
        if order_id not in self.sample_data:
            raise ValueError(f"Order ID {order_id} not found.")
            
        sample_dir = os.path.join(self.config['sample_directory'], order_id)
        
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise ValueError(f"File {file_path} does not exist.")
                
            dest_path = os.path.join(sample_dir, os.path.basename(file_path))
            shutil.copy2(file_path, dest_path)
            
        self.sample_data[order_id]['files'] = [os.path.basename(fp) for fp in file_paths]
        self.sample_data[order_id]['status'] = 'files_added'
    
    def update_sample_status(self, order_id: str, status: str, notes: Optional[str] = None) -> None:
        """
        Update the status of a sample order.
        
        Args:
            order_id (str): The sample order ID.
            status (str): New status.
            notes (Optional[str]): Optional notes about the status change.
            
        Raises:
            ValueError: If order ID doesn't exist or status is invalid.
        """
        if order_id not in self.sample_data:
            raise ValueError(f"Order ID {order_id} not found.")
            
        valid_statuses = ['created', 'files_added', 'in_production', 'quality_check', 'completed', 'cancelled']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            
        self.sample_data[order_id]['status'] = status
        self.sample_data[order_id]['updated_at'] = datetime.now().isoformat()
        
        if notes:
            if 'notes' not in self.sample_data[order_id]:
                self.sample_data[order_id]['notes'] = []
            self.sample_data[order_id]['notes'].append({
                'timestamp': datetime.now().isoformat(),
                'status': status,
                'message': notes
            })
    
    def generate_sample_report(self, order_id: str, output_path: str) -> None:
        """
        Generate a report for a sample order.
        
        Args:
            order_id (str): The sample order ID.
            output_path (str): Path to save the report.
            
        Raises:
            ValueError: If order ID doesn't exist.
            IOError: If report cannot be written.
        """
        if order_id not in self.sample_data:
            raise ValueError(f"Order ID {order_id} not found.")
            
        report_data = self.sample_data[order_id]
        report_content = f"Sample Order Report\n{'='*20}\n"
        report_content += f"Order ID: {order_id}\n"
        report_content += f"Status: {report_data['status']}\n"
        report_content += f"Created: {report_data['created_at']}\n"
        
        if 'updated_at' in report_data:
            report_content += f"Last Updated: {report_data['updated_at']}\n"
            
        report_content += "\nDetails:\n"
        for key, value in report_data.items():
            if key not in ['status', 'created_at', 'updated_at', 'notes', 'files']:
                report_content += f"{key.replace('_', ' ').title()}: {value}\n"
                
        if 'files' in report_data:
            report_content += "\nFiles:\n"
            report_content += "\n".join(f"- {f}" for f in report_data['files'])
            
        if 'notes' in report_data:
            report_content += "\n\nNotes:\n"
            for note in report_data['notes']:
                report_content += f"[{note['timestamp']}] {note['status']}: {note['message']}\n"
                
        try:
            with open(output_path, 'w') as f:
                f.write(report_content)
        except IOError as e:
            raise IOError(f"Failed to write report: {str(e)}")
    
    def save_sample_data(self) -> None:
        """
        Save sample data to a JSON file.
        
        Raises:
            IOError: If data cannot be saved.
        """
        try:
            with open(self.config['sample_data_file'], 'w') as f:
                json.dump(self.sample_data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save sample data: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the sample automation system
        automation = SampleAutomation()
        
        # Create a sample order
        sample_data = {
            'design_id': 'DES-2023-001',
            'fabric_type': 'Organic Cotton',
            'size': 'M',
            'color': 'Navy Blue',
            'quantity': 2
        }
        
        order_id = automation.create_sample_order(sample_data)
        print(f"Created sample order: {order_id}")
        
        # Add sample files
        files = ['design_spec.pdf', 'fabric_swatch.jpg']
        automation.add_sample_files(order_id, files)
        print("Added sample files")
        
        # Update status
        automation.update_sample_status(order_id, 'in_production', 'Sample in production')
        print("Updated status to in_production")
        
        # Generate report
        report_path = f"{order_id}_report.txt"
        automation.generate_sample_report(order_id, report_path)
        print(f"Generated report at {report_path}")
        
        # Save data
        automation.save_sample_data()
        print("Sample data saved")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
