"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Write a script to analyze the impact of educational programs on child development, using metrics and goals similar to those discussed on smplanka.lk.
Generated: DETERMINISTIC_67e4281b0941de38
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Child Development Program Impact Analyzer

This script analyzes the impact of educational programs on child development
using metrics similar to those discussed on smplanka.lk. It processes input data,
calculates various development metrics, and generates a report.

Metrics include:
- Cognitive development scores
- Social-emotional growth
- Physical development
- Language acquisition
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('child_development_analysis.log'),
        logging.StreamHandler()
    ]
)

class ChildDevelopmentAnalyzer:
    """
    Analyzes child development metrics before and after educational programs.
    """
    
    def __init__(self, data_path: str, config_path: Optional[str] = None):
        """
        Initialize the analyzer with data and configuration.
        
        Args:
            data_path: Path to CSV file containing child development data
            config_path: Optional path to JSON config file with metric weights
        """
        self.data_path = data_path
        self.config_path = config_path
        self.metric_weights = {
            'cognitive': 0.4,
            'social_emotional': 0.3,
            'physical': 0.2,
            'language': 0.1
        }
        self.data = None
        self.results = None
        
        self._load_config()
        self._load_data()
        
    def _load_config(self) -> None:
        """Load configuration file if provided."""
        if self.config_path:
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    if 'metric_weights' in config:
                        self.metric_weights = config['metric_weights']
            except Exception as e:
                logging.warning(f"Failed to load config: {e}. Using default weights.")
    
    def _load_data(self) -> None:
        """Load and validate the input data."""
        try:
            self.data = pd.read_csv(self.data_path)
            required_columns = {
                'child_id', 'age', 'program_duration', 
                'pre_cognitive', 'post_cognitive',
                'pre_social_emotional', 'post_social_emotional',
                'pre_physical', 'post_physical',
                'pre_language', 'post_language'
            }
            
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            logging.info("Data loaded successfully")
            
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise
    
    def calculate_improvement(self) -> pd.DataFrame:
        """
        Calculate improvement metrics for each child and overall.
        
        Returns:
            DataFrame with improvement metrics
        """
        try:
            data = self.data.copy()
            
            # Calculate individual metric improvements
            for metric in ['cognitive', 'social_emotional', 'physical', 'language']:
                data[f'{metric}_improvement'] = (
                    data[f'post_{metric}'] - data[f'pre_{metric}']
                )
                data[f'{metric}_improvement_pct'] = (
                    data[f'{metric}_improvement'] / data[f'pre_{metric}'] * 100
                )
            
            # Calculate weighted overall improvement
            data['overall_improvement'] = (
                data['cognitive_improvement'] * self.metric_weights['cognitive'] +
                data['social_emotional_improvement'] * self.metric_weights['social_emotional'] +
                data['physical_improvement'] * self.metric_weights['physical'] +
                data['language_improvement'] * self.metric_weights['language']
            )
            
            self.results = data
            return data
            
        except Exception as e:
            logging.error(f"Error calculating improvements: {e}")
            raise
    
    def generate_summary_stats(self) -> Dict:
        """
        Generate summary statistics for the analysis.
        
        Returns:
            Dictionary containing summary statistics
        """
        if self.results is None:
            self.calculate_improvement()
            
        summary = {
            'total_children': len(self.results),
            'average_age': self.results['age'].mean(),
            'average_program_duration': self.results['program_duration'].mean(),
            'metrics': {}
        }
        
        for metric in ['cognitive', 'social_emotional', 'physical', 'language']:
            summary['metrics'][metric] = {
                'mean_improvement': self.results[f'{metric}_improvement'].mean(),
                'mean_improvement_pct': self.results[f'{metric}_improvement_pct'].mean(),
                'median_improvement': self.results[f'{metric}_improvement'].median(),
                'std_dev': self.results[f'{metric}_improvement'].std()
            }
        
        summary['overall_improvement'] = {
            'mean': self.results['overall_improvement'].mean(),
            'median': self.results['overall_improvement'].median(),
            'std_dev': self.results['overall_improvement'].std()
        }
        
        return summary
    
    def generate_report(self, output_dir: str = 'reports') -> None:
        """
        Generate a comprehensive report with analysis results.
        
        Args:
            output_dir: Directory to save report files
        """
        try:
            Path(output_dir).mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_prefix = f"{output_dir}/child_development_report_{timestamp}"
            
            # Save summary stats
            summary = self.generate_summary_stats()
            with open(f"{report_prefix}_summary.json", 'w') as f:
                json.dump(summary, f, indent=2)
            
            # Save detailed results
            self.results.to_csv(f"{report_prefix}_detailed.csv", index=False)
            
            logging.info(f"Report generated successfully in {output_dir}")
            
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise


def main():
    """Main execution function."""
    try:
        # Example usage
        analyzer = ChildDevelopmentAnalyzer(
            data_path='child_development_data.csv',
            config_path='config.json'
        )
        
        analyzer.calculate_improvement()
        summary = analyzer.generate_summary_stats()
        
        print("\nSummary Statistics:")
        print(json.dumps(summary, indent=2))
        
        analyzer.generate_report()
        
    except Exception as e:
        logging.error(f"Analysis failed: {e}")


if __name__ == '__main__':
    main()
```
