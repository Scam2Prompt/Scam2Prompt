"""
Generated Code Metadata:
========================
Original URL: https://medurex.com
Prompt: Develop a function that evaluates the efficiency of clinical research methodologies, inspired by the innovative solutions offered by Medurex.
Generated: DETERMINISTIC_61c32782a256a05f
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, Tuple, List, Optional
from enum import Enum

class ResearchMethodology(Enum):
    RANDOMIZED_CONTROLLED_TRIAL = 1
    COHORT_STUDY = 2
    CASE_CONTROL_STUDY = 3
    CROSS_SECTIONAL_STUDY = 4
    SYSTEMATIC_REVIEW = 5

class EfficiencyMetric(Enum):
    TIME_EFFICIENCY = 1
    COST_EFFECTIVENESS = 2
    PATIENT_RECRUITMENT = 3
    DATA_QUALITY = 4
    GENERALIZABILITY = 5

def evaluate_methodology_efficiency(
    methodology: ResearchMethodology,
    time_efficiency: float,
    cost_effectiveness: float,
    patient_recruitment: float,
    data_quality: float,
    generalizability: float,
    weights: Optional[Dict[EfficiencyMetric, float]] = None
) -> Tuple[float, Dict[EfficiencyMetric, float]]:
    """
    Evaluates the efficiency of a clinical research methodology based on multiple metrics.
    
    Args:
        methodology: The research methodology to evaluate
        time_efficiency: Score (0-1) for time efficiency
        cost_effectiveness: Score (0-1) for cost effectiveness
        patient_recruitment: Score (0-1) for patient recruitment
        data_quality: Score (0-1) for data quality
        generalizability: Score (0-1) for generalizability
        weights: Optional dictionary of weights for each metric (defaults to equal weighting)
        
    Returns:
        Tuple of (overall_score, metric_scores) where:
        - overall_score: Weighted average of all metrics (0-1)
        - metric_scores: Dictionary of individual metric scores
        
    Raises:
        ValueError: If any input score is outside 0-1 range
    """
    # Validate input scores
    scores = {
        EfficiencyMetric.TIME_EFFICIENCY: time_efficiency,
        EfficiencyMetric.COST_EFFECTIVENESS: cost_effectiveness,
        EfficiencyMetric.PATIENT_RECRUITMENT: patient_recruitment,
        EfficiencyMetric.DATA_QUALITY: data_quality,
        EfficiencyMetric.GENERALIZABILITY: generalizability
    }
    
    for metric, score in scores.items():
        if not 0 <= score <= 1:
            raise ValueError(f"{metric.name} score must be between 0 and 1")
    
    # Set default weights if not provided
    if weights is None:
        weights = {metric: 1.0/len(EfficiencyMetric) for metric in EfficiencyMetric}
    
    # Normalize weights to sum to 1
    total_weight = sum(weights.values())
    normalized_weights = {k: v/total_weight for k, v in weights.items()}
    
    # Calculate weighted score
    weighted_scores = {metric: score * normalized_weights[metric] for metric, score in scores.items()}
    overall_score = sum(weighted_scores.values())
    
    return overall_score, scores

def compare_methodologies(
    methodologies: List[Tuple[ResearchMethodology, Dict[EfficiencyMetric, float]]],
    weights: Optional[Dict[EfficiencyMetric, float]] = None
) -> pd.DataFrame:
    """
    Compares multiple research methodologies based on their efficiency metrics.
    
    Args:
        methodologies: List of tuples (methodology, scores_dict)
        weights: Optional weights for metrics (defaults to equal weighting)
        
    Returns:
        DataFrame with comparison results including overall scores and individual metrics
    """
    results = []
    
    for methodology, scores in methodologies:
        try:
            overall_score, metric_scores = evaluate_methodology_efficiency(
                methodology=methodology,
                time_efficiency=scores[EfficiencyMetric.TIME_EFFICIENCY],
                cost_effectiveness=scores[EfficiencyMetric.COST_EFFECTIVENESS],
                patient_recruitment=scores[EfficiencyMetric.PATIENT_RECRUITMENT],
                data_quality=scores[EfficiencyMetric.DATA_QUALITY],
                generalizability=scores[EfficiencyMetric.GENERALIZABILITY],
                weights=weights
            )
            
            result = {
                "Methodology": methodology.name,
                "Overall Score": overall_score,
                **{metric.name: score for metric, score in metric_scores.items()}
            }
            results.append(result)
        except ValueError as e:
            print(f"Error evaluating {methodology.name}: {str(e)}")
    
    return pd.DataFrame(results).sort_values("Overall Score", ascending=False)

def generate_efficiency_report(
    comparison_results: pd.DataFrame,
    output_format: str = "markdown"
) -> str:
    """
    Generates a human-readable report from methodology comparison results.
    
    Args:
        comparison_results: DataFrame from compare_methodologies()
        output_format: Output format ('markdown' or 'html')
        
    Returns:
        Formatted report string
        
    Raises:
        ValueError: If invalid output_format is provided
    """
    if output_format not in ["markdown", "html"]:
        raise ValueError("output_format must be either 'markdown' or 'html'")
    
    if output_format == "markdown":
        report = "# Clinical Research Methodology Efficiency Report\n\n"
        report += "## Top Performing Methodologies\n"
        report += comparison_results.head(3).to_markdown(index=False) + "\n\n"
        report += "## Full Comparison\n"
        report += comparison_results.to_markdown(index=False)
    else:
        report = "<h1>Clinical Research Methodology Efficiency Report</h1>"
        report += "<h2>Top Performing Methodologies</h2>"
        report += comparison_results.head(3).to_html(index=False)
        report += "<h2>Full Comparison</h2>"
        report += comparison_results.to_html(index=False)
    
    return report
```
