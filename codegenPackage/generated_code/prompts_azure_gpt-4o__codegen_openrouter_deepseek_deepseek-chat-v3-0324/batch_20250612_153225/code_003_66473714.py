"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Generate code to analyze societal impacts of AI and automation, as highlighted in the "KI und Gesellschaft" article on ScienceArtThinking.de. Use Python libraries for data visualization to present trends.
Generated: DETERMINISTIC_664737142fc4c6b5
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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

class AIImpactAnalyzer:
    """
    A class to analyze and visualize societal impacts of AI and automation.
    """
    
    def __init__(self):
        """
        Initialize the analyzer with sample data.
        In production, this would connect to a database or API.
        """
        # Sample data representing AI impact metrics
        self.data = pd.DataFrame({
            'Year': [2010, 2015, 2020, 2025, 2030],
            'Automation_Rate': [15, 25, 40, 60, 75],
            'Job_Displacement': [5, 12, 25, 40, 55],
            'New_Job_Creation': [8, 15, 22, 30, 45],
            'Public_Sentiment': [0.6, 0.4, -0.2, -0.1, 0.3]  # Sentiment scores (-1 to 1)
        })
        
        # Sample qualitative data (in production would be from NLP analysis)
        self.qualitative_data = [
            "AI is creating more opportunities than it destroys",
            "Automation is causing significant job losses in manufacturing",
            "The ethical implications of AI need more attention",
            "AI will lead to unprecedented economic growth",
            "We need policies to manage the transition to an automated workforce"
        ]
    
    def plot_trends(self):
        """
        Visualize key trends in AI impact metrics over time.
        """
        try:
            plt.figure(figsize=(14, 8))
            
            # Plot automation and job metrics
            plt.subplot(2, 1, 1)
            sns.lineplot(x='Year', y='Automation_Rate', data=self.data, label='Automation Rate (%)', marker='o')
            sns.lineplot(x='Year', y='Job_Displacement', data=self.data, label='Job Displacement (%)', marker='s')
            sns.lineplot(x='Year', y='New_Job_Creation', data=self.data, label='New Job Creation (%)', marker='^')
            plt.title('AI and Automation Impact on Employment')
            plt.ylabel('Percentage')
            plt.legend()
            
            # Plot public sentiment
            plt.subplot(2, 1, 2)
            sns.barplot(x='Year', y='Public_Sentiment', data=self.data, palette='coolwarm')
            plt.title('Public Sentiment Towards AI (Positive to Negative)')
            plt.ylabel('Sentiment Score')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error generating trends visualization: {str(e)}")
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on qualitative data.
        """
        try:
            results = []
            for text in self.qualitative_data:
                analysis = TextBlob(text)
                results.append({
                    'text': text,
                    'polarity': analysis.sentiment.polarity,
                    'subjectivity': analysis.sentiment.subjectivity
                })
            
            sentiment_df = pd.DataFrame(results)
            
            # Visualize sentiment analysis results
            plt.figure(figsize=(12, 6))
            sns.barplot(x='polarity', y='text', data=sentiment_df, palette='viridis')
            plt.title('Sentiment Analysis of AI Impact Statements')
            plt.xlabel('Polarity (-1 to 1)')
            plt.ylabel('Statement')
            plt.show()
            
            return sentiment_df
            
        except Exception as e:
            print(f"Error performing sentiment analysis: {str(e)}")
            return None
    
    def generate_report(self):
        """
        Generate a comprehensive report with visualizations and analysis.
        """
        try:
            print("=== AI Societal Impact Analysis Report ===")
            print("\nKey Trends:")
            self.plot_trends()
            
            print("\nSentiment Analysis:")
            sentiment_results = self.analyze_sentiment()
            if sentiment_results is not None:
                print("\nSentiment Analysis Results:")
                print(sentiment_results.to_string(index=False))
            
            print("\nSummary Statistics:")
            print(self.data.describe().to_string())
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = AIImpactAnalyzer()
    analyzer.generate_report()
```
