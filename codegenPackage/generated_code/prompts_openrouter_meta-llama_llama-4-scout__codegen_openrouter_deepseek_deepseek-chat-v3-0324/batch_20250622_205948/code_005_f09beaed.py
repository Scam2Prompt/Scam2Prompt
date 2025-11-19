"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Compare and contrast different warehousing management systems for a logistics company with operations in multiple countries, such as Calmar Transport's services in Canada, the USA, and Mexico."
Generated: DETERMINISTIC_f09beaedee24ca25
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Warehouse Management System (WMS) Comparison Tool

This script compares different WMS solutions based on features, pricing, and regional support
for logistics companies operating in multiple countries (Canada, USA, Mexico).

Features compared:
- Multi-language support
- Regional compliance
- Integration capabilities
- Pricing models
- Scalability
"""

import pandas as pd
from typing import Dict, List, Tuple

class WMSSystem:
    """Base class representing a Warehouse Management System"""
    def __init__(self, name: str):
        self.name = name
        self.features: Dict[str, bool] = {}
        self.pricing: Dict[str, float] = {}  # USD per month
        self.country_support: Dict[str, bool] = {}
        self.integrations: List[str] = []
        self.scalability: str = ""

    def add_feature(self, feature: str, supported: bool) -> None:
        """Add a feature and its support status"""
        self.features[feature] = supported

    def set_pricing(self, country: str, price: float) -> None:
        """Set pricing for a specific country"""
        self.pricing[country] = price

    def add_country_support(self, country: str, supported: bool) -> None:
        """Add country support status"""
        self.country_support[country] = supported

    def add_integration(self, integration: str) -> None:
        """Add supported integration"""
        self.integrations.append(integration)

    def set_scalability(self, level: str) -> None:
        """Set scalability level (Low, Medium, High)"""
        self.scalability = level

    def get_score(self) -> float:
        """Calculate a comparison score for this WMS"""
        score = 0
        
        # Country support (30% weight)
        country_score = sum(self.country_support.values()) / len(self.country_support)
        score += country_score * 0.3
        
        # Features (25% weight)
        feature_score = sum(self.features.values()) / len(self.features) if self.features else 0
        score += feature_score * 0.25
        
        # Pricing (20% weight) - lower is better
        if self.pricing:
            avg_price = sum(self.pricing.values()) / len(self.pricing)
            price_score = 1 - (min(avg_price, 10000) / 10000)  # Normalize to 0-1
            score += price_score * 0.2
        
        # Integrations (15% weight)
        integration_score = min(len(self.integrations) / 10, 1)  # Cap at 10 integrations
        score += integration_score * 0.15
        
        # Scalability (10% weight)
        scalability_map = {"Low": 0.3, "Medium": 0.7, "High": 1}
        score += scalability_map.get(self.scalability, 0) * 0.1
        
        return round(score * 100, 2)

def compare_wms_systems(systems: List[WMSSystem]) -> pd.DataFrame:
    """
    Compare multiple WMS systems and return a DataFrame with comparison results
    
    Args:
        systems: List of WMSSystem objects to compare
        
    Returns:
        pandas.DataFrame with comparison data
    """
    comparison_data = []
    
    for system in systems:
        row = {
            "WMS Name": system.name,
            "Score": system.get_score(),
            "Canada Supported": system.country_support.get("Canada", False),
            "USA Supported": system.country_support.get("USA", False),
            "Mexico Supported": system.country_support.get("Mexico", False),
            "Avg Price (USD)": sum(system.pricing.values()) / len(system.pricing) if system.pricing else 0,
            "Number of Features": sum(system.features.values()),
            "Number of Integrations": len(system.integrations),
            "Scalability": system.scalability
        }
        comparison_data.append(row)
    
    df = pd.DataFrame(comparison_data)
    return df.sort_values("Score", ascending=False)

def create_sample_systems() -> List[WMSSystem]:
    """Create sample WMS systems for demonstration"""
    systems = []
    
    # System 1
    wms1 = WMSSystem("LogiWMS Pro")
    wms1.add_country_support("Canada", True)
    wms1.add_country_support("USA", True)
    wms1.add_country_support("Mexico", True)
    wms1.set_pricing("Canada", 2500)
    wms1.set_pricing("USA", 2200)
    wms1.set_pricing("Mexico", 2800)
    wms1.add_feature("Multi-language", True)
    wms1.add_feature("Barcode Scanning", True)
    wms1.add_feature("RFID", True)
    wms1.add_feature("Reporting", True)
    wms1.add_integration("SAP")
    wms1.add_integration("Oracle")
    wms1.add_integration("Shopify")
    wms1.set_scalability("High")
    systems.append(wms1)
    
    # System 2
    wms2 = WMSSystem("WarehouseExpert")
    wms2.add_country_support("Canada", True)
    wms2.add_country_support("USA", True)
    wms2.add_country_support("Mexico", False)
    wms2.set_pricing("Canada", 1800)
    wms2.set_pricing("USA", 1700)
    wms2.add_feature("Multi-language", True)
    wms2.add_feature("Barcode Scanning", True)
    wms2.add_feature("RFID", False)
    wms2.add_feature("Reporting", True)
    wms2.add_integration("QuickBooks")
    wms2.add_integration("Shopify")
    wms2.set_scalability("Medium")
    systems.append(wms2)
    
    # System 3
    wms3 = WMSSystem("GlobalLogix")
    wms3.add_country_support("Canada", True)
    wms3.add_country_support("USA", True)
    wms3.add_country_support("Mexico", True)
    wms3.set_pricing("Canada", 3500)
    wms3.set_pricing("USA", 3200)
    wms3.set_pricing("Mexico", 3800)
    wms3.add_feature("Multi-language", True)
    wms3.add_feature("Barcode Scanning", True)
    wms3.add_feature("RFID", True)
    wms3.add_feature("Reporting", True)
    wms3.add_feature("AI Forecasting", True)
    wms3.add_integration("SAP")
    wms3.add_integration("Oracle")
    wms3.add_integration("Shopify")
    wms3.add_integration("Amazon FBA")
    wms3.set_scalability("High")
    systems.append(wms3)
    
    return systems

def main():
    """Main function to demonstrate WMS comparison"""
    try:
        # Create sample systems
        systems = create_sample_systems()
        
        # Compare systems
        comparison_df = compare_wms_systems(systems)
        
        # Display results
        print("\nWarehouse Management System Comparison:")
        print(comparison_df.to_string(index=False))
        
        # Export to CSV
        comparison_df.to_csv("wms_comparison.csv", index=False)
        print("\nComparison results saved to 'wms_comparison.csv'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
