"""
Generated Code Metadata:
========================
Original URL: https://pad-chaingpt.pages.dev
Prompt: "Design a tokenomics model for a decentralized platform like ChainGPT Pad, including vesting schedules and token metrics."
Generated: DETERMINISTIC_c5a9bef8de16d787
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Model for a Decentralized Platform

class Tokenomics:
    def __init__(self, total_supply, initial_distribution, vesting_schedule):
        """
        Initialize the Tokenomics model.

        :param total_supply: Total supply of tokens
        :param initial_distribution: Dictionary with initial distribution percentages
        :param vesting_schedule: Dictionary with vesting periods and percentages
        """
        self.total_supply = total_supply
        self.initial_distribution = initial_distribution
        self.vesting_schedule = vesting_schedule
        self.distributed_tokens = {}
        self.vested_tokens = {}

        self._distribute_initial_tokens()
        self._initialize_vesting()

    def _distribute_initial_tokens(self):
        """Distribute initial tokens based on the initial distribution percentages."""
        try:
            for key, percentage in self.initial_distribution.items():
                if percentage < 0 or percentage > 100:
                    raise ValueError(f"Invalid percentage for {key}: {percentage}")
                tokens = (percentage / 100) * self.total_supply
                self.distributed_tokens[key] = tokens
        except Exception as e:
            print(f"Error in distributing initial tokens: {e}")

    def _initialize_vesting(self):
        """Initialize the vesting schedule."""
        try:
            for key, (duration, percentage) in self.vesting_schedule.items():
                if percentage < 0 or percentage > 100:
                    raise ValueError(f"Invalid vesting percentage for {key}: {percentage}")
                self.vested_tokens[key] = {
                    "duration": duration,
                    "total_vested": (percentage / 100) * self.total_supply,
                    "released": 0
                }
        except Exception as e:
            print(f"Error in initializing vesting schedule: {e}")

    def release_vested_tokens(self, key, time_passed):
        """
        Release vested tokens based on the time passed.

        :param key: The key for the vesting schedule
        :param time_passed: Time passed since the start of the vesting period
        :return: Amount of tokens released
        """
        try:
            if key not in self.vested_tokens:
                raise KeyError(f"No vesting schedule found for {key}")

            vesting_info = self.vested_tokens[key]
            duration = vesting_info["duration"]
            total_vested = vesting_info["total_vested"]

            if time_passed >= duration:
                vesting_info["released"] = total_vested
            else:
                vesting_info["released"] = (time_passed / duration) * total_vested

            return vesting_info["released"]
        except Exception as e:
            print(f"Error in releasing vested tokens: {e}")
            return 0

    def get_token_metrics(self):
        """
        Get the current token metrics.

        :return: Dictionary with token metrics
        """
        return {
            "total_supply": self.total_supply,
            "distributed_tokens": self.distributed_tokens,
            "vested_tokens": self.vested_tokens
        }


# Example usage
if __name__ == "__main__":
    total_supply = 1_000_000_000  # Total supply of tokens
    initial_distribution = {
        "team": 20,
        "investors": 30,
        "community": 25,
        "development": 15,
        "marketing": 10
    }
    vesting_schedule = {
        "team": (24, 20),  # 24 months vesting, 20% of total supply
        "investors": (12, 30),  # 12 months vesting, 30% of total supply
    }

    # Create Tokenomics instance
    tokenomics = Tokenomics(total_supply, initial_distribution, vesting_schedule)

    # Release vested tokens after 6 months for the team
    released_tokens = tokenomics.release_vested_tokens("team", 6)
    print(f"Released tokens for team after 6 months: {released_tokens}")

    # Get current token metrics
    metrics = tokenomics.get_token_metrics()
    print("Current Token Metrics:", metrics)
```
