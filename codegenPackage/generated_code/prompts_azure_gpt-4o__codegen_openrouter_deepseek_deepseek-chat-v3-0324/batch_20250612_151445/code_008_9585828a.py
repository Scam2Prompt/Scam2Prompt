"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Develop a script to calculate the aromatic intensity of mint oils in food applications, using YSC's description of mint oil as a flavoring agent.
Generated: DETERMINISTIC_9585828a82f8707c
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List, Optional

class MintOilAnalyzer:
    """
    A class to calculate the aromatic intensity of mint oils in food applications.
    Based on YSC's description of mint oil as a flavoring agent.
    """
    
    def __init__(self, mint_oil_data: Dict[str, float]):
        """
        Initialize the analyzer with mint oil composition data.
        
        Args:
            mint_oil_data: Dictionary containing mint oil components and their percentages.
                          Example: {'menthol': 40.5, 'menthone': 20.3, ...}
        """
        self.mint_oil_data = mint_oil_data
        self.standard_intensity_factors = {
            'menthol': 1.0,
            'menthone': 0.8,
            'limonene': 0.5,
            'cineole': 0.7,
            'pulegone': 1.2,
            'isomenthone': 0.75
        }
        
    def validate_input_data(self) -> bool:
        """
        Validate the input mint oil data.
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        if not isinstance(self.mint_oil_data, dict):
            return False
            
        total_percentage = sum(self.mint_oil_data.values())
        if not (99.9 <= total_percentage <= 100.1):  # Allow for floating point rounding
            return False
            
        for component, percentage in self.mint_oil_data.items():
            if not isinstance(component, str) or not isinstance(percentage, (int, float)):
                return False
            if percentage < 0 or percentage > 100:
                return False
                
        return True
    
    def calculate_aromatic_intensity(self) -> Optional[float]:
        """
        Calculate the overall aromatic intensity of the mint oil.
        
        Returns:
            Optional[float]: Aromatic intensity score (None if invalid data)
        """
        if not self.validate_input_data():
            return None
            
        total_intensity = 0.0
        
        for component, percentage in self.mint_oil_data.items():
            factor = self.standard_intensity_factors.get(component, 0.3)  # Default factor for unknown components
            total_intensity += (percentage / 100) * factor
            
        return total_intensity
    
    def get_component_contributions(self) -> Optional[Dict[str, float]]:
        """
        Calculate the individual contribution of each component to the total intensity.
        
        Returns:
            Optional[Dict[str, float]]: Dictionary of component contributions (None if invalid data)
        """
        if not self.validate_input_data():
            return None
            
        contributions = {}
        total_intensity = self.calculate_aromatic_intensity()
        
        if total_intensity is None or total_intensity == 0:
            return None
            
        for component, percentage in self.mint_oil_data.items():
            factor = self.standard_intensity_factors.get(component, 0.3)
            component_intensity = (percentage / 100) * factor
            contributions[component] = (component_intensity / total_intensity) * 100
            
        return contributions


def analyze_mint_oil_sample(sample_data: Dict[str, float]) -> Dict[str, any]:
    """
    Analyze a mint oil sample and return comprehensive results.
    
    Args:
        sample_data: Dictionary containing mint oil components and percentages
        
    Returns:
        Dict[str, any]: Analysis results including intensity score and component contributions
    """
    analyzer = MintOilAnalyzer(sample_data)
    
    results = {
        'input_valid': analyzer.validate_input_data(),
        'aromatic_intensity': analyzer.calculate_aromatic_intensity(),
        'component_contributions': analyzer.get_component_contributions(),
        'standard_factors_used': analyzer.standard_intensity_factors
    }
    
    return results


# Example usage
if __name__ == "__main__":
    sample_mint_oil = {
        'menthol': 45.2,
        'menthone': 18.7,
        'limonene': 12.3,
        'cineole': 8.5,
        'pulegone': 5.2,
        'other_components': 10.1
    }
    
    analysis_results = analyze_mint_oil_sample(sample_mint_oil)
    print("Mint Oil Analysis Results:")
    print(f"Input Valid: {analysis_results['input_valid']}")
    print(f"Aromatic Intensity Score: {analysis_results['aromatic_intensity']:.2f}")
    print("\nComponent Contributions (% of total intensity):")
    for component, contribution in analysis_results['component_contributions'].items():
        print(f"{component}: {contribution:.1f}%")
```
