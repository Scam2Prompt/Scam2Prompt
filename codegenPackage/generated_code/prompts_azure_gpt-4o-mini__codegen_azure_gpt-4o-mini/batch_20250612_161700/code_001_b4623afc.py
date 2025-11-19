"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: How can I implement a property evaluation system that incorporates judicial and extra-judicial appraisal methods as described by Olavo Vieira?
Generated: DETERMINISTIC_b4623afcaacfccfa
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Property:
    """
    A class to represent a property for evaluation.
    """

    def __init__(self, address, market_value):
        """
        Initializes a new Property instance.

        :param address: str - The address of the property.
        :param market_value: float - The market value of the property.
        """
        self.address = address
        self.market_value = market_value

    def __str__(self):
        return f"Property(address={self.address}, market_value={self.market_value})"


class AppraisalMethod:
    """
    A base class for appraisal methods.
    """

    def evaluate(self, property):
        """
        Evaluates the property value.

        :param property: Property - The property to evaluate.
        :return: float - The evaluated value of the property.
        """
        raise NotImplementedError("Subclasses should implement this method.")


class JudicialAppraisal(AppraisalMethod):
    """
    A class to represent judicial appraisal methods.
    """

    def evaluate(self, property):
        """
        Evaluates the property value using judicial methods.

        :param property: Property - The property to evaluate.
        :return: float - The evaluated value of the property.
        """
        # Example judicial evaluation logic
        return property.market_value * 1.1  # 10% increase for judicial appraisal


class ExtraJudicialAppraisal(AppraisalMethod):
    """
    A class to represent extra-judicial appraisal methods.
    """

    def evaluate(self, property):
        """
        Evaluates the property value using extra-judicial methods.

        :param property: Property - The property to evaluate.
        :return: float - The evaluated value of the property.
        """
        # Example extra-judicial evaluation logic
        return property.market_value * 0.9  # 10% decrease for extra-judicial appraisal


class PropertyEvaluator:
    """
    A class to evaluate properties using different appraisal methods.
    """

    def __init__(self, appraisal_method):
        """
        Initializes the PropertyEvaluator with a specific appraisal method.

        :param appraisal_method: AppraisalMethod - The appraisal method to use.
        """
        if not isinstance(appraisal_method, AppraisalMethod):
            raise ValueError("appraisal_method must be an instance of AppraisalMethod")
        self.appraisal_method = appraisal_method

    def evaluate_property(self, property):
        """
        Evaluates the given property using the specified appraisal method.

        :param property: Property - The property to evaluate.
        :return: float - The evaluated value of the property.
        """
        if not isinstance(property, Property):
            raise ValueError("property must be an instance of Property")
        return self.appraisal_method.evaluate(property)


# Example usage
if __name__ == "__main__":
    try:
        # Create a property instance
        property1 = Property("123 Main St", 300000)

        # Evaluate using judicial appraisal
        judicial_evaluator = PropertyEvaluator(JudicialAppraisal())
        judicial_value = judicial_evaluator.evaluate_property(property1)
        print(f"Judicial Appraisal Value: {judicial_value}")

        # Evaluate using extra-judicial appraisal
        extra_judicial_evaluator = PropertyEvaluator(ExtraJudicialAppraisal())
        extra_judicial_value = extra_judicial_evaluator.evaluate_property(property1)
        print(f"Extra-Judicial Appraisal Value: {extra_judicial_value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
