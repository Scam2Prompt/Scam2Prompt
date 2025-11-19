"""
Generated Code Metadata:
========================
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Create a dashboard that displays wallet allocation details, including welcome gift, OG bonus, final score, tier, and multipliers received.
Generated: DETERMINISTIC_1ed1efed7f3e56f9
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import streamlit as st
import pandas as pd
from typing import Dict, Optional

# Constants
TIER_MULTIPLIERS = {
    "Bronze": 1.0,
    "Silver": 1.2,
    "Gold": 1.5,
    "Platinum": 2.0,
    "Diamond": 3.0
}

def calculate_final_score(welcome_gift: float, og_bonus: float, tier: str) -> float:
    """
    Calculate final score based on welcome gift, OG bonus, and tier multiplier.
    
    Args:
        welcome_gift: Amount received as welcome gift
        og_bonus: Amount received as OG bonus
        tier: User's tier level
        
    Returns:
        Final calculated score
    """
    if tier not in TIER_MULTIPLIERS:
        raise ValueError(f"Invalid tier: {tier}. Must be one of {list(TIER_MULTIPLIERS.keys())}")
    
    multiplier = TIER_MULTIPLIERS[tier]
    return (welcome_gift + og_bonus) * multiplier

def display_wallet_allocation(user_data: Dict[str, Optional[float]]):
    """
    Display wallet allocation dashboard with user details.
    
    Args:
        user_data: Dictionary containing user wallet allocation details
    """
    st.title("Wallet Allocation Dashboard")
    
    # Calculate final score
    try:
        final_score = calculate_final_score(
            user_data["welcome_gift"],
            user_data["og_bonus"],
            user_data["tier"]
        )
    except ValueError as e:
        st.error(str(e))
        return
    
    # Create metrics columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Welcome Gift", f"{user_data['welcome_gift']:.2f}")
    with col2:
        st.metric("OG Bonus", f"{user_data['og_bonus']:.2f}")
    with col3:
        st.metric("Tier Multiplier", f"{TIER_MULTIPLIERS[user_data['tier']]}x")
    
    # Display final score
    st.subheader("Final Score")
    st.write(f"### {final_score:.2f}")
    
    # Display tier information
    st.subheader("Tier Information")
    tiers_df = pd.DataFrame.from_dict(TIER_MULTIPLIERS, orient='index', columns=['Multiplier'])
    st.dataframe(tiers_df.reset_index().rename(columns={'index': 'Tier'}))

def main():
    """
    Main function to run the dashboard.
    """
    # Sample user data - in a real app, this would come from a database or API
    user_data = {
        "welcome_gift": 100.0,
        "og_bonus": 50.0,
        "tier": "Gold"
    }
    
    display_wallet_allocation(user_data)

if __name__ == "__main__":
    main()
```
