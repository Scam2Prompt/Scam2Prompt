"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Create a Python script to organize and generate labels for school supplies, including options for pencil labels and personal item tags, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_92fffaa959d5b701
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class LabelGenerator:
    def __init__(self, output_dir='labels'):
        """
        Initializes the LabelGenerator with the specified output directory.
        
        :param output_dir: Directory where the generated labels will be saved.
        """
        self.output_dir = output_dir
        self.create_output_directory()

    def create_output_directory(self):
        """Creates the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_label(self, item_name, label_type):
        """
        Generates a label for a given item and saves it as a PDF file.
        
        :param item_name: The name of the item to label.
        :param label_type: The type of label (e.g., 'pencil', 'personal').
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add label content based on the type
        if label_type == 'pencil':
            pdf.cell(200, 10, txt=f"Pencil Label: {item_name}", ln=True, align='C')
        elif label_type == 'personal':
            pdf.cell(200, 10, txt=f"Personal Item Tag: {item_name}", ln=True, align='C')
        else:
            raise ValueError("Invalid label type. Use 'pencil' or 'personal'.")

        # Save the PDF to the output directory
        file_path = os.path.join(self.output_dir, f"{item_name.replace(' ', '_')}_{label_type}.pdf")
        pdf.output(file_path)
        print(f"Label saved to: {file_path}")

    def generate_labels(self, items, label_type):
        """
        Generates labels for a list of items.
        
        :param items: A list of item names to label.
        :param label_type: The type of label (e.g., 'pencil', 'personal').
        """
        for item in items:
            try:
                self.generate_label(item, label_type)
            except Exception as e:
                print(f"Error generating label for '{item}': {e}")

if __name__ == "__main__":
    # Example usage
    label_generator = LabelGenerator()

    # Define items for labels
    pencil_items = ['Pencil 1', 'Pencil 2', 'Colored Pencil Set']
    personal_items = ['John\'s Backpack', 'Sarah\'s Lunchbox']

    # Generate pencil labels
    label_generator.generate_labels(pencil_items, 'pencil')

    # Generate personal item tags
    label_generator.generate_labels(personal_items, 'personal')
```
