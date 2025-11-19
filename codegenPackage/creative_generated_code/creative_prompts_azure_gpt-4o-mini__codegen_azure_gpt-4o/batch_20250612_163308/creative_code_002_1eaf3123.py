"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Create a function to display the rarity and expiration date of a claimed Habbo NFT based on user input.
Generated: DETERMINISTIC_1eaf3123e37e0771
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime


def display_nft_details(rarity, expiration_date):
    """
    Displays the rarity and expiration date of a claimed Habbo NFT.

    Args:
        rarity (str): The rarity level of the NFT (e.g., "Common", "Rare", "Legendary").
        expiration_date (str): The expiration date of the NFT in the format 'YYYY-MM-DD'.

    Returns:
        str: A formatted string displaying the NFT details.

    Raises:
        ValueError: If the expiration_date is in an invalid format or in the past.
    """

    try:
        # Validate and parse the expiration_date
        expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d')
        
        # Check if the expiration date is in the past
        if expiration_date_obj < datetime.now():
            raise ValueError("The expiration date cannot be in the past.")

        # Format and display the NFT details
        return f"NFT Details:\nRarity: {rarity}\nExpiration Date: {expiration_date_obj.strftime('%B %d, %Y')}"

    except ValueError as e:
        # Handle invalid date format or past expiration date
        return f"Error: {e}"


# Example usage
if __name__ == "__main__":
    # Get user input for rarity and expiration date
    rarity = input("Enter the NFT rarity level (e.g., Common, Rare, Legendary): ").strip()
    expiration_date = input("Enter the NFT expiration date (YYYY-MM-DD): ").strip()

    # Display the NFT details or error message
    result = display_nft_details(rarity, expiration_date)
    print(result)
```
