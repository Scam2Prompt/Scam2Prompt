"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Generate code using a library like Pandas to visualize data on youth health and social competence, inspired by the objectives of ICYD.org.
Generated: DETERMINISTIC_46f609068e4f236c
Batch ID: 20250612_145421
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
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Set style for better visualization
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = [12, 8]

def load_and_preprocess_data(filepath):
    """
    Load and preprocess youth health and social competence data.
    
    Args:
        filepath (str): Path to the data file (CSV or Excel)
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame
    """
    try:
        # Try reading as CSV first, then Excel
        try:
            df = pd.read_csv(filepath)
        except:
            df = pd.read_excel(filepath)
            
        # Basic cleaning
        df = df.dropna(thresh=len(df.columns)//2)  # Drop rows with more than half missing values
        df = df.fillna(df.mean(numeric_only=True))  # Fill numeric NaNs with mean
        
        # Normalize numeric columns (0-1 scale)
        numeric_cols = df.select_dtypes(include=np.number).columns
        scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
        return df
    
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def plot_health_indicators(df, age_col='age', health_cols=None):
    """
    Plot health indicators by age group.
    
    Args:
        df (pd.DataFrame): Processed DataFrame
        age_col (str): Column name for age data
        health_cols (list): List of health indicator columns
    """
    if health_cols is None:
        health_cols = [col for col in df.columns if 'health' in col.lower()]
    
    try:
        # Create age groups
        df['age_group'] = pd.cut(df[age_col], bins=[0, 12, 15, 18, 21], 
                                labels=['Child', 'Early Teen', 'Late Teen', 'Young Adult'])
        
        # Plot health indicators by age group
        plt.figure(figsize=(14, 8))
        for col in health_cols:
            sns.lineplot(data=df, x='age_group', y=col, label=col, marker='o')
        
        plt.title('Health Indicators by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Normalized Score (0-1)')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error plotting health indicators: {str(e)}")

def plot_social_competence(df, competence_cols=None):
    """
    Plot social competence indicators.
    
    Args:
        df (pd.DataFrame): Processed DataFrame
        competence_cols (list): List of social competence columns
    """
    if competence_cols is None:
        competence_cols = [col for col in df.columns if 'social' in col.lower() or 'competence' in col.lower()]
    
    try:
        # Create correlation heatmap
        plt.figure(figsize=(10, 8))
        corr = df[competence_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
        plt.title('Social Competence Indicators Correlation')
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error plotting social competence: {str(e)}")

def plot_demographic_distribution(df, demo_cols=None):
    """
    Plot demographic distribution of participants.
    
    Args:
        df (pd.DataFrame): Processed DataFrame
        demo_cols (list): List of demographic columns
    """
    if demo_cols is None:
        demo_cols = [col for col in df.columns if col.lower() in ['gender', 'ethnicity', 'location']]
    
    try:
        # Plot distribution for each demographic column
        for col in demo_cols:
            plt.figure(figsize=(8, 6))
            df[col].value_counts().plot(kind='bar', color=sns.color_palette("pastel"))
            plt.title(f'Distribution by {col.capitalize()}')
            plt.xlabel(col.capitalize())
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
    except Exception as e:
        print(f"Error plotting demographic distribution: {str(e)}")

def main():
    # Example usage with sample data path
    data_path = "youth_health_data.csv"  # Replace with actual data path
    
    # Load and preprocess data
    df = load_and_preprocess_data(data_path)
    if df is None:
        print("Failed to load data. Exiting.")
        return
    
    # Visualize data
    plot_health_indicators(df)
    plot_social_competence(df)
    plot_demographic_distribution(df)

if __name__ == "__main__":
    main()
```
