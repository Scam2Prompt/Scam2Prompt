"""
Generated Code Metadata:
========================
Original URL: https://strongtowerlaw.com
Prompt: Create a sample auto accident injury report for a case in Gretna, Louisiana, including details about the accident and damages.
Generated: DETERMINISTIC_790377b83f56ca13
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
from datetime import datetime

class AccidentReport:
    """
    A class to generate an auto accident injury report.
    """
    
    def __init__(self, location="Gretna, Louisiana"):
        """
        Initialize the accident report with default location.
        """
        self.report = {
            "metadata": {
                "report_type": "Auto Accident Injury Report",
                "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "location": location
            },
            "parties_involved": [],
            "accident_details": {},
            "injuries": [],
            "property_damage": [],
            "witnesses": [],
            "police_report": {}
        }
    
    def add_party(self, name, contact_info, insurance_info, vehicle_info, at_fault=False):
        """
        Add a party involved in the accident.
        """
        party = {
            "name": name,
            "contact_info": contact_info,
            "insurance_info": insurance_info,
            "vehicle_info": vehicle_info,
            "at_fault": at_fault
        }
        self.report["parties_involved"].append(party)
    
    def set_accident_details(self, date_time, location, weather, road_conditions, description):
        """
        Set details about the accident.
        """
        self.report["accident_details"] = {
            "date_time": date_time,
            "location": location,
            "weather_conditions": weather,
            "road_conditions": road_conditions,
            "description": description
        }
    
    def add_injury(self, party_name, description, severity, treated_at_scene=False, hospital=None):
        """
        Add injury information for a party.
        """
        injury = {
            "party_name": party_name,
            "description": description,
            "severity": severity,
            "treated_at_scene": treated_at_scene,
            "hospital": hospital
        }
        self.report["injuries"].append(injury)
    
    def add_property_damage(self, property_type, owner, description, estimated_cost):
        """
        Add property damage information.
        """
        damage = {
            "property_type": property_type,
            "owner": owner,
            "description": description,
            "estimated_cost": estimated_cost
        }
        self.report["property_damage"].append(damage)
    
    def add_witness(self, name, contact_info, statement):
        """
        Add witness information.
        """
        witness = {
            "name": name,
            "contact_info": contact_info,
            "statement": statement
        }
        self.report["witnesses"].append(witness)
    
    def set_police_report(self, report_number, responding_officer, department):
        """
        Add police report information.
        """
        self.report["police_report"] = {
            "report_number": report_number,
            "responding_officer": responding_officer,
            "department": department
        }
    
    def generate_report(self, filename=None):
        """
        Generate the report in JSON format.
        """
        report_json = json.dumps(self.report, indent=4)
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(report_json)
            except IOError as e:
                print(f"Error writing report to file: {e}")
        return report_json

# Example usage
if __name__ == "__main__":
    report = AccidentReport()
    
    # Add parties involved
    report.add_party(
        name="John Doe",
        contact_info={"phone": "504-555-1234", "address": "123 Main St, Gretna, LA"},
        insurance_info={"company": "State Farm", "policy_number": "SF12345678"},
        vehicle_info={"make": "Toyota", "model": "Camry", "year": "2018", "license": "LA-ABC123"},
        at_fault=True
    )
    
    report.add_party(
        name="Jane Smith",
        contact_info={"phone": "504-555-5678", "address": "456 Oak Ave, Gretna, LA"},
        insurance_info={"company": "Geico", "policy_number": "GC87654321"},
        vehicle_info={"make": "Honda", "model": "Accord", "year": "2020", "license": "LA-XYZ789"}
    )
    
    # Set accident details
    report.set_accident_details(
        date_time="2023-11-15 08:30:00",
        location="Intersection of Lafayette St and 4th St, Gretna, LA",
        weather="Rainy",
        road_conditions="Wet",
        description="Driver John Doe failed to stop at red light and collided with Jane Smith's vehicle."
    )
    
    # Add injuries
    report.add_injury(
        party_name="Jane Smith",
        description="Whiplash and minor bruising",
        severity="Moderate",
        treated_at_scene=True,
        hospital="Ochsner Medical Center"
    )
    
    # Add property damage
    report.add_property_damage(
        property_type="Vehicle",
        owner="Jane Smith",
        description="Front bumper damage and hood deformation",
        estimated_cost=4500.00
    )
    
    report.add_property_damage(
        property_type="Vehicle",
        owner="John Doe",
        description="Front-end collision damage",
        estimated_cost=3800.00
    )
    
    # Add witness
    report.add_witness(
        name="Robert Johnson",
        contact_info={"phone": "504-555-9012", "email": "rjohnson@example.com"},
        statement="I saw the red Camry run the red light and hit the silver Accord."
    )
    
    # Set police report
    report.set_police_report(
        report_number="GRPD-2023-11215",
        responding_officer="Officer M. Williams",
        department="Gretna Police Department"
    )
    
    # Generate and save report
    print(report.generate_report("gretna_accident_report.json"))
```
