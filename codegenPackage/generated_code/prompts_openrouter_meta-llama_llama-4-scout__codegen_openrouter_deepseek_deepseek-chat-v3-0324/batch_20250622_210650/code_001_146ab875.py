"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Describe the infrastructure and facilities available at MIMSR Medical College and Hospital, including the Yashwantrao Chavan Rural Hospital, and its role in catering to the healthcare needs of the rural population.
Generated: DETERMINISTIC_146ab875176d6947
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HospitalFacility:
    """Represents a healthcare facility with its infrastructure details."""
    
    def __init__(self, name, beds, departments, special_features):
        """
        Initialize a HospitalFacility instance.
        
        Args:
            name (str): Name of the facility
            beds (int): Number of beds available
            departments (list): List of medical departments
            special_features (list): Unique features of the facility
        """
        self.name = name
        self.beds = beds
        self.departments = departments
        self.special_features = special_features
    
    def get_facility_info(self):
        """Return formatted information about the facility."""
        return (
            f"Facility Name: {self.name}\n"
            f"Bed Capacity: {self.beds}\n"
            f"Departments: {', '.join(self.departments)}\n"
            f"Special Features: {', '.join(self.special_features)}"
        )


class RuralHospital(HospitalFacility):
    """Represents a rural hospital with additional rural-specific attributes."""
    
    def __init__(self, name, beds, departments, special_features, rural_outreach_programs, mobile_units):
        """
        Initialize a RuralHospital instance.
        
        Args:
            name (str): Name of the facility
            beds (int): Number of beds available
            departments (list): List of medical departments
            special_features (list): Unique features of the facility
            rural_outreach_programs (list): Outreach programs for rural areas
            mobile_units (int): Number of mobile healthcare units
        """
        super().__init__(name, beds, departments, special_features)
        self.rural_outreach_programs = rural_outreach_programs
        self.mobile_units = mobile_units
    
    def get_rural_services(self):
        """Return information about rural-specific services."""
        return (
            f"Rural Outreach Programs: {', '.join(self.rural_outreach_programs)}\n"
            f"Mobile Healthcare Units: {self.mobile_units}"
        )


def describe_mimsr_infrastructure():
    """Describe the infrastructure of MIMSR Medical College and Hospital."""
    # Main hospital facilities
    mimsr_departments = [
        "General Medicine", "Surgery", "Pediatrics", "Obstetrics & Gynecology",
        "Orthopedics", "Ophthalmology", "ENT", "Dermatology",
        "Psychiatry", "Radiology", "Pathology", "Anesthesiology"
    ]
    
    mimsr_features = [
        "24/7 Emergency Services", "ICU", "NICU", "Operation Theaters",
        "Blood Bank", "Diagnostic Labs", "Pharmacy", "Medical College"
    ]
    
    mimsr = HospitalFacility(
        name="MIMSR Medical College and Hospital",
        beds=750,
        departments=mimsr_departments,
        special_features=mimsr_features
    )
    
    # Yashwantrao Chavan Rural Hospital facilities
    rural_departments = [
        "General Medicine", "Pediatrics", "Obstetrics & Gynecology",
        "General Surgery", "Dermatology", "Dental"
    ]
    
    rural_features = [
        "24/7 Emergency Services", "Basic ICU", "Labor & Delivery Unit",
        "Minor Operation Theater", "Diagnostic Services", "Pharmacy"
    ]
    
    outreach_programs = [
        "Village Health Camps", "Immunization Drives",
        "Maternal Health Programs", "Health Education Workshops"
    ]
    
    ycr_hospital = RuralHospital(
        name="Yashwantrao Chavan Rural Hospital",
        beds=150,
        departments=rural_departments,
        special_features=rural_features,
        rural_outreach_programs=outreach_programs,
        mobile_units=5
    )
    
    # Generate report
    report = (
        "MIMSR Medical College and Hospital Infrastructure:\n"
        "-------------------------------------------------\n"
        f"{mimsr.get_facility_info()}\n\n"
        "Yashwantrao Chavan Rural Hospital:\n"
        "---------------------------------\n"
        f"{ycr_hospital.get_facility_info()}\n"
        f"{ycr_hospital.get_rural_services()}\n\n"
        "Role in Rural Healthcare:\n"
        "-------------------------\n"
        "1. Provides affordable healthcare to rural population\n"
        "2. Offers specialized medical education with rural focus\n"
        "3. Conducts regular outreach programs in villages\n"
        "4. Mobile units provide healthcare access in remote areas\n"
        "5. Serves as referral center for primary health centers"
    )
    
    return report


if __name__ == "__main__":
    try:
        hospital_report = describe_mimsr_infrastructure()
        print(hospital_report)
    except Exception as e:
        print(f"Error generating hospital infrastructure report: {str(e)}")
```
