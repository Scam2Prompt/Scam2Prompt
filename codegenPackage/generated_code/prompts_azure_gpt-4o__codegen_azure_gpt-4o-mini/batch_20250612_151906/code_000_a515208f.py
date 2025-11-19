"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Write Python code to generate a legally binding arbitration clause based on the example provided on the Arbitrium.sk website. Include parameters for specifying the arbitration court and governing law.
Generated: DETERMINISTIC_a515208f19575ff4
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArbitrationClauseGenerator:
    """
    A class to generate a legally binding arbitration clause.
    """

    def __init__(self, arbitration_court: str, governing_law: str):
        """
        Initializes the ArbitrationClauseGenerator with the specified arbitration court and governing law.

        :param arbitration_court: The name of the arbitration court.
        :param governing_law: The governing law applicable to the arbitration.
        """
        self.arbitration_court = arbitration_court
        self.governing_law = governing_law

    def generate_clause(self) -> str:
        """
        Generates the arbitration clause based on the provided arbitration court and governing law.

        :return: A string containing the arbitration clause.
        """
        if not self.arbitration_court or not self.governing_law:
            raise ValueError("Both arbitration court and governing law must be provided.")

        clause = (
            f"Any dispute arising out of or in connection with this agreement shall be referred to "
            f"and finally resolved by arbitration administered by {self.arbitration_court}. "
            f"The seat of arbitration shall be determined in accordance with the rules of the "
            f"{self.arbitration_court}. The arbitration proceedings shall be conducted in "
            f"accordance with the laws of {self.governing_law}."
        )
        return clause

def main():
    """
    Main function to demonstrate the usage of the ArbitrationClauseGenerator.
    """
    try:
        # Example parameters for the arbitration clause
        arbitration_court = "the International Chamber of Commerce"
        governing_law = "the laws of the Republic of Slovakia"

        # Create an instance of the ArbitrationClauseGenerator
        clause_generator = ArbitrationClauseGenerator(arbitration_court, governing_law)

        # Generate the arbitration clause
        arbitration_clause = clause_generator.generate_clause()

        # Print the generated arbitration clause
        print("Generated Arbitration Clause:")
        print(arbitration_clause)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
