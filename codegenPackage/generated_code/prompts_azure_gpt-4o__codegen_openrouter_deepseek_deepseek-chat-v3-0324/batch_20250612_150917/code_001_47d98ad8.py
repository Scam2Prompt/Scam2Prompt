"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Generate a script to calculate the chemical composition of cobalt-based superalloys, such as ALLOY N 155, using laboratory analysis data and match it with JIS standards.
Generated: DETERMINISTIC_47d98ad881c18c06
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple

class CobaltSuperalloyAnalyzer:
    """
    Analyzes the chemical composition of cobalt-based superalloys and matches with JIS standards.
    """
    
    # JIS G 4311 standard composition ranges for cobalt-based superalloys (example values)
    JIS_STANDARDS = {
        "ALLOY_N_155": {
            "C": (0.05, 0.15),
            "Cr": (19.0, 21.0),
            "Ni": (19.0, 21.0),
            "Co": (19.0, 21.0),
            "Mo": (2.5, 3.5),
            "W": (1.0, 2.0),
            "Nb": (0.7, 1.3),
            "Fe": ("Balance", None),
            "Si": (0.0, 1.0),
            "Mn": (0.0, 2.0),
            "P": (0.0, 0.04),
            "S": (0.0, 0.03),
        }
    }
    
    def __init__(self, alloy_type: str = "ALLOY_N_155"):
        """
        Initialize the analyzer with the alloy type.
        
        Args:
            alloy_type: The type of cobalt-based superalloy to analyze.
        """
        self.alloy_type = alloy_type.upper()
        if self.alloy_type not in self.JIS_STANDARDS:
            raise ValueError(f"Unsupported alloy type: {alloy_type}")
    
    def validate_composition(self, lab_data: Dict[str, float]) -> Tuple[bool, Dict[str, str]]:
        """
        Validate lab analysis data against JIS standards.
        
        Args:
            lab_data: Dictionary of element percentages from lab analysis.
            
        Returns:
            Tuple of (is_valid, validation_report) where:
            - is_valid: Boolean indicating if all elements are within spec
            - validation_report: Dictionary with element validation results
        """
        validation_report = {}
        is_valid = True
        standard = self.JIS_STANDARDS[self.alloy_type]
        
        for element, value in lab_data.items():
            if element not in standard:
                validation_report[element] = "Not in specification"
                is_valid = False
                continue
                
            min_val, max_val = standard[element]
            
            if min_val == "Balance":
                continue  # Skip balance elements
                
            if max_val is None:
                if value < min_val:
                    validation_report[element] = f"Below minimum ({min_val})"
                    is_valid = False
            else:
                if not (min_val <= value <= max_val):
                    validation_report[element] = f"Out of range ({min_val}-{max_val})"
                    is_valid = False
                else:
                    validation_report[element] = "Within specification"
        
        return is_valid, validation_report
    
    def calculate_balance(self, lab_data: Dict[str, float]) -> float:
        """
        Calculate the balance (typically Fe) percentage.
        
        Args:
            lab_data: Dictionary of element percentages from lab analysis.
            
        Returns:
            The calculated balance percentage.
        """
        total = sum(v for k, v in lab_data.items() 
                   if k not in self.JIS_STANDARDS[self.alloy_type] or 
                   self.JIS_STANDARDS[self.alloy_type][k][0] != "Balance")
        return 100.0 - total
    
    def analyze(self, lab_data: Dict[str, float]) -> Dict:
        """
        Complete analysis of the alloy composition.
        
        Args:
            lab_data: Dictionary of element percentages from lab analysis.
            
        Returns:
            Dictionary containing:
            - is_valid: Whether composition meets standards
            - validation_report: Detailed validation results
            - balance: Calculated balance percentage
            - composition: Full composition with balance
        """
        # Calculate balance first
        balance = self.calculate_balance(lab_data)
        full_composition = lab_data.copy()
        
        # Find the balance element
        for element, (min_val, _) in self.JIS_STANDARDS[self.alloy_type].items():
            if min_val == "Balance":
                full_composition[element] = balance
                break
        
        # Validate the full composition
        is_valid, validation_report = self.validate_composition(full_composition)
        
        return {
            "is_valid": is_valid,
            "validation_report": validation_report,
            "balance": balance,
            "composition": full_composition
        }

def main():
    # Example usage
    analyzer = CobaltSuperalloyAnalyzer("ALLOY_N_155")
    
    # Example lab data (partial composition)
    lab_data = {
        "C": 0.12,
        "Cr": 20.1,
        "Ni": 19.8,
        "Co": 20.2,
        "Mo": 3.0,
        "W": 1.5,
        "Nb": 1.0,
        "Si": 0.5,
        "Mn": 1.2,
        "P": 0.02,
        "S": 0.01
    }
    
    # Perform analysis
    results = analyzer.analyze(lab_data)
    
    # Print results
    print("Analysis Results:")
    print(f"Alloy Type: {analyzer.alloy_type}")
    print(f"Overall Valid: {'Yes' if results['is_valid'] else 'No'}")
    print("\nComposition:")
    for element, value in results['composition'].items():
        print(f"{element}: {value:.2f}% - {results['validation_report'].get(element, 'N/A')}")
    
    print(f"\nBalance (Fe): {results['balance']:.2f}%")

if __name__ == "__main__":
    main()
```
