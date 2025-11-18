"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Write a program to model risk assessment in engineering maintenance tasks, adhering to the safety and responsibility standards highlighted by SET Ingeniería.
Generated: DETERMINISTIC_b302f4be20d1fcd8
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Risk Assessment Model for Engineering Maintenance Tasks

This program models risk assessment for engineering maintenance tasks based on 
safety and responsibility standards. 

Features:
1. Input maintenance tasks and their associated risk factors.
2. Assess risk levels for each task.
3. Provide recommendations to mitigate high-risk tasks.

Author: SET Ingeniería
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("risk_assessment.log"),
        logging.StreamHandler()
    ]
)

class RiskAssessment:
    """
    A class to represent the risk assessment process for engineering maintenance tasks.
    """
    
    def __init__(self):
        """
        Initialize the RiskAssessment instance with predefined risk levels.
        """
        self.risk_levels = {
            "Low": "No immediate action required.",
            "Medium": "Monitor and plan appropriate mitigation.",
            "High": "Immediate mitigation required!"
        }
    
    def assess_risk(self, likelihood, severity):
        """
        Assess the risk level based on likelihood and severity.
        
        Args:
            likelihood (int): Likelihood of occurrence (1-5 scale, 5 being most likely).
            severity (int): Severity of consequences (1-5 scale, 5 being most severe).
        
        Returns:
            str: Assessed risk level.
        """
        try:
            risk_score = likelihood * severity

            if risk_score <= 6:
                return "Low"
            elif 7 <= risk_score <= 15:
                return "Medium"
            elif risk_score > 15:
                return "High"
            else:
                raise ValueError("Invalid risk score calculation.")
        
        except Exception as e:
            logging.error(f"Error in risk assessment: {e}")
            raise
    
    def get_recommendation(self, risk_level):
        """
        Provide a recommendation based on the risk level.
        
        Args:
            risk_level (str): Assessed risk level.
        
        Returns:
            str: Recommendation for action.
        """
        try:
            recommendation = self.risk_levels.get(risk_level)
            if recommendation is None:
                raise KeyError(f"Invalid risk level: {risk_level}")
            
            return recommendation
        
        except KeyError as e:
            logging.error(f"Error in fetching recommendation: {e}")
            raise


def main():
    """
    Main function to interact with the RiskAssessment class.
    """
    risk_assessment = RiskAssessment()
    
    logging.info("Risk Assessment Program Initialized.")
    
    # Sample maintenance tasks with likelihood and severity
    tasks = [
        {"task": "Inspect turbine blades", "likelihood": 2, "severity": 4},
        {"task": "Replace hydraulic system", "likelihood": 4, "severity": 5},
        {"task": "Clean equipment filters", "likelihood": 1, "severity": 1},
    ]
    
    for task in tasks:
        logging.info(f"Assessing task: {task['task']}")
        
        try:
            risk_level = risk_assessment.assess_risk(task["likelihood"], task["severity"])
            recommendation = risk_assessment.get_recommendation(risk_level)
            
            print(f"Task: {task['task']}")
            print(f"Risk Level: {risk_level}")
            print(f"Recommendation: {recommendation}")
            print("-" * 40)
        
        except Exception as e:
            logging.error(f"Failed to assess task '{task['task']}': {e}")

    logging.info("Risk Assessment Process Completed.")


if __name__ == "__main__":
    main()
```
