"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordifypro.pages.dev
Prompt: Develop a script to calculate vesting schedules for tokens allocated in Ordify's seed, private, and community rounds based on the provided vesting dynamics.
Generated: DETERMINISTIC_2976ff2cd5129213
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class VestingSchedule:
    """
    Class to calculate token vesting schedules for various allocation rounds.
    """

    def __init__(self, total_tokens, cliff_months, vesting_months, round_name):
        """
        Initialize the vesting schedule parameters.

        :param total_tokens: Total tokens allocated for this round.
        :param cliff_months: Number of months before vesting starts.
        :param vesting_months: Number of months over which tokens vest after the cliff.
        :param round_name: Name of the allocation round (e.g., Seed, Private, Community).
        """
        self.total_tokens = total_tokens
        self.cliff_months = cliff_months
        self.vesting_months = vesting_months
        self.round_name = round_name
        self.start_date = datetime.date.today()
        self.schedule = []

    def calculate_schedule(self):
        """
        Calculate the vesting schedule based on the cliff and vesting months.

        :return: List of vesting amounts and dates.
        """
        try:
            # After the cliff period, calculate monthly vested tokens
            monthly_vesting = self.total_tokens / self.vesting_months
            vesting_start_date = self.start_date + datetime.timedelta(days=self.cliff_months * 30)

            for month in range(self.vesting_months):
                vesting_date = vesting_start_date + datetime.timedelta(days=month * 30)
                vested_amount = monthly_vesting
                self.schedule.append({
                    "round_name": self.round_name,
                    "date": vesting_date,
                    "amount": round(vested_amount, 2)
                })

            return self.schedule
        except Exception as e:
            print(f"Error calculating vesting schedule: {e}")
            return None

    def display_schedule(self):
        """
        Print the calculated vesting schedule.
        """
        if not self.schedule:
            print(f"No schedule calculated for {self.round_name}.")
            return

        print(f"\nVesting Schedule for {self.round_name} Round:")
        print("Date\t\t\tVested Amount")
        print("---------------------------------")
        for entry in self.schedule:
            print(f"{entry['date']}\t{entry['amount']}")


def main():
    """
    Main function to initialize vesting schedule instances and calculate/display schedules.
    """
    try:
        # Example input for different token allocation rounds
        seed_round = VestingSchedule(total_tokens=1000000, cliff_months=6, vesting_months=12, round_name="Seed")
        private_round = VestingSchedule(total_tokens=2000000, cliff_months=3, vesting_months=18, round_name="Private")
        community_round = VestingSchedule(total_tokens=500000, cliff_months=1, vesting_months=6, round_name="Community")

        # Calculate schedules
        seed_round.calculate_schedule()
        private_round.calculate_schedule()
        community_round.calculate_schedule()

        # Display schedules
        seed_round.display_schedule()
        private_round.display_schedule()
        community_round.display_schedule()
    except Exception as e:
        print(f"Error in main execution: {e}")


if __name__ == "__main__":
    main()
```
