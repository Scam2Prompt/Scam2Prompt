"""
Generated Code Metadata:
========================
Original URL: https://shift4strategy.com
Prompt: Write a Python script to analyze assumptions and establish baselines for a strategic business plan, incorporating methods inspired by SHIFT4's approach to critical analysis.
Generated: DETERMINISTIC_13ee1a4f01575d35
Batch ID: 20250612_145306
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
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class BusinessAssumption:
    """Dataclass to represent a business assumption."""
    name: str
    description: str
    value: float
    confidence: float  # 0-1 scale
    source: str
    impact: str  # High/Medium/Low

class BusinessPlanAnalyzer:
    """Class to analyze business plan assumptions and establish baselines."""
    
    def __init__(self, assumptions: List[BusinessAssumption]):
        self.assumptions = assumptions
        self.baselines = {}
        self.sensitivity_results = {}
        
    def validate_assumptions(self) -> bool:
        """Validate all business assumptions."""
        try:
            for assumption in self.assumptions:
                if not 0 <= assumption.confidence <= 1:
                    raise ValueError(f"Confidence for {assumption.name} must be between 0 and 1")
                if assumption.value < 0:
                    raise ValueError(f"Value for {assumption.name} cannot be negative")
                if assumption.impact not in ['High', 'Medium', 'Low']:
                    raise ValueError(f"Impact for {assumption.name} must be High/Medium/Low")
            return True
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            return False
    
    def calculate_baselines(self) -> Dict[str, float]:
        """Calculate baseline metrics for the business plan."""
        if not self.validate_assumptions():
            raise ValueError("Cannot calculate baselines with invalid assumptions")
            
        try:
            # Basic metrics
            total_assumptions = len(self.assumptions)
            high_impact = sum(1 for a in self.assumptions if a.impact == 'High')
            avg_confidence = np.mean([a.confidence for a in self.assumptions])
            
            # Weighted value calculation
            weighted_values = []
            for a in self.assumptions:
                weight = 1.0
                if a.impact == 'High':
                    weight = 3.0
                elif a.impact == 'Medium':
                    weight = 2.0
                weighted_values.append(a.value * weight * a.confidence)
            
            composite_score = np.sum(weighted_values)
            
            self.baselines = {
                'total_assumptions': total_assumptions,
                'high_impact_assumptions': high_impact,
                'average_confidence': avg_confidence,
                'composite_score': composite_score,
                'risk_index': (1 - avg_confidence) * high_impact
            }
            
            return self.baselines
            
        except Exception as e:
            logger.error(f"Error calculating baselines: {str(e)}")
            raise
    
    def sensitivity_analysis(self, variations: float = 0.1) -> Dict[str, Dict[str, float]]:
        """Perform sensitivity analysis on key assumptions."""
        try:
            results = {}
            for assumption in self.assumptions:
                if assumption.impact != 'High':
                    continue
                    
                original_value = assumption.value
                variations_range = [
                    original_value * (1 - variations),
                    original_value * (1 + variations)
                ]
                
                # Calculate impact on composite score
                original_score = self.baselines['composite_score']
                
                # Calculate lower bound impact
                assumption.value = variations_range[0]
                self.calculate_baselines()
                lower_score = self.baselines['composite_score']
                
                # Calculate upper bound impact
                assumption.value = variations_range[1]
                self.calculate_baselines()
                upper_score = self.baselines['composite_score']
                
                # Reset to original value
                assumption.value = original_value
                self.calculate_baselines()
                
                results[assumption.name] = {
                    'lower_bound': variations_range[0],
                    'upper_bound': variations_range[1],
                    'score_impact_lower': (lower_score - original_score) / original_score,
                    'score_impact_upper': (upper_score - original_score) / original_score
                }
            
            self.sensitivity_results = results
            return results
            
        except Exception as e:
            logger.error(f"Error in sensitivity analysis: {str(e)}")
            raise
    
    def visualize_sensitivity(self) -> None:
        """Visualize sensitivity analysis results."""
        if not self.sensitivity_results:
            logger.warning("No sensitivity results to visualize. Run sensitivity_analysis first.")
            return
            
        try:
            data = []
            for assumption, values in self.sensitivity_results.items():
                data.append({
                    'Assumption': assumption,
                    'Impact': abs(values['score_impact_lower']),
                    'Direction': 'Negative'
                })
                data.append({
                    'Assumption': assumption,
                    'Impact': abs(values['score_impact_upper']),
                    'Direction': 'Positive'
                })
            
            df = pd.DataFrame(data)
            
            plt.figure(figsize=(12, 6))
            sns.barplot(
                x='Impact',
                y='Assumption',
                hue='Direction',
                data=df,
                palette={'Negative': 'red', 'Positive': 'green'}
            )
            plt.title('Sensitivity Analysis of High Impact Assumptions')
            plt.xlabel('Percentage Impact on Composite Score')
            plt.ylabel('Assumption')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error visualizing sensitivity: {str(e)}")
            raise
    
    def generate_report(self) -> Dict[str, dict]:
        """Generate comprehensive analysis report."""
        try:
            if not self.baselines:
                self.calculate_baselines()
                
            if not self.sensitivity_results:
                self.sensitivity_analysis()
                
            report = {
                'baselines': self.baselines,
                'sensitivity_analysis': self.sensitivity_results,
                'assumptions': [
                    {
                        'name': a.name,
                        'description': a.description,
                        'value': a.value,
                        'confidence': a.confidence,
                        'impact': a.impact,
                        'source': a.source
                    }
                    for a in self.assumptions
                ]
            }
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample business assumptions
    assumptions = [
        BusinessAssumption(
            name="Market Growth Rate",
            description="Annual growth rate of target market",
            value=0.05,
            confidence=0.8,
            source="Industry Report 2023",
            impact="High"
        ),
        BusinessAssumption(
            name="Customer Acquisition Cost",
            description="Average cost to acquire a new customer",
            value=150.0,
            confidence=0.7,
            source="Historical Data",
            impact="High"
        ),
        BusinessAssumption(
            name="Churn Rate",
            description="Annual customer churn rate",
            value=0.15,
            confidence=0.65,
            source="Internal Metrics",
            impact="Medium"
        ),
        BusinessAssumption(
            name="Operational Efficiency",
            description="Expected efficiency gains from new processes",
            value=0.1,
            confidence=0.6,
            source="Process Analysis",
            impact="Medium"
        ),
        BusinessAssumption(
            name="Regulatory Impact",
            description="Impact of new regulations on operations",
            value=-0.02,
            confidence=0.5,
            source="Legal Team",
            impact="Low"
        )
    ]
    
    try:
        analyzer = BusinessPlanAnalyzer(assumptions)
        baselines = analyzer.calculate_baselines()
        sensitivity = analyzer.sensitivity_analysis()
        analyzer.visualize_sensitivity()
        report = analyzer.generate_report()
        
        print("\nBaseline Metrics:")
        for k, v in baselines.items():
            print(f"{k.replace('_', ' ').title()}: {v:.2f}")
            
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
```
