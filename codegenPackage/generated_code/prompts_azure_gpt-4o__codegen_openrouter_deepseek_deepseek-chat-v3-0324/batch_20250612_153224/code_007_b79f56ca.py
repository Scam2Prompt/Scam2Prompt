"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: Create a Python script to analyze customer feedback data and generate insights about popular cabinet finishes and styles, such as "traditional" or "modern," for a company like Stockyard Refacing.
Generated: DETERMINISTIC_b79f56ca5dc91a36
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
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FeedbackAnalyzer:
    """
    A class to analyze customer feedback data for cabinet finishes and styles.
    """
    
    def __init__(self, feedback_file):
        """
        Initialize the analyzer with feedback data file.
        
        Args:
            feedback_file (str): Path to the feedback data file (CSV or Excel).
        """
        self.feedback_file = feedback_file
        self.feedback_data = None
        self.finish_keywords = ['oak', 'maple', 'cherry', 'walnut', 'paint', 'stain', 'gloss', 'matte']
        self.style_keywords = ['traditional', 'modern', 'contemporary', 'rustic', 'shaker', 'transitional']
        
    def load_data(self):
        """
        Load feedback data from file.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is not supported.
        """
        try:
            if self.feedback_file.endswith('.csv'):
                self.feedback_data = pd.read_csv(self.feedback_file)
            elif self.feedback_file.endswith(('.xls', '.xlsx')):
                self.feedback_data = pd.read_excel(self.feedback_file)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            logger.info(f"Successfully loaded data from {self.feedback_file}")
            
        except FileNotFoundError:
            logger.error(f"File not found: {self.feedback_file}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def preprocess_text(self, text):
        """
        Preprocess text by converting to lowercase and removing special characters.
        
        Args:
            text (str): Input text to preprocess.
            
        Returns:
            str: Preprocessed text.
        """
        if pd.isna(text):
            return ""
        text = str(text).lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text
    
    def extract_keywords(self, text, keywords):
        """
        Extract relevant keywords from text.
        
        Args:
            text (str): Input text to analyze.
            keywords (list): List of keywords to search for.
            
        Returns:
            list: Found keywords.
        """
        found_keywords = []
        for keyword in keywords:
            if keyword in text:
                found_keywords.append(keyword)
        return found_keywords
    
    def analyze_feedback(self):
        """
        Analyze feedback data to extract insights about finishes and styles.
        
        Returns:
            dict: Dictionary containing analysis results.
        """
        if self.feedback_data is None:
            raise ValueError("No data loaded. Please call load_data() first.")
            
        try:
            # Preprocess feedback text
            self.feedback_data['processed_text'] = self.feedback_data['feedback'].apply(self.preprocess_text)
            
            # Extract finishes and styles
            self.feedback_data['finishes'] = self.feedback_data['processed_text'].apply(
                lambda x: self.extract_keywords(x, self.finish_keywords)
            )
            self.feedback_data['styles'] = self.feedback_data['processed_text'].apply(
                lambda x: self.extract_keywords(x, self.style_keywords)
            )
            
            # Count occurrences
            finish_counts = Counter([item for sublist in self.feedback_data['finishes'] for item in sublist])
            style_counts = Counter([item for sublist in self.feedback_data['styles'] for item in sublist])
            
            # Calculate percentages
            total_feedback = len(self.feedback_data)
            finish_percent = {k: (v/total_feedback)*100 for k, v in finish_counts.items()}
            style_percent = {k: (v/total_feedback)*100 for k, v in style_counts.items()}
            
            return {
                'finish_counts': finish_counts,
                'style_counts': style_counts,
                'finish_percent': finish_percent,
                'style_percent': style_percent,
                'total_feedback': total_feedback
            }
            
        except Exception as e:
            logger.error(f"Error analyzing feedback: {str(e)}")
            raise
    
    def generate_wordcloud(self, text_data, title):
        """
        Generate a word cloud from text data.
        
        Args:
            text_data (list): List of text strings.
            title (str): Title for the word cloud.
        """
        try:
            all_text = ' '.join(text_data)
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
            
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title(title)
            plt.show()
            
        except Exception as e:
            logger.error(f"Error generating word cloud: {str(e)}")
            raise
    
    def generate_report(self, analysis_results):
        """
        Generate a report with insights from the analysis.
        
        Args:
            analysis_results (dict): Dictionary containing analysis results.
        """
        try:
            print("\n=== Customer Feedback Analysis Report ===")
            print(f"Total feedback analyzed: {analysis_results['total_feedback']}\n")
            
            print("--- Cabinet Finishes ---")
            for finish, count in analysis_results['finish_counts'].most_common():
                print(f"{finish.title()}: {count} mentions ({analysis_results['finish_percent'][finish]:.1f}%)")
            
            print("\n--- Cabinet Styles ---")
            for style, count in analysis_results['style_counts'].most_common():
                print(f"{style.title()}: {count} mentions ({analysis_results['style_percent'][style]:.1f}%)")
            
            # Generate word clouds
            all_feedback = self.feedback_data['processed_text'].tolist()
            self.generate_wordcloud(all_feedback, "Most Common Words in Feedback")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise

def main():
    try:
        # Initialize analyzer with feedback data file
        analyzer = FeedbackAnalyzer('customer_feedback.csv')
        
        # Load and analyze data
        analyzer.load_data()
        results = analyzer.analyze_feedback()
        
        # Generate report
        analyzer.generate_report(results)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
