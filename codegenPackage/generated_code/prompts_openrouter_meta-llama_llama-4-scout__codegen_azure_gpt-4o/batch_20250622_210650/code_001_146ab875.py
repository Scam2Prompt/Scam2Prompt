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
# Import necessary libraries
import json

# Define a class to represent the infrastructure and facilities
class MedicalCollegeAndHospital:
    def __init__(self, name, location, facilities, hospital_name, hospital_role):
        """
        Initialize the MedicalCollegeAndHospital object.

        :param name: Name of the medical college
        :param location: Location of the medical college
        :param facilities: List of facilities available at the medical college
        :param hospital_name: Name of the associated hospital
        :param hospital_role: Role of the hospital in healthcare delivery
        """
        self.name = name
        self.location = location
        self.facilities = facilities
        self.hospital_name = hospital_name
        self.hospital_role = hospital_role

    def describe_infrastructure(self):
        """
        Generate a description of the infrastructure and facilities.

        :return: A dictionary containing the infrastructure details
        """
        return {
            "Medical College": {
                "Name": self.name,
                "Location": self.location,
                "Facilities": self.facilities
            },
            "Associated Hospital": {
                "Name": self.hospital_name,
                "Role": self.hospital_role
            }
        }

# Define a function to handle errors and display infrastructure details
def display_infrastructure_details(college):
    """
    Display the infrastructure details of the medical college and hospital.

    :param college: An instance of MedicalCollegeAndHospital
    """
    try:
        # Generate the infrastructure description
        infrastructure_details = college.describe_infrastructure()
        
        # Convert the details to a JSON string for better readability
        infrastructure_json = json.dumps(infrastructure_details, indent=4)
        
        # Print the infrastructure details
        print("Infrastructure and Facilities:")
        print(infrastructure_json)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while displaying infrastructure details: {e}")

# Main function to demonstrate the functionality
def main():
    """
    Main function to create an instance of MedicalCollegeAndHospital and display its details.
    """
    # Define the infrastructure details
    college_name = "MIMSR Medical College and Hospital"
    college_location = "Latur, Maharashtra, India"
    college_facilities = [
        "Modern lecture halls",
        "Well-equipped laboratories",
        "Library with medical resources",
        "Hostel facilities",
        "Sports and recreational facilities"
    ]
    hospital_name = "Yashwantrao Chavan Rural Hospital"
    hospital_role = (
        "Provides healthcare services to the rural population, "
        "including outpatient and inpatient care, emergency services, "
        "and specialized treatments."
    )

    # Create an instance of MedicalCollegeAndHospital
    mimsrc_college = MedicalCollegeAndHospital(
        name=college_name,
        location=college_location,
        facilities=college_facilities,
        hospital_name=hospital_name,
        hospital_role=hospital_role
    )

    # Display the infrastructure details
    display_infrastructure_details(mimsrc_college)

# Entry point of the script
if __name__ == "__main__":
    main()
```
