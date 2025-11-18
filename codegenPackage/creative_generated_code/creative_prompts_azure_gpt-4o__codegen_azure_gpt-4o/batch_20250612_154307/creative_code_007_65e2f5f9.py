"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Write code to implement a bonus purchase system for casino games, allowing players to buy benefits like free spins or multipliers using cryptocurrency.
Generated: DETERMINISTIC_65e2f5f97a0f535c
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
import logging
import uuid

# Setup basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
AVAILABLE_BONUSES = {
    "free_spins": {"price": decimal.Decimal("0.001"), "description": "10 free spins"},
    "multiplier": {"price": decimal.Decimal("0.005"), "description": "2x multiplier for next game"},
}
SUPPORTED_CRYPTOCURRENCIES = {"BTC", "ETH", "USDT"}

# Simulated User Wallets (mocked for demonstration purposes)
USER_WALLETS = {
    "player1": {"BTC": decimal.Decimal("0.01"), "ETH": decimal.Decimal("0.2"), "USDT": decimal.Decimal("50")},
    "player2": {"BTC": decimal.Decimal("0.0005"), "ETH": decimal.Decimal("0.05"), "USDT": decimal.Decimal("10")},
}

class InsufficientFundsError(Exception):
    """Raised when a player has insufficient funds in their wallet."""
    pass

class BonusPurchaseSystem:
    def __init__(self, user_id):
        """
        Initialize the bonus purchase system for a given player.

        :param user_id: The unique identifier of the player.
        """
        self.user_id = user_id

    def get_available_bonuses(self):
        """
        Retrieve the available bonuses that players can purchase.

        :return: Dictionary of available bonuses with details.
        """
        return AVAILABLE_BONUSES

    def get_player_wallet(self):
        """
        Get the wallet information for the current player.

        :return: Dictionary of cryptocurrencies and balances.
        """
        wallet = USER_WALLETS.get(self.user_id)
        if not wallet:
            logging.error(f"Player '{self.user_id}' not found.")
            raise ValueError("Player not found.")
        return wallet

    def purchase_bonus(self, bonus_key, cryptocurrency):
        """
        Purchase a bonus using cryptocurrency.

        :param bonus_key: Key of the bonus to purchase (e.g., "free_spins").
        :param cryptocurrency: Cryptocurrency to use for payment (e.g., "BTC").
        :return: Confirmation message if purchase is successful.
        """
        # Validate bonus
        bonus = AVAILABLE_BONUSES.get(bonus_key)
        if not bonus:
            logging.error(f"Invalid bonus selected: {bonus_key}")
            raise ValueError("Invalid bonus selected.")

        # Validate cryptocurrency
        if cryptocurrency not in SUPPORTED_CRYPTOCURRENCIES:
            logging.error(f"Unsupported cryptocurrency: {cryptocurrency}")
            raise ValueError("Unsupported cryptocurrency.")

        # Validate player's wallet and funds
        wallet = self.get_player_wallet()
        if cryptocurrency not in wallet:
            logging.error(f"Player '{self.user_id}' does not have {cryptocurrency} in their wallet.")
            raise ValueError(f"{cryptocurrency} not found in player's wallet.")

        # Check if sufficient funds are available
        price = bonus["price"]
        balance = wallet[cryptocurrency]
        if balance < price:
            logging.error(f"Insufficient funds: Player '{self.user_id}' needs {price} {cryptocurrency} but has {balance}.")
            raise InsufficientFundsError(f"Insufficient funds: {price} {cryptocurrency} required.")

        # Deduct payment from wallet
        wallet[cryptocurrency] -= price
        logging.info(f"Player '{self.user_id}' purchased '{bonus_key}' using {price} {cryptocurrency}. New balance: {wallet[cryptocurrency]}")

        # Generate transaction ID
        transaction_id = uuid.uuid4()
        logging.info(f"Transaction ID for purchase: {transaction_id}")

        return {
            "message": f"Successfully purchased '{bonus_key}' using {price} {cryptocurrency}.",
            "bonus_description": bonus["description"],
            "remaining_balance": wallet[cryptocurrency],
            "transaction_id": str(transaction_id)
        }

# Example usage (mocked)
if __name__ == "__main__":
    # Initialize system for player1
    player_id = "player1"
    bonus_system = BonusPurchaseSystem(player_id)

    # Display available bonuses
    print("Available Bonuses:")
    for bonus_key, bonus_details in bonus_system.get_available_bonuses().items():
        print(f" - {bonus_key}: {bonus_details['description']} (Price: {bonus_details['price']} BTC)")

    # Purchase a bonus
    try:
        result = bonus_system.purchase_bonus("free_spins", "BTC")
        print("\nPurchase Confirmation:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except (ValueError, InsufficientFundsError) as e:
        print(f"Error: {e}")
```
