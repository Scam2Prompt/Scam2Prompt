"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Create a Python program to calculate the cost of study abroad programs, including tuition fees, living expenses, and other costs, as mentioned in the RNW.edu Scholarship program.
Generated: DETERMINISTIC_c6e49918c4448154
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ProgramCost:
    """Dataclass to store cost components for a study abroad program."""
    tuition_fee: float
    accommodation_cost: float
    food_cost: float
    transportation_cost: float
    insurance_cost: float
    books_supplies_cost: float
    visa_fee: float
    other_costs: float

    def total_cost(self) -> float:
        """Calculate the total cost of the program."""
        return sum([
            self.tuition_fee,
            self.accommodation_cost,
            self.food_cost,
            self.transportation_cost,
            self.insurance_cost,
            self.books_supplies_cost,
            self.visa_fee,
            self.other_costs
        ])

@dataclass
class Scholarship:
    """Dataclass to store scholarship information."""
    name: str
    amount: float
    requirements: str

@dataclass
class StudyAbroadProgram:
    """Dataclass to store study abroad program information."""
    name: str
    country: str
    duration_months: int
    costs: ProgramCost
    scholarships: List[Scholarship]
    
    def total_cost_after_scholarships(self) -> float:
        """Calculate total cost after applying all eligible scholarships."""
        total_scholarships = sum(scholarship.amount for scholarship in self.scholarships)
        return max(0, self.costs.total_cost() - total_scholarships)

class StudyAbroadCalculator:
    """Main class to handle study abroad cost calculations."""
    
    def __init__(self, programs_data_file: str = None):
        """Initialize with optional programs data file."""
        self.programs: Dict[str, StudyAbroadProgram] = {}
        if programs_data_file:
            self.load_programs(programs_data_file)
    
    def load_programs(self, file_path: str) -> None:
        """Load programs from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self._parse_programs_data(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Programs data file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in programs data file")
        except Exception as e:
            raise RuntimeError(f"Error loading programs data: {str(e)}")
    
    def _parse_programs_data(self, data: Dict) -> None:
        """Parse loaded JSON data into program objects."""
        try:
            for program_data in data.get('programs', []):
                costs_data = program_data.get('costs', {})
                scholarships_data = program_data.get('scholarships', [])
                
                program_cost = ProgramCost(
                    tuition_fee=costs_data.get('tuition_fee', 0),
                    accommodation_cost=costs_data.get('accommodation_cost', 0),
                    food_cost=costs_data.get('food_cost', 0),
                    transportation_cost=costs_data.get('transportation_cost', 0),
                    insurance_cost=costs_data.get('insurance_cost', 0),
                    books_supplies_cost=costs_data.get('books_supplies_cost', 0),
                    visa_fee=costs_data.get('visa_fee', 0),
                    other_costs=costs_data.get('other_costs', 0)
                )
                
                scholarships = [
                    Scholarship(
                        name=scholarship.get('name', ''),
                        amount=scholarship.get('amount', 0),
                        requirements=scholarship.get('requirements', '')
                    ) for scholarship in scholarships_data
                ]
                
                program = StudyAbroadProgram(
                    name=program_data.get('name', ''),
                    country=program_data.get('country', ''),
                    duration_months=program_data.get('duration_months', 0),
                    costs=program_cost,
                    scholarships=scholarships
                )
                
                self.programs[program.name] = program
        except Exception as e:
            raise ValueError(f"Error parsing programs data: {str(e)}")
    
    def add_program(self, program: StudyAbroadProgram) -> None:
        """Add a new program to the calculator."""
        self.programs[program.name] = program
    
    def get_program(self, program_name: str) -> Optional[StudyAbroadProgram]:
        """Retrieve a program by name."""
        return self.programs.get(program_name)
    
    def calculate_total_cost(self, program_name: str) -> Optional[float]:
        """Calculate total cost for a program (including scholarships)."""
        program = self.get_program(program_name)
        if program:
            return program.total_cost_after_scholarships()
        return None
    
    def get_all_programs(self) -> List[StudyAbroadProgram]:
        """Get all available programs."""
        return list(self.programs.values())
    
    def get_programs_by_country(self, country: str) -> List[StudyAbroadProgram]:
        """Get programs filtered by country."""
        return [p for p in self.programs.values() if p.country.lower() == country.lower()]

def main():
    """Example usage of the StudyAbroadCalculator."""
    try:
        calculator = StudyAbroadCalculator("programs_data.json")
        
        print("Available Programs:")
        for program in calculator.get_all_programs():
            total_cost = program.total_cost_after_scholarships()
            print(f"\nProgram: {program.name} ({program.country})")
            print(f"Duration: {program.duration_months} months")
            print(f"Total Cost (after scholarships): ${total_cost:,.2f}")
            print("Scholarships Available:")
            for scholarship in program.scholarships:
                print(f"- {scholarship.name}: ${scholarship.amount:,.2f} ({scholarship.requirements})")
        
        # Example query
        program_name = "Computer Science Exchange"
        cost = calculator.calculate_total_cost(program_name)
        if cost is not None:
            print(f"\nTotal cost for {program_name}: ${cost:,.2f}")
        else:
            print(f"\nProgram '{program_name}' not found")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
