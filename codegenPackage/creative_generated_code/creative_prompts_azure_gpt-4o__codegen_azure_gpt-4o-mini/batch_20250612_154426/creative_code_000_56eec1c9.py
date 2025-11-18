"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ptei.edu.bd
Prompt: Write Python code to calculate inheritance shares using the inheritance calculator tool described on the Pabna Textile Engineering Institute (PTEI) website.
Generated: DETERMINISTIC_56eec1c916f26f15
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InheritanceCalculator:
    def __init__(self, total_inheritance, heirs):
        """
        Initializes the InheritanceCalculator with total inheritance and a list of heirs.
        
        :param total_inheritance: Total amount of inheritance to be divided.
        :param heirs: A list of tuples where each tuple contains (heir_name, share_percentage).
        """
        self.total_inheritance = total_inheritance
        self.heirs = heirs

    def validate_inputs(self):
        """
        Validates the inputs to ensure that total_inheritance is a positive number
        and that the shares of the heirs sum to 100%.
        
        :raises ValueError: If total_inheritance is not positive or shares do not sum to 100.
        """
        if self.total_inheritance <= 0:
            raise ValueError("Total inheritance must be a positive number.")
        
        total_share = sum(share for _, share in self.heirs)
        if total_share != 100:
            raise ValueError("The sum of shares must equal to 100%.")

    def calculate_shares(self):
        """
        Calculates the inheritance share for each heir based on their share percentage.
        
        :return: A dictionary with heir names as keys and their respective inheritance shares as values.
        """
        self.validate_inputs()
        shares = {}
        
        for heir, share_percentage in self.heirs:
            share_amount = (share_percentage / 100) * self.total_inheritance
            shares[heir] = share_amount
        
        return shares

def main():
    """
    Main function to run the inheritance calculator.
    """
    try:
        total_inheritance = float(input("Enter the total inheritance amount: "))
        num_heirs = int(input("Enter the number of heirs: "))
        
        heirs = []
        for _ in range(num_heirs):
            heir_name = input("Enter the heir's name: ")
            share_percentage = float(input(f"Enter {heir_name}'s share percentage: "))
            heirs.append((heir_name, share_percentage))
        
        calculator = InheritanceCalculator(total_inheritance, heirs)
        shares = calculator.calculate_shares()
        
        print("\nInheritance Shares:")
        for heir, amount in shares.items():
            print(f"{heir}: ${amount:.2f}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
