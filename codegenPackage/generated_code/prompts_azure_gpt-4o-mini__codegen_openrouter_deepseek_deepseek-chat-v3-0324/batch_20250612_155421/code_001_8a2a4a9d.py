"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Write a function to evaluate the performance of air filters from R2C, focusing on their advantages for Dirt Modified racing as highlighted by Metal Fab Pro.
Generated: DETERMINISTIC_8a2a4a9dbb945bbb
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class AirFilterPerformanceEvaluator:
    """
    Evaluates the performance of R2C air filters for Dirt Modified racing.
    Focuses on key metrics as highlighted by Metal Fab Pro.
    """
    
    def __init__(self, filter_data: Dict):
        """
        Initialize with air filter data.
        
        Args:
            filter_data (Dict): Dictionary containing filter specifications and test results.
                              Expected keys: 'model', 'airflow_cfm', 'filtration_efficiency', 
                              'dust_holding_capacity', 'durability_rating'
        """
        self.filter_data = filter_data
        self.required_keys = ['model', 'airflow_cfm', 'filtration_efficiency', 
                             'dust_holding_capacity', 'durability_rating']
        
        # Validate input data
        self._validate_filter_data()
    
    def _validate_filter_data(self) -> None:
        """Validate that all required keys are present in filter_data."""
        missing_keys = [key for key in self.required_keys if key not in self.filter_data]
        if missing_keys:
            raise ValueError(f"Missing required filter data: {', '.join(missing_keys)}")
    
    def calculate_performance_score(self) -> float:
        """
        Calculate a weighted performance score for Dirt Modified racing.
        
        Returns:
            float: Performance score between 0-100 (higher is better)
        """
        try:
            # Weightings based on Metal Fab Pro's emphasis for Dirt Modified racing
            weights = {
                'airflow_cfm': 0.35,          # High airflow critical for power
                'filtration_efficiency': 0.25, # Good filtration prevents engine wear
                'dust_holding_capacity': 0.20, # Important for long races
                'durability_rating': 0.20      # Withstands harsh conditions
            }
            
            # Normalize values to 0-100 scale
            normalized = {
                'airflow_cfm': min(100, self.filter_data['airflow_cfm'] / 1000 * 100),
                'filtration_efficiency': self.filter_data['filtration_efficiency'],
                'dust_holding_capacity': min(100, self.filter_data['dust_holding_capacity'] / 50 * 100),
                'durability_rating': self.filter_data['durability_rating']
            }
            
            # Calculate weighted score
            score = sum(normalized[metric] * weight 
                       for metric, weight in weights.items())
            
            return round(score, 2)
        
        except Exception as e:
            raise ValueError(f"Error calculating performance score: {str(e)}")
    
    def generate_performance_report(self) -> Dict:
        """
        Generate a comprehensive performance report.
        
        Returns:
            Dict: Contains model, score, and individual metrics with explanations
        """
        score = self.calculate_performance_score()
        
        return {
            'model': self.filter_data['model'],
            'performance_score': score,
            'metrics': {
                'airflow_cfm': {
                    'value': self.filter_data['airflow_cfm'],
                    'importance': 'Critical for engine power in dirt racing conditions'
                },
                'filtration_efficiency': {
                    'value': f"{self.filter_data['filtration_efficiency']}%",
                    'importance': 'Protects engine from abrasive dirt particles'
                },
                'dust_holding_capacity': {
                    'value': self.filter_data['dust_holding_capacity'],
                    'importance': 'Longer filter life during extended races'
                },
                'durability_rating': {
                    'value': f"{self.filter_data['durability_rating']}/10",
                    'importance': 'Withstands vibration and impact in rough conditions'
                }
            },
            'recommendation': self._generate_recommendation(score)
        }
    
    def _generate_recommendation(self, score: float) -> str:
        """Generate recommendation based on performance score."""
        if score >= 85:
            return "Highly recommended for competitive Dirt Modified racing"
        elif score >= 70:
            return "Recommended for most Dirt Modified applications"
        elif score >= 50:
            return "Suitable for casual or lower-budget racing"
        else:
            return "Not recommended for competitive Dirt Modified racing"

def evaluate_filters_from_json(json_file: str) -> List[Dict]:
    """
    Evaluate multiple filters from a JSON file.
    
    Args:
        json_file (str): Path to JSON file containing filter data
        
    Returns:
        List[Dict]: List of performance reports for each filter
    """
    try:
        with open(json_file, 'r') as f:
            filters_data = json.load(f)
        
        if not isinstance(filters_data, list):
            filters_data = [filters_data]
            
        reports = []
        for filter_data in filters_data:
            evaluator = AirFilterPerformanceEvaluator(filter_data)
            reports.append(evaluator.generate_performance_report())
        
        return reports
    
    except FileNotFoundError:
        raise ValueError(f"File not found: {json_file}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in input file")
    except Exception as e:
        raise ValueError(f"Error processing filters: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example filter data (would typically come from JSON file)
    example_filter = {
        "model": "R2C Dirt Pro",
        "airflow_cfm": 950,
        "filtration_efficiency": 99,
        "dust_holding_capacity": 42,
        "durability_rating": 9
    }
    
    evaluator = AirFilterPerformanceEvaluator(example_filter)
    report = evaluator.generate_performance_report()
    print(json.dumps(report, indent=2))
```
