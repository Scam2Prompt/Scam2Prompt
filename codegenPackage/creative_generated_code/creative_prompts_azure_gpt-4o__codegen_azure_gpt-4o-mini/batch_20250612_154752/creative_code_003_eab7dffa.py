"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase2-blockdag-networks.pages.dev
Prompt: Create a referral tracking system in Python that calculates and displays the 10% bonus earned from referred investments in BDAG presale.
Generated: DETERMINISTIC_eab7dffa60cb210c
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralTrackingSystem:
    def __init__(self):
        """Initialize the referral tracking system with an empty referral list and a bonus rate."""
        self.referrals = {}
        self.bonus_rate = 0.10  # 10% bonus

    def add_referral(self, referrer: str, investment: float):
        """
        Add a referral and calculate the bonus earned.

        Args:
            referrer (str): The name of the person who made the referral.
            investment (float): The amount invested by the referred.

        Raises:
            ValueError: If the investment is not a positive number.
        """
        if investment <= 0:
            raise ValueError("Investment must be a positive number.")
        
        if referrer not in self.referrals:
            self.referrals[referrer] = 0.0
        
        # Calculate the bonus for the referral
        bonus = self.calculate_bonus(investment)
        self.referrals[referrer] += bonus

    def calculate_bonus(self, investment: float) -> float:
        """
        Calculate the bonus based on the investment amount.

        Args:
            investment (float): The amount invested.

        Returns:
            float: The calculated bonus.
        """
        return investment * self.bonus_rate

    def display_referral_bonuses(self):
        """Display the total bonuses earned by each referrer."""
        if not self.referrals:
            print("No referrals found.")
            return

        print("Referral Bonuses:")
        for referrer, bonus in self.referrals.items():
            print(f"{referrer}: ${bonus:.2f}")

    def reset_referrals(self):
        """Reset the referral system, clearing all referrals and bonuses."""
        self.referrals.clear()


if __name__ == "__main__":
    # Example usage of the ReferralTrackingSystem
    referral_system = ReferralTrackingSystem()

    try:
        referral_system.add_referral("Alice", 1000.00)
        referral_system.add_referral("Bob", 500.00)
        referral_system.add_referral("Alice", 2000.00)
        
        # Display the bonuses for each referrer
        referral_system.display_referral_bonuses()
    except ValueError as e:
        print(f"Error: {e}")
```
