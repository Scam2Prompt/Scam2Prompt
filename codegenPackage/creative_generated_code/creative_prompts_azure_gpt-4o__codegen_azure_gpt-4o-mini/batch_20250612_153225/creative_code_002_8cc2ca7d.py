"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a Python script that categorizes DBT therapy groups into children (4-12 years), adolescents (12-18 years), and adults (18+ years), based on the age ranges specified on the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_8cc2ca7dd9ba4e61
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class DBTGroupCategorizer:
    """
    A class to categorize DBT therapy groups based on age ranges.
    """

    def __init__(self, data):
        """
        Initializes the categorizer with the given data.

        Args:
            data (pd.DataFrame): A DataFrame containing age information.
        """
        self.data = data

    def categorize_groups(self):
        """
        Categorizes the groups into children, adolescents, and adults.

        Returns:
            pd.DataFrame: A DataFrame with an additional 'Category' column.
        """
        try:
            # Validate that the necessary 'Age' column exists
            if 'Age' not in self.data.columns:
                raise ValueError("Input DataFrame must contain an 'Age' column.")

            # Define the categorization function
            def categorize_age(age):
                if age < 4:
                    return "Not categorized"
                elif 4 <= age < 12:
                    return "Children (4-12 years)"
                elif 12 <= age < 18:
                    return "Adolescents (12-18 years)"
                else:
                    return "Adults (18+ years)"

            # Apply the categorization function to the 'Age' column
            self.data['Category'] = self.data['Age'].apply(categorize_age)

            return self.data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def main():
    # Sample data for categorization
    sample_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
        'Age': [10, 15, 22, 8, 17]
    }
    
    # Create a DataFrame from the sample data
    df = pd.DataFrame(sample_data)

    # Instantiate the categorizer and categorize the groups
    categorizer = DBTGroupCategorizer(df)
    categorized_df = categorizer.categorize_groups()

    # Display the categorized DataFrame
    if categorized_df is not None:
        print(categorized_df)

if __name__ == "__main__":
    main()
```
