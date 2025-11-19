"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Generate a Python script to analyze patient satisfaction ratings for a plastic surgery clinic like Dr. Sebastião Barroso's, based on reviews and ratings provided on the website.
Generated: DETERMINISTIC_d93f992bbad4935c
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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import re
from datetime import datetime

class PatientSatisfactionAnalyzer:
    """
    Analyzes patient satisfaction ratings and reviews for a plastic surgery clinic.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str): Path to CSV file containing reviews data. If None, empty DF is created.
        """
        if data_path:
            try:
                self.reviews_df = pd.read_csv(data_path)
                self._validate_data()
            except FileNotFoundError:
                raise FileNotFoundError(f"Data file not found at {data_path}")
            except Exception as e:
                raise Exception(f"Error loading data: {str(e)}")
        else:
            self.reviews_df = pd.DataFrame(columns=['patient_id', 'date', 'rating', 'review_text', 'doctor'])
        
        self._clean_data()
    
    def _validate_data(self):
        """
        Validate the input data has required columns.
        """
        required_columns = ['patient_id', 'date', 'rating', 'review_text', 'doctor']
        missing_cols = [col for col in required_columns if col not in self.reviews_df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
    
    def _clean_data(self):
        """
        Clean and preprocess the data.
        """
        # Convert date to datetime
        self.reviews_df['date'] = pd.to_datetime(self.reviews_df['date'], errors='coerce')
        
        # Clean review text
        self.reviews_df['clean_review'] = self.reviews_df['review_text'].apply(self._clean_text)
        
        # Ensure rating is numeric
        self.reviews_df['rating'] = pd.to_numeric(self.reviews_df['rating'], errors='coerce')
        
        # Drop rows with missing essential data
        self.reviews_df = self.reviews_df.dropna(subset=['rating', 'review_text'])
    
    def _clean_text(self, text):
        """
        Clean review text by removing special characters and extra spaces.
        
        Args:
            text (str): Raw review text
            
        Returns:
            str: Cleaned review text
        """
        if pd.isna(text):
            return ""
        text = re.sub(r'[^a-zA-Z0-9\s]', '', str(text))
        text = re.sub(r'\s+', ' ', text).strip()
        return text.lower()
    
    def add_review(self, patient_id, date, rating, review_text, doctor):
        """
        Add a new review to the dataset.
        
        Args:
            patient_id (str): Unique patient identifier
            date (str): Date of review in YYYY-MM-DD format
            rating (float): Satisfaction rating (1-5)
            review_text (str): Patient's review text
            doctor (str): Name of the doctor
        """
        try:
            new_review = pd.DataFrame({
                'patient_id': [patient_id],
                'date': [pd.to_datetime(date)],
                'rating': [float(rating)],
                'review_text': [review_text],
                'doctor': [doctor]
            })
            
            self.reviews_df = pd.concat([self.reviews_df, new_review], ignore_index=True)
            self._clean_data()
        except Exception as e:
            print(f"Error adding review: {str(e)}")
    
    def get_sentiment(self, text):
        """
        Analyze sentiment of text using TextBlob.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            float: Sentiment polarity (-1 to 1)
        """
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def analyze_sentiments(self):
        """
        Perform sentiment analysis on all reviews.
        
        Returns:
            pd.DataFrame: DataFrame with added sentiment columns
        """
        self.reviews_df['sentiment'] = self.reviews_df['clean_review'].apply(self.get_sentiment)
        self.reviews_df['sentiment_category'] = pd.cut(
            self.reviews_df['sentiment'],
            bins=[-1, -0.1, 0.1, 1],
            labels=['negative', 'neutral', 'positive']
        )
        return self.reviews_df
    
    def get_rating_stats(self):
        """
        Calculate basic statistics for ratings.
        
        Returns:
            dict: Dictionary containing rating statistics
        """
        if self.reviews_df.empty:
            return {}
            
        stats = {
            'average_rating': self.reviews_df['rating'].mean(),
            'median_rating': self.reviews_df['rating'].median(),
            'min_rating': self.reviews_df['rating'].min(),
            'max_rating': self.reviews_df['rating'].max(),
            'total_reviews': len(self.reviews_df)
        }
        return stats
    
    def get_doctor_performance(self):
        """
        Calculate performance metrics by doctor.
        
        Returns:
            pd.DataFrame: Performance metrics grouped by doctor
        """
        if self.reviews_df.empty:
            return pd.DataFrame()
            
        doctor_stats = self.reviews_df.groupby('doctor').agg({
            'rating': ['mean', 'count'],
            'sentiment': 'mean'
        }).reset_index()
        
        doctor_stats.columns = ['doctor', 'avg_rating', 'review_count', 'avg_sentiment']
        doctor_stats = doctor_stats.sort_values('avg_rating', ascending=False)
        return doctor_stats
    
    def plot_rating_distribution(self, save_path=None):
        """
        Plot distribution of ratings.
        
        Args:
            save_path (str): Optional path to save the plot
        """
        if self.reviews_df.empty:
            print("No data to plot")
            return
            
        plt.figure(figsize=(10, 6))
        sns.countplot(x='rating', data=self.reviews_df, palette='viridis')
        plt.title('Distribution of Patient Ratings')
        plt.xlabel('Rating (1-5)')
        plt.ylabel('Number of Reviews')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()
    
    def plot_sentiment_over_time(self, save_path=None):
        """
        Plot sentiment trends over time.
        
        Args:
            save_path (str): Optional path to save the plot
        """
        if self.reviews_df.empty:
            print("No data to plot")
            return
            
        # Ensure sentiment analysis has been done
        if 'sentiment' not in self.reviews_df.columns:
            self.analyze_sentiments()
            
        time_series = self.reviews_df.set_index('date').resample('M')['sentiment'].mean()
        
        plt.figure(figsize=(12, 6))
        time_series.plot()
        plt.title('Average Sentiment Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score (-1 to 1)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()
    
    def get_common_words(self, n=10, sentiment='positive'):
        """
        Get most common words in reviews by sentiment.
        
        Args:
            n (int): Number of words to return
            sentiment (str): 'positive', 'negative', or 'all'
            
        Returns:
            pd.Series: Series of word counts
        """
        if self.reviews_df.empty:
            return pd.Series()
            
        # Ensure sentiment analysis has been done
        if 'sentiment_category' not in self.reviews_df.columns:
            self.analyze_sentiments()
            
        if sentiment != 'all':
            reviews = self.reviews_df[self.reviews_df['sentiment_category'] == sentiment]
        else:
            reviews = self.reviews_df
            
        words = ' '.join(reviews['clean_review']).split()
        word_counts = pd.Series(words).value_counts()
        return word_counts.head(n)
    
    def save_analysis_report(self, output_path):
        """
        Save comprehensive analysis report to CSV.
        
        Args:
            output_path (str): Path to save the report
        """
        try:
            if self.reviews_df.empty:
                print("No data to save")
                return
                
            # Ensure all analyses are done
            if 'sentiment' not in self.reviews_df.columns:
                self.analyze_sentiments()
                
            self.reviews_df.to_csv(output_path, index=False)
            print(f"Report saved successfully to {output_path}")
        except Exception as e:
            print(f"Error saving report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer (replace with actual data path)
        analyzer = PatientSatisfactionAnalyzer()
        
        # Add some sample reviews
        analyzer.add_review(
            patient_id="PT001",
            date="2023-01-15",
            rating=5,
            review_text="Dr. Barroso was amazing! The results exceeded my expectations.",
            doctor="Dr. Sebastião Barroso"
