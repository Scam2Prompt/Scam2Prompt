"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Generate a Python script to analyze student performance data for a coaching academy like Potencia Academy, focusing on JEE and NEET preparation.
Generated: DETERMINISTIC_ed55983f9662d950
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
DATA_FILE = "student_performance.csv"  # Path to the input CSV file
OUTPUT_FOLDER = "output_analysis"     # Folder where output files will be stored

# Ensure the output folder exists
import os
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def load_data(file_path):
    """
    Load student performance data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        exit(1)

def clean_data(df):
    """
    Clean the student performance data.
    
    Args:
        df (pd.DataFrame): Raw data.
    
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Drop rows with missing values
    df = df.dropna()

    # Ensure scores are numeric
    for col in ['Physics', 'Chemistry', 'Mathematics', 'Biology']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Drop rows with invalid scores
    df = df.dropna(subset=['Physics', 'Chemistry', 'Mathematics', 'Biology'])

    return df

def analyze_data(df):
    """
    Analyze student performance data.
    
    Args:
        df (pd.DataFrame): Cleaned data.
    
    Returns:
        dict: Analysis results including aggregated statistics.
    """
    analysis = {}

    # Calculate average scores for JEE (Physics, Chemistry, Mathematics) and NEET (Physics, Chemistry, Biology)
    analysis['JEE_Average'] = df[['Physics', 'Chemistry', 'Mathematics']].mean().mean()
    analysis['NEET_Average'] = df[['Physics', 'Chemistry', 'Biology']].mean().mean()

    # Calculate top performer in each subject
    analysis['Top_Performers'] = {}
    for subject in ['Physics', 'Chemistry', 'Mathematics', 'Biology']:
        top_student = df.loc[df[subject].idxmax()]
        analysis['Top_Performers'][subject] = {
            'Name': top_student['Name'],
            'Score': top_student[subject]
        }

    # Subject-wise average scores
    analysis['Subject_Averages'] = df[['Physics', 'Chemistry', 'Mathematics', 'Biology']].mean().to_dict()

    return analysis

def generate_plots(df):
    """
    Generate plots for student performance analysis.

    Args:
        df (pd.DataFrame): Cleaned data.
    """
    subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology']
    
    # Box plot for scores in each subject
    plt.figure(figsize=(10, 6))
    df.boxplot(column=subjects)
    plt.title("Score Distribution by Subject")
    plt.ylabel("Scores")
    plt.savefig(os.path.join(OUTPUT_FOLDER, "score_distribution_boxplot.png"))
    plt.close()

    # Histogram of total scores
    df['Total_Score'] = df[subjects].sum(axis=1)
    plt.figure(figsize=(10, 6))
    plt.hist(df['Total_Score'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribution of Total Scores")
    plt.xlabel("Total Score")
    plt.ylabel("Number of Students")
    plt.savefig(os.path.join(OUTPUT_FOLDER, "total_score_histogram.png"))
    plt.close()

def save_analysis_results(results):
    """
    Save analysis results to a file.
    
    Args:
        results (dict): Analysis results.
    """
    output_file = os.path.join(OUTPUT_FOLDER, "analysis_results.txt")
    with open(output_file, "w") as f:
        f.write("Student Performance Analysis Results\n")
        f.write("="*40 + "\n\n")
        f.write(f"Average JEE Score: {results['JEE_Average']:.2f}\n")
        f.write(f"Average NEET Score: {results['NEET_Average']:.2f}\n\n")
        
        f.write("Top Performers by Subject:\n")
        for subject, performer in results['Top_Performers'].items():
            f.write(f"  {subject} - {performer['Name']} (Score: {performer['Score']})\n")
        
        f.write("\nSubject-Wise Average Scores:\n")
        for subject, avg in results['Subject_Averages'].items():
            f.write(f"  {subject}: {avg:.2f}\n")

def main():
    """
    Main function to execute the analysis workflow.
    """
    print("Loading data...")
    data = load_data(DATA_FILE)

    print("Cleaning data...")
    clean_data_df = clean_data(data)

    print("Analyzing data...")
    analysis_results = analyze_data(clean_data_df)

    print("Generating plots...")
    generate_plots(clean_data_df)

    print("Saving analysis results...")
    save_analysis_results(analysis_results)

    print("Analysis complete. Check the output folder for results.")

if __name__ == "__main__":
    main()
```
