"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Suggest a methodology for blending qualitative and quantitative data in program evaluations, inspired by GLOW Consultants' evaluation services.
Generated: DETERMINISTIC_a3af80e9553bf4b4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Methodology for blending qualitative and quantitative data in program evaluations.
Inspired by GLOW Consultants' evaluation services.
"""

import pandas as pd
from typing import Dict, List, Union
from collections import defaultdict
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import textblob  # For sentiment analysis of qualitative data
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProgramEvaluator:
    """
    A class to blend qualitative and quantitative data for program evaluation.
    """
    
    def __init__(self):
        self.quantitative_data = None
        self.qualitative_data = None
        self.normalized_data = None
        self.combined_results = None
        
    def load_quantitative_data(self, file_path: str) -> None:
        """
        Load quantitative data from CSV file.
        
        Args:
            file_path (str): Path to CSV file containing quantitative data
        """
        try:
            self.quantitative_data = pd.read_csv(file_path)
            logger.info("Quantitative data loaded successfully")
        except Exception as e:
            logger.error(f"Error loading quantitative data: {str(e)}")
            raise
            
    def load_qualitative_data(self, file_path: str) -> None:
        """
        Load qualitative data from CSV file.
        
        Args:
            file_path (str): Path to CSV file containing qualitative data
        """
        try:
            self.qualitative_data = pd.read_csv(file_path)
            logger.info("Qualitative data loaded successfully")
        except Exception as e:
            logger.error(f"Error loading qualitative data: {str(e)}")
            raise
    
    def _normalize_quantitative_data(self) -> pd.DataFrame:
        """
        Normalize quantitative data using MinMax scaling.
        
        Returns:
            pd.DataFrame: Normalized quantitative data
        """
        try:
            scaler = MinMaxScaler()
            quant_data = self.quantitative_data.select_dtypes(include=[np.number])
            normalized = pd.DataFrame(
                scaler.fit_transform(quant_data),
                columns=quant_data.columns,
                index=quant_data.index
            )
            return normalized
        except Exception as e:
            logger.error(f"Error normalizing quantitative data: {str(e)}")
            raise
    
    def _analyze_qualitative_data(self) -> pd.DataFrame:
        """
        Analyze qualitative data by extracting sentiment scores.
        
        Returns:
            pd.DataFrame: Processed qualitative data with sentiment scores
        """
        try:
            qual_data = self.qualitative_data.copy()
            
            # Simple sentiment analysis (can be replaced with more sophisticated NLP)
            def get_sentiment(text: str) -> float:
                try:
                    return textblob.TextBlob(str(text)).sentiment.polarity
                except:
                    return 0.0
                    
            qual_data['sentiment_score'] = qual_data['text_data'].apply(get_sentiment)
            
            # Group by evaluation dimensions if needed
            if 'dimension' in qual_data.columns:
                qual_data = qual_data.groupby('dimension')['sentiment_score'].mean().reset_index()
                
            return qual_data
        except Exception as e:
            logger.error(f"Error analyzing qualitative data: {str(e)}")
            raise
    
    def blend_data(self, quant_weight: float = 0.6, qual_weight: float = 0.4) -> Dict[str, float]:
        """
        Blend normalized quantitative and qualitative data with specified weights.
        
        Args:
            quant_weight (float): Weight for quantitative data (default 0.6)
            qual_weight (float): Weight for qualitative data (default 0.4)
            
        Returns:
            Dict[str, float]: Combined evaluation scores by dimension
        """
        try:
            if quant_weight + qual_weight != 1.0:
                raise ValueError("Weights must sum to 1.0")
                
            # Process both data types
            norm_quant = self._normalize_quantitative_data()
            processed_qual = self._analyze_qualitative_data()
            
            # Combine data (example implementation - adjust based on actual data structure)
            combined = defaultdict(float)
            
            # Handle quantitative data
            for col in norm_quant.columns:
                combined[col] = norm_quant[col].mean() * quant_weight
                
            # Handle qualitative data
            for _, row in processed_qual.iterrows():
                dimension = row['dimension'] if 'dimension' in row else 'overall'
                combined[dimension] += row['sentiment_score'] * qual_weight
                
            self.combined_results = dict(combined)
            return self.combined_results
        except Exception as e:
            logger.error(f"Error blending data: {str(e)}")
            raise
    
    def generate_report(self, output_format: str = 'dict') -> Union[Dict, pd.DataFrame, str]:
        """
        Generate evaluation report in specified format.
        
        Args:
            output_format (str): Format of report ('dict', 'dataframe', or 'string')
            
        Returns:
            Report in requested format
        """
        if not self.combined_results:
            raise ValueError("No results to report. Run blend_data() first.")
            
        if output_format == 'dict':
            return self.combined_results
        elif output_format == 'dataframe':
            return pd.DataFrame.from_dict(self.combined_results, orient='index', columns=['score'])
        elif output_format == 'string':
            report = ["Program Evaluation Results:"]
            for dimension, score in self.combined_results.items():
                report.append(f"{dimension}: {score:.2f}")
            return "\n".join(report)
        else:
            raise ValueError("Invalid output format. Choose 'dict', 'dataframe', or 'string'")

# Example usage
if __name__ == "__main__":
    evaluator = ProgramEvaluator()
    
    try:
        evaluator.load_quantitative_data("quant_data.csv")
        evaluator.load_qualitative_data("qual_data.csv")
        
        results = evaluator.blend_data()
        report = evaluator.generate_report('string')
        
        print(report)
    except Exception as e:
        logger.error(f"Evaluation failed: {str(e)}")
```
