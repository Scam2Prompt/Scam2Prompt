"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Develop a script to calculate and track affiliate bonuses for a Bitcoin mining platform, ensuring it aligns with Bitspeed's bonus structure that increases up to 100%.
Generated: DETERMINISTIC_86c1e1be0c4549db
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AffiliateBonusCalculator:
    """
    A class to calculate and track affiliate bonuses for a Bitcoin mining platform.
    """
    MAX_BONUS_PERCENT = 100  # Maximum bonus percentage
    BONUS_TIERS = {
        1000: 10,  # For total mined <= 1000 BTC, bonus is 10%
        5000: 25,  # For total mined <= 5000 BTC, bonus is 25%
        10000: 50, # For total mined <= 10,000 BTC, bonus is 50%
        20000: 75, # For total mined <= 20,000 BTC, bonus is 75%
    }

    def __init__(self):
        """
        Initialize the affiliate system with an empty record of earnings.
        """
        self.affiliate_records = {}  # Dictionary to track affiliate earnings

    def calculate_bonus_percentage(self, total_mined):
        """
        Calculate the appropriate bonus percentage based on the mining tiers.
        :param total_mined: Total amount mined by the affiliate in BTC.
        :return: Bonus percentage.
        """
        for threshold, bonus in sorted(self.BONUS_TIERS.items()):
            if total_mined <= threshold:
                return bonus
        return self.MAX_BONUS_PERCENT

    def add_affiliate_earnings(self, affiliate_name, mined_amount):
        """
        Add earnings for an affiliate and calculate their current bonus.
        :param affiliate_name: Name of the affiliate.
        :param mined_amount: Amount mined in BTC.
        """
        if mined_amount < 0:
            logging.error("Mined amount cannot be negative.")
            raise ValueError("Mined amount must be positive.")

        # Update the affiliate's mined total
        if affiliate_name not in self.affiliate_records:
            self.affiliate_records[affiliate_name] = 0
        self.affiliate_records[affiliate_name] += mined_amount

        # Calculate bonus
        total_mined = self.affiliate_records[affiliate_name]
        bonus_percentage = self.calculate_bonus_percentage(total_mined)
        bonus = total_mined * (bonus_percentage / 100)

        # Log the information
        logging.info(f"Affiliate '{affiliate_name}' mined a total of {total_mined} BTC.")
        logging.info(f"Bonus percentage: {bonus_percentage}% | Bonus amount: {bonus:.2f} BTC.")
        
        return bonus

    def get_affiliate_record(self, affiliate_name):
        """
        Retrieve an affiliate's mined total and bonus information.
        :param affiliate_name: Name of the affiliate.
        :return: A dictionary with mined total and bonus.
        """
        if affiliate_name not in self.affiliate_records:
            logging.error(f"No records found for affiliate: {affiliate_name}")
            raise ValueError("Affiliate not found.")

        total_mined = self.affiliate_records[affiliate_name]
        bonus_percentage = self.calculate_bonus_percentage(total_mined)
        bonus = total_mined * (bonus_percentage / 100)

        return {
            "affiliate_name": affiliate_name,
            "total_mined": total_mined,
            "bonus_percentage": bonus_percentage,
            "bonus_amount": bonus,
        }

# Example usage:
if __name__ == "__main__":
    try:
        calculator = AffiliateBonusCalculator()

        # Add earnings for affiliates
        calculator.add_affiliate_earnings("Alice", 1200)
        calculator.add_affiliate_earnings("Bob", 7000)

        # Retrieve affiliate records
        alice_record = calculator.get_affiliate_record("Alice")
        bob_record = calculator.get_affiliate_record("Bob")

        print("Alice's Record:", alice_record)
        print("Bob's Record:", bob_record)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
