"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: Generate code to enable users to pay in fiat currency (e.g., USD) and automatically convert the payment to $SOPH tokens during the presale stage.
Generated: DETERMINISTIC_574ac3c80eb42eae
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class FiatToSophPaymentProcessor:
    """
    A class to handle fiat currency payments and convert them to SOPH tokens during the presale stage.
    """

    def __init__(self, soph_token_price_usd):
        """
        Initializes the payment processor.

        :param soph_token_price_usd: The current price of 1 SOPH token in USD.
        """
        self.soph_token_price_usd = soph_token_price_usd

    def get_conversion_rate(self):
        """
        Fetches the USD to SOPH conversion rate.

        :return: Conversion rate for SOPH tokens.
        """
        return self.soph_token_price_usd

    def process_payment(self, payment_amount_usd):
        """
        Processes fiat payment and converts it to SOPH tokens.

        :param payment_amount_usd: The fiat payment amount in USD.
        :return: The amount of SOPH tokens credited to the user.
        """
        try:
            conversion_rate = self.get_conversion_rate()
            soph_tokens = payment_amount_usd / conversion_rate
            return soph_tokens
        except ZeroDivisionError:
            raise ValueError("Conversion rate cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the payment: {str(e)}")

    def pay_and_credit_tokens(self, user_wallet_address, payment_amount_usd):
        """
        Handles the full payment process and credits SOPH tokens to the user's wallet.

        :param user_wallet_address: The user's wallet address to credit the tokens.
        :param payment_amount_usd: The fiat payment amount in USD.
        :return: Confirmation message with payment details.
        """
        try:
            # Convert fiat currency to SOPH tokens
            soph_tokens = self.process_payment(payment_amount_usd)

            # Simulate crediting tokens to the user's wallet
            self.credit_tokens_to_wallet(user_wallet_address, soph_tokens)

            return f"Payment successful! Credited {soph_tokens:.2f} SOPH tokens to wallet {user_wallet_address}."
        except ValueError as ve:
            return f"Payment failed: {str(ve)}"
        except RuntimeError as re:
            return f"Payment failed: {str(re)}"

    def credit_tokens_to_wallet(self, wallet_address, soph_tokens):
        """
        Simulates the process of crediting SOPH tokens to a user's wallet.

        :param wallet_address: The user's wallet address.
        :param soph_tokens: The amount of SOPH tokens to credit.
        """
        # Here you would integrate with a blockchain API or smart contract to transfer tokens.
        # For this example, we simply print a confirmation message.
        print(f"Crediting {soph_tokens:.2f} SOPH tokens to wallet {wallet_address}.")


# Example usage:
if __name__ == "__main__":
    # Initialize the payment processor with the presale SOPH token price (e.g., $0.5 per SOPH token)
    presale_token_price_usd = 0.5
    payment_processor = FiatToSophPaymentProcessor(presale_token_price_usd)

    # User details
    user_wallet = "0x123456789ABCDEF"
    payment_amount = 100.0  # $100 USD payment

    # Process user payment and credit tokens
    result = payment_processor.pay_and_credit_tokens(user_wallet, payment_amount)
    print(result)
```
