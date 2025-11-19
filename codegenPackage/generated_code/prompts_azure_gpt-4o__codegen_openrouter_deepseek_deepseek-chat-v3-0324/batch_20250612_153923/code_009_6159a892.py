"""
Generated Code Metadata:
========================
Original URL: https://ff-info-online.com
Prompt: Create a Python library for FixedFloat numbers that includes methods for arithmetic operations, precision adjustment, and efficient storage.
Generated: DETERMINISTIC_6159a89247bfaf7c
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal
from decimal import Decimal, getcontext
from typing import Union, Optional, Tuple

class FixedFloat:
    """
    A class for handling fixed-point decimal numbers with configurable precision.
    Provides arithmetic operations, precision adjustment, and efficient storage.
    """
    
    def __init__(self, value: Union[str, int, float, Decimal], precision: int = 2):
        """
        Initialize a FixedFloat with a value and precision.
        
        Args:
            value: The initial value (can be str, int, float, or Decimal)
            precision: Number of decimal places to maintain (default: 2)
        """
        if not isinstance(precision, int) or precision < 0:
            raise ValueError("Precision must be a non-negative integer")
            
        self._precision = precision
        self._context = getcontext()
        self._context.prec = 28  # Sufficient for most financial calculations
        
        try:
            if isinstance(value, Decimal):
                self._value = value
            else:
                self._value = Decimal(str(value))
        except (decimal.InvalidOperation, ValueError, TypeError) as e:
            raise ValueError(f"Invalid value for FixedFloat: {value}") from e
            
        self._normalize()
    
    def _normalize(self) -> None:
        """Normalize the value to the specified precision."""
        self._value = self._value.quantize(Decimal(f"1.{'0' * self._precision}"))
    
    @property
    def value(self) -> Decimal:
        """Get the normalized decimal value."""
        return self._value
    
    @property
    def precision(self) -> int:
        """Get the current precision setting."""
        return self._precision
    
    @precision.setter
    def precision(self, new_precision: int) -> None:
        """Set a new precision and normalize the value."""
        if not isinstance(new_precision, int) or new_precision < 0:
            raise ValueError("Precision must be a non-negative integer")
        self._precision = new_precision
        self._normalize()
    
    def __repr__(self) -> str:
        return f"FixedFloat('{str(self._value)}', precision={self._precision})"
    
    def __str__(self) -> str:
        return str(self._value)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        return self._value == other_value
    
    def __hash__(self) -> int:
        return hash((self._value, self._precision))
    
    def __add__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> 'FixedFloat':
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        result = self._value + other_value
        return FixedFloat(result, precision=max(self._precision, getattr(other, '_precision', self._precision)))
    
    def __sub__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> 'FixedFloat':
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        result = self._value - other_value
        return FixedFloat(result, precision=max(self._precision, getattr(other, '_precision', self._precision)))
    
    def __mul__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> 'FixedFloat':
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        result = self._value * other_value
        return FixedFloat(result, precision=max(self._precision, getattr(other, '_precision', self._precision)))
    
    def __truediv__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> 'FixedFloat':
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        if other_value == 0:
            raise ZeroDivisionError("Division by zero")
        result = self._value / other_value
        return FixedFloat(result, precision=max(self._precision, getattr(other, '_precision', self._precision)))
    
    def __neg__(self) -> 'FixedFloat':
        return FixedFloat(-self._value, precision=self._precision)
    
    def __pos__(self) -> 'FixedFloat':
        return FixedFloat(+self._value, precision=self._precision)
    
    def __abs__(self) -> 'FixedFloat':
        return FixedFloat(abs(self._value), precision=self._precision)
    
    def __round__(self, n: Optional[int] = None) -> 'FixedFloat':
        if n is None:
            n = self._precision
        return FixedFloat(round(self._value, n), precision=n)
    
    def __lt__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> bool:
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        return self._value < other_value
    
    def __le__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> bool:
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        return self._value <= other_value
    
    def __gt__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> bool:
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        return self._value > other_value
    
    def __ge__(self, other: Union['FixedFloat', Decimal, int, float, str]) -> bool:
        if not isinstance(other, (FixedFloat, Decimal, int, float, str)):
            return NotImplemented
        other_value = other._value if isinstance(other, FixedFloat) else Decimal(str(other))
        return self._value >= other_value
    
    def to_tuple(self) -> Tuple[str, int]:
        """
        Convert the FixedFloat to a tuple of (value_string, precision).
        Useful for serialization.
        """
        return (str(self._value), self._precision)
    
    @classmethod
    def from_tuple(cls, data: Tuple[str, int]) -> 'FixedFloat':
        """
        Create a FixedFloat from a tuple of (value_string, precision).
        Useful for deserialization.
        """
        if not isinstance(data, tuple) or len(data) != 2:
            raise ValueError("Input must be a tuple of (value_string, precision)")
        return cls(data[0], precision=data[1])
    
    def to_bytes(self) -> bytes:
        """
        Convert the FixedFloat to a compact byte representation.
        Format: [precision (1 byte)][value as decimal string (UTF-8)]
        """
        value_str = str(self._value)
        return bytes([self._precision]) + value_str.encode('utf-8')
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'FixedFloat':
        """
        Create a FixedFloat from its byte representation.
        """
        if len(data) < 1:
            raise ValueError("Invalid byte data: too short")
        precision = data[0]
        value_str = data[1:].decode('utf-8')
        return cls(value_str, precision=precision)
```
