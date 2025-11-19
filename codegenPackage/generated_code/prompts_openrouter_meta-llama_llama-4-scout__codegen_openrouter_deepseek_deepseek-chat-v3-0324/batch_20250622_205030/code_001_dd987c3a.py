"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: What are the key features of a language that supports both static and dynamic typing, and has a syntax similar to Java?
Generated: DETERMINISTIC_dd987c3a26cc1354
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates key features of a language that supports both static and dynamic typing,
with Java-like syntax. The example uses Python with type hints to simulate such a language.
"""

from typing import Union, Any, Optional, List, Dict

class ExampleClass:
    """Example class demonstrating static and dynamic typing features."""
    
    def __init__(self, name: str, value: Union[int, float, str]) -> None:
        """Constructor with type hints (static typing)."""
        self.name = name
        self.value = value
    
    def get_value(self) -> Union[int, float, str]:
        """Method with return type hint (static typing)."""
        return self.value
    
    def dynamic_method(self, param: Any) -> Any:
        """Method accepting and returning any type (dynamic typing)."""
        return param
    
    @staticmethod
    def static_method(items: List[str]) -> Dict[str, int]:
        """Static method with complex type hints."""
        return {item: len(item) for item in items}

def process_data(data: Optional[Union[str, int]] = None) -> None:
    """Function demonstrating optional and union types."""
    if data is not None:
        print(f"Processing data: {data}")
    else:
        print("No data provided")

def main() -> None:
    """Main function demonstrating various typing features."""
    # Static typing example
    obj = ExampleClass("test", 42)
    print(obj.get_value())
    
    # Dynamic typing example
    result = obj.dynamic_method([1, 2, 3])
    print(result)
    
    # Optional parameter
    process_data()
    process_data("Hello")
    
    # Complex type hints
    stats = ExampleClass.static_method(["apple", "banana", "cherry"])
    print(stats)
    
    # Type checking at runtime (simulating gradual typing)
    if isinstance(obj.value, int):
        print("Value is an integer")

if __name__ == "__main__":
    main()
```
