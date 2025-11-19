"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Using the brands listed on Roshako's website (e.g., Esab, Miller, Dewalt, Victor), write a script to recommend industrial tools based on user input for specific industries like oil & gas or marine engineering.
Generated: DETERMINISTIC_dd055eff3c1f1717
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

# Database of tools by brand and industry
TOOL_DATABASE = {
    "Esab": {
        "oil & gas": ["Welding machines", "Cutting systems", "Automation equipment"],
        "marine engineering": ["Marine welding equipment", "Shipbuilding tools"],
        "construction": ["Portable welders", "Plasma cutters"]
    },
    "Miller": {
        "oil & gas": ["Industrial welders", "Pipe welding tools"],
        "marine engineering": ["Marine-grade welders", "Aluminum welding equipment"],
        "construction": ["MIG welders", "TIG welders"]
    },
    "Dewalt": {
        "oil & gas": ["Heavy-duty drills", "Impact wrenches"],
        "marine engineering": ["Waterproof tools", "Corrosion-resistant tools"],
        "construction": ["Power drills", "Saws", "Grinders"]
    },
    "Victor": {
        "oil & gas": ["Gas regulators", "Cutting torches"],
        "marine engineering": ["Marine cutting equipment", "Oxy-fuel systems"],
        "construction": ["Torch kits", "Gas control equipment"]
    }
}

def get_industry_tools(brand: str, industry: str) -> Optional[List[str]]:
    """
    Retrieve tools for a specific brand and industry.
    
    Args:
        brand: The brand name (e.g., 'Esab', 'Miller')
        industry: The target industry (e.g., 'oil & gas', 'marine engineering')
    
    Returns:
        List of tools or None if not found
    """
    brand_data = TOOL_DATABASE.get(brand.title())
    if not brand_data:
        return None
    
    return brand_data.get(industry.lower())

def recommend_tools(industry: str, preferred_brands: List[str] = None) -> Dict[str, List[str]]:
    """
    Recommend tools from various brands for a specific industry.
    
    Args:
        industry: Target industry for tool recommendations
        preferred_brands: Optional list of preferred brands to filter by
    
    Returns:
        Dictionary mapping brands to their recommended tools for the industry
    """
    recommendations = {}
    
    for brand, industries in TOOL_DATABASE.items():
        if preferred_brands and brand not in [b.title() for b in preferred_brands]:
            continue
            
        tools = industries.get(industry.lower())
        if tools:
            recommendations[brand] = tools
    
    return recommendations

def main():
    """Main interactive function for tool recommendations."""
    print("Industrial Tool Recommendation System")
    print("Supported industries: oil & gas, marine engineering, construction")
    print("Supported brands: Esab, Miller, Dewalt, Victor\n")
    
    try:
        industry = input("Enter your industry: ").strip()
        if not industry:
            raise ValueError("Industry cannot be empty")
            
        brand_preference = input("Enter preferred brands (comma separated, or leave blank for all): ").strip()
        preferred_brands = [b.strip() for b in brand_preference.split(",")] if brand_preference else None
        
        recommendations = recommend_tools(industry, preferred_brands)
        
        if not recommendations:
            print("\nNo tools found for the specified criteria.")
            return
            
        print("\nRecommended Tools:")
        for brand, tools in recommendations.items():
            print(f"\n{brand}:")
            for tool in tools:
                print(f"- {tool}")
                
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
```
