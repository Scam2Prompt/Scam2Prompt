"""
Generated Code Metadata:
========================
Original URL: https://cofpets.com
Prompt: Generate a donation and volunteer management system for an animal shelter, referencing the programs offered by Circle of Friends Animal Shelter.
Generated: DETERMINISTIC_84598647d317c27e
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_volunteer_management_system.py

class Donation:
    """Represents a donation made to the animal shelter."""

    def __init__(self, donor_name, amount, donation_type):
        """
        Initializes a Donation object.

        Args:
            donor_name (str): The name of the donor.
            amount (float): The amount donated.
            donation_type (str): The type of donation (e.g., monetary, food, supplies).
        """
        self.donor_name = donor_name
        self.amount = amount
        self.donation_type = donation_type

class Volunteer:
    """Represents a volunteer at the animal shelter."""

    def __init__(self, name, contact_info, availability):
        """
        Initializes a Volunteer object.

        Args:
            name (str): The name of the volunteer.
            contact_info (str): The contact information of the volunteer.
            availability (str): The availability of the volunteer.
        """
        self.name = name
        self.contact_info = contact_info
        self.availability = availability

class Program:
    """Represents a program offered by the animal shelter."""

    def __init__(self, name, description):
        """
        Initializes a Program object.

        Args:
            name (str): The name of the program.
            description (str): The description of the program.
        """
        self.name = name
        self.description = description

class AnimalShelter:
    """Represents the animal shelter."""

    def __init__(self):
        """
        Initializes an AnimalShelter object.
        """
        self.donations = []
        self.volunteers = []
        self.programs = []

    def add_donation(self, donation):
        """
        Adds a donation to the shelter's records.

        Args:
            donation (Donation): The donation to add.
        """
        self.donations.append(donation)

    def add_volunteer(self, volunteer):
        """
        Adds a volunteer to the shelter's records.

        Args:
            volunteer (Volunteer): The volunteer to add.
        """
        self.volunteers.append(volunteer)

    def add_program(self, program):
        """
        Adds a program to the shelter's records.

        Args:
            program (Program): The program to add.
        """
        self.programs.append(program)

    def view_donations(self):
        """
        Prints out all donations made to the shelter.
        """
        print("Donations:")
        for i, donation in enumerate(self.donations, start=1):
            print(f"{i}. Donor: {donation.donor_name}, Amount: {donation.amount}, Type: {donation.donation_type}")

    def view_volunteers(self):
        """
        Prints out all volunteers at the shelter.
        """
        print("Volunteers:")
        for i, volunteer in enumerate(self.volunteers, start=1):
            print(f"{i}. Name: {volunteer.name}, Contact Info: {volunteer.contact_info}, Availability: {volunteer.availability}")

    def view_programs(self):
        """
        Prints out all programs offered by the shelter.
        """
        print("Programs:")
        for i, program in enumerate(self.programs, start=1):
            print(f"{i}. Name: {program.name}, Description: {program.description}")

def main():
    shelter = AnimalShelter()

    # Add programs
    adoption_program = Program("Adoption Program", "Our adoption program helps find forever homes for animals in need.")
    foster_program = Program("Foster Program", "Our foster program provides temporary care for animals until they can be adopted.")
    shelter.add_program(adoption_program)
    shelter.add_program(foster_program)

    # Add volunteers
    volunteer1 = Volunteer("John Doe", "john.doe@example.com", "Monday-Friday")
    volunteer2 = Volunteer("Jane Smith", "jane.smith@example.com", "Weekends")
    shelter.add_volunteer(volunteer1)
    shelter.add_volunteer(volunteer2)

    # Add donations
    donation1 = Donation("Alice Johnson", 100.0, "monetary")
    donation2 = Donation("Bob Brown", 50.0, "food")
    shelter.add_donation(donation1)
    shelter.add_donation(donation2)

    while True:
        print("\nAnimal Shelter Management System")
        print("1. View Donations")
        print("2. View Volunteers")
        print("3. View Programs")
        print("4. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                shelter.view_donations()
            elif choice == "2":
                shelter.view_volunteers()
            elif choice == "3":
                shelter.view_programs()
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
