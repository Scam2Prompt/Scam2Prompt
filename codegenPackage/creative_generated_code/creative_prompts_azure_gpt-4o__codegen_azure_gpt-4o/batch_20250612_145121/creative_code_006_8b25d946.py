"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Generate code to display the token metrics and roadmap of a project launched on ChainGPT Pad, including dynamic updates for the swap and claim periods.
Generated: DETERMINISTIC_8b25d946bcba365d
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import time

class ProjectMetrics:
    """
    Class to manage token metrics and dynamic roadmap updates for a project launched on ChainGPT Pad.
    """

    def __init__(self, project_name, token_metrics, roadmap):
        """
        Initializes the ProjectMetrics object.

        :param project_name: Name of the project
        :param token_metrics: Dictionary containing token metrics (e.g., price, supply)
        :param roadmap: Dictionary containing roadmap milestones and deadlines
        """
        self.project_name = project_name
        self.token_metrics = token_metrics
        self.roadmap = roadmap
        self.swap_period_start = None   # Start time for swap period
        self.swap_period_end = None     # End time for swap period
        self.claim_period_start = None  # Start time for claim period
        self.claim_period_end = None    # End time for claim period

    def set_periods(self, swap_start, swap_end, claim_start, claim_end):
        """
        Sets the swap and claim periods.

        :param swap_start: Start time for the swap period (datetime object)
        :param swap_end: End time for the swap period (datetime object)
        :param claim_start: Start time for the claim period (datetime object)
        :param claim_end: End time for the claim period (datetime object)
        """
        self.swap_period_start = swap_start
        self.swap_period_end = swap_end
        self.claim_period_start = claim_start
        self.claim_period_end = claim_end

    def display_metrics(self):
        """
        Display the token metrics for the project.
        """
        print(f"Project: {self.project_name}")
        print("Token Metrics:")
        for key, value in self.token_metrics.items():
            print(f"  {key}: {value}")

    def display_roadmap(self):
        """
        Display the roadmap milestones and deadlines for the project.
        """
        print(f"\nRoadmap for {self.project_name}:")
        for milestone, deadline in self.roadmap.items():
            print(f"  {milestone}: {deadline}")

    def monitor_periods(self):
        """
        Dynamically updates the status of swap and claim periods and displays them.
        """
        while True:
            now = datetime.datetime.now()
            print("\nCurrent Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

            if self.swap_period_start and self.swap_period_end:
                if self.swap_period_start <= now <= self.swap_period_end:
                    print("Swap Period: ACTIVE")
                elif now < self.swap_period_start:
                    print("Swap Period: UPCOMING")
                else:
                    print("Swap Period: ENDED")
            else:
                print("Swap Period: NOT SET")

            if self.claim_period_start and self.claim_period_end:
                if self.claim_period_start <= now <= self.claim_period_end:
                    print("Claim Period: ACTIVE")
                elif now < self.claim_period_start:
                    print("Claim Period: UPCOMING")
                else:
                    print("Claim Period: ENDED")
            else:
                print("Claim Period: NOT SET")

            # Refresh every 30 seconds
            time.sleep(30)


# Example Usage
if __name__ == "__main__":
    token_metrics = {
        "Token Price": "$0.05",
        "Total Supply": "1,000,000",
        "Circulating Supply": "500,000",
    }

    roadmap = {
        "Launch on ChainGPT Pad": "2023-10-01",
        "Token Distribution": "2023-10-15",
        "Mainnet Deployment": "2023-12-01",
    }

    project = ProjectMetrics(project_name="ChainGPTToken", token_metrics=token_metrics, roadmap=roadmap)

    # Set dynamic swap and claim periods
    swap_start = datetime.datetime(2023, 10, 1, 10, 0, 0)
    swap_end = datetime.datetime(2023, 10, 15, 18, 0, 0)
    claim_start = datetime.datetime(2023, 10, 16, 10, 0, 0)
    claim_end = datetime.datetime(2023, 10, 30, 18, 0, 0)
    
    project.set_periods(swap_start, swap_end, claim_start, claim_end)

    # Display token metrics and roadmap
    project.display_metrics()
    project.display_roadmap()

    # Start monitoring periods
    project.monitor_periods()
```
