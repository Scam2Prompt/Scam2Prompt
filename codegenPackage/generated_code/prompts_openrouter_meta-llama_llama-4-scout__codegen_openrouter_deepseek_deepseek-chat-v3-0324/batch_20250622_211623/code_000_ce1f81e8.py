"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write a Python script to generate customized labels for identifying children's school effects, using a template with name and ID fields.
Generated: DETERMINISTIC_ce1f81e82c6824ab
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class LabelGenerator:
    """
    A class to generate customized labels for children's school effects.
    
    Attributes:
        template_path (str): Path to the label template file.
        output_dir (str): Directory to save generated labels.
        labels (List[Dict]): List of label data containing name and ID.
    """
    
    def __init__(self, template_path: str, output_dir: str = "output_labels"):
        """
        Initialize the LabelGenerator with template path and output directory.
        
        Args:
            template_path: Path to the label template file.
            output_dir: Directory to save generated labels. Defaults to "output_labels".
        """
        self.template_path = template_path
        self.output_dir = output_dir
        self.labels = []
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_labels_from_csv(self, csv_path: str) -> None:
        """
        Load label data from a CSV file.
        
        CSV format should be: name,id
        
        Args:
            csv_path: Path to the CSV file containing label data.
            
        Raises:
            FileNotFoundError: If the CSV file does not exist.
            ValueError: If the CSV file is malformed.
        """
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        self.labels = []
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' not in row or 'id' not in row:
                    raise ValueError("CSV file must contain 'name' and 'id' columns")
                self.labels.append({'name': row['name'], 'id': row['id']})
    
    def generate_labels(self) -> List[str]:
        """
        Generate labels using the loaded template and label data.
        
        Returns:
            List of file paths for the generated labels.
            
        Raises:
            FileNotFoundError: If the template file does not exist.
            ValueError: If no label data is loaded.
        """
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template file not found: {self.template_path}")
        
        if not self.labels:
            raise ValueError("No label data loaded. Please load label data first.")
        
        generated_files = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        with open(self.template_path, 'r', encoding='utf-8') as template_file:
            template = template_file.read()
            
            for label in self.labels:
                # Replace placeholders in template
                label_content = template.replace('{{name}}', label['name'])
                label_content = label_content.replace('{{id}}', label['id'])
                
                # Generate output filename
                filename = f"label_{label['name'].lower().replace(' ', '_')}_{timestamp}.txt"
                filepath = os.path.join(self.output_dir, filename)
                
                # Save label to file
                with open(filepath, 'w', encoding='utf-8') as output_file:
                    output_file.write(label_content)
                
                generated_files.append(filepath)
        
        return generated_files

# Example usage
if __name__ == "__main__":
    try:
        # Initialize label generator
        generator = LabelGenerator(template_path="label_template.txt")
        
        # Load labels from CSV
        generator.load_labels_from_csv("labels_data.csv")
        
        # Generate labels
        generated_files = generator.generate_labels()
        print(f"Generated {len(generated_files)} labels:")
        for file in generated_files:
            print(f"- {file}")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
