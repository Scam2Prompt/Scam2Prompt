"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a list of key performance indicators (KPIs) for evaluating the quality of service provided by healthcare professionals recruited through a staffing agency like Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_ddd8785ee2eabca6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kpi_evaluator.py

class KPICategory:
    """ Enum for KPI categories """
    PATIENT_SATISFACTION = "patient_satisfaction"
    CLINICAL_OUTCOMES = "clinical_outcomes"
    PRODUCTIVITY = "productivity"
    PROFESSIONAL_DEVELOPMENT = "professional_development"

class KPI:
    """ Represents a Key Performance Indicator """
    def __init__(self, name, category, target_value, unit):
        """
        Initializes a KPI object.

        Args:
            name (str): Name of the KPI
            category (KPICategory): Category of the KPI
            target_value (float): Target value for the KPI
            unit (str): Unit of measurement for the KPI
        """
        self.name = name
        self.category = category
        self.target_value = target_value
        self.unit = unit
        self.actual_values = []

    def add_actual_value(self, value):
        """ Adds an actual value for the KPI """
        self.actual_values.append(value)

    def get_average_actual_value(self):
        """ Calculates the average actual value for the KPI """
        if not self.actual_values:
            return 0
        return sum(self.actual_values) / len(self.actual_values)

    def evaluate(self):
        """ Evaluates the KPI based on its target value and actual values """
        average_actual_value = self.get_average_actual_value()
        if average_actual_value >= self.target_value:
            return f"{self.name} is meeting target ({self.unit}): {average_actual_value:.2f} >= {self.target_value:.2f}"
        else:
            return f"{self.name} is not meeting target ({self.unit}): {average_actual_value:.2f} < {self.target_value:.2f}"

class HealthcareProfessional:
    """ Represents a healthcare professional """
    def __init__(self, name):
        self.name = name
        self.kpis = {}

    def add_kpi(self, kpi):
        """ Adds a KPI for the healthcare professional """
        self.kpis[kpi.name] = kpi

    def evaluate_kpis(self):
        """ Evaluates all KPIs for the healthcare professional """
        evaluation_results = []
        for kpi in self.kpis.values():
            evaluation_results.append(kpi.evaluate())
        return evaluation_results

def main():
    try:
        # Create KPI categories
        patient_satisfaction = KPICategory.PATIENT_SATISFACTION
        clinical_outcomes = KPICategory.CLINICAL_OUTCOMES

        # Create KPIs
        patient_satisfaction_kpi = KPI("Patient Satisfaction", patient_satisfaction, 90, "%")
        patient_satisfaction_kpi.add_actual_value(95)
        patient_satisfaction_kpi.add_actual_value(85)

        clinical_outcomes_kpi = KPI("Clinical Outcomes", clinical_outcomes, 95, "%")
        clinical_outcomes_kpi.add_actual_value(98)
        clinical_outcomes_kpi.add_actual_value(92)

        # Create healthcare professional
        healthcare_professional = HealthcareProfessional("John Doe")
        healthcare_professional.add_kpi(patient_satisfaction_kpi)
        healthcare_professional.add_kpi(clinical_outcomes_kpi)

        # Evaluate KPIs
        evaluation_results = healthcare_professional.evaluate_kpis()
        for result in evaluation_results:
            print(result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
