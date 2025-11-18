"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Suggest a library for creating interactive visualizations of PSHP's career guidance and capacity-building programs for pharmacists across Pakistan.
Generated: DETERMINISTIC_e47f35808cb8f87c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import plotly.express as px  # For creating interactive visualizations
import pandas as pd          # For data manipulation and storage

# Function to create an interactive visualization for PSHP's programs
def create_visualization(data_file):
    """
    Function to create an interactive visualization of career guidance and capacity-building programs
    conducted by PSHP for pharmacists across Pakistan.

    Args:
        data_file (str): Path to the CSV file containing the program data.
                         The CSV should include the following columns:
                         'Program Name', 'City', 'Number of Participants', 'Year'

    Returns:
        None. Displays the interactive visualization.
    """
    try:
        # Load the data from a CSV file
        data = pd.read_csv(data_file)

        # Validate that required columns exist in the dataset
        required_columns = ['Program Name', 'City', 'Number of Participants', 'Year']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Create an interactive scatter plot
        fig = px.scatter(
            data,
            x='Year',
            y='Number of Participants',
            color='City',
            size='Number of Participants',
            hover_name='Program Name',
            title="PSHP Career Guidance and Capacity-Building Programs",
            labels={
                'Year': 'Year of Program',
                'Number of Participants': 'Participants',
                'City': 'City of Program'
            }
        )

        # Display the visualization
        fig.show()

    except FileNotFoundError:
        print(f"Error: The file {data_file} was not found. Please check the file path.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
# NOTE: Replace 'program_data.csv' with the actual path to your CSV file containing program data.
create_visualization('program_data.csv')
```

This code uses `plotly.express` to create interactive visualizations and handles common errors like missing files or incorrect data formats. Ensure your dataset is properly formatted before running the code.
