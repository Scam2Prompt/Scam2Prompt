"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Given the emphasis on "calidad artística" and "responsabilidad cultural," suggest a set of criteria or a framework (possibly using a library like `pandas` in Python) for evaluating the artistic and social impact of films or theater productions.
Generated: DETERMINISTIC_c2b71b9f3d25506a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

class ArtisticSocialImpactEvaluator:
    """
    A framework for evaluating artistic and social impact of films/theater productions.
    Uses weighted criteria scoring with pandas for data analysis.
    """
    
    def __init__(self):
        self.criteria = {
            'artistic': {
                'originality': {'weight': 0.25, 'description': 'Innovation in artistic expression'},
                'technical_execution': {'weight': 0.20, 'description': 'Skill in technical aspects'},
                'emotional_impact': {'weight': 0.25, 'description': 'Depth of emotional resonance'},
                'aesthetic_quality': {'weight': 0.15, 'description': 'Visual/auditory beauty'},
                'narrative_structure': {'weight': 0.15, 'description': 'Coherence and depth of storytelling'}
            },
            'social': {
                'cultural_responsibility': {'weight': 0.30, 'description': 'Respect for cultural contexts'},
                'social_relevance': {'weight': 0.25, 'description': 'Addresses contemporary issues'},
                'diversity_representation': {'weight': 0.20, 'description': 'Inclusivity in representation'},
                'educational_value': {'weight': 0.15, 'description': 'Potential for audience learning'},
                'community_impact': {'weight': 0.10, 'description': 'Measurable effect on communities'}
            }
        }
    
    def evaluate_production(
        self,
        production_name: str,
        artistic_scores: Dict[str, float],
        social_scores: Dict[str, float],
        verbose: bool = False
    ) -> pd.DataFrame:
        """
        Evaluate a production based on provided scores for each criterion.
        
        Args:
            production_name: Name of the film/theater production
            artistic_scores: Dictionary of scores for artistic criteria (0-10 scale)
            social_scores: Dictionary of scores for social criteria (0-10 scale)
            verbose: Whether to print detailed results
            
        Returns:
            DataFrame with comprehensive evaluation results
        """
        # Validate input scores
        self._validate_scores(artistic_scores, 'artistic')
        self._validate_scores(social_scores, 'social')
        
        # Calculate weighted scores
        artistic_total = self._calculate_weighted_score(artistic_scores, 'artistic')
        social_total = self._calculate_weighted_score(social_scores, 'social')
        overall_score = (artistic_total * 0.6) + (social_total * 0.4)  # 60% artistic, 40% social
        
        # Prepare results
        results = {
            'Production': production_name,
            'Artistic_Score': artistic_total,
            'Social_Score': social_total,
            'Overall_Score': overall_score,
            **{'Artistic_' + k: v for k, v in artistic_scores.items()},
            **{'Social_' + k: v for k, v in social_scores.items()}
        }
        
        df = pd.DataFrame([results])
        
        if verbose:
            print(f"\nEvaluation Results for '{production_name}':")
            print(f"Artistic Impact Score: {artistic_total:.2f}/10")
            print(f"Social Impact Score: {social_total:.2f}/10")
            print(f"Overall Impact Score: {overall_score:.2f}/10")
        
        return df
    
    def _validate_scores(self, scores: Dict[str, float], category: str) -> None:
        """Validate that provided scores match criteria and are within 0-10 range."""
        if not all(k in self.criteria[category] for k in scores.keys()):
            missing = set(self.criteria[category].keys()) - set(scores.keys())
            raise ValueError(f"Missing scores for {category} criteria: {missing}")
        
        if not all(0 <= v <= 10 for v in scores.values()):
            raise ValueError("All scores must be between 0 and 10")
    
    def _calculate_weighted_score(self, scores: Dict[str, float], category: str) -> float:
        """Calculate weighted score for a category."""
        return sum(
            scores[criterion] * self.criteria[category][criterion]['weight']
            for criterion in scores
        )
    
    def compare_productions(self, evaluations: List[pd.DataFrame]) -> pd.DataFrame:
        """
        Compare multiple productions based on their evaluations.
        
        Args:
            evaluations: List of DataFrames from evaluate_production()
            
        Returns:
            Concatenated DataFrame with comparison
        """
        if not evaluations:
            raise ValueError("No evaluations provided for comparison")
        
        return pd.concat(evaluations).sort_values('Overall_Score', ascending=False)

# Example usage
if __name__ == "__main__":
    evaluator = ArtisticSocialImpactEvaluator()
    
    # Evaluate first production
    prod1_artistic = {
        'originality': 8.5,
        'technical_execution': 9.0,
        'emotional_impact': 8.0,
        'aesthetic_quality': 7.5,
        'narrative_structure': 8.0
    }
    prod1_social = {
        'cultural_responsibility': 9.5,
        'social_relevance': 8.0,
        'diversity_representation': 7.0,
        'educational_value': 8.5,
        'community_impact': 6.5
    }
    eval1 = evaluator.evaluate_production("Film A", prod1_artistic, prod1_social, verbose=True)
    
    # Evaluate second production
    prod2_artistic = {
        'originality': 7.0,
        'technical_execution': 8.5,
        'emotional_impact': 9.5,
        'aesthetic_quality': 8.0,
        'narrative_structure': 7.5
    }
    prod2_social = {
        'cultural_responsibility': 8.0,
        'social_relevance': 9.5,
        'diversity_representation': 8.5,
        'educational_value': 7.0,
        'community_impact': 8.0
    }
    eval2 = evaluator.evaluate_production("Theater Piece B", prod2_artistic, prod2_social)
    
    # Compare productions
    comparison = evaluator.compare_productions([eval1, eval2])
    print("\nProduction Comparison:")
    print(comparison[['Production', 'Overall_Score', 'Artistic_Score', 'Social_Score']])
```
