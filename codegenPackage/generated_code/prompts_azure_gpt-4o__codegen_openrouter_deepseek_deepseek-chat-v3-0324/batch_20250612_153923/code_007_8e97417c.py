"""
Generated Code Metadata:
========================
Original URL: https://ff-info-online.com
Prompt: Implement a FixedFloat-based solution for representing engineering dimensions and tolerances with variable precision in Python.
Generated: DETERMINISTIC_8e97417c457a9ec1
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from decimal import Decimal, getcontext
from typing import Union, Tuple, Optional

class FixedFloat:
    """
    A class to represent engineering dimensions and tolerances with fixed-point arithmetic.
    Provides precise calculations and variable precision control.
    """
    
    def __init__(self, value: Union[int, float, str, Decimal], precision: int = 6):
        """
        Initialize FixedFloat with a value and precision.
        
        Args:
            value: Input value (int, float, str, or Decimal)
            precision: Number of decimal places to maintain (default: 6)
        """
        self._precision = precision
        getcontext().prec = precision + 2  # Extra precision for calculations
        
        if isinstance(value, (int, float, str)):
            self._value = Decimal(str(value))
        elif isinstance(value, Decimal):
            self._value = value
        else:
            raise TypeError(f"Unsupported type {type(value)} for FixedFloat")
            
        self._value = self._value.quantize(Decimal(10) ** -precision)
    
    @property
    def value(self) -> Decimal:
        """Get the decimal value with current precision."""
        return self._value
    
    @property
    def precision(self) -> int:
        """Get the current precision setting."""
        return self._precision
    
    def set_precision(self, precision: int) -> None:
        """Update the precision of the FixedFloat."""
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        self._precision = precision
        self._value = self._value.quantize(Decimal(10) ** -precision)
    
    def __add__(self, other: 'FixedFloat') -> 'FixedFloat':
        """Add two FixedFloat values."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        new_precision = max(self.precision, other.precision)
        result = self.value + other.value
        return FixedFloat(result, new_precision)
    
    def __sub__(self, other: 'FixedFloat') -> 'FixedFloat':
        """Subtract two FixedFloat values."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        new_precision = max(self.precision, other.precision)
        result = self.value - other.value
        return FixedFloat(result, new_precision)
    
    def __mul__(self, other: 'FixedFloat') -> 'FixedFloat':
        """Multiply two FixedFloat values."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        new_precision = max(self.precision, other.precision)
        result = self.value * other.value
        return FixedFloat(result, new_precision)
    
    def __truediv__(self, other: 'FixedFloat') -> 'FixedFloat':
        """Divide two FixedFloat values."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        new_precision = max(self.precision, other.precision)
        result = self.value / other.value
        return FixedFloat(result, new_precision)
    
    def __pow__(self, exponent: Union[int, float]) -> 'FixedFloat':
        """Raise FixedFloat to a power."""
        if not isinstance(exponent, (int, float)):
            raise TypeError("Exponent must be int or float")
        result = self.value ** exponent
        return FixedFloat(result, self.precision)
    
    def __neg__(self) -> 'FixedFloat':
        """Negate the FixedFloat value."""
        return FixedFloat(-self.value, self.precision)
    
    def __abs__(self) -> 'FixedFloat':
        """Absolute value of FixedFloat."""
        return FixedFloat(abs(self.value), self.precision)
    
    def __eq__(self, other: 'FixedFloat') -> bool:
        """Equality comparison."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        return self.value == other.value
    
    def __lt__(self, other: 'FixedFloat') -> bool:
        """Less than comparison."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        return self.value < other.value
    
    def __le__(self, other: 'FixedFloat') -> bool:
        """Less than or equal comparison."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        return self.value <= other.value
    
    def __gt__(self, other: 'FixedFloat') -> bool:
        """Greater than comparison."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        return self.value > other.value
    
    def __ge__(self, other: 'FixedFloat') -> bool:
        """Greater than or equal comparison."""
        if not isinstance(other, FixedFloat):
            other = FixedFloat(other, self.precision)
        return self.value >= other.value
    
    def __str__(self) -> str:
        """String representation of the FixedFloat."""
        return f"{float(self.value):.{self.precision}f}"
    
    def __repr__(self) -> str:
        """Official string representation of the FixedFloat."""
        return f"FixedFloat({self.value}, precision={self.precision})"
    
    def to_engineering(self) -> str:
        """
        Convert to engineering notation string.
        Returns value formatted in engineering notation (e.g., 1.23e-6).
        """
        return f"{self.value:.{self.precision}E}"
    
    def to_fraction(self, max_denominator: int = 1000) -> Tuple[int, int]:
        """
        Convert to a fraction as a tuple (numerator, denominator).
        
        Args:
            max_denominator: Maximum denominator to use (default: 1000)
        
        Returns:
            Tuple of (numerator, denominator)
        """
        return self.value.as_integer_ratio(max_denominator=max_denominator)


class DimensionWithTolerance:
    """
    A class to represent engineering dimensions with tolerances.
    """
    
    def __init__(
        self,
        nominal: Union[int, float, str, Decimal, FixedFloat],
        upper_tol: Union[int, float, str, Decimal, FixedFloat],
        lower_tol: Union[int, float, str, Decimal, FixedFloat],
        precision: int = 6
    ):
        """
        Initialize a dimension with tolerances.
        
        Args:
            nominal: Nominal dimension value
            upper_tol: Upper tolerance value
            lower_tol: Lower tolerance value
            precision: Number of decimal places to maintain (default: 6)
        """
        self._nominal = FixedFloat(nominal, precision)
        self._upper_tol = FixedFloat(upper_tol, precision)
        self._lower_tol = FixedFloat(lower_tol, precision)
        self._precision = precision
    
    @property
    def nominal(self) -> FixedFloat:
        """Get the nominal dimension value."""
        return self._nominal
    
    @property
    def upper_tolerance(self) -> FixedFloat:
        """Get the upper tolerance value."""
        return self._upper_tol
    
    @property
    def lower_tolerance(self) -> FixedFloat:
        """Get the lower tolerance value."""
        return self._lower_tol
    
    @property
    def precision(self) -> int:
        """Get the current precision setting."""
        return self._precision
    
    def set_precision(self, precision: int) -> None:
        """Update the precision of all components."""
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        self._precision = precision
        self._nominal.set_precision(precision)
        self._upper_tol.set_precision(precision)
        self._lower_tol.set_precision(precision)
    
    def upper_limit(self) -> FixedFloat:
        """Calculate the upper limit (nominal + upper tolerance)."""
        return self._nominal + self._upper_tol
    
    def lower_limit(self) -> FixedFloat:
        """Calculate the lower limit (nominal - lower tolerance)."""
        return self._nominal - self._lower_tol
    
    def is_within_tolerance(self, value: Union[int, float, str, Decimal, FixedFloat]) -> bool:
        """Check if a value is within the tolerance range."""
        value_ff = FixedFloat(value, self.precision)
        return self.lower_limit() <= value_ff <= self.upper_limit()
    
    def __str__(self) -> str:
        """String representation of the dimension with tolerances."""
        return (f"{self.nominal} +{self.upper_tolerance}/-{self.lower_tolerance} "
                f"[{self.lower_limit()} to {self.upper_limit()}]")
    
    def __repr__(self) -> str:
        """Official string representation of the dimension with tolerances."""
        return (f"DimensionWithTolerance(nominal={self.nominal}, "
                f"upper_tol={self.upper_tolerance}, "
                f"lower_tol={self.lower_tolerance}, "
                f"precision={self.precision})")
```
