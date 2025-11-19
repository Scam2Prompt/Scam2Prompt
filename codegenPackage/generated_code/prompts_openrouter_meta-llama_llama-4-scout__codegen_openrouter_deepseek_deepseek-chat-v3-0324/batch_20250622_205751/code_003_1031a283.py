"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Create a code snippet to analyze customer testimonials for a business training course and provide insights on course effectiveness.
Generated: DETERMINISTIC_1031a283372e14db
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict
from textblob import TextBlob
import matplotlib.pyplot as plt

class TestimonialAnalyzer:
    """
    Analyzes customer testimonials to provide insights on course effectiveness.
    """
    
    def __init__(self):
        self.testimonials = []
        self.keywords = ['effective', 'helpful', 'valuable', 'insightful', 'transformative', 
                        'recommend', 'excellent', 'outstanding', 'impact', 'beneficial']
    
    def add_testimonial(self, text):
        """
        Add a testimonial to be analyzed.
        
        Args:
            text (str): Customer testimonial text
        """
        if not isinstance(text, str):
            raise ValueError("Testimonial must be a string")
        self.testimonials.append(text)
    
    def _clean_text(self, text):
        """
        Clean text by removing special characters and converting to lowercase.
        
        Args:
            text (str): Text to clean
            
        Returns:
            str: Cleaned text
        """
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text.lower()
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on all testimonials.
        
        Returns:
            dict: Dictionary with sentiment statistics
        """
        if not self.testimonials:
            raise ValueError("No testimonials to analyze")
            
        results = {
            'positive': 0,
            'neutral': 0,
            'negative': 0,
            'average_polarity': 0
        }
        
        total_polarity = 0
        
        for testimonial in self.testimonials:
            analysis = TextBlob(testimonial)
            polarity = analysis.sentiment.polarity
            total_polarity += polarity
            
            if polarity > 0.1:
                results['positive'] += 1
            elif polarity < -0.1:
                results['negative'] += 1
            else:
                results['neutral'] += 1
        
        results['average_polarity'] = total_polarity / len(self.testimonials)
        return results
    
    def keyword_analysis(self):
        """
        Analyze frequency of positive keywords in testimonials.
        
        Returns:
            dict: Dictionary with keyword frequencies
        """
        keyword_counts = defaultdict(int)
        
        for testimonial in self.testimonials:
            cleaned_text = self._clean_text(testimonial)
            words = cleaned_text.split()
            
            for word in words:
                if word in self.keywords:
                    keyword_counts[word] += 1
                    
        return dict(keyword_counts)
    
    def generate_report(self):
        """
        Generate a comprehensive report on testimonial analysis.
        
        Returns:
            dict: Dictionary containing all analysis results
        """
        try:
            sentiment = self.analyze_sentiment()
            keywords = self.keyword_analysis()
            
            return {
                'sentiment_analysis': sentiment,
                'keyword_analysis': keywords,
                'total_testimonials': len(self.testimonials)
            }
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")
    
    def visualize_results(self, report):
        """
        Create visualizations of the analysis results.
        
        Args:
            report (dict): Analysis report from generate_report()
        """
        try:
            # Sentiment pie chart
            plt.figure(figsize=(12, 5))
            
            plt.subplot(1, 2, 1)
            sentiments = ['Positive', 'Neutral', 'Negative']
            counts = [
                report['sentiment_analysis']['positive'],
                report['sentiment_analysis']['neutral'],
                report['sentiment_analysis']['negative']
            ]
            plt.pie(counts, labels=sentiments, autopct='%1.1f%%')
            plt.title('Sentiment Distribution')
            
            # Keyword bar chart
            plt.subplot(1, 2, 2)
            keywords = list(report['keyword_analysis'].keys())
            values = list(report['keyword_analysis'].values())
            plt.bar(keywords, values)
            plt.xticks(rotation=45)
            plt.title('Positive Keyword Frequency')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise RuntimeError(f"Error visualizing results: {str(e)}")


# Example usage
if __name__ == "__main__":
    analyzer = TestimonialAnalyzer()
    
    # Add sample testimonials
    analyzer.add_testimonial("This course was extremely effective and transformative for my career.")
    analyzer.add_testimonial("The training was helpful but could use more practical examples.")
    analyzer.add_testimonial("I didn't find the course valuable and wouldn't recommend it.")
    analyzer.add_testimonial("Excellent content and outstanding delivery by the instructors!")
    analyzer.add_testimonial("The insights gained were beneficial for my business growth.")
    
    # Generate and display report
    report = analyzer.generate_report()
    print("Analysis Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
    
    # Visualize results
    analyzer.visualize_results(report)
```
