"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Create a Python script to automate customer feedback collection and analysis for an art studio, inspired by the "Guest Feedback" section of "The Perfect Studio."
Generated: DETERMINISTIC_50edf7460d6c7129
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import csv
from datetime import datetime
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

class FeedbackCollector:
    """
    A class to collect, analyze, and manage customer feedback for an art studio.
    """
    
    def __init__(self, config_file='config.json'):
        """
        Initialize the FeedbackCollector with configuration settings.
        """
        self.config = self._load_config(config_file)
        self.feedback_data = []
        self.ensure_data_directory()
        
    def _load_config(self, config_file):
        """
        Load configuration from JSON file.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Config file {config_file} not found.")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in config file {config_file}.")
    
    def ensure_data_directory(self):
        """
        Ensure the data directory exists.
        """
        os.makedirs(self.config['data_directory'], exist_ok=True)
    
    def collect_feedback(self, customer_name, feedback_text, rating, email=None):
        """
        Collect feedback from a customer and store it.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
            
        feedback = {
            'timestamp': datetime.now().isoformat(),
            'customer_name': customer_name,
            'feedback_text': feedback_text,
            'rating': rating,
            'email': email
        }
        
        self.feedback_data.append(feedback)
        self._save_feedback(feedback)
        
        if email and self.config['send_email_receipt']:
            self._send_feedback_receipt(feedback)
            
        return feedback
    
    def _save_feedback(self, feedback):
        """
        Save feedback to a CSV file.
        """
        file_path = os.path.join(
            self.config['data_directory'],
            f"feedback_{datetime.now().strftime('%Y%m')}.csv"
        )
        
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=feedback.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(feedback)
    
    def _send_feedback_receipt(self, feedback):
        """
        Send a thank-you email for the feedback.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email_settings']['sender']
            msg['To'] = feedback['email']
            msg['Subject'] = "Thank you for your feedback!"
            
            body = f"""
            Dear {feedback['customer_name']},
            
            Thank you for taking the time to provide feedback about your experience at our art studio.
            We truly appreciate your input and will use it to improve our services.
            
            Your feedback:
            {feedback['feedback_text']}
            
            Rating: {feedback['rating']}/5
            
            Best regards,
            {self.config['studio_name']} Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(
                self.config['email_settings']['smtp_server'],
                self.config['email_settings']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email_settings']['username'],
                    self.config['email_settings']['password']
                )
                server.send_message(msg)
                
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    
    def load_all_feedback(self):
        """
        Load all feedback data from CSV files.
        """
        feedback_files = [
            f for f in os.listdir(self.config['data_directory'])
            if f.startswith('feedback_') and f.endswith('.csv')
        ]
        
        all_feedback = []
        for file in feedback_files:
            file_path = os.path.join(self.config['data_directory'], file)
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                all_feedback.extend(list(reader))
                
        return all_feedback
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of feedback text.
        """
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def generate_report(self):
        """
        Generate a comprehensive feedback report.
        """
        feedback = self.load_all_feedback()
        if not feedback:
            return None
            
        df = pd.DataFrame(feedback)
        df['rating'] = pd.to_numeric(df['rating'])
        df['sentiment'] = df['feedback_text'].apply(self.analyze_sentiment)
        
        # Basic statistics
        avg_rating = df['rating'].mean()
        total_feedback = len(df)
        positive_feedback = len(df[df['sentiment'] > 0.1])
        negative_feedback = len(df[df['sentiment'] < -0.1])
        
        # Generate plots
        self._generate_plots(df)
        
        report = {
            'average_rating': round(avg_rating, 2),
            'total_feedback': total_feedback,
            'positive_feedback': positive_feedback,
            'negative_feedback': negative_feedback,
            'common_themes': self._identify_common_themes(df),
            'plots': {
                'rating_distribution': 'rating_distribution.png',
                'sentiment_analysis': 'sentiment_analysis.png'
            }
        }
        
        return report
    
    def _generate_plots(self, df):
        """
        Generate visualization plots for feedback data.
        """
        # Rating distribution
        plt.figure(figsize=(10, 6))
        df['rating'].value_counts().sort_index().plot(kind='bar')
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        plt.savefig(os.path.join(self.config['data_directory'], 'rating_distribution.png'))
        plt.close()
        
        # Sentiment analysis
        plt.figure(figsize=(10, 6))
        df['sentiment'].plot(kind='hist', bins=20)
        plt.title('Sentiment Analysis')
        plt.xlabel('Sentiment Polarity')
        plt.ylabel('Count')
        plt.savefig(os.path.join(self.config['data_directory'], 'sentiment_analysis.png'))
        plt.close()
    
    def _identify_common_themes(self, df, top_n=5):
        """
        Identify common themes in feedback text.
        """
        positive_feedback = ' '.join(df[df['sentiment'] > 0.1]['feedback_text'])
        negative_feedback = ' '.join(df[df['sentiment'] < -0.1]['feedback_text'])
        
        positive_words = self._extract_keywords(positive_feedback, top_n)
        negative_words = self._extract_keywords(negative_feedback, top_n)
        
        return {
            'positive_themes': positive_words,
            'negative_themes': negative_words
        }
    
    def _extract_keywords(self, text, top_n):
        """
        Extract top keywords from text.
        """
        words = TextBlob(text).words
        word_counts = defaultdict(int)
        
        for word in words:
            if len(word) > 3:  # Ignore short words
                word_counts[word.lower()] += 1
                
        return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize feedback collector
        collector = FeedbackCollector()
        
        # Example feedback collection
        collector.collect_feedback(
            customer_name="Jane Doe",
            feedback_text="The painting class was wonderful! The instructor was very knowledgeable.",
            rating=5,
            email="jane@example.com"
        )
        
        collector.collect_feedback(
            customer_name="John Smith",
            feedback_text="The studio was a bit crowded and materials were limited.",
            rating=3,
            email="john@example.com"
        )
        
        # Generate and print report
        report = collector.generate_report()
        if report:
            print("\nFeedback Analysis Report:")
            print(f"Average Rating: {report['average_rating']}")
            print(f"Total Feedback Collected: {report['total_feedback']}")
            print(f"Positive Feedback: {report['positive_feedback']}")
            print(f"Negative Feedback: {report['negative_feedback']}")
            print("\nCommon Positive Themes:", report['common_themes']['positive_themes'])
            print("Common Negative Themes:", report['common_themes']['negative_themes'])
            print("\nVisualizations saved to data directory.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
