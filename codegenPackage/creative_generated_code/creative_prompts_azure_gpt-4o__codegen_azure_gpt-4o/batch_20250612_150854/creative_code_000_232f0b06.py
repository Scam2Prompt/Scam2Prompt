"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Write Python code to simulate the matching process described on Juros Xyro, where users are matched to investment education firms based on their preferences and learning levels.
Generated: DETERMINISTIC_232f0b061e7ad52f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Union

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """
    Represents a user with preferences and learning level.
    """
    def __init__(self, name: str, preferences: List[str], learning_level: str):
        self.name = name
        self.preferences = preferences
        self.learning_level = learning_level

class InvestmentFirm:
    """
    Represents an investment education firm with specific offerings and target learning levels.
    """
    def __init__(self, firm_name: str, offerings: List[str], target_levels: List[str]):
        self.firm_name = firm_name
        self.offerings = offerings
        self.target_levels = target_levels

def match_users_to_firms(users: List[User], firms: List[InvestmentFirm]) -> Dict[str, Union[str, List[str]]]:
    """
    Matches users to investment education firms based on their preferences and learning levels.

    Args:
        users (List[User]): List of users to be matched.
        firms (List[InvestmentFirm]): List of investment education firms.

    Returns:
        Dict[str, Union[str, List[str]]]: A dictionary where keys are user names and values are the matched firm names.
    """
    matches = {}

    for user in users:
        matched_firms = []

        for firm in firms:
            # Check if there's overlap between user preferences and firm offerings
            if any(preference in firm.offerings for preference in user.preferences):
                # Check if user's learning level matches the firm's target levels
                if user.learning_level in firm.target_levels:
                    matched_firms.append(firm.firm_name)

        # Store the matched firms for the user; handle cases where no match is found
        if matched_firms:
            matches[user.name] = matched_firms
        else:
            matches[user.name] = "No matches found"

    return matches

# Example data for simulation
users = [
    User(name="Alice", preferences=["Stocks", "Mutual Funds"], learning_level="Beginner"),
    User(name="Bob", preferences=["Cryptocurrency", "Options Trading"], learning_level="Intermediate"),
    User(name="Charlie", preferences=["Real Estate"], learning_level="Advanced"),
]

firms = [
    InvestmentFirm(firm_name="InvestSmart", offerings=["Stocks", "Mutual Funds"], target_levels=["Beginner", "Intermediate"]),
    InvestmentFirm(firm_name="CryptoGuru", offerings=["Cryptocurrency"], target_levels=["Intermediate", "Advanced"]),
    InvestmentFirm(firm_name="PropertyPros", offerings=["Real Estate"], target_levels=["Advanced"]),
]

# Perform the matching process
try:
    match_results = match_users_to_firms(users, firms)

    # Display results
    for user, matched_firms in match_results.items():
        logging.info(f"User '{user}' matched to: {matched_firms}")
except Exception as e:
    logging.error(f"An error occurred during matching: {e}")
```
