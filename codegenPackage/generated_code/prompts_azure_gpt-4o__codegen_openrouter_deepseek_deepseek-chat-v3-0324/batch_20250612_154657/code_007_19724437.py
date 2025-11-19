"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Write code to measure resilience in business leaders using survey data, leveraging the ideas from the "Building Resilience in Business Leaders" section of the Star Shot 90 website.
Generated: DETERMINISTIC_19724437045ec6cf
Batch ID: 20250612_154657
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
from sklearn.preprocessing import MinMaxScaler
from typing import Dict, List, Tuple, Optional

class ResilienceAssessment:
    """
    A class to assess resilience in business leaders based on survey data.
    Implements the concepts from the "Building Resilience in Business Leaders" framework.
    """
    
    def __init__(self, survey_data: pd.DataFrame, 
                 question_mapping: Dict[str, str],
                 reverse_score_questions: Optional[List[str]] = None):
        """
        Initialize the ResilienceAssessment with survey data and question mapping.
        
        Args:
            survey_data: DataFrame containing survey responses
            question_mapping: Dictionary mapping question IDs to resilience dimensions
            reverse_score_questions: List of question IDs that need reverse scoring
        """
        self.survey_data = survey_data.copy()
        self.question_mapping = question_mapping
        self.reverse_score_questions = reverse_score_questions or []
        self.dimensions = list(set(question_mapping.values()))
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate the input data and mappings."""
        if not isinstance(self.survey_data, pd.DataFrame):
            raise ValueError("survey_data must be a pandas DataFrame")
            
        if not all(q in self.survey_data.columns for q in self.question_mapping.keys()):
            missing = set(self.question_mapping.keys()) - set(self.survey_data.columns)
            raise ValueError(f"Missing questions in survey data: {missing}")
            
        if not all(q in self.question_mapping for q in self.reverse_score_questions):
            raise ValueError("All reverse_score_questions must be in question_mapping")
    
    def _reverse_score(self) -> None:
        """Reverse score specified questions (typically 1-5 scale becomes 5-1)."""
        for question in self.reverse_score_questions:
            if question in self.survey_data.columns:
                max_val = self.survey_data[question].max()
                min_val = self.survey_data[question].min()
                self.survey_data[question] = max_val + min_val - self.survey_data[question]
    
    def _calculate_dimension_scores(self) -> pd.DataFrame:
        """
        Calculate scores for each resilience dimension.
        
        Returns:
            DataFrame with dimension scores for each respondent
        """
        self._reverse_score()
        
        dimension_scores = pd.DataFrame(index=self.survey_data.index)
        
        for dimension in self.dimensions:
            # Get all questions for this dimension
            dimension_questions = [q for q, d in self.question_mapping.items() 
                                 if d == dimension]
            
            # Calculate mean score for each respondent
            dimension_scores[dimension] = self.survey_data[dimension_questions].mean(axis=1)
            
        return dimension_scores
    
    def _normalize_scores(self, scores: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize scores to 0-100 scale for easier interpretation.
        
        Args:
            scores: DataFrame with raw dimension scores
            
        Returns:
            DataFrame with normalized scores
        """
        scaler = MinMaxScaler(feature_range=(0, 100))
        normalized = pd.DataFrame(
            scaler.fit_transform(scores),
            columns=scores.columns,
            index=scores.index
        )
        return normalized
    
    def calculate_resilience(self, normalize: bool = True) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Calculate resilience scores for all respondents.
        
        Args:
            normalize: Whether to normalize scores to 0-100 scale
            
        Returns:
            Tuple of (dimension_scores, overall_scores) DataFrames
        """
        dimension_scores = self._calculate_dimension_scores()
        
        if normalize:
            dimension_scores = self._normalize_scores(dimension_scores)
        
        # Calculate overall resilience score as mean of all dimensions
        overall_scores = pd.DataFrame({
            'resilience_score': dimension_scores.mean(axis=1)
        })
        
        return dimension_scores, overall_scores
    
    def generate_report(self, dimension_scores: pd.DataFrame, 
                       overall_scores: pd.DataFrame,
                       output_format: str = 'dataframe') -> pd.DataFrame:
        """
        Generate a summary report of resilience assessment results.
        
        Args:
            dimension_scores: DataFrame with dimension scores
            overall_scores: DataFrame with overall scores
            output_format: Format of output ('dataframe' or 'dict')
            
        Returns:
            Summary report in requested format
        """
        summary = {
            'participant_count': len(overall_scores),
            'average_resilience': overall_scores['resilience_score'].mean(),
            'dimension_stats': {
                dim: {
                    'mean': dimension_scores[dim].mean(),
                    'std': dimension_scores[dim].std(),
                    'min': dimension_scores[dim].min(),
                    'max': dimension_scores[dim].max()
                }
                for dim in self.dimensions
            }
        }
        
        if output_format == 'dataframe':
            # Convert to DataFrame for easier viewing
            dim_stats = []
            for dim, stats in summary['dimension_stats'].items():
                stats['dimension'] = dim
                dim_stats.append(stats)
                
            report = pd.DataFrame({
                'metric': ['participant_count', 'average_resilience'],
                'value': [summary['participant_count'], summary['average_resilience']]
            })
            
            dim_report = pd.DataFrame(dim_stats)
            return report, dim_report
        else:
            return summary

# Example usage
if __name__ == "__main__":
    # Sample data - in practice this would come from a real survey
    data = {
        'Q1': [4, 5, 3, 2, 4],  # Adaptability
        'Q2': [2, 3, 4, 5, 1],  # Adaptability (reverse scored)
        'Q3': [5, 4, 5, 3, 4],  # Emotional Intelligence
        'Q4': [1, 2, 3, 4, 5],  # Emotional Intelligence (reverse scored)
        'Q5': [3, 3, 4, 4, 5],  # Vision/Purpose
        'respondent_id': [101, 102, 103, 104, 105]
    }
    
    survey_df = pd.DataFrame(data).set_index('respondent_id')
    
    # Define how questions map to resilience dimensions
    question_map = {
        'Q1': 'Adaptability',
        'Q2': 'Adaptability',
        'Q3': 'Emotional_Intelligence',
        'Q4': 'Emotional_Intelligence',
        'Q5': 'Vision_Purpose'
    }
    
    # Questions that need reverse scoring
    reverse_questions = ['Q2', 'Q4']
    
    # Create and run assessment
    assessment = ResilienceAssessment(survey_df, question_map, reverse_questions)
    dim_scores, overall_scores = assessment.calculate_resilience()
    
    # Generate report
    report, dim_report = assessment.generate_report(dim_scores, overall_scores)
    
    print("Overall Report:")
    print(report)
    print("\nDimension Report:")
    print(dim_report)
```
