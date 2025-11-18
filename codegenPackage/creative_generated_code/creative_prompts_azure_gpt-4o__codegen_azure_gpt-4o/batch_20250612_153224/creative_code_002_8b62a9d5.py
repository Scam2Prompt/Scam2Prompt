"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gbngroup.com.mx
Prompt: Generate code to simulate a "Mystery Shopper" evaluation process, incorporating customer segmentation and satisfaction metrics as outlined by GBN Group.
Generated: DETERMINISTIC_8b62a9d5206ee913
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define constants for customer segmentation and satisfaction levels
CUSTOMER_SEGMENTS = ['Budget', 'Mid-range', 'Luxury']
SATISFACTION_LEVELS = ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']

class MysteryShopper:
    """
    Class for simulating a Mystery Shopper evaluation process.
    """
    def __init__(self):
        self.evaluation_records = []

    def simulate_shopper_experience(self):
        """
        Simulates a single shopper experience.
        Randomly assigns a customer segment and satisfaction level.
        """
        segment = random.choice(CUSTOMER_SEGMENTS)
        satisfaction = random.choice(SATISFACTION_LEVELS)
        record = {
            'Customer Segment': segment,
            'Satisfaction Level': satisfaction
        }
        self.evaluation_records.append(record)

    def simulate_multiple_experiences(self, num_experiences):
        """
        Simulates multiple shopper experiences.

        Args:
            num_experiences (int): Number of experiences to simulate.
        """
        try:
            if num_experiences <= 0:
                raise ValueError("Number of experiences must be greater than zero.")
            
            for _ in range(num_experiences):
                self.simulate_shopper_experience()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_summary(self):
        """
        Provides a summary of the evaluation records.

        Returns:
            dict: Summary of satisfaction levels within each customer segment.
        """
        summary = {segment: {level: 0 for level in SATISFACTION_LEVELS} for segment in CUSTOMER_SEGMENTS}
        
        for record in self.evaluation_records:
            segment = record['Customer Segment']
            satisfaction = record['Satisfaction Level']
            summary[segment][satisfaction] += 1
        
        return summary

    def display_summary(self):
        """
        Displays the summary of the evaluation records in a formatted manner.
        """
        summary = self.get_summary()
        
        print("\nMystery Shopper Evaluation Summary:")
        for segment, satisfaction_data in summary.items():
            print(f"\nCustomer Segment: {segment}")
            for satisfaction, count in satisfaction_data.items():
                print(f"  {satisfaction}: {count}")


def main():
    """
    Main entry point for the Mystery Shopper evaluation simulation.
    """
    try:
        print("Welcome to the Mystery Shopper Evaluation Simulation!")
        num_experiences = int(input("Enter the number of shopper experiences to simulate: "))
        
        # Initialize the Mystery Shopper simulation
        simulation = MysteryShopper()
        simulation.simulate_multiple_experiences(num_experiences)
        
        # Display the summary
        simulation.display_summary()
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
