"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write a Python script to analyze the demographics of beneficiaries of a non-profit organization's programs, such as the Tabuk Community Development Association, assuming the data is stored in a CSV file.
Generated: DETERMINISTIC_a2bfc5a16f902968
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from datetime import datetime

def load_data(file_path):
    """
    Load demographic data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        sys.exit(1)

def clean_data(data):
    """
    Clean the demographic data by handling missing values and converting data types.
    
    Args:
        data (pandas.DataFrame): Raw demographic data.
    
    Returns:
        pandas.DataFrame: Cleaned data.
    """
    # Fill missing age values with median
    if 'age' in data.columns:
        data['age'].fillna(data['age'].median(), inplace=True)
    
    # Convert date columns to datetime if they exist
    date_columns = ['enrollment_date', 'birth_date']
    for col in date_columns:
        if col in data.columns:
            try:
                data[col] = pd.to_datetime(data[col])
            except Exception as e:
                print(f"Warning: Could not convert column '{col}' to datetime: {str(e)}")
    
    # Drop rows with missing essential columns
    essential_columns = ['gender', 'program']
    for col in essential_columns:
        if col in data.columns:
            data.dropna(subset=[col], inplace=True)
    
    return data

def analyze_demographics(data):
    """
    Analyze demographic data and generate insights.
    
    Args:
        data (pandas.DataFrame): Cleaned demographic data.
    """
    print("\nDemographic Analysis Report")
    print("=" * 50)
    
    # Basic statistics
    if 'age' in data.columns:
        print("\nAge Statistics:")
        print(data['age'].describe())
    
    # Gender distribution
    if 'gender' in data.columns:
        print("\nGender Distribution:")
        gender_counts = data['gender'].value_counts(normalize=True) * 100
        print(gender_counts)
        
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x='gender')
        plt.title("Gender Distribution")
        plt.savefig('gender_distribution.png')
        plt.close()
    
    # Program participation
    if 'program' in data.columns:
        print("\nProgram Participation:")
        program_counts = data['program'].value_counts()
        print(program_counts)
        
        plt.figure(figsize=(10, 6))
        sns.countplot(data=data, y='program', order=program_counts.index)
        plt.title("Program Participation")
        plt.savefig('program_participation.png')
        plt.close()
    
    # Age distribution by program
    if 'age' in data.columns and 'program' in data.columns:
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=data, x='program', y='age')
        plt.title("Age Distribution by Program")
        plt.xticks(rotation=45)
        plt.savefig('age_by_program.png')
        plt.close()
    
    # Enrollment trends over time
    if 'enrollment_date' in data.columns:
        data['enrollment_month'] = data['enrollment_date'].dt.to_period('M')
        monthly_enrollments = data.groupby('enrollment_month').size()
        
        plt.figure(figsize=(12, 6))
        monthly_enrollments.plot(kind='line', marker='o')
        plt.title("Monthly Enrollment Trends")
        plt.xlabel("Month")
        plt.ylabel("Number of Enrollments")
        plt.savefig('enrollment_trends.png')
        plt.close()

def main():
    """
    Main function to execute the demographic analysis.
    """
    # Configuration
    data_file = "beneficiary_data.csv"
    
    # Load and clean data
    data = load_data(data_file)
    cleaned_data = clean_data(data)
    
    # Analyze demographics
    analyze_demographics(cleaned_data)
    
    print("\nAnalysis complete. Charts saved to current directory.")

if __name__ == "__main__":
    main()
```
