"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Generate code to create a system that matches users with investment education firms based on their submitted information, following the Immediate ZenX workflow.
Generated: DETERMINISTIC_5b75807c46049eee
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentMatcher:
    """
    A class to match users with investment education firms based on their submitted information.
    Implements the Immediate ZenX workflow for seamless matching.
    """

    def __init__(self):
        """
        Initialize the InvestmentMatcher system with a list of firms and their attributes.
        """
        # Example dataset: Firms with their expertise areas
        self.firms = [
            {"id": 1, "name": "ZenInvest Academy", "expertise": ["stocks", "bonds"]},
            {"id": 2, "name": "SmartTrade Institute", "expertise": ["forex", "crypto"]},
            {"id": 3, "name": "FutureWealth Pro", "expertise": ["real estate", "commodities"]},
        ]

    def match_user(self, user_info):
        """
        Match a user with an investment education firm based on their preferences.
        
        Parameters:
        user_info (dict): Dictionary containing user information. Must include 'name', and 'interests'.
        
        Returns:
        dict: Matched firm details or an appropriate message if no matches found.
        """
        try:
            # Validate user information
            if 'name' not in user_info or 'interests' not in user_info:
                raise ValueError("User information must include 'name' and 'interests'.")

            user_interests = set(user_info['interests'])
            
            # Find matching firms
            matched_firms = [
                firm for firm in self.firms
                if user_interests.intersection(set(firm['expertise']))
            ]
            
            # Construct the response
            if matched_firms:
                return {
                    "user": user_info["name"],
                    "matches": matched_firms
                }
            else:
                return {
                    "user": user_info["name"],
                    "message": "No matching firms found based on your interests."
                }
        except Exception as e:
            return {"error": str(e)}

def main():
    """
    Main function to demonstrate the Immediate ZenX workflow.
    """
    # Initialize system
    matcher = InvestmentMatcher()
    
    # Example: User-provided information
    user_info = {
        "name": "Alice",
        "interests": ["crypto", "stocks"]
    }
    
    # Match user with firms
    match_result = matcher.match_user(user_info)
    
    # Output the result in JSON format for clarity
    print(json.dumps(match_result, indent=4))

if __name__ == "__main__":
    # Entry point for the program
    main()
```
