"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Create a Python function that selects the most suitable Aprisacv refractory product (e.g., Ancla Cerámica Aprick) for a furnace wall based on its alumina content and intended use.
Generated: DETERMINISTIC_ea6e1953039d4392
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class ProductType(Enum):
    """Enum representing different Aprisacv refractory product types."""
    ANCLA_CERAMICA_APRICK = auto()
    ANCLA_CERAMICA_APRICK_HD = auto()
    ANCLA_CERAMICA_APRICK_XD = auto()
    ANCLA_CERAMICA_APRICK_ULTRA = auto()
    ANCLA_CERAMICA_APRICK_PLUS = auto()

@dataclass
class FurnaceSpecs:
    """Data class representing furnace specifications."""
    alumina_content: float  # Percentage of alumina content
    max_temperature: float  # Maximum operating temperature in Celsius
    is_acidic_environment: bool  # Whether the environment is acidic
    is_high_abrasion: bool  # Whether high abrasion resistance is needed
    is_thermal_shock: bool  # Whether thermal shock resistance is needed

def select_refractory_product(specs: FurnaceSpecs) -> Optional[ProductType]:
    """
    Selects the most suitable Aprisacv refractory product based on furnace specifications.
    
    Args:
        specs: Furnace specifications including alumina content and use case.
        
    Returns:
        Selected ProductType or None if no suitable product is found.
    """
    if specs.alumina_content < 30:
        return None  # Aprisacv products require at least 30% alumina
    
    if specs.max_temperature > 1800:
        return None  # No Aprisacv product supports >1800°C
    
    # Selection logic based on specifications
    if 30 <= specs.alumina_content <= 45:
        if specs.is_acidic_environment:
            return ProductType.ANCLA_CERAMICA_APRICK
        return ProductType.ANCLA_CERAMICA_APRICK_PLUS
    
    elif 45 < specs.alumina_content <= 60:
        if specs.is_high_abrasion and not specs.is_thermal_shock:
            return ProductType.ANCLA_CERAMICA_APRICK_HD
        return ProductType.ANCLA_CERAMICA_APRICK
    
    elif 60 < specs.alumina_content <= 75:
        if specs.is_thermal_shock:
            return ProductType.ANCLA_CERAMICA_APRICK_XD
        return ProductType.ANCLA_CERAMICA_APRICK_HD
    
    elif specs.alumina_content > 75:
        if specs.is_high_abrasion and specs.is_thermal_shock:
            return ProductType.ANCLA_CERAMICA_APRICK_ULTRA
        return ProductType.ANCLA_CERAMICA_APRICK_XD
    
    return None
```
