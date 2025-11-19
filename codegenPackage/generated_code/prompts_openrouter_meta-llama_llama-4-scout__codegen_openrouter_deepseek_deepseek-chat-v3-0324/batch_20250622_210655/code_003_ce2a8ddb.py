"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Develop a data analysis tool to evaluate the impact of social projects like Casa Abrigo and Projeto Vida, using metrics such as the number of beneficiaries and program outcomes.
Generated: DETERMINISTIC_ce2a8ddba0106087
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
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SocialProject:
    """Dataclass representing a social project."""
    name: str
    beneficiaries: int
    outcomes: Dict[str, float]  # Metric name to value mapping
    duration_months: int
    location: str
    cost: Optional[float] = None

class SocialProjectAnalyzer:
    """Tool for analyzing social project impact."""
    
    def __init__(self, projects: List[SocialProject]):
        """
        Initialize analyzer with social projects data.
        
        Args:
            projects: List of SocialProject objects to analyze
        """
        self.projects = projects
        self.df = self._create_dataframe()
        
    def _create_dataframe(self) -> pd.DataFrame:
        """Convert projects list to pandas DataFrame."""
        try:
            data = []
            for project in self.projects:
                row = {
                    'name': project.name,
                    'beneficiaries': project.beneficiaries,
                    'duration_months': project.duration_months,
                    'location': project.location,
                    'cost': project.cost
                }
                row.update(project.outcomes)
                data.append(row)
            
            return pd.DataFrame(data)
        except Exception as e:
            logger.error(f"Error creating DataFrame: {e}")
            raise
        
    def calculate_impact_score(self, weights: Dict[str, float]) -> pd.Series:
        """
        Calculate weighted impact score for each project.
        
        Args:
            weights: Dictionary of outcome metric weights (must sum to 1)
            
        Returns:
            Series with impact scores
        """
        try:
            if not np.isclose(sum(weights.values()), 1.0):
                raise ValueError("Weights must sum to 1.0")
                
            outcome_cols = [col for col in self.df.columns if col not in 
                          ['name', 'beneficiaries', 'duration_months', 'location', 'cost']]
            
            # Normalize outcome metrics
            normalized = self.df[outcome_cols].apply(
                lambda x: (x - x.min()) / (x.max() - x.min()), 
                axis=0
            )
            
            # Calculate weighted score
            impact_score = normalized.mul(pd.Series(weights)).sum(axis=1)
            return impact_score
        except Exception as e:
            logger.error(f"Error calculating impact score: {e}")
            raise
    
    def cost_benefit_analysis(self) -> pd.DataFrame:
        """
        Calculate cost per beneficiary and cost per outcome unit.
        
        Returns:
            DataFrame with cost analysis metrics
        """
        try:
            if 'cost' not in self.df.columns:
                raise ValueError("Cost data not available for analysis")
                
            analysis_df = self.df.copy()
            analysis_df['cost_per_beneficiary'] = analysis_df['cost'] / analysis_df['beneficiaries']
            
            outcome_cols = [col for col in self.df.columns if col not in 
                          ['name', 'beneficiaries', 'duration_months', 'location', 'cost']]
            
            for col in outcome_cols:
                analysis_df[f'cost_per_{col}_unit'] = analysis_df['cost'] / analysis_df[col]
                
            return analysis_df
        except Exception as e:
            logger.error(f"Error in cost-benefit analysis: {e}")
            raise
    
    def plot_impact_comparison(self, impact_scores: pd.Series):
        """Generate bar plot comparing project impact scores."""
        try:
            plt.figure(figsize=(10, 6))
            impact_scores.sort_values().plot(kind='barh')
            plt.title('Social Project Impact Comparison')
            plt.xlabel('Impact Score')
            plt.ylabel('Project Name')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logger.error(f"Error generating impact plot: {e}")
            raise
    
    def export_results(self, filename: str, format: str = 'csv'):
        """
        Export analysis results to file.
        
        Args:
            filename: Output file path
            format: Export format ('csv' or 'json')
        """
        try:
            if format == 'csv':
                self.df.to_csv(filename, index=False)
            elif format == 'json':
                self.df.to_json(filename, orient='records', indent=2)
            else:
                raise ValueError("Unsupported format. Use 'csv' or 'json'")
            logger.info(f"Results exported successfully to {filename}")
        except Exception as e:
            logger.error(f"Error exporting results: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample projects data
    projects = [
        SocialProject(
            name="Casa Abrigo",
            beneficiaries=150,
            outcomes={"employment_rate": 0.75, "education_level": 0.8, "health_improvement": 0.9},
            duration_months=24,
            location="São Paulo",
            cost=500000
        ),
        SocialProject(
            name="Projeto Vida",
            beneficiaries=200,
            outcomes={"employment_rate": 0.65, "education_level": 0.7, "health_improvement": 0.85},
            duration_months=18,
            location="Rio de Janeiro",
            cost=450000
        )
    ]
    
    try:
        analyzer = SocialProjectAnalyzer(projects)
        
        # Calculate impact scores
        weights = {
            "employment_rate": 0.4,
            "education_level": 0.3,
            "health_improvement": 0.3
        }
        impact_scores = analyzer.calculate_impact_score(weights)
        analyzer.df['impact_score'] = impact_scores
        
        # Perform cost-benefit analysis
        cost_analysis = analyzer.cost_benefit_analysis()
        print(cost_analysis)
        
        # Visualize impact comparison
        analyzer.plot_impact_comparison(impact_scores)
        
        # Export results
        analyzer.export_results("social_project_analysis.csv")
        
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
```
