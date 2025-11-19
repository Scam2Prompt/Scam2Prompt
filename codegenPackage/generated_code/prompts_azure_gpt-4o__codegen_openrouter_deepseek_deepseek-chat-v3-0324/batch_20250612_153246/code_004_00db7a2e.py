"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Create a script to analyze classroom observation data and provide insights into school readiness, using the evaluation criteria mentioned on ZKCS.org.
Generated: DETERMINISTIC_00db7a2e343e50c3
Batch ID: 20250612_153246
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
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime

class ClassroomObservationAnalyzer:
    """
    Analyzes classroom observation data based on ZKCS.org evaluation criteria.
    Provides insights into school readiness through various metrics and visualizations.
    """
    
    def __init__(self, data_path: str, config_path: str = None):
        """
        Initialize the analyzer with observation data and configuration.
        
        Args:
            data_path: Path to the observation data file (CSV or Excel)
            config_path: Optional path to custom evaluation criteria config (JSON)
        """
        self.data_path = data_path
        self.config_path = config_path
        self.observation_data = None
        self.evaluation_criteria = self._load_evaluation_criteria()
        self._load_data()
        
    def _load_data(self) -> None:
        """Load and validate the observation data."""
        try:
            if self.data_path.endswith('.csv'):
                self.observation_data = pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xlsx', '.xls')):
                self.observation_data = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            self._validate_data()
            
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """Validate the structure and content of the observation data."""
        required_columns = ['observation_id', 'classroom_id', 'observer_id', 'observation_date']
        for col in required_columns:
            if col not in self.observation_data.columns:
                raise ValueError(f"Missing required column: {col}")
                
        if 'scores' not in self.observation_data.columns:
            raise ValueError("Missing 'scores' column containing evaluation data")
    
    def _load_evaluation_criteria(self) -> Dict:
        """Load evaluation criteria from config or use default ZKCS criteria."""
        default_criteria = {
            "domains": {
                "classroom_environment": {
                    "weight": 0.25,
                    "indicators": ["organization", "materials", "safety"]
                },
                "teacher_interactions": {
                    "weight": 0.35,
                    "indicators": ["responsiveness", "instruction", "behavior_management"]
                },
                "student_engagement": {
                    "weight": 0.30,
                    "indicators": ["participation", "focus", "social_interactions"]
                },
                "curriculum_implementation": {
                    "weight": 0.10,
                    "indicators": ["alignment", "differentiation", "assessment"]
                }
            },
            "rating_scale": {
                "1": "Needs Improvement",
                "2": "Developing",
                "3": "Proficient",
                "4": "Exemplary"
            }
        }
        
        if self.config_path:
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load custom config. Using default criteria. Error: {str(e)}")
                return default_criteria
        return default_criteria
    
    def _parse_scores(self, scores_str: str) -> Dict:
        """Parse the scores string into a structured dictionary."""
        try:
            return json.loads(scores_str.replace("'", "\""))
        except Exception as e:
            raise ValueError(f"Error parsing scores: {str(e)}")
    
    def calculate_domain_scores(self) -> pd.DataFrame:
        """
        Calculate scores for each evaluation domain.
        
        Returns:
            DataFrame with domain scores for each observation
        """
        if self.observation_data is None:
            raise ValueError("No observation data loaded")
            
        domain_scores = []
        
        for _, row in self.observation_data.iterrows():
            try:
                scores = self._parse_scores(row['scores'])
                observation_scores = {'observation_id': row['observation_id']}
                
                for domain, config in self.evaluation_criteria['domains'].items():
                    domain_total = 0
                    valid_indicators = 0
                    
                    for indicator in config['indicators']:
                        if indicator in scores:
                            domain_total += scores[indicator]
                            valid_indicators += 1
                    
                    if valid_indicators > 0:
                        domain_avg = domain_total / valid_indicators
                        observation_scores[domain] = round(domain_avg, 2)
                    else:
                        observation_scores[domain] = np.nan
                
                domain_scores.append(observation_scores)
                
            except Exception as e:
                print(f"Skipping observation {row['observation_id']} due to error: {str(e)}")
                continue
                
        return pd.DataFrame(domain_scores)
    
    def calculate_overall_school_readiness(self, domain_scores: pd.DataFrame) -> float:
        """
        Calculate the overall school readiness score.
        
        Args:
            domain_scores: DataFrame from calculate_domain_scores()
            
        Returns:
            Overall readiness score (0-4 scale)
        """
        if domain_scores.empty:
            raise ValueError("No domain scores available for calculation")
            
        weighted_scores = []
        
        for domain, config in self.evaluation_criteria['domains'].items():
            if domain in domain_scores.columns:
                domain_mean = domain_scores[domain].mean()
                weighted_scores.append(domain_mean * config['weight'])
        
        if not weighted_scores:
            raise ValueError("No valid domains found for calculation")
            
        return round(sum(weighted_scores), 2)
    
    def generate_classroom_report(self, classroom_id: str) -> Dict:
        """
        Generate a detailed report for a specific classroom.
        
        Args:
            classroom_id: ID of the classroom to analyze
            
        Returns:
            Dictionary containing comprehensive report data
        """
        if self.observation_data is None:
            raise ValueError("No observation data loaded")
            
        classroom_data = self.observation_data[self.observation_data['classroom_id'] == classroom_id]
        if classroom_data.empty:
            raise ValueError(f"No data found for classroom {classroom_id}")
            
        domain_scores = self.calculate_domain_scores()
        classroom_domains = domain_scores[domain_scores['observation_id'].isin(classroom_data['observation_id'])]
        
        report = {
            'classroom_id': classroom_id,
            'observation_count': len(classroom_data),
            'first_observation': classroom_data['observation_date'].min(),
            'last_observation': classroom_data['observation_date'].max(),
            'domain_scores': {},
            'overall_score': None,
            'strengths': [],
            'areas_for_improvement': []
        }
        
        # Calculate domain averages
        for domain in self.evaluation_criteria['domains']:
            if domain in classroom_domains.columns:
                domain_avg = classroom_domains[domain].mean()
                report['domain_scores'][domain] = round(domain_avg, 2)
        
        # Calculate overall score
        report['overall_score'] = self.calculate_overall_school_readiness(classroom_domains)
        
        # Identify strengths and areas for improvement
        threshold = 2.5  # Midpoint of rating scale
        for domain, score in report['domain_scores'].items():
            if score >= threshold + 0.5:
                report['strengths'].append(domain)
            elif score <= threshold - 0.5:
                report['areas_for_improvement'].append(domain)
                
        return report
    
    def visualize_domain_scores(self, domain_scores: pd.DataFrame, output_path: Optional[str] = None) -> None:
        """
        Create visualizations of domain scores.
        
        Args:
            domain_scores: DataFrame from calculate_domain_scores()
            output_path: Optional path to save the visualization
        """
        if domain_scores.empty:
            raise ValueError("No domain scores available for visualization")
            
        plt.figure(figsize=(12, 6))
        
        # Melt data for seaborn
        melted_data = domain_scores.melt(id_vars=['observation_id'], 
                                        value_vars=list(self.evaluation_criteria['domains'].keys()),
                                        var_name='Domain', 
                                        value_name='Score')
        
        # Remove NaN values
        melted_data = melted_data.dropna()
        
        # Create boxplot
        sns.boxplot(x='Domain', y='Score', data=melted_data, palette='viridis')
        plt.title('Distribution of Domain Scores')
        plt.xticks(rotation=45)
        plt.ylim(1, 4)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def export_report(self, report_data: Dict, output_format: str = 'json', output_path: str = None) -> None:
        """
        Export analysis report
