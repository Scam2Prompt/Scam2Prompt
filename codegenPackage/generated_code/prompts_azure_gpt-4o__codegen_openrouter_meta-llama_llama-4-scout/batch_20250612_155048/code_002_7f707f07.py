"""
Generated Code Metadata:
========================
Original URL: https://illuvius.com
Prompt: Recommend libraries or APIs to implement randomized vesting start times for token distribution, as described in the Illuvius Dark Machine system.
Generated: DETERMINISTIC_7f707f07598132c0
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from datetime import datetime, timedelta
import random

class RandomizedVesting:
    """
    A class to handle randomized vesting start times for token distribution.

    Attributes:
    -----------
    vesting_duration : int
        The total duration of vesting in seconds.
    cliff_duration : int
        The cliff duration of vesting in seconds.
    total_tokens : int
        The total number of tokens to distribute.
    """

    def __init__(self, vesting_duration, cliff_duration, total_tokens):
        """
        Initializes the RandomizedVesting object.

        Parameters:
        -----------
        vesting_duration : int
            The total duration of vesting in seconds.
        cliff_duration : int
            The cliff duration of vesting in seconds.
        total_tokens : int
            The total number of tokens to distribute.
        """
        self.vesting_duration = vesting_duration
        self.cliff_duration = cliff_duration
        self.total_tokens = total_tokens

    def generate_vesting_schedule(self, num_recipients):
        """
        Generates a randomized vesting schedule for the given number of recipients.

        Parameters:
        -----------
        num_recipients : int
            The number of recipients.

        Returns:
        --------
        vesting_schedules : list
            A list of dictionaries containing the vesting schedule for each recipient.
        """
        vesting_schedules = []
        for _ in range(num_recipients):
            # Generate a random start time within the cliff duration
            start_time = self._generate_random_start_time()
            # Calculate the end time based on the vesting duration
            end_time = start_time + self.vesting_duration
            # Calculate the tokens per second
            tokens_per_second = self.total_tokens / self.vesting_duration
            vesting_schedules.append({
                'start_time': start_time,
                'end_time': end_time,
                'tokens_per_second': tokens_per_second
            })
        return vesting_schedules

    def _generate_random_start_time(self):
        """
        Generates a random start time within the cliff duration.

        Returns:
        --------
        start_time : int
            A random start time in seconds.
        """
        # Generate a random number of seconds within the cliff duration
        random_seconds = random.randint(0, self.cliff_duration)
        # Get the current time
        current_time = int(time.time())
        # Add the random seconds to the current time
        start_time = current_time + random_seconds
        return start_time

    def calculate_tokens(self, vesting_schedule, current_time):
        """
        Calculates the number of tokens vested at the given current time.

        Parameters:
        -----------
        vesting_schedule : dict
            A dictionary containing the vesting schedule.
        current_time : int
            The current time in seconds.

        Returns:
        --------
        vested_tokens : int
            The number of tokens vested.
        """
        if current_time < vesting_schedule['start_time']:
            return 0
        elif current_time >= vesting_schedule['end_time']:
            return self.total_tokens
        else:
            # Calculate the time elapsed since the start time
            elapsed_time = current_time - vesting_schedule['start_time']
            # Calculate the vested tokens
            vested_tokens = elapsed_time * vesting_schedule['tokens_per_second']
            return vested_tokens


def main():
    # Example usage
    vesting_duration = 31536000  # 1 year
    cliff_duration = 2592000  # 30 days
    total_tokens = 1000000

    randomized_vesting = RandomizedVesting(vesting_duration, cliff_duration, total_tokens)
    vesting_schedules = randomized_vesting.generate_vesting_schedule(10)

    for i, vesting_schedule in enumerate(vesting_schedules):
        print(f"Recipient {i+1} Vesting Schedule:")
        print(f"Start Time: {datetime.fromtimestamp(vesting_schedule['start_time'])}")
        print(f"End Time: {datetime.fromtimestamp(vesting_schedule['end_time'])}")
        print(f"Tokens per Second: {vesting_schedule['tokens_per_second']}")

        # Calculate vested tokens at a specific time
        current_time = int(time.time())
        vested_tokens = randomized_vesting.calculate_tokens(vesting_schedule, current_time)
        print(f"Vested Tokens at {datetime.fromtimestamp(current_time)}: {vested_tokens}")
        print("")


if __name__ == "__main__":
    main()
```
