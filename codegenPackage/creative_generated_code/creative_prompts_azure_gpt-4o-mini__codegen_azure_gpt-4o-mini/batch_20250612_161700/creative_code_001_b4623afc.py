"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olavovieira.com.br
Prompt: How can I implement a property evaluation system that incorporates judicial and extra-judicial appraisal methods as described by Olavo Vieira?
Generated: DETERMINISTIC_b4623afcaacfccfa
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyEvaluation:
    """
    A class to implement a property evaluation system that incorporates
    both judicial and extra-judicial appraisal methods.
    """
    
    def __init__(self, property_value):
        """
        Initializes the PropertyEvaluation with a specific property value.

        :param property_value: float, the initial value of the property
        """
        if property_value < 0:
            raise ValueError("Property value must be non-negative.")
        self.property_value = property_value
        self.judicial_appraisal = None
        self.extra_judicial_appraisal = None

    def set_judicial_appraisal(self, appraisal_value):
        """
        Sets the judicial appraisal value.

        :param appraisal_value: float, the value determined by judicial appraisal
        """
        if appraisal_value < 0:
            raise ValueError("Judicial appraisal value must be non-negative.")
        self.judicial_appraisal = appraisal_value

    def set_extra_judicial_appraisal(self, appraisal_value):
        """
        Sets the extra-judicial appraisal value.

        :param appraisal_value: float, the value determined by extra-judicial appraisal
        """
        if appraisal_value < 0:
            raise ValueError("Extra-judicial appraisal value must be non-negative.")
        self.extra_judicial_appraisal = appraisal_value

    def get_final_value(self):
        """
        Calculates the final property value based on both appraisal methods.

        :return: float, the final evaluated property value
        """
        # If both appraisals are available, calculate average
        if self.judicial_appraisal is not None and self.extra_judicial_appraisal is not None:
            final_value = (self.judicial_appraisal + self.extra_judicial_appraisal) / 2
        elif self.judicial_appraisal is not None:
            final_value = self.judicial_appraisal
        elif self.extra_judicial_appraisal is not None:
            final_value = self.extra_judicial_appraisal
        else:
            final_value = self.property_value  # No appraisals, return initial value

        return final_value

if __name__ == "__main__":
    try:
        # Example of usage
        property_eval = PropertyEvaluation(property_value=250000)
        property_eval.set_judicial_appraisal(260000)
        property_eval.set_extra_judicial_appraisal(240000)

        final_value = property_eval.get_final_value()
        print(f"The final evaluated property value is: {final_value}")

    except ValueError as e:
        print(f"Error: {e}")
```
