"""
Generated Code Metadata:
========================
Original URL: https://deviationinfotech.in
Prompt: "Generate a content marketing strategy for a small business using Python and natural language processing techniques, as described in Deviation Infotech's content marketing blog posts."
Generated: DETERMINISTIC_5cf81be64a843724
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/marketing-blog": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/digital-marketing-advice": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
import re

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class ContentMarketingStrategyGenerator:
    """
    Generates content marketing strategy using NLP techniques
    """
    
    def __init__(self, business_name, industry, target_audience):
        """
        Initialize with business details
        """
        self.business_name = business_name
        self.industry = industry
        self.target_audience = target_audience
        self.stop_words = set(stopwords.words('english'))
        self.sia = SentimentIntensityAnalyzer()
        
    def analyze_competitor_content(self, urls):
        """
        Analyze competitor websites for content insights
        """
        competitor_data = []
        
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = ' '.join([p.get_text() for p in soup.find_all('p')])
                
                # Clean text
                text = re.sub(r'[^\w\s]', '', text.lower())
                words = word_tokenize(text)
                filtered_words = [word for word in words if word not in self.stop_words]
                
                # Get most common words
                word_freq = Counter(filtered_words)
                common_words = word_freq.most_common(20)
                
                competitor_data.append({
                    'url': url,
                    'common_words': common_words,
                    'word_count': len(filtered_words),
                    'sentiment': self.sia.polarity_scores(text)
                })
            except Exception as e:
                print(f"Error analyzing {url}: {str(e)}")
                continue
                
        return competitor_data
    
    def generate_word_cloud(self, texts):
        """
        Generate word cloud from content
        """
        combined_text = ' '.join(texts)
        wordcloud = WordCloud(width=800, height=400, 
                             background_color='white',
                             stopwords=self.stop_words).generate(combined_text)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Content Word Cloud for {self.business_name}')
        plt.show()
    
    def analyze_sentiment(self, text):
        """
        Perform sentiment analysis on content
        """
        return self.sia.polarity_scores(text)
    
    def extract_key_themes(self, texts, num_themes=5):
        """
        Extract key themes from content
        """
        combined_text = ' '.join(texts)
        words = word_tokenize(combined_text.lower())
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 3]
        
        word_freq = Counter(filtered_words)
        return word_freq.most_common(num_themes)
    
    def generate_content_strategy(self, competitor_urls, sample_content=None):
        """
        Generate comprehensive content marketing strategy
        """
        strategy = {
            'business_name': self.business_name,
            'industry': self.industry,
            'target_audience': self.target_audience,
            'competitor_analysis': None,
            'content_themes': None,
            'recommended_topics': [],
            'content_types': ['Blog Posts', 'Social Media', 'Videos', 'Infographics'],
            'publishing_frequency': {
                'blog': '2 posts/week',
                'social_media': 'Daily',
                'newsletter': 'Monthly'
            }
        }
        
        # Analyze competitors if URLs provided
        if competitor_urls:
            competitor_data = self.analyze_competitor_content(competitor_urls)
            strategy['competitor_analysis'] = competitor_data
            
            # Extract common themes from competitors
            competitor_texts = []
            for data in competitor_data:
                if 'common_words' in data:
                    competitor_texts.extend([word[0] for word in data['common_words']])
            
            strategy['content_themes'] = Counter(competitor_texts).most_common(10)
        
        # Analyze sample content if provided
        if sample_content:
            strategy['sample_content_analysis'] = {
                'sentiment': self.analyze_sentiment(sample_content),
                'key_themes': self.extract_key_themes([sample_content])
            }
            
            # Generate topic ideas based on themes
            themes = [theme[0] for theme in strategy['sample_content_analysis']['key_themes']]
            for theme in themes:
                strategy['recommended_topics'].extend([
                    f"How {theme} is changing {self.industry}",
                    f"The ultimate guide to {theme} for {self.target_audience}",
                    f"5 ways to leverage {theme} in your business"
                ])
        
        return strategy
    
    def generate_report(self, strategy, output_file='content_strategy_report.html'):
        """
        Generate HTML report from strategy
        """
        try:
            with open(output_file, 'w') as f:
                f.write(f"<h1>Content Marketing Strategy for {strategy['business_name']}</h1>")
                f.write(f"<h2>Industry: {strategy['industry']}</h2>")
                f.write(f"<h2>Target Audience: {strategy['target_audience']}</h2>")
                
                f.write("<h3>Recommended Content Types:</h3>")
                f.write("<ul>")
                for content_type in strategy['content_types']:
                    f.write(f"<li>{content_type}</li>")
                f.write("</ul>")
                
                f.write("<h3>Publishing Frequency:</h3>")
                f.write("<ul>")
                for key, value in strategy['publishing_frequency'].items():
                    f.write(f"<li>{key.replace('_', ' ').title()}: {value}</li>")
                f.write("</ul>")
                
                if strategy['content_themes']:
                    f.write("<h3>Top Content Themes:</h3>")
                    f.write("<ul>")
                    for theme, count in strategy['content_themes']:
                        f.write(f"<li>{theme.title()} (appears {count} times in competitor content)</li>")
                    f.write("</ul>")
                
                if strategy['recommended_topics']:
                    f.write("<h3>Recommended Topics:</h3>")
                    f.write("<ol>")
                    for topic in strategy['recommended_topics']:
                        f.write(f"<li>{topic}</li>")
                    f.write("</ol>")
                
                f.write("<footer>Generated using NLP Content Strategy Tool</footer>")
            
            print(f"Report generated successfully: {output_file}")
        except Exception as e:
            print(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with business details
    strategy_gen = ContentMarketingStrategyGenerator(
        business_name="Deviation Infotech",
        industry="Digital Marketing",
        target_audience="Small business owners"
    )
    
    # Sample competitor URLs (replace with real ones)
    competitor_urls = [
        "https://example.com/marketing-blog",
        "https://example.com/digital-marketing-advice"
    ]
    
    # Sample content (replace with real content)
    sample_content = """
    Content marketing is essential for small businesses to establish their brand online.
    By creating valuable content, businesses can attract and engage their target audience.
    SEO optimization helps content rank higher in search results.
    """
    
    # Generate strategy
    strategy = strategy_gen.generate_content_strategy(
        competitor_urls=competitor_urls,
        sample_content=sample_content
    )
    
    # Generate report
    strategy_gen.generate_report(strategy)
    
    # Optional: Generate word cloud
    strategy_gen.generate_word_cloud([sample_content])
```
