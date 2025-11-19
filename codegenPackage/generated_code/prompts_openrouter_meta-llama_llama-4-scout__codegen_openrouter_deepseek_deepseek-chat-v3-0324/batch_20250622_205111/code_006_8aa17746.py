"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Write a function to convert wTAO to rsTAO and vice versa, considering the 1:1 exchange rate and potential slippage in a real-world scenario.
Generated: DETERMINISTIC_8aa17746ad619ac4
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TAOConverter:
    """
    A utility class to convert between wTAO and rsTAO tokens.
    Assumes a 1:1 exchange rate with optional slippage handling.
    """
    
    def __init__(self, slippage: float = 0.0):
        """
        Initialize the converter with optional slippage.
        
        Args:
            slippage: Percentage slippage (0-1) to account for in conversions.
                     Default is 0 (no slippage).
        """
        if slippage < 0 or slippage > 1:
            raise ValueError("Slippage must be between 0 and 1")
        self.slippage = slippage
    
    def wtao_to_rstao(self, amount: float) -> float:
        """
        Convert wTAO to rsTAO considering slippage.
        
        Args:
            amount: Amount of wTAO to convert
            
        Returns:
            Equivalent rsTAO amount after slippage adjustment
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * (1 - self.slippage)
    
    def rstao_to_wtao(self, amount: float) -> float:
        """
        Convert rsTAO to wTAO considering slippage.
        
        Args:
            amount: Amount of rsTAO to convert
            
        Returns:
            Equivalent wTAO amount after slippage adjustment
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * (1 - self.slippage)
    
    def set_slippage(self, slippage: float) -> None:
        """
        Update the slippage percentage.
        
        Args:
            slippage: New slippage percentage (0-1)
            
        Raises:
            ValueError: If slippage is not between 0 and 1
        """
        if slippage < 0 or slippage > 1:
            raise ValueError("Slippage must be between 0 and 1")
        self.slippage = slippage
```
