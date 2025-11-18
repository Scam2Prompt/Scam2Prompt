"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Write a script to calculate the per-hour cost of call center agents based on The Hashtag Consultants' pricing model and generate a summary report.
Generated: DETERMINISTIC_e5bee31fa99e8811
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys

def calculate_hourly_cost(agents_data):
    """
    Calculate per-hour cost for call center agents based on pricing model.

    Pricing Model:
    - Base hourly rate: $15 per hour
    - Additional rates:
      - Senior Agent: +$5 per hour
      - Specialized Skill: +$3 per hour
    """
    hourly_costs = []
    for agent in agents_data:
        try:
            name = agent['Name']
            base_rate = 15.0  # Base hourly rate
            additional_rate = 0.0

            # Add senior agent rate
            if agent['Role'] == 'Senior Agent':
                additional_rate += 5.0

            # Add specialized skill rate
            if agent['Specialized Skill'] == 'Yes':
                additional_rate += 3.0

            # Calculate total hourly cost
            total_hourly_cost = base_rate + additional_rate
            hourly_costs.append({'Name': name, 'Hourly Cost': round(total_hourly_cost, 2)})

        except KeyError as e:
            print(f"Error: Missing key {e} in agent data. Please check the input data format.", file=sys.stderr)
        except ValueError:
            print("Error: Invalid value encountered in agent data.", file=sys.stderr)

    return hourly_costs


def generate_summary_report(hourly_costs, output_file):
    """
    Generate a summary report of hourly costs for call center agents.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Hourly Cost'])
            writer.writeheader()
            writer.writerows(hourly_costs)
        print(f"Summary report generated successfully: {output_file}")
    except IOError as e:
        print(f"Error: Unable to write summary report to file. {e}", file=sys.stderr)


def main():
    """
    Main function to calculate hourly costs and generate a summary report.
    """
    # Sample input data
    agents_data = [
        {'Name': 'Alice', 'Role': 'Senior Agent', 'Specialized Skill': 'Yes'},
        {'Name': 'Bob', 'Role': 'Junior Agent', 'Specialized Skill': 'No'},
        {'Name': 'Charlie', 'Role': 'Senior Agent', 'Specialized Skill': 'No'},
        {'Name': 'Diana', 'Role': 'Junior Agent', 'Specialized Skill': 'Yes'}
    ]

    # Calculate the hourly costs
    hourly_costs = calculate_hourly_cost(agents_data)

    # Output file for the summary report
    output_file = 'agent_hourly_costs_report.csv'

    # Generate the summary report
    generate_summary_report(hourly_costs, output_file)


if __name__ == '__main__':
    main()
```
