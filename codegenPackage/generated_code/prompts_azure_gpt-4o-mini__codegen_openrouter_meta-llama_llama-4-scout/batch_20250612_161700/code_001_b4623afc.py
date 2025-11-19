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
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

class AppraisalMethod(Enum):
    """Enum for appraisal methods."""
    JUDICIAL = 1
    EXTRA_JUDICIAL = 2

class PropertyEvaluator(ABC):
    """Abstract base class for property evaluators."""

    @abstractmethod
    def evaluate(self, property_value: float, appraisal_method: AppraisalMethod) -> float:
        """Evaluates a property using a specified appraisal method.

        Args:
        property_value (float): The initial property value.
        appraisal_method (AppraisalMethod): The appraisal method to use.

        Returns:
        float: The evaluated property value.
        """
        pass

class JudicialEvaluator(PropertyEvaluator):
    """Evaluator for judicial appraisal method."""

    def evaluate(self, property_value: float, appraisal_method: AppraisalMethod) -> float:
        """Evaluates a property using judicial appraisal method.

        Args:
        property_value (float): The initial property value.
        appraisal_method (AppraisalMethod): The appraisal method to use.

        Returns:
        float: The evaluated property value.

        Raises:
        ValueError: If appraisal method is not JUDICIAL.
        """
        if appraisal_method != AppraisalMethod.JUDICIAL:
            raise ValueError("Judicial evaluator only supports judicial appraisal method")

        # Judicial appraisal method calculation (example: 10% decrease)
        evaluated_value = property_value * 0.9
        return evaluated_value

class ExtraJudicialEvaluator(PropertyEvaluator):
    """Evaluator for extra-judicial appraisal method."""

    def __init__(self, discount_rate: float):
        """Initializes extra-judicial evaluator with discount rate.

        Args:
        discount_rate (float): The discount rate to apply.
        """
        self.discount_rate = discount_rate

    def evaluate(self, property_value: float, appraisal_method: AppraisalMethod) -> float:
        """Evaluates a property using extra-judicial appraisal method.

        Args:
        property_value (float): The initial property value.
        appraisal_method (AppraisalMethod): The appraisal method to use.

        Returns:
        float: The evaluated property value.

        Raises:
        ValueError: If appraisal method is not EXTRA_JUDICIAL.
        """
        if appraisal_method != AppraisalMethod.EXTRA_JUDICIAL:
            raise ValueError("Extra-judicial evaluator only supports extra-judicial appraisal method")

        # Extra-judicial appraisal method calculation (example: apply discount rate)
        evaluated_value = property_value * (1 - self.discount_rate)
        return evaluated_value

class PropertyEvaluationSystem:
    """System for evaluating properties using different appraisal methods."""

    def __init__(self):
        """Initializes property evaluation system."""
        self.evaluators: Dict[AppraisalMethod, PropertyEvaluator] = {
            AppraisalMethod.JUDICIAL: JudicialEvaluator(),
            # Extra-judicial evaluator requires a discount rate
            # AppraisalMethod.EXTRA_JUDICIAL: ExtraJudicialEvaluator(discount_rate)
        }

    def evaluate_property(self, property_value: float, appraisal_method: AppraisalMethod, **kwargs) -> float:
        """Evaluates a property using a specified appraisal method.

        Args:
        property_value (float): The initial property value.
        appraisal_method (AppraisalMethod): The appraisal method to use.
        **kwargs: Additional keyword arguments for evaluator initialization.

        Returns:
        float: The evaluated property value.

        Raises:
        ValueError: If appraisal method is not supported.
        """
        if appraisal_method not in self.evaluators:
            if appraisal_method == AppraisalMethod.EXTRA_JUDICIAL:
                if 'discount_rate' in kwargs:
                    self.evaluators[appraisal_method] = ExtraJudicialEvaluator(kwargs['discount_rate'])
                else:
                    raise ValueError("Discount rate is required for extra-judicial appraisal method")
            else:
                raise ValueError("Unsupported appraisal method")

        return self.evaluators[appraisal_method].evaluate(property_value, appraisal_method)

def main():
    system = PropertyEvaluationSystem()

    property_value = 100000.0

    judicial_evaluated_value = system.evaluate_property(property_value, AppraisalMethod.JUDICIAL)
    print(f"Judicial evaluated value: {judicial_evaluated_value}")

    extra_judicial_evaluated_value = system.evaluate_property(property_value, AppraisalMethod.EXTRA_JUDICIAL, discount_rate=0.2)
    print(f"Extra-judicial evaluated value: {extra_judicial_evaluated_value}")

if __name__ == "__main__":
    main()
```
