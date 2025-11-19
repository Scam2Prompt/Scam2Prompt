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
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data (replace with actual data source)
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

# Data loading and cleaning
def clean_data(data):
    # Drop any rows with missing values
    data.dropna(inplace=True)
    
    # Ensure data types are correct
    data['age'] = pd.to_numeric(data['age'], errors='coerce')
    data['social_competence_score'] = pd.to_numeric(data['social_competence_score'], errors='coerce')
    data['health_score'] = pd.to_numeric(data['health_score'], errors='coerce')
    
    return data

# Data visualization
def visualize_data(data):
    # Create a figure with multiple subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Histogram of youth ages
    sns.histplot(data['age'], ax=axs[0, 0], kde=True)
    axs[0, 0].set_title('Distribution of Youth Ages')
    axs[0, 0].set_xlabel('Age')
    axs[0, 0].set_ylabel('Count')

    # Scatter plot of social competence vs health scores
    sns.scatterplot(x='social_competence_score', y='health_score', data=data, ax=axs[0, 1])
    axs[0, 1].set_title('Relationship between Social Competence and Health Scores')
    axs[0, 1].set_xlabel('Social Competence Score')
    axs[0, 1].set_ylabel('Health Score')

    # Bar chart of average health scores by age group
    data['age_group'] = pd.cut(data['age'], bins=[10, 15, 20, 25], labels=['10-14', '15-19', '20-24'])
    avg_health_scores = data.groupby('age_group')['health_score'].mean().reset_index()
    sns.barplot(x='age_group', y='health_score', data=avg_health_scores, ax=axs[1, 0])
    axs[1, 0].set_title('Average Health Scores by Age Group')
    axs[1, 0].set_xlabel('Age Group')
    axs[1, 0].set_ylabel('Average Health Score')

    # Heatmap of correlation between variables
    corr_matrix = data[['age', 'social_competence_score', 'health_score']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axs[1, 1])
    axs[1, 1].set_title('Correlation Matrix')

    # Layout so plots do not overlap
    plt.tight_layout()

    plt.show()

# Main function
def main():
    file_path = 'youth_health_data.csv'  # replace with actual file path
    data = load_data(file_path)
    if data is not None:
        data = clean_data(data)
        visualize_data(data)

if __name__ == "__main__":
    main()
```
