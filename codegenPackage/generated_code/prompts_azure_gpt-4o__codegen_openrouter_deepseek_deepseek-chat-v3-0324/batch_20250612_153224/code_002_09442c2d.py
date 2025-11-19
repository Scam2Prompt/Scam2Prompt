"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Generate code to analyze survey data from child-led initiatives, such as the Campaign 2024 survey conducted by AIDA, and visualize the results using Python.
Generated: DETERMINISTIC_09442c2d14a250cc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

class SurveyAnalyzer:
    """
    A class to analyze and visualize survey data from child-led initiatives.
    """
    
    def __init__(self, data_path):
        """
        Initialize the SurveyAnalyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing survey data.
        """
        try:
            self.df = pd.read_csv(data_path)
            self.clean_data()
            print("Data loaded and cleaned successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def clean_data(self):
        """
        Clean the survey data by handling missing values and standardizing formats.
        """
        # Fill missing values with 'Unknown' for categorical data
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        self.df[categorical_cols] = self.df[categorical_cols].fillna('Unknown')
        
        # Fill numerical missing values with median
        numerical_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
        for col in numerical_cols:
            self.df[col].fillna(self.df[col].median(), inplace=True)
    
    def demographic_analysis(self, demographic_cols):
        """
        Analyze demographic distribution of survey respondents.
        
        Args:
            demographic_cols (list): List of column names containing demographic info.
        """
        for col in demographic_cols:
            if col in self.df.columns:
                plt.figure(figsize=(10, 6))
                if self.df[col].nunique() > 10:
                    # For numerical data, use histogram
                    sns.histplot(data=self.df, x=col, kde=True)
                    plt.title(f'Distribution of {col}')
                else:
                    # For categorical data, use count plot
                    sns.countplot(data=self.df, y=col, order=self.df[col].value_counts().index)
                    plt.title(f'Respondent Count by {col}')
                plt.tight_layout()
                plt.show()
            else:
                print(f"Column '{col}' not found in data.")
    
    def question_analysis(self, question_cols):
        """
        Analyze responses to survey questions.
        
        Args:
            question_cols (list): List of column names containing survey questions.
        """
        for col in question_cols:
            if col in self.df.columns:
                plt.figure(figsize=(10, 6))
                if self.df[col].nunique() > 5:
                    # For Likert scale or numerical responses
                    sns.histplot(data=self.df, x=col, bins=10)
                    plt.title(f'Distribution of Responses for: {col}')
                else:
                    # For categorical responses
                    counts = self.df[col].value_counts()
                    plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
                    plt.title(f'Response Distribution for: {col}')
                plt.tight_layout()
                plt.show()
            else:
                print(f"Column '{col}' not found in data.")
    
    def cross_analysis(self, question_col, demographic_col):
        """
        Analyze relationship between a question and demographic factor.
        
        Args:
            question_col (str): Column name of survey question.
            demographic_col (str): Column name of demographic factor.
        """
        if question_col in self.df.columns and demographic_col in self.df.columns:
            plt.figure(figsize=(12, 8))
            
            if self.df[question_col].nunique() > 5:
                # Numerical question vs categorical demographic
                sns.boxplot(data=self.df, x=demographic_col, y=question_col)
            else:
                # Categorical question vs categorical demographic
                ct = pd.crosstab(self.df[demographic_col], self.df[question_col])
                ct.plot(kind='bar', stacked=True)
            
            plt.title(f'Relationship between {question_col} and {demographic_col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("One or both columns not found in data.")
    
    def word_cloud_analysis(self, text_col):
        """
        Generate word cloud from text responses (requires wordcloud package).
        
        Args:
            text_col (str): Column name containing text responses.
        """
        try:
            from wordcloud import WordCloud
            if text_col in self.df.columns:
                text = ' '.join(response for response in self.df[text_col].astype(str))
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
                
                plt.figure(figsize=(15, 8))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title(f'Word Cloud for {text_col}')
                plt.show()
            else:
                print(f"Column '{text_col}' not found in data.")
        except ImportError:
            print("WordCloud package not installed. Install with: pip install wordcloud")
    
    def save_visualizations(self, prefix='survey_analysis'):
        """
        Save all generated visualizations to files.
        
        Args:
            prefix (str): Prefix for saved files.
        """
        import os
        os.makedirs('visualizations', exist_ok=True)
        
        for i, fig in enumerate(plt.get_fignums()):
            plt.figure(fig)
            plt.savefig(f'visualizations/{prefix}_figure_{i}.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        print(f"Visualizations saved to 'visualizations' directory with prefix '{prefix}'.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer with survey data
        analyzer = SurveyAnalyzer('campaign_2024_survey.csv')
        
        # Analyze demographics (adjust column names as needed)
        analyzer.demographic_analysis(['age', 'gender', 'location'])
        
        # Analyze survey questions (adjust column names as needed)
        analyzer.question_analysis(['q1_importance', 'q2_satisfaction', 'q3_support'])
        
        # Cross analysis between questions and demographics
        analyzer.cross_analysis('q1_importance', 'age')
        analyzer.cross_analysis('q2_satisfaction', 'gender')
        
        # Word cloud for open-ended responses (if available)
        analyzer.word_cloud_analysis('open_ended_response')
        
        # Save all visualizations
        analyzer.save_visualizations('campaign_2024')
        
    except Exception as e:
        print(f"Error in analysis: {e}")
```
