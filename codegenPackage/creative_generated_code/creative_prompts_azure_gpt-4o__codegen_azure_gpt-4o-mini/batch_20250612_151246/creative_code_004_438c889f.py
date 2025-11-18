"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Create a script to automate the burning of unsold tokens every three months for three years, as described in Pushd's token burn program.
Generated: DETERMINISTIC_438c889f74c92871
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import schedule
from datetime import datetime, timedelta

class TokenBurnProgram:
    def __init__(self, burn_interval_months=3, total_years=3):
        """
        Initializes the TokenBurnProgram.

        Args:
            burn_interval_months (int): Interval in months to burn tokens.
            total_years (int): Total years to run the burning program.
        """
        self.burn_interval = timedelta(days=burn_interval_months * 30)  # Approximate monthly interval
        self.end_time = datetime.now() + timedelta(days=total_years * 365)  # Total duration of the program
        self.burn_schedule = []

    def schedule_burn(self):
        """
        Schedules the token burn at the defined intervals.
        """
        next_burn = datetime.now() + self.burn_interval
        while next_burn < self.end_time:
            self.burn_schedule.append(next_burn)
            next_burn += self.burn_interval

    def burn_tokens(self):
        """
        Simulates the burning of unsold tokens.

        Raises:
            RuntimeError: If burning process fails.
        """
        try:
            # Simulating the burning process
            print(f"Burning unsold tokens at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            # Here would be the logic to interact with the blockchain to burn tokens
            # For example: blockchain.burn_tokens(amount)
        except Exception as e:
            raise RuntimeError("Token burn process failed.") from e

    def run(self):
        """
        Starts the token burn process according to the scheduled times.
        """
        self.schedule_burn()
        for burn_time in self.burn_schedule:
            schedule.every().day.at(burn_time.strftime("%H:%M")).do(self.burn_tokens)
        
        while datetime.now() < self.end_time:
            schedule.run_pending()
            time.sleep(1)  # Sleep to prevent hammering the CPU

if __name__ == "__main__":
    # Entry point for the script
    try:
        token_burn_program = TokenBurnProgram()
        token_burn_program.run()
    except KeyboardInterrupt:
        print("Token burn program stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** This code assumes the use of a scheduling library `schedule` for timing tasks, and it simulates the token burn process with print statements. In a real-world scenario, you would replace the print statement with actual token burn logic interacting with the blockchain. Make sure to install the `schedule` library using pip if not already installed:

```bash
pip install schedule
```
