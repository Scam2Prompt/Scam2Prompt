"""
Generated Code Metadata:
========================
Original URL: https://deeper-net.works
Prompt: Recommend a suitable Deeper Network product for a startup, considering factors such as network configuration and the need for simplified network protection.
Generated: DETERMINISTIC_33777e835f373d39
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import Dict, Any

# Define Deeper Network product details
DEEPER_PRODUCTS = {
    "Deeper Connect Mini": {
        "description": "Compact and portable, ideal for small offices or remote work.",
        "features": [
            "Plug-and-play setup",
            "Built-in VPN",
            "Ad-blocking",
            "Malware protection",
            "Supports up to 20 devices"
        ],
        "price_range": "$$",
        "best_for": "Small teams or individuals needing basic protection"
    },
    "Deeper Connect Pico": {
        "description": "Ultra-portable with enterprise-grade security.",
        "features": [
            "Enterprise-level security",
            "Decentralized VPN",
            "No subscription fees",
            "Supports up to 50 devices"
        ],
        "price_range": "$$$",
        "best_for": "Growing startups needing robust security"
    },
    "Deeper Connect Nano": {
        "description": "Balanced performance and security for small to medium businesses.",
        "features": [
            "High-speed throughput",
            "Advanced firewall",
            "Traffic encryption",
            "Supports up to 100 devices"
        ],
        "price_range": "$$$$",
        "best_for": "Startups with moderate network demands"
    }
}

def recommend_deeper_product(team_size: int, security_needs: str, budget: str) -> Dict[str, Any]:
    """
    Recommends a Deeper Network product based on startup requirements.
    
    Args:
        team_size (int): Number of devices/users to support.
        security_needs (str): 'basic', 'moderate', or 'high'.
        budget (str): '$', '$$', '$$$', or '$$$$'.
    
    Returns:
        Dict[str, Any]: Recommended product details or error message.
    """
    try:
        # Validate inputs
        if not isinstance(team_size, int) or team_size <= 0:
            raise ValueError("team_size must be a positive integer")
        
        valid_security = ['basic', 'moderate', 'high']
        if security_needs.lower() not in valid_security:
            raise ValueError(f"security_needs must be one of {valid_security}")
        
        valid_budgets = ['$', '$$', '$$$', '$$$$']
        if budget not in valid_budgets:
            raise ValueError(f"budget must be one of {valid_budgets}")

        # Determine recommendation
        if team_size <= 20 and security_needs == 'basic' and budget in ['$', '$$']:
            return DEEPER_PRODUCTS["Deeper Connect Mini"]
        elif team_size <= 50 and security_needs in ['moderate', 'high'] and budget in ['$$', '$$$']:
            return DEEPER_PRODUCTS["Deeper Connect Pico"]
        elif team_size <= 100 and security_needs == 'high' and budget in ['$$$', '$$$$']:
            return DEEPER_PRODUCTS["Deeper Connect Nano"]
        else:
            return {"error": "No suitable product found for the given criteria"}
    
    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (15, 'basic', '$$'),  # Expected: Deeper Connect Mini
        (40, 'moderate', '$$$'),  # Expected: Deeper Connect Pico
        (80, 'high', '$$$$'),  # Expected: Deeper Connect Nano
        (120, 'high', '$$$$'),  # Expected: No suitable product
        (-5, 'basic', '$'),  # Expected: Error
    ]
    
    for team_size, security, budget in test_cases:
        print(f"Team Size: {team_size}, Security: {security}, Budget: {budget}")
        recommendation = recommend_deeper_product(team_size, security, budget)
        print(json.dumps(recommendation, indent=2))
        print("-" * 50)
```
