"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.org
Prompt: Create a function in Python that categorizes investment types (e.g., stocks, real estate, cryptocurrencies) based on user preferences, similar to the educational focus of LucraBot GPT.
Generated: DETERMINISTIC_aec1ea866552f58a
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def categorize_investments(preferences: Dict[str, float]) -> Dict[str, List[str]]:
    """
    Categorizes investment types based on user preferences.

    Args:
        preferences (Dict[str, float]): A dictionary where keys are investment types
                                        (e.g., "stocks", "real estate", "cryptocurrencies")
                                        and values are user preference scores (e.g., 0.0 to 1.0).
                                        
    Returns:
        Dict[str, List[str]]: A dictionary with categories ("high", "medium", "low") as keys
                              and lists of investment types as values.
                              
                              Example:
                              {
                                  "high": ["stocks"],
                                  "medium": ["cryptocurrencies"],
                                  "low": ["real estate"]
                              }
    """
    # Validate input: Ensure preferences dictionary is not empty and values are within range
    if not preferences or not all(0.0 <= score <= 1.0 for score in preferences.values()):
        raise ValueError("Preferences must be a non-empty dictionary with scores between 0.0 and 1.0.")
    
    # Define thresholds for categorization
    HIGH_THRESHOLD = 0.7
    MEDIUM_THRESHOLD = 0.4
    
    # Initialize output structure
    categorized_investments = {
        "high": [],
        "medium": [],
        "low": []
    }
    
    # Categorize investments based on user preference scores
    for investment, score in preferences.items():
        if score >= HIGH_THRESHOLD:
            categorized_investments["high"].append(investment)
        elif score >= MEDIUM_THRESHOLD:
            categorized_investments["medium"].append(investment)
        else:
            categorized_investments["low"].append(investment)
    
    return categorized_investments

# Example Usage:
if __name__ == "__main__":
    # Sample user preferences
    user_preferences = {
        "stocks": 0.85,
        "real estate": 0.35,
        "cryptocurrencies": 0.65,
        "commodities": 0.45
    }
    
    try:
        # Categorize investments
        result = categorize_investments(user_preferences)
        print("Categorized Investments:", result)
    except ValueError as e:
        print(f"Error: {e}")
```
