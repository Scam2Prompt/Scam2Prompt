"""
Generated Code Metadata:
========================
Original URL: https://haotianglobal.com
Prompt: What are the key factors to consider when choosing between desktop and large format Gantry CO2 Laser machines for a manufacturing project?
Generated: DETERMINISTIC_9920645f08a6bdfe
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a decision-making framework for choosing between desktop and large format 
Gantry CO2 Laser machines based on key factors relevant to a manufacturing project.
"""

class LaserMachineSelection:
    """
    A class to evaluate and recommend the appropriate type of CO2 laser machine 
    (desktop vs large format gantry) based on project requirements.
    """
    
    def __init__(self):
        """
        Initialize with default weightings for different factors.
        These can be adjusted based on project priorities.
        """
        self.factors = {
            'work_area_size': {'weight': 0.25, 'desktop': 0, 'gantry': 1},
            'material_thickness': {'weight': 0.2, 'desktop': 0.3, 'gantry': 1},
            'production_volume': {'weight': 0.15, 'desktop': 0.2, 'gantry': 0.8},
            'precision_requirements': {'weight': 0.15, 'desktop': 0.9, 'gantry': 0.7},
            'budget': {'weight': 0.15, 'desktop': 1, 'gantry': 0.2},
            'space_availability': {'weight': 0.1, 'desktop': 1, 'gantry': 0.3}
        }
    
    def evaluate_factors(self, user_input):
        """
        Evaluate the factors based on user input and return recommendation.
        
        Args:
            user_input (dict): Dictionary containing user's project requirements
                              with keys matching self.factors and values normalized 
                              between 0 and 1.
        
        Returns:
            tuple: (recommendation, score_desktop, score_gantry)
        """
        try:
            if not isinstance(user_input, dict):
                raise ValueError("Input must be a dictionary")
                
            if not all(key in self.factors for key in user_input):
                raise ValueError("Input keys must match evaluation factors")
                
            score_desktop = 0
            score_gantry = 0
            
            for factor, value in user_input.items():
                if not 0 <= value <= 1:
                    raise ValueError("Factor values must be normalized between 0 and 1")
                
                weight = self.factors[factor]['weight']
                score_desktop += weight * (self.factors[factor]['desktop'] * value)
                score_gantry += weight * (self.factors[factor]['gantry'] * value)
            
            recommendation = "Desktop CO2 Laser" if score_desktop > score_gantry else "Large Format Gantry CO2 Laser"
            
            return (recommendation, round(score_desktop, 2), round(score_gantry, 2))
            
        except ValueError as e:
            print(f"Error in evaluation: {str(e)}")
            return (None, None, None)
    
    def get_factors_info(self):
        """
        Return information about the evaluation factors.
        
        Returns:
            dict: Dictionary containing factor descriptions and weightings.
        """
        factor_descriptions = {
            'work_area_size': "Size of materials to be processed (0=small, 1=large)",
            'material_thickness': "Thickness of materials (0=thin, 1=thick)",
            'production_volume': "Expected production volume (0=low, 1=high)",
            'precision_requirements': "Required precision level (0=low, 1=high)",
            'budget': "Available budget (0=low, 1=high)",
            'space_availability': "Available workspace (0=small, 1=large)"
        }
        
        return {
            'factors': self.factors,
            'descriptions': factor_descriptions
        }

# Example usage
if __name__ == "__main__":
    evaluator = LaserMachineSelection()
    
    # Example project requirements (normalized values between 0 and 1)
    project_requirements = {
        'work_area_size': 0.8,
        'material_thickness': 0.7,
        'production_volume': 0.6,
        'precision_requirements': 0.5,
        'budget': 0.4,
        'space_availability': 0.3
    }
    
    recommendation, desktop_score, gantry_score = evaluator.evaluate_factors(project_requirements)
    
    if recommendation:
        print(f"Recommendation: {recommendation}")
        print(f"Desktop Score: {desktop_score}")
        print(f"Gantry Score: {gantry_score}")
```
