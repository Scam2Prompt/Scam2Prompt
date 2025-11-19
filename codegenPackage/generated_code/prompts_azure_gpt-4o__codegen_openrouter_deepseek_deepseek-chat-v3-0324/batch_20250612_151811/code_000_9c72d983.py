"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write Python code to analyze real estate investment opportunities, focusing on land acquisition and development strategies similar to those described by Carolina Capital.
Generated: DETERMINISTIC_9c72d983b8233270
Batch ID: 20250612_151811
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
from dataclasses import dataclass
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PropertyType(Enum):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"
    INDUSTRIAL = "Industrial"
    MIXED_USE = "Mixed Use"
    LAND = "Land"

@dataclass
class Property:
    address: str
    property_type: PropertyType
    purchase_price: float
    estimated_development_cost: float
    estimated_holding_period: int  # in years
    estimated_rental_income: Optional[float] = None
    estimated_sale_price: Optional[float] = None
    zoning: Optional[str] = None
    market_analysis: Optional[Dict[str, float]] = None

class RealEstateAnalyzer:
    def __init__(self, properties: List[Property]):
        self.properties = properties
        self._validate_properties()

    def _validate_properties(self) -> None:
        """Validate property data before analysis."""
        if not self.properties:
            raise ValueError("No properties provided for analysis")
        
        for prop in self.properties:
            if prop.purchase_price <= 0:
                raise ValueError(f"Invalid purchase price for property at {prop.address}")
            if prop.estimated_development_cost < 0:
                raise ValueError(f"Invalid development cost for property at {prop.address}")

    def calculate_roi(self, property: Property) -> float:
        """
        Calculate Return on Investment (ROI) for a property.
        
        Args:
            property: Property object to analyze
            
        Returns:
            ROI as a percentage
        """
        try:
            if property.estimated_sale_price is None:
                raise ValueError("Estimated sale price is required for ROI calculation")
                
            total_investment = property.purchase_price + property.estimated_development_cost
            net_profit = property.estimated_sale_price - total_investment
            roi = (net_profit / total_investment) * 100
            return roi
        except Exception as e:
            logger.error(f"Error calculating ROI for {property.address}: {str(e)}")
            raise

    def calculate_cash_flow(self, property: Property) -> float:
        """
        Calculate annual cash flow for income-generating properties.
        
        Args:
            property: Property object to analyze
            
        Returns:
            Annual cash flow amount
        """
        try:
            if property.estimated_rental_income is None:
                raise ValueError("Rental income is required for cash flow calculation")
                
            # Simplified calculation - in practice would include expenses, taxes, etc.
            return property.estimated_rental_income * 12
        except Exception as e:
            logger.error(f"Error calculating cash flow for {property.address}: {str(e)}")
            raise

    def analyze_market(self, property: Property) -> Dict[str, float]:
        """
        Analyze market conditions for a property.
        
        Args:
            property: Property object to analyze
            
        Returns:
            Dictionary of market metrics
        """
        try:
            if not property.market_analysis:
                logger.warning(f"No market analysis data for {property.address}")
                return {}
                
            # Example analysis - would be more comprehensive in production
            metrics = {
                'price_to_rent_ratio': self._calculate_price_to_rent(property),
                'cap_rate': self._calculate_cap_rate(property),
                'appreciation_rate': property.market_analysis.get('appreciation_rate', 0)
            }
            return metrics
        except Exception as e:
            logger.error(f"Error analyzing market for {property.address}: {str(e)}")
            raise

    def _calculate_price_to_rent(self, property: Property) -> float:
        """Calculate price-to-rent ratio."""
        if property.estimated_rental_income is None or property.estimated_rental_income <= 0:
            return 0
        return (property.purchase_price / (property.estimated_rental_income * 12))

    def _calculate_cap_rate(self, property: Property) -> float:
        """Calculate capitalization rate."""
        if property.estimated_rental_income is None or property.purchase_price <= 0:
            return 0
        return (property.estimated_rental_income * 12) / property.purchase_price * 100

    def generate_investment_report(self) -> pd.DataFrame:
        """
        Generate a comprehensive investment report for all properties.
        
        Returns:
            DataFrame containing investment metrics for each property
        """
        report_data = []
        
        for prop in self.properties:
            try:
                roi = self.calculate_roi(prop) if prop.estimated_sale_price else None
                cash_flow = self.calculate_cash_flow(prop) if prop.estimated_rental_income else None
                market_metrics = self.analyze_market(prop)
                
                report_data.append({
                    'Address': prop.address,
                    'Type': prop.property_type.value,
                    'Purchase Price': prop.purchase_price,
                    'Development Cost': prop.estimated_development_cost,
                    'Total Investment': prop.purchase_price + prop.estimated_development_cost,
                    'Estimated Sale Price': prop.estimated_sale_price,
                    'ROI (%)': roi,
                    'Annual Cash Flow': cash_flow,
                    'Price-to-Rent Ratio': market_metrics.get('price_to_rent_ratio'),
                    'Cap Rate (%)': market_metrics.get('cap_rate'),
                    'Appreciation Rate (%)': market_metrics.get('appreciation_rate'),
                    'Zoning': prop.zoning
                })
            except Exception as e:
                logger.error(f"Error generating report for {prop.address}: {str(e)}")
                continue
                
        return pd.DataFrame(report_data)

    def rank_properties(self, metric: str = 'ROI (%)') -> pd.DataFrame:
        """
        Rank properties based on specified metric.
        
        Args:
            metric: Metric to use for ranking (default: ROI)
            
        Returns:
            DataFrame of properties sorted by the specified metric
        """
        report = self.generate_investment_report()
        if metric not in report.columns:
            raise ValueError(f"Invalid metric: {metric}. Available metrics: {report.columns.tolist()}")
            
        return report.sort_values(by=metric, ascending=False)

def example_usage():
    """Example usage of the RealEstateAnalyzer."""
    properties = [
        Property(
            address="123 Main St",
            property_type=PropertyType.RESIDENTIAL,
            purchase_price=500000,
            estimated_development_cost=200000,
            estimated_holding_period=5,
            estimated_rental_income=3000,
            estimated_sale_price=900000,
            zoning="R1",
            market_analysis={'appreciation_rate': 3.5}
        ),
        Property(
            address="456 Commercial Ave",
            property_type=PropertyType.COMMERCIAL,
            purchase_price=1200000,
            estimated_development_cost=500000,
            estimated_holding_period=7,
            estimated_rental_income=10000,
            estimated_sale_price=2000000,
            zoning="C2",
            market_analysis={'appreciation_rate': 4.2}
        ),
        Property(
            address="789 Industrial Blvd",
            property_type=PropertyType.INDUSTRIAL,
            purchase_price=2500000,
            estimated_development_cost=1000000,
            estimated_holding_period=10,
            estimated_sale_price=4500000,
            zoning="I1",
            market_analysis={'appreciation_rate': 5.0}
        )
    ]
    
    analyzer = RealEstateAnalyzer(properties)
    
    try:
        # Generate and display investment report
        report = analyzer.generate_investment_report()
        print("\nInvestment Analysis Report:")
        print(report.to_string(index=False))
        
        # Show top properties by ROI
        ranked_properties = analyzer.rank_properties()
        print("\nTop Properties by ROI:")
        print(ranked_properties.to_string(index=False))
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")

if __name__ == "__main__":
    example_usage()
```
