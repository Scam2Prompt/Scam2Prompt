"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Generate a Python script to analyze the budget data for the Galmudug State of Somalia, referencing the Budget Framework Paper FY 2025 and the approved budget details.
Generated: DETERMINISTIC_d209960e951cbe68
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import os

def load_budget_data(file_path):
    """
    Load budget data from a CSV file.

    Args:
        file_path (str): Path to the budget data file.

    Returns:
        pd.DataFrame: DataFrame containing the budget data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not in the correct format.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    try:
        budget_data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")
    
    return budget_data

def analyze_budget_data(budget_data):
    """
    Analyze the loaded budget data.

    Args:
        budget_data (pd.DataFrame): DataFrame containing budget data.

    Returns:
        dict: Summary of the budget analysis.
    """
    try:
        # Check if required columns exist
        required_columns = ['Department', 'Category', 'Allocated Budget', 'Actual Spending']
        for column in required_columns:
            if column not in budget_data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        # Calculate total allocated budget
        total_allocated = budget_data['Allocated Budget'].sum()

        # Calculate total actual spending
        total_spent = budget_data['Actual Spending'].sum()

        # Calculate variance
        variance = total_allocated - total_spent

        # Department-wise analysis
        department_summary = budget_data.groupby('Department').agg({
            'Allocated Budget': 'sum',
            'Actual Spending': 'sum'
        }).reset_index()
        department_summary['Variance'] = department_summary['Allocated Budget'] - department_summary['Actual Spending']

        return {
            'total_allocated_budget': total_allocated,
            'total_actual_spending': total_spent,
            'overall_variance': variance,
            'department_summary': department_summary
        }
    
    except Exception as e:
        raise ValueError(f"Error analyzing budget data: {e}")

def save_analysis_results(results, output_path):
    """
    Save the analysis results to a file.

    Args:
        results (dict): Dictionary containing analysis results.
        output_path (str): Path to save the results file.

    Raises:
        ValueError: If saving the file fails.
    """
    try:
        # Save department summary to a CSV file
        department_summary = results['department_summary']
        department_summary.to_csv(output_path, index=False)
    except Exception as e:
        raise ValueError(f"Error saving analysis results: {e}")

def main():
    """
    Main function to orchestrate the loading, analysis, and saving of budget data.
    """
    try:
        # Define file paths
        input_file_path = "budget_data_galmudug.csv"  # Replace with the actual file path
        output_file_path = "budget_analysis_results.csv"

        # Load budget data
        print("Loading budget data...")
        budget_data = load_budget_data(input_file_path)

        # Analyze budget data
        print("Analyzing budget data...")
        analysis_results = analyze_budget_data(budget_data)

        # Display summary
        print(f"Total Allocated Budget: ${analysis_results['total_allocated_budget']}")
        print(f"Total Actual Spending: ${analysis_results['total_actual_spending']}")
        print(f"Overall Variance: ${analysis_results['overall_variance']}")
        
        print("\nDepartment Summary:")
        print(analysis_results['department_summary'])

        # Save analysis results
        print("Saving analysis results...")
        save_analysis_results(analysis_results, output_file_path)
        print(f"Results saved successfully to {output_file_path}")

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
