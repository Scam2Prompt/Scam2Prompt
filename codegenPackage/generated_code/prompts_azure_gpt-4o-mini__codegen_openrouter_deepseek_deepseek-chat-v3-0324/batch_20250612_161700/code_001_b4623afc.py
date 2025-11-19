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
"""
Property Evaluation System incorporating judicial and extra-judicial appraisal methods.

This system is inspired by the methodologies described by Olavo Vieira for property valuation.
It includes both judicial (court-ordered) and extra-judicial (private) appraisal methods.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict
import datetime
import math
import statistics
from enum import Enum, auto


class AppraisalType(Enum):
    """Enumeration of appraisal types."""
    JUDICIAL = auto()
    EXTRA_JUDICIAL = auto()


class PropertyType(Enum):
    """Enumeration of property types."""
    RESIDENTIAL = auto()
    COMMERCIAL = auto()
    INDUSTRIAL = auto()
    RURAL = auto()
    LAND = auto()


@dataclass
class Property:
    """Data class representing a property."""
    id: str
    address: str
    area: float  # in square meters
    property_type: PropertyType
    registration_number: str
    construction_year: int
    market_value: Optional[float] = None


class AppraisalMethod(ABC):
    """Abstract base class for appraisal methods."""
    
    @abstractmethod
    def calculate_value(self, property: Property) -> float:
        """Calculate the property value using the specific method."""
        pass


class ComparativeMarketAnalysis(AppraisalMethod):
    """
    Extra-judicial method that compares the property with similar recently sold properties.
    """
    
    def __init__(self, comparable_properties: List[Property]):
        self.comparable_properties = comparable_properties
    
    def calculate_value(self, property: Property) -> float:
        """Calculate value based on comparable properties."""
        if not self.comparable_properties:
            raise ValueError("No comparable properties provided")
        
        # Filter comparable properties by type and similar characteristics
        similar_properties = [
            p for p in self.comparable_properties
            if p.property_type == property.property_type
            and abs(p.area - property.area) / property.area < 0.2  # within 20% size difference
        ]
        
        if not similar_properties:
            raise ValueError("No sufficiently similar comparable properties found")
        
        # Calculate average price per square meter
        price_per_sqm = [p.market_value / p.area for p in similar_properties if p.market_value]
        avg_price = statistics.mean(price_per_sqm)
        
        return avg_price * property.area


class IncomeCapitalization(AppraisalMethod):
    """
    Extra-judicial method that values property based on its income potential.
    """
    
    def __init__(self, annual_net_income: float, capitalization_rate: float):
        self.annual_net_income = annual_net_income
        self.capitalization_rate = capitalization_rate
    
    def calculate_value(self, property: Property) -> float:
        """Calculate value based on income capitalization."""
        if self.capitalization_rate <= 0:
            raise ValueError("Capitalization rate must be positive")
        return self.annual_net_income / self.capitalization_rate


class CostApproach(AppraisalMethod):
    """
    Judicial method that values property based on replacement cost.
    """
    
    def __init__(self, construction_cost_per_sqm: float, land_value: float, depreciation_rate: float):
        self.construction_cost_per_sqm = construction_cost_per_sqm
        self.land_value = land_value
        self.depreciation_rate = depreciation_rate
    
    def calculate_value(self, property: Property) -> float:
        """Calculate value based on cost approach."""
        current_year = datetime.datetime.now().year
        age = current_year - property.construction_year
        
        # Calculate depreciated construction value
        construction_value = property.area * self.construction_cost_per_sqm
        depreciation_factor = (1 - self.depreciation_rate) ** age
        depreciated_construction_value = construction_value * depreciation_factor
        
        return depreciated_construction_value + self.land_value


class PropertyEvaluator:
    """
    Main class for property evaluation that can use different appraisal methods.
    """
    
    def __init__(self):
        self.methods: Dict[AppraisalType, AppraisalMethod] = {}
    
    def register_method(self, appraisal_type: AppraisalType, method: AppraisalMethod):
        """Register an appraisal method for a specific type."""
        self.methods[appraisal_type] = method
    
    def evaluate(self, property: Property, appraisal_type: AppraisalType) -> float:
        """
        Evaluate a property using the specified appraisal type.
        
        Args:
            property: The property to evaluate
            appraisal_type: Type of appraisal to perform
            
        Returns:
            The calculated property value
            
        Raises:
            ValueError: If no method is registered for the appraisal type
        """
        if appraisal_type not in self.methods:
            raise ValueError(f"No method registered for appraisal type: {appraisal_type}")
        
        method = self.methods[appraisal_type]
        return method.calculate_value(property)


# Example usage
if __name__ == "__main__":
    # Create a sample property
    sample_property = Property(
        id="12345",
        address="123 Main St",
        area=150.0,
        property_type=PropertyType.RESIDENTIAL,
        registration_number="ABC123",
        construction_year=2010
    )
    
    # Create comparable properties for CMA
    comparable_properties = [
        Property(
            id="1",
            address="100 Oak St",
            area=140.0,
            property_type=PropertyType.RESIDENTIAL,
            registration_number="XYZ456",
            construction_year=2012,
            market_value=420000.0
        ),
        Property(
            id="2",
            address="200 Pine St",
            area=160.0,
            property_type=PropertyType.RESIDENTIAL,
            registration_number="DEF789",
            construction_year=2008,
            market_value=480000.0
        )
    ]
    
    # Initialize evaluator
    evaluator = PropertyEvaluator()
    
    # Register methods
    evaluator.register_method(
        AppraisalType.EXTRA_JUDICIAL,
        ComparativeMarketAnalysis(comparable_properties)
    )
    
    evaluator.register_method(
        AppraisalType.EXTRA_JUDICIAL,
        IncomeCapitalization(annual_net_income=30000.0, capitalization_rate=0.05)
    )
    
    evaluator.register_method(
        AppraisalType.JUDICIAL,
        CostApproach(
            construction_cost_per_sqm=2000.0,
            land_value=100000.0,
            depreciation_rate=0.02
        )
    )
    
    # Perform evaluations
    try:
        cma_value = evaluator.evaluate(sample_property, AppraisalType.EXTRA_JUDICIAL)
        print(f"Comparative Market Analysis Value: ${cma_value:,.2f}")
        
        income_value = evaluator.evaluate(sample_property, AppraisalType.EXTRA_JUDICIAL)
        print(f"Income Capitalization Value: ${income_value:,.2f}")
        
        cost_value = evaluator.evaluate(sample_property, AppraisalType.JUDICIAL)
        print(f"Cost Approach Value: ${cost_value:,.2f}")
    except ValueError as e:
        print(f"Evaluation error: {e}")
```
