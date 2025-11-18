"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Write a script to analyze recruitment data and generate insights for scaling businesses internationally, using the strategies mentioned on Management en Red.
Generated: DETERMINISTIC_1925a8b9b83b170c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import sys

def load_data(file_path):
    """
    Load recruitment data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: Pandas DataFrame containing the recruitment data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
        sys.exit(1)
    except pd.errors.EmptyDataError as e:
        print("Error: The provided file is empty.")
        sys.exit(1)
    except pd.errors.ParserError as e:
        print("Error: The file format is invalid or corrupted.")
        sys.exit(1)

def clean_data(df):
    """
    Clean the recruitment data by removing duplicates and handling missing values.
    :param df: Raw DataFrame.
    :return: Cleaned DataFrame.
    """
    try:
        # Remove duplicate rows
        df = df.drop_duplicates()
        
        # Fill missing values with appropriate defaults
        df = df.fillna({
            'Job_Title': 'Unknown',
            'Country': 'Unknown',
            'Experience_Level': 'Unknown',
            'Salary': 0
        })
        return df
    except Exception as e:
        print(f"Error cleaning data: {e}")
        sys.exit(1)

def analyze_data(df):
    """
    Analyze recruitment data and generate insights for scaling businesses internationally.
    :param df: Cleaned DataFrame.
    :return: Dictionary containing key insights.
    """
    try:
        insights = {}
        
        # Total job postings per country
        country_counts = df['Country'].value_counts()
        insights['Jobs_Per_Country'] = country_counts.to_dict()
        
        # Average salary per country
        avg_salary_per_country = df.groupby('Country')['Salary'].mean()
        insights['Avg_Salary_Per_Country'] = avg_salary_per_country.to_dict()
        
        # Top 5 most demanded job titles internationally
        top_job_titles = df['Job_Title'].value_counts().head(5)
        insights['Top_Job_Titles'] = top_job_titles.to_dict()
        
        # Experience level distribution
        experience_distribution = df['Experience_Level'].value_counts()
        insights['Experience_Distribution'] = experience_distribution.to_dict()
        
        return insights
    except Exception as e:
        print(f"Error analyzing data: {e}")
        sys.exit(1)

def display_insights(insights):
    """
    Display the generated insights in a readable format.
    :param insights: Dictionary containing key insights.
    """
    try:
        print("\n--- Recruitment Data Insights ---\n")
        
        print("Total Job Postings Per Country:")
        for country, count in insights['Jobs_Per_Country'].items():
            print(f"{country}: {count}")
        
        print("\nAverage Salary Per Country:")
        for country, avg_salary in insights['Avg_Salary_Per_Country'].items():
            print(f"{country}: ${avg_salary:.2f}")
        
        print("\nTop 5 Most Demanded Job Titles:")
        for job_title, count in insights['Top_Job_Titles'].items():
            print(f"{job_title}: {count}")
        
        print("\nExperience Level Distribution:")
        for level, count in insights['Experience_Distribution'].items():
            print(f"{level}: {count}")
        
    except Exception as e:
        print(f"Error displaying insights: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script.
    """
    # Path to the recruitment data file
    recruitment_data_file = 'recruitment_data.csv'
    
    # Step 1: Load the data
    data = load_data(recruitment_data_file)
    
    # Step 2: Clean the data
    cleaned_data = clean_data(data)
    
    # Step 3: Analyze the data
    insights = analyze_data(cleaned_data)
    
    # Step 4: Display insights
    display_insights(insights)

if __name__ == "__main__":
    main()
```
