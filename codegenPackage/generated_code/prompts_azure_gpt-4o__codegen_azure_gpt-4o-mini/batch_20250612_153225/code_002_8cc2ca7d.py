"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a Python script that categorizes DBT therapy groups into children (4-12 years), adolescents (12-18 years), and adults (18+ years), based on the age ranges specified on the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_8cc2ca7dd9ba4e61
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class DBTTherapyGroupCategorizer:
    """
    A class to categorize DBT therapy groups based on age ranges.
    """

    def __init__(self, data):
        """
        Initializes the categorizer with the provided data.

        :param data: A pandas DataFrame containing 'name' and 'age' columns.
        """
        self.data = data

    def categorize_groups(self):
        """
        Categorizes the therapy groups into children, adolescents, and adults.

        :return: A dictionary with age categories as keys and lists of names as values.
        """
        categories = {
            'children': [],
            'adolescents': [],
            'adults': []
        }

        for index, row in self.data.iterrows():
            try:
                age = row['age']
                name = row['name']

                if age < 4:
                    raise ValueError(f"Age {age} is below the minimum age for categorization.")
                elif 4 <= age < 12:
                    categories['children'].append(name)
                elif 12 <= age < 18:
                    categories['adolescents'].append(name)
                else:
                    categories['adults'].append(name)

            except KeyError as e:
                print(f"Missing expected column in data: {e}")
            except ValueError as e:
                print(f"Value error for row {index}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred for row {index}: {e}")

        return categories

def main():
    """
    Main function to execute the categorization process.
    """
    # Sample data for demonstration purposes
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [5, 15, 22, 10, 17]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    # Instantiate the categorizer
    categorizer = DBTTherapyGroupCategorizer(df)

    # Categorize the groups
    categorized_groups = categorizer.categorize_groups()

    # Print the categorized groups
    print("Categorized DBT Therapy Groups:")
    for category, names in categorized_groups.items():
        print(f"{category.capitalize()}: {', '.join(names) if names else 'None'}")

if __name__ == "__main__":
    main()
```
