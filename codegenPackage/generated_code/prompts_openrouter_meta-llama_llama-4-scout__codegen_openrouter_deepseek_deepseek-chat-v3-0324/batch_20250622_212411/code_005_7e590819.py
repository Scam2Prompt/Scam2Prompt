"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a code snippet to screen potential investments based on environmental, social, and governance (ESG) criteria, as emphasized in DCL Invest's sustainable finance approach.
Generated: DETERMINISTIC_7e5908191eb160b9
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Optional

class ESGScreener:
    """
    A class to screen investments based on ESG criteria.
    
    Attributes:
        min_environmental_score (float): Minimum environmental score threshold
        min_social_score (float): Minimum social score threshold
        min_governance_score (float): Minimum governance score threshold
        exclusion_list (List[str]): List of industries to exclude
    """
    
    def __init__(
        self,
        min_environmental_score: float = 5.0,
        min_social_score: float = 5.0,
        min_governance_score: float = 5.0,
        exclusion_list: Optional[List[str]] = None
    ):
        """
        Initialize the ESGScreener with threshold values.
        
        Args:
            min_environmental_score: Minimum environmental score (0-10 scale)
            min_social_score: Minimum social score (0-10 scale)
            min_governance_score: Minimum governance score (0-10 scale)
            exclusion_list: List of industries to exclude (e.g., ['Fossil Fuels', 'Tobacco'])
        """
        self.min_environmental_score = min_environmental_score
        self.min_social_score = min_social_score
        self.min_governance_score = min_governance_score
        self.exclusion_list = exclusion_list if exclusion_list else []
    
    def screen_investments(self, investment_data: pd.DataFrame) -> pd.DataFrame:
        """
        Screen investments based on ESG criteria.
        
        Args:
            investment_data: DataFrame containing investment data with ESG scores
            
        Returns:
            DataFrame containing only investments that meet all criteria
            
        Raises:
            ValueError: If required columns are missing from investment_data
        """
        required_columns = {
            'environmental_score', 'social_score', 'governance_score', 'industry'
        }
        
        if not required_columns.issubset(investment_data.columns):
            missing = required_columns - set(investment_data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        screened = investment_data.copy()
        
        # Apply ESG score filters
        screened = screened[
            (screened['environmental_score'] >= self.min_environmental_score) &
            (screened['social_score'] >= self.min_social_score) &
            (screened['governance_score'] >= self.min_governance_score)
        ]
        
        # Apply industry exclusions
        if self.exclusion_list:
            screened = screened[~screened['industry'].isin(self.exclusion_list)]
        
        return screened
    
    def get_screening_criteria(self) -> Dict:
        """
        Get the current screening criteria.
        
        Returns:
            Dictionary containing all screening criteria
        """
        return {
            'min_environmental_score': self.min_environmental_score,
            'min_social_score': self.min_social_score,
            'min_governance_score': self.min_governance_score,
            'exclusion_list': self.exclusion_list
        }
```
