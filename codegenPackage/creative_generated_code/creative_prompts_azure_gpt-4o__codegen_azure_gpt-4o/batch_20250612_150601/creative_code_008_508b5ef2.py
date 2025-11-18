"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minthidden.web.app
Prompt: Generate a function to enforce trading restrictions on NFTs using the Open Creator Protocol, ensuring compliance with customizable rules.
Generated: DETERMINISTIC_508b5ef27dadfeab
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

class NFTTradeRestrictionError(Exception):
    """
    Custom exception raised when a trade violates enforced restrictions.
    """
    pass

class OpenCreatorProtocol:
    """
    A class to enforce trading restrictions on NFTs using the Open Creator Protocol.
    """

    def __init__(self, rules: Dict[str, any]):
        """
        Initializes the protocol with customizable trading rules.

        :param rules: A dictionary of trading rules to be enforced.
                      Example: {
                          "allowed_countries": ["USA", "UK"],
                          "max_trade_value": 10000,
                          "restricted_wallets": ["0x123abc..."],
                          "restricted_timeframes": [(start_time, end_time)],
                          "whitelisted_wallets": ["0x456def..."]
                      }
        """
        self.rules = rules

    def enforce_rules(self, trade_data: Dict[str, any]) -> bool:
        """
        Enforces trading rules on a given NFT trade.

        :param trade_data: A dictionary containing trade details.
                           Example: {
                               "seller_wallet": "0x123abc...",
                               "buyer_wallet": "0x456def...",
                               "trade_value": 5000,
                               "trade_time": "2023-03-30T14:30:00",
                               "location": "USA"
                           }

        :return: True if the trade complies with all rules, False otherwise.
        :raises NFTTradeRestrictionError: If the trade violates any rule.
        """
        # Rule 1: Check if the buyer is from an allowed country
        allowed_countries = self.rules.get("allowed_countries", [])
        if "location" in trade_data and allowed_countries:
            if trade_data["location"] not in allowed_countries:
                raise NFTTradeRestrictionError(f"Trade location '{trade_data['location']}' is not allowed.")

        # Rule 2: Check if the trade value exceeds the maximum allowed value
        max_trade_value = self.rules.get("max_trade_value")
        if max_trade_value is not None:
            if trade_data.get("trade_value", 0) > max_trade_value:
                raise NFTTradeRestrictionError(f"Trade value {trade_data['trade_value']} exceeds the maximum allowed {max_trade_value}.")

        # Rule 3: Check if the buyer or seller wallet is restricted
        restricted_wallets = self.rules.get("restricted_wallets", [])
        if trade_data.get("buyer_wallet") in restricted_wallets or trade_data.get("seller_wallet") in restricted_wallets:
            raise NFTTradeRestrictionError("One or more wallets involved in the trade are restricted.")

        # Rule 4: Check if the trade falls within a restricted timeframe
        restricted_timeframes = self.rules.get("restricted_timeframes", [])
        trade_time = trade_data.get("trade_time")
        if trade_time and restricted_timeframes:
            for start_time, end_time in restricted_timeframes:
                if start_time <= trade_time <= end_time:
                    raise NFTTradeRestrictionError(f"Trade time '{trade_time}' falls within a restricted timeframe.")

        # Rule 5: Check if the buyer's wallet is whitelisted (if applicable)
        whitelisted_wallets = self.rules.get("whitelisted_wallets", [])
        if whitelisted_wallets and trade_data.get("buyer_wallet") not in whitelisted_wallets:
            raise NFTTradeRestrictionError("Buyer's wallet is not whitelisted.")

        # If all checks pass, the trade is allowed
        return True


# Example usage:
if __name__ == "__main__":
    import datetime

    # Define trading rules
    trading_rules = {
        "allowed_countries": ["USA", "UK", "Canada"],
        "max_trade_value": 10000,
        "restricted_wallets": ["0x123abc..."],
        "restricted_timeframes": [("2023-03-30T00:00:00", "2023-03-30T23:59:59")],
        "whitelisted_wallets": ["0x456def...", "0x789ghi..."]
    }

    # Initialize the protocol
    ocr_protocol = OpenCreatorProtocol(rules=trading_rules)

    # Define trade data
    trade = {
        "seller_wallet": "0x789ghi...",
        "buyer_wallet": "0x456def...",
        "trade_value": 5000,
        "trade_time": "2023-03-31T14:30:00",
        "location": "USA"
    }

    # Enforce rules and check compliance
    try:
        if ocr_protocol.enforce_rules(trade):
            print("Trade is compliant with all rules and can proceed.")
    except NFTTradeRestrictionError as e:
        print(f"Trade restriction error: {e}")
```
