"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System.

This module provides a function to calculate the effectiveness based on performance metrics.
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OccupationalHealthAndSafetyManagementSystem:
    """
    Evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System.
    """

    def __init__(self, injury_rate, illness_rate, lost_time_injury_rate, 
                 hazard_identification_rate, risk_assessment_rate, 
                 employee_training_rate, compliance_rate):
        """
        Initializes the OccupationalHealthAndSafetyManagementSystem.

        Args:
            injury_rate (float): The rate of work-related injuries per 100 full-time equivalent employees.
            illness_rate (float): The rate of work-related illnesses per 100 full-time equivalent employees.
            lost_time_injury_rate (float): The rate of lost-time injuries per 100 full-time equivalent employees.
            hazard_identification_rate (float): The rate of identified hazards per 100 full-time equivalent employees.
            risk_assessment_rate (float): The rate of conducted risk assessments per 100 full-time equivalent employees.
            employee_training_rate (float): The rate of trained employees per 100 full-time equivalent employees.
            compliance_rate (float): The rate of compliance with regulatory requirements.

        Raises:
            ValueError: If any of the input rates are not between 0 and 100.
        """
        if not all(0 <= rate <= 100 for rate in [injury_rate, illness_rate, lost_time_injury_rate, 
                                                 hazard_identification_rate, risk_assessment_rate, 
                                                 employee_training_rate, compliance_rate]):
            raise ValueError("All input rates must be between 0 and 100")

        self.injury_rate = injury_rate
        self.illness_rate = illness_rate
        self.lost_time_injury_rate = lost_time_injury_rate
        self.hazard_identification_rate = hazard_identification_rate
        self.risk_assessment_rate = risk_assessment_rate
        self.employee_training_rate = employee_training_rate
        self.compliance_rate = compliance_rate

    def evaluate_effectiveness(self):
        """
        Evaluates the effectiveness of the Occupational Health and Safety Management System.

        Returns:
            dict: A dictionary containing the effectiveness score and recommendations.
        """
        # Calculate the effectiveness score based on performance metrics
        effectiveness_score = (self.injury_rate * 0.2 + 
                               self.illness_rate * 0.15 + 
                               self.lost_time_injury_rate * 0.2 + 
                               self.hazard_identification_rate * 0.1 + 
                               self.risk_assessment_rate * 0.1 + 
                               self.employee_training_rate * 0.15 + 
                               self.compliance_rate * 0.1)

        # Determine the effectiveness level based on the score
        if effectiveness_score >= 80:
            effectiveness_level = "Excellent"
        elif effectiveness_score >= 60:
            effectiveness_level = "Good"
        elif effectiveness_score >= 40:
            effectiveness_level = "Fair"
        else:
            effectiveness_level = "Poor"

        # Generate recommendations based on the performance metrics
        recommendations = []
        if self.injury_rate > 5:
            recommendations.append("Implement additional safety training programs")
        if self.hazard_identification_rate < 80:
            recommendations.append("Increase the frequency of hazard identifications")
        if self.compliance_rate < 90:
            recommendations.append("Enhance compliance monitoring and reporting")

        return {
            "effectiveness_score": effectiveness_score,
            "effectiveness_level": effectiveness_level,
            "recommendations": recommendations
        }


def main():
    try:
        # Example usage
        ohsms = OccupationalHealthAndSafetyManagementSystem(
            injury_rate=3.5,
            illness_rate=2.1,
            lost_time_injury_rate=1.8,
            hazard_identification_rate=85,
            risk_assessment_rate=90,
            employee_training_rate=95,
            compliance_rate=92
        )

        evaluation_result = ohsms.evaluate_effectiveness()
        logging.info("Effectiveness Score: {:.2f}".format(evaluation_result["effectiveness_score"]))
        logging.info("Effectiveness Level: {}".format(evaluation_result["effectiveness_level"]))
        logging.info("Recommendations:")
        for recommendation in evaluation_result["recommendations"]:
            logging.info("- {}".format(recommendation))

    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))


if __name__ == "__main__":
    main()
```
