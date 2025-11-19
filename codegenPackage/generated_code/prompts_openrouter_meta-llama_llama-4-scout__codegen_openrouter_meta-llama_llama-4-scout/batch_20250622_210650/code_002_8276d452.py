"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: What are the details of the academic programs offered at MIMSR, including the intake capacity for UG and PG students, and the various departments and specialties available?
Generated: DETERMINISTIC_8276d45287d85bcf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mimsr_academic_programs.py

class AcademicProgram:
    def __init__(self, name, intake_capacity, department, specialty):
        """
        Represents an academic program at MIMSR.

        Args:
            name (str): Name of the program.
            intake_capacity (int): Intake capacity of the program.
            department (str): Department offering the program.
            specialty (str): Specialty of the program.
        """
        self.name = name
        self.intake_capacity = intake_capacity
        self.department = department
        self.specialty = specialty

class MIMSR:
    def __init__(self):
        """
        Represents MIMSR and its academic programs.
        """
        self.ug_programs = []
        self.pg_programs = []

    def add_ug_program(self, program):
        """
        Adds an undergraduate program.

        Args:
            program (AcademicProgram): Program to add.
        """
        self.ug_programs.append(program)

    def add_pg_program(self, program):
        """
        Adds a postgraduate program.

        Args:
            program (AcademicProgram): Program to add.
        """
        self.pg_programs.append(program)

    def get_ug_programs(self):
        """
        Gets the undergraduate programs.

        Returns:
            list[AcademicProgram]: Undergraduate programs.
        """
        return self.ug_programs

    def get_pg_programs(self):
        """
        Gets the postgraduate programs.

        Returns:
            list[AcademicProgram]: Postgraduate programs.
        """
        return self.pg_programs

def main():
    try:
        # Create MIMSR
        mimsr = MIMSR()

        # Add UG programs
        mimsr.add_ug_program(AcademicProgram("MBBS", 150, "Medical", "General Medicine"))
        mimsr.add_ug_program(AcademicProgram("BDS", 50, "Dental", "Dentistry"))

        # Add PG programs
        mimsr.add_pg_program(AcademicProgram("MD - General Medicine", 10, "Medical", "General Medicine"))
        mimsr.add_pg_program(AcademicProgram("MS - General Surgery", 8, "Surgical", "General Surgery"))
        mimsr.add_pg_program(AcademicProgram("MDS - Orthodontics", 5, "Dental", "Orthodontics"))

        # Get UG programs
        print("Undergraduate Programs:")
        for i, program in enumerate(mimsr.get_ug_programs()):
            print(f"{i+1}. {program.name} - Intake Capacity: {program.intake_capacity}, Department: {program.department}, Specialty: {program.specialty}")

        # Get PG programs
        print("\nPostgraduate Programs:")
        for i, program in enumerate(mimsr.get_pg_programs()):
            print(f"{i+1}. {program.name} - Intake Capacity: {program.intake_capacity}, Department: {program.department}, Specialty: {program.specialty}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
