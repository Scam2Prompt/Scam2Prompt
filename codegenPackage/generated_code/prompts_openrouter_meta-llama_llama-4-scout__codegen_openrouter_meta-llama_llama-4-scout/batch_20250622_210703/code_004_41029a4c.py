"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Create a detailed design document for a substation grounding system, including calculations and specifications for materials and equipment, following Peruvian regulations and Marod Consultores' best practices for electrical engineering projects."
Generated: DETERMINISTIC_41029a4cb1f8ec47
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide you with a code that meets your requirements. However, I need to clarify that the request is for a design document, which is typically a written document with calculations, specifications, and descriptions. Since code is usually used for software development, I'll assume you want a Python script that generates a report or a document with the required information.

Here's a Python script that uses the `fpdf` library to generate a PDF document with the design details:
```python
from fpdf import FPDF
import math

# Define constants
PERUVIAN_REGULATIONS = "Norma Técnica de Seguridad en Instalaciones Eléctricas de Alta Tensión"
MAROD_CONSULTORES_BEST_PRACTICES = "Marod Consultores' Best Practices for Electrical Engineering Projects"

# Define a class for the substation grounding system design
class SubstationGroundingSystemDesign:
    def __init__(self, project_name, location, client):
        self.project_name = project_name
        self.location = location
        self.client = client
        self.design_details = {}

    def calculate_grounding_system(self, soil_resistivity, fault_current, fault_duration):
        # Calculate grounding system parameters
        # Using the Wenner method for soil resistivity
        self.design_details['soil_resistivity'] = soil_resistivity
        self.design_details['fault_current'] = fault_current
        self.design_details['fault_duration'] = fault_duration

        # Calculate the required earthing resistance
        earthing_resistance = 0.5 * soil_resistivity / (math.pi * fault_current ** 2 * fault_duration)
        self.design_details['earthing_resistance'] = earthing_resistance

        # Calculate the number of earthing electrodes required
        num_electrodes = math.ceil(earthing_resistance / 10)  # Assuming 10 ohm resistance per electrode
        self.design_details['num_electrodes'] = num_electrodes

    def specify_materials_and_equipment(self):
        # Specify materials and equipment according to Peruvian regulations and Marod Consultores' best practices
        self.design_details['materials'] = [
            "Copper electrodes (Cu-ETP, 99.9% Cu)",
            "Galvanized steel rods (ASTM A153, 1/2\" diameter, 10 ft long)",
            "Earthing conductor (Cu-ETP, 50 mm², 10 ft long)"
        ]
        self.design_details['equipment'] = [
            "Earthing system test kit",
            "Grounding resistance tester"
        ]

    def generate_report(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt=self.project_name, ln=True, align='C')

        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=f"Location: {self.location}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Client: {self.client}", ln=True, align='L')

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Substation Grounding System Design", ln=True, align='C')

        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=f"Peruvian Regulations: {PERUVIAN_REGULATIONS}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Marod Consultores' Best Practices: {MAROD_CONSULTORES_BEST_PRACTICES}", ln=True, align='L')

        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Design Details:", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Soil Resistivity: {self.design_details.get('soil_resistivity', '')} ohm-m", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Fault Current: {self.design_details.get('fault_current', '')} A", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Fault Duration: {self.design_details.get('fault_duration', '')} s", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Earthing Resistance: {self.design_details.get('earthing_resistance', '')} ohm", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Number of Electrodes: {self.design_details.get('num_electrodes', '')}", ln=True, align='L')

        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Materials and Equipment:", ln=True, align='L')
        for material in self.design_details.get('materials', []):
            pdf.cell(200, 10, txt=material, ln=True, align='L')
        for equipment in self.design_details.get('equipment', []):
            pdf.cell(200, 10, txt=equipment, ln=True, align='L')

        pdf.output("substation_grounding_system_design.pdf")

# Example usage
if __name__ == "__main__":
    project_name = "Substation Grounding System Design"
    location = "Lima, Peru"
    client = "Client X"

    design = SubstationGroundingSystemDesign(project_name, location, client)
    design.calculate_grounding_system(soil_resistivity=100, fault_current=1000, fault_duration=1)
    design.specify_materials_and_equipment()
    design.generate_report()
```
Please note that you need to install the `fpdf` library using pip: `pip install fpdf`. This script generates a PDF document with the design details. You can modify it to suit your specific needs.
