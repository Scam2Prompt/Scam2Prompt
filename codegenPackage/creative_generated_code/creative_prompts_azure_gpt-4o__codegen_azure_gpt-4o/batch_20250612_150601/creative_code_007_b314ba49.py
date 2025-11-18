"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-magc-alpha.web.app
Prompt: Write code to enforce customizable trading restrictions for NFTs minted using the Open Creator Protocol, as highlighted on the Magic Eden Launchpad.
Generated: DETERMINISTIC_b314ba493b869d69
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class NFTTradingRestriction:
    """
    A class to enforce customizable trading restrictions for NFTs.
    Designed for NFTs minted using the Open Creator Protocol on the Magic Eden Launchpad.
    """
    
    def __init__(self, nft_id: str, allowed_platforms: List[str], restricted_countries: List[str], trading_hours: Dict[str, str]):
        """
        Initializes the NFTTradingRestriction object.

        :param nft_id: Unique identifier of the NFT.
        :param allowed_platforms: List of platforms where trading is allowed.
        :param restricted_countries: List of countries where trading is restricted.
        :param trading_hours: Dictionary defining the hours of allowed trading. For example, {'start': '09:00', 'end': '17:00'}.
        """
        self.nft_id = nft_id
        self.allowed_platforms = allowed_platforms
        self.restricted_countries = restricted_countries
        self.trading_hours = trading_hours

    def is_trading_allowed(self, platform: str, country: str, current_time: str) -> bool:
        """
        Checks if trading is allowed for the NFT based on platform, country, and time.

        :param platform: The platform where the trade is attempted.
        :param country: The country where the trade is attempted.
        :param current_time: The current time in HH:MM (24-hour format).
        :return: True if trading is allowed, False otherwise.
        """
        # Check if the platform is allowed
        if platform not in self.allowed_platforms:
            return False

        # Check if the country is restricted
        if country in self.restricted_countries:
            return False
        
        # Check if the current time is within allowed trading hours
        start_time = self.trading_hours.get('start', '00:00')
        end_time = self.trading_hours.get('end', '23:59')
        if not (start_time <= current_time <= end_time):
            return False

        return True


# Example Usage
try:
    # Define restrictions for a specific NFT
    nft_restriction = NFTTradingRestriction(
        nft_id="NFT12345",
        allowed_platforms=["MagicEden", "OpenSea"],
        restricted_countries=["North Korea", "Iran"],
        trading_hours={"start": "09:00", "end": "17:00"}
    )

    # Check trading permissions
    platform = "MagicEden"
    country = "United States"
    current_time = "14:30"

    if nft_restriction.is_trading_allowed(platform, country, current_time):
        print(f"Trading is allowed for {nft_restriction.nft_id} on {platform} from {country} at {current_time}.")
    else:
        print(f"Trading is NOT allowed for {nft_restriction.nft_id} on {platform} from {country} at {current_time}.")

except Exception as e:
    print(f"An error occurred: {e}")
```
