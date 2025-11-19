"""
Generated Code Metadata:
========================
Original URL: https://axos-management.com
Prompt: Generate code to analyze target audience groups and create goal-oriented reports, as outlined in Axos Management's influencer management process.
Generated: DETERMINISTIC_99676e8817e3841e
Batch ID: 20250612_145153
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
from typing import List, Dict, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AudienceAnalyzer:
    """
    Analyzes audience data and generates goal-oriented reports.
    """
    
    def __init__(self, audience_data: pd.DataFrame):
        """
        Initialize with audience data.
        
        Args:
            audience_data: DataFrame containing audience metrics with columns:
                - age
                - gender
                - location
                - interests
                - engagement_rate
                - follower_count
                - timestamp
        """
        self.data = audience_data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input data structure and content."""
        required_columns = {
            'age', 'gender', 'location', 'interests', 
            'engagement_rate', 'follower_count', 'timestamp'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if self.data.isnull().values.any():
            logger.warning("Data contains missing values which may affect analysis")
    
    def _clean_data(self) -> pd.DataFrame:
        """Clean and preprocess the data."""
        data = self.data.copy()
        
        # Convert timestamp to datetime
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        # Clean age outliers
        data = data[(data['age'] >= 13) & (data['age'] <= 80)]
        
        # Clean engagement rate
        data = data[(data['engagement_rate'] >= 0) & (data['engagement_rate'] <= 1)]
        
        return data
    
    def analyze_demographics(self) -> Dict[str, Dict]:
        """
        Analyze audience demographics.
        
        Returns:
            Dictionary containing demographic statistics:
                - age_distribution
                - gender_distribution
                - top_locations
        """
        clean_data = self._clean_data()
        
        # Age distribution
        age_bins = [13, 18, 25, 35, 45, 55, 65, 80]
        age_labels = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
        age_dist = pd.cut(
            clean_data['age'], 
            bins=age_bins, 
            labels=age_labels
        ).value_counts(normalize=True).to_dict()
        
        # Gender distribution
        gender_dist = clean_data['gender'].value_counts(normalize=True).to_dict()
        
        # Top locations
        top_locations = clean_data['location'].value_counts().head(10).to_dict()
        
        return {
            'age_distribution': age_dist,
            'gender_distribution': gender_dist,
            'top_locations': top_locations
        }
    
    def analyze_interests(self, top_n: int = 5) -> Dict[str, float]:
        """
        Analyze audience interests.
        
        Args:
            top_n: Number of top interests to return
            
        Returns:
            Dictionary of top interests and their prevalence
        """
        clean_data = self._clean_data()
        
        # Split and count interests
        all_interests = clean_data['interests'].str.split(',').explode()
        all_interests = all_interests.str.strip().str.lower()
        interest_counts = all_interests.value_counts(normalize=True)
        
        return interest_counts.head(top_n).to_dict()
    
    def analyze_engagement(self) -> Dict[str, float]:
        """
        Analyze audience engagement metrics.
        
        Returns:
            Dictionary containing engagement statistics:
                - avg_engagement_rate
                - engagement_by_age
                - engagement_by_gender
        """
        clean_data = self._clean_data()
        
        avg_engagement = clean_data['engagement_rate'].mean()
        
        engagement_by_age = clean_data.groupby('age')['engagement_rate'] \
            .mean().sort_values(ascending=False).head(5).to_dict()
            
        engagement_by_gender = clean_data.groupby('gender')['engagement_rate'] \
            .mean().to_dict()
            
        return {
            'avg_engagement_rate': avg_engagement,
            'engagement_by_age': engagement_by_age,
            'engagement_by_gender': engagement_by_gender
        }
    
    def generate_report(self, report_type: str = "full") -> Dict:
        """
        Generate a goal-oriented report.
        
        Args:
            report_type: Type of report to generate ("demographics", "interests", "engagement", or "full")
            
        Returns:
            Dictionary containing the requested report data
        """
        report = {}
        
        try:
            if report_type in ("demographics", "full"):
                report['demographics'] = self.analyze_demographics()
                
            if report_type in ("interests", "full"):
                report['interests'] = self.analyze_interests()
                
            if report_type in ("engagement", "full"):
                report['engagement'] = self.analyze_engagement()
                
            logger.info(f"Successfully generated {report_type} report")
            return report
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
    
    def save_report(self, report: Dict, filename: str, format: str = "csv") -> None:
        """
        Save report to file.
        
        Args:
            report: Report data to save
            filename: Output filename (without extension)
            format: Output format ("csv", "json", or "excel")
        """
        try:
            if format == "csv":
                # Flatten report structure for CSV
                flat_data = {}
                for section, metrics in report.items():
                    for metric, values in metrics.items():
                        flat_data[f"{section}_{metric}"] = values
                
                df = pd.DataFrame.from_dict(flat_data, orient='index').T
                df.to_csv(f"{filename}.csv", index=False)
                
            elif format == "json":
                import json
                with open(f"{filename}.json", 'w') as f:
                    json.dump(report, f, indent=2)
                    
            elif format == "excel":
                with pd.ExcelWriter(f"{filename}.xlsx") as writer:
                    for section, metrics in report.items():
                        df = pd.DataFrame.from_dict(metrics, orient='index')
                        df.to_excel(writer, sheet_name=section)
                        
            logger.info(f"Report saved successfully as {filename}.{format}")
            
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    sample_data = {
        'age': [25, 30, 18, 45, 32, 28, 55, 22, 38, 27],
        'gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'],
        'location': ['NY', 'CA', 'TX', 'FL', 'NY', 'CA', 'TX', 'FL', 'NY', 'CA'],
        'interests': ['tech,travel', 'fashion,food', 'sports', 'tech', 'travel,food', 
                     'fashion', 'sports,tech', 'travel', 'food', 'tech,fashion'],
        'engagement_rate': [0.05, 0.08, 0.12, 0.03, 0.07, 0.09, 0.04, 0.11, 0.06, 0.10],
        'follower_count': [10000, 15000, 8000, 20000, 12000, 18000, 9000, 11000, 13000, 16000],
        'timestamp': ['2023-01-01'] * 10
    }
    
    df = pd.DataFrame(sample_data)
    
    try:
        analyzer = AudienceAnalyzer(df)
        report = analyzer.generate_report()
        analyzer.save_report(report, "audience_report", format="json")
        
    except Exception as e:
        logger.error(f"Error in analysis process: {str(e)}")
```
