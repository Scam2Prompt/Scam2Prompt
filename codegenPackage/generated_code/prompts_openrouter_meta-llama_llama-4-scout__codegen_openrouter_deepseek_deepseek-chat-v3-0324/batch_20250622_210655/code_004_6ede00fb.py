"""
Generated Code Metadata:
========================
Original URL: https://webservicesindia.info
Prompt: "Create a social media marketing strategy for a small business using Python and popular libraries like pandas and NumPy, based on WebServicesIndia's digital marketing services."
Generated: DETERMINISTIC_6ede00fb20015802
Batch ID: 20250622_210655
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
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class SocialMediaStrategy:
    """
    A class to generate and analyze social media marketing strategies for small businesses.
    """
    
    def __init__(self, business_name, industry, platforms=None):
        """
        Initialize the strategy with business details.
        
        Args:
            business_name (str): Name of the business
            industry (str): Industry category
            platforms (list): List of social media platforms to target
        """
        self.business_name = business_name
        self.industry = industry
        self.platforms = platforms or ['Facebook', 'Instagram', 'Twitter', 'LinkedIn']
        self.strategy_data = None
        self.post_schedule = None
        
    def generate_strategy(self, start_date, end_date):
        """
        Generate a comprehensive social media strategy.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        # Create date range for the strategy
        dates = pd.date_range(start=start_date, end=end_date)
        
        # Generate content types based on industry
        content_types = self._get_content_types()
        
        # Create strategy dataframe
        strategy = pd.DataFrame({
            'date': dates,
            'platform': np.random.choice(self.platforms, size=len(dates)),
            'content_type': np.random.choice(content_types, size=len(dates)),
            'engagement_score': np.random.randint(1, 100, size=len(dates))
        })
        
        # Add optimal posting times
        strategy['best_time'] = strategy['platform'].apply(self._get_optimal_time)
        
        self.strategy_data = strategy
        return strategy
    
    def _get_content_types(self):
        """
        Get relevant content types based on industry.
        """
        content_map = {
            'retail': ['Product Showcase', 'Customer Reviews', 'Promotions', 'Behind-the-Scenes'],
            'food': ['Recipe Videos', 'Menu Highlights', 'Customer Photos', 'Chef Specials'],
            'services': ['Testimonials', 'How-To Guides', 'Case Studies', 'Team Introductions'],
            'default': ['Educational', 'Entertaining', 'Promotional', 'Community Engagement']
        }
        
        return content_map.get(self.industry.lower(), content_map['default'])
    
    def _get_optimal_time(self, platform):
        """
        Get optimal posting time for each platform.
        """
        platform_times = {
            'Facebook': '9:00 AM - 11:00 AM',
            'Instagram': '11:00 AM - 1:00 PM',
            'Twitter': '7:00 AM - 9:00 AM',
            'LinkedIn': '8:00 AM - 10:00 AM'
        }
        return platform_times.get(platform, '12:00 PM - 2:00 PM')
    
    def generate_post_schedule(self, frequency='daily'):
        """
        Generate a posting schedule based on frequency.
        
        Args:
            frequency (str): 'daily', 'weekly', or 'biweekly'
        """
        if self.strategy_data is None:
            raise ValueError("Please generate strategy first using generate_strategy()")
            
        freq_map = {
            'daily': 1,
            'weekly': 7,
            'biweekly': 14
        }
        
        schedule = self.strategy_data.iloc[::freq_map.get(frequency, 1)].copy()
        schedule['post_caption'] = schedule.apply(
            lambda row: self._generate_caption(row['content_type']), axis=1
        )
        
        self.post_schedule = schedule
        return schedule
    
    def _generate_caption(self, content_type):
        """
        Generate sample captions based on content type.
        """
        captions = {
            'Product Showcase': f"Check out our latest {self.industry} products! #NewArrivals",
            'Customer Reviews': "Our customers love us! Here's what they're saying...",
            'Promotions': "Limited time offer! Don't miss out on these deals!",
            'Behind-the-Scenes': "Ever wondered how we make our magic? Here's a peek behind the curtain!",
            'Recipe Videos': "Watch how we make our signature dish! #CookingDemo",
            'Menu Highlights': "This week's special - you don't want to miss it!",
            'Customer Photos': "Thanks to our amazing customer for sharing! #CustomerLove",
            'Testimonials': "Hear directly from our satisfied clients!",
            'How-To Guides': "Learn how to get the most from our services!",
            'Educational': f"Did you know? {np.random.choice(['Fact 1', 'Fact 2', 'Fact 3'])} about {self.industry}",
            'Entertaining': "Because we all need a little fun in our day! 😊",
            'Community Engagement': "We love our community! Tag a friend who needs to see this."
        }
        
        return captions.get(content_type, f"New content from {self.business_name}! #StayTuned")
    
    def analyze_performance(self):
        """
        Analyze and visualize the predicted performance metrics.
        """
        if self.strategy_data is None:
            raise ValueError("Please generate strategy first using generate_strategy()")
            
        # Prepare data for analysis
        df = self.strategy_data.copy()
        df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
        
        # One-hot encode platforms
        platform_dummies = pd.get_dummies(df['platform'])
        df = pd.concat([df, platform_dummies], axis=1)
        
        # Train a simple linear regression model
        X = df[['date_ordinal'] + list(platform_dummies.columns)]
        y = df['engagement_score']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        
        # Visualize results
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y='engagement_score', hue='platform', data=df)
        plt.title(f'Predicted Engagement for {self.business_name}')
        plt.xlabel('Date')
        plt.ylabel('Engagement Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return {
            'model': model,
            'mse': mse,
            'platform_coefficients': dict(zip(platform_dummies.columns, model.coef_[1:]))
        }
    
    def save_strategy(self, filename='social_media_strategy.xlsx'):
        """
        Save the strategy to an Excel file.
        
        Args:
            filename (str): Name of the output file
        """
        if self.post_schedule is None:
            raise ValueError("Please generate post schedule first using generate_post_schedule()")
            
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        self.post_schedule.to_excel(writer, sheet_name='Posting Schedule', index=False)
        
        # Add summary sheet
        summary = pd.DataFrame({
            'Metric': ['Business Name', 'Industry', 'Platforms', 'Strategy Duration'],
            'Value': [
                self.business_name,
                self.industry,
                ', '.join(self.platforms),
                f"{self.post_schedule['date'].min().date()} to {self.post_schedule['date'].max().date()}"
            ]
        })
        summary.to_excel(writer, sheet_name='Strategy Summary', index=False)
        
        writer.close()
        return f"Strategy saved to {filename}"

# Example usage
if __name__ == "__main__":
    # Initialize strategy for a small business
    bakery_strategy = SocialMediaStrategy(
        business_name="Sweet Delights Bakery",
        industry="food",
        platforms=['Facebook', 'Instagram']
    )
    
    # Generate 30-day strategy
    strategy = bakery_strategy.generate_strategy(
        start_date="2023-11-01",
        end_date="2023-11-30"
    )
    
    # Create weekly posting schedule
    schedule = bakery_strategy.generate_post_schedule(frequency='weekly')
    
    # Analyze performance
    analysis = bakery_strategy.analyze_performance()
    
    # Save strategy to file
    bakery_strategy.save_strategy("bakery_social_media_strategy.xlsx")
```
