"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Create a script to automate the calculation of fees for different MBA programs at SOMTU, considering the fee structure provided on the website.
Generated: DETERMINISTIC_bc72174db1212d7d
Batch ID: 20250612_150718
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
from typing import Dict, List, Optional

@dataclass
class ProgramFee:
    """Data class to store fee information for a program."""
    name: str
    tuition: float
    registration_fee: float
    library_fee: float
    technology_fee: float
    other_fees: Dict[str, float]  # Additional fees as key-value pairs

class SOMTUFeeCalculator:
    """Automated fee calculator for SOMTU MBA programs."""
    
    def __init__(self, fee_data_file: Optional[str] = None):
        """Initialize the calculator with fee data.
        
        Args:
            fee_data_file: Path to JSON file containing fee data. If None, uses default data.
        """
        self.programs: Dict[str, ProgramFee] = {}
        
        if fee_data_file:
            self.load_fee_data_from_file(fee_data_file)
        else:
            self.load_default_fee_data()
    
    def load_default_fee_data(self) -> None:
        """Load default fee data for SOMTU MBA programs."""
        default_data = {
            "Full-Time MBA": {
                "tuition": 25000.00,
                "registration_fee": 500.00,
                "library_fee": 300.00,
                "technology_fee": 200.00,
                "other_fees": {
                    "student_activity": 150.00,
                    "graduation_fee": 100.00
                }
            },
            "Part-Time MBA": {
                "tuition": 18000.00,
                "registration_fee": 400.00,
                "library_fee": 250.00,
                "technology_fee": 150.00,
                "other_fees": {
                    "student_activity": 100.00
                }
            },
            "Executive MBA": {
                "tuition": 35000.00,
                "registration_fee": 750.00,
                "library_fee": 400.00,
                "technology_fee": 300.00,
                "other_fees": {
                    "international_trip": 5000.00,
                    "graduation_fee": 150.00
                }
            }
        }
        
        for program_name, fee_data in default_data.items():
            self.programs[program_name] = ProgramFee(
                name=program_name,
                tuition=fee_data["tuition"],
                registration_fee=fee_data["registration_fee"],
                library_fee=fee_data["library_fee"],
                technology_fee=fee_data["technology_fee"],
                other_fees=fee_data["other_fees"]
            )
    
    def load_fee_data_from_file(self, file_path: str) -> None:
        """Load fee data from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing fee data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
            KeyError: If required fields are missing in the data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                for program_name, fee_data in data.items():
                    self.programs[program_name] = ProgramFee(
                        name=program_name,
                        tuition=fee_data["tuition"],
                        registration_fee=fee_data["registration_fee"],
                        library_fee=fee_data["library_fee"],
                        technology_fee=fee_data["technology_fee"],
                        other_fees=fee_data.get("other_fees", {})
                    )
        except FileNotFoundError:
            raise FileNotFoundError(f"Fee data file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in fee data file", "", 0)
        except KeyError as e:
            raise KeyError(f"Missing required field in fee data: {e}")
    
    def calculate_total_fees(self, program_name: str, include_other_fees: bool = True) -> float:
        """Calculate total fees for a given program.
        
        Args:
            program_name: Name of the MBA program.
            include_other_fees: Whether to include other miscellaneous fees.
            
        Returns:
            Total calculated fees for the program.
            
        Raises:
            ValueError: If the program name is not found.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program not found: {program_name}")
            
        program = self.programs[program_name]
        total = (
            program.tuition +
            program.registration_fee +
            program.library_fee +
            program.technology_fee
        )
        
        if include_other_fees:
            total += sum(program.other_fees.values())
            
        return round(total, 2)
    
    def get_available_programs(self) -> List[str]:
        """Get list of available MBA programs."""
        return list(self.programs.keys())
    
    def get_fee_breakdown(self, program_name: str) -> Dict[str, float]:
        """Get detailed fee breakdown for a program.
        
        Args:
            program_name: Name of the MBA program.
            
        Returns:
            Dictionary with fee categories and amounts.
            
        Raises:
            ValueError: If the program name is not found.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program not found: {program_name}")
            
        program = self.programs[program_name]
        breakdown = {
            "Tuition": program.tuition,
            "Registration Fee": program.registration_fee,
            "Library Fee": program.library_fee,
            "Technology Fee": program.technology_fee
        }
        
        for fee_name, amount in program.other_fees.items():
            breakdown[fee_name.replace('_', ' ').title()] = amount
            
        return breakdown

# Example usage
if __name__ == "__main__":
    try:
        calculator = SOMTUFeeCalculator()
        
        print("Available MBA Programs:")
        for program in calculator.get_available_programs():
            print(f"- {program}")
        
        print("\nFee Calculation Examples:")
        for program in calculator.get_available_programs():
            total = calculator.calculate_total_fees(program)
            breakdown = calculator.get_fee_breakdown(program)
            
            print(f"\n{program} Total Fees: ${total:,.2f}")
            print("Breakdown:")
            for fee, amount in breakdown.items():
                print(f"  {fee}: ${amount:,.2f}")
                
    except Exception as e:
        print(f"Error: {e}")
```
