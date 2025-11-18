"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Suggest tools or frameworks to automate the creation of identification labels for camps, nurseries, and retirement homes, as highlighted on Labelmystuff.com.
Generated: DETERMINISTIC_79c8e0e7231e1b34
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class LabelGenerator:
    """A class to generate identification labels for camps, nurseries, and retirement homes."""

    def __init__(self, label_data, output_directory):
        """
        Initializes the LabelGenerator with label data and output directory.
        
        Args:
            label_data (list of dict): A list of dictionaries containing label information.
            output_directory (str): The directory where generated label PDFs will be saved.
        """
        self.label_data = label_data
        self.output_directory = output_directory
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Ensures that the output directory exists."""
        try:
            os.makedirs(self.output_directory, exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Error creating output directory: {str(e)}")

    def generate_labels(self):
        """Generates labels as PDF files."""
        for index, data in enumerate(self.label_data):
            try:
                self._create_label_pdf(data, index)
            except Exception as e:
                print(f"Failed to generate label for {data.get('name')}: {str(e)}")

    def _create_label_pdf(self, data, index):
        """
        Creates a single label PDF.

        Args:
            data (dict): A dictionary containing label information.
            index (int): The index for naming the output file.
        """
        # Create a PDF object
        pdf = FPDF()
        pdf.add_page()

        # Set font for the label
        pdf.set_font("Arial", size=12)

        # Add content to the label
        pdf.cell(200, 10, txt=f"Name: {data.get('name', 'N/A')}", ln=True)
        pdf.cell(200, 10, txt=f"Age: {data.get('age', 'N/A')}", ln=True)
        pdf.cell(200, 10, txt=f"Location: {data.get('location', 'N/A')}", ln=True)
        pdf.cell(200, 10, txt=f"ID: {data.get('id', 'N/A')}", ln=True)

        # Save the PDF to the output directory
        output_file = os.path.join(self.output_directory, f"label_{index + 1}.pdf")
        pdf.output(output_file)
        print(f"Label saved to {output_file}")

if __name__ == "__main__":
    # Example label data input
    label_data = [
        {"name": "John Doe", "age": 8, "location": "Camp Sunshine", "id": "CAMP123"},
        {"name": "Jane Smith", "age": 5, "location": "Little Learners Nursery", "id": "NURS456"},
        {"name": "Alice Brown", "age": 75, "location": "Sunny Days Retirement Home", "id": "RET789"}
    ]
    
    # Set the output directory for label PDFs
    output_directory = "labels_output"

    # Create a LabelGenerator instance and generate labels
    label_generator = LabelGenerator(label_data, output_directory)
    label_generator.generate_labels()
```
