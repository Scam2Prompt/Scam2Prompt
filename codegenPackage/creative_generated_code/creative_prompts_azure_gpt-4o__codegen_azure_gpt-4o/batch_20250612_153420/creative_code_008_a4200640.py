"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nfp-erq.pages.dev
Prompt: Develop a tool to track and display the timeline for claiming $NFP airdrops, including pre-launch and post-launch phases.
Generated: DETERMINISTIC_a42006401290e3ea
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class AirdropTracker:
    """
    AirdropTracker Class to track and display a timeline for claiming NFP airdrops
    during pre-launch and post-launch phases.
    """

    def __init__(self, pre_launch_start: datetime.datetime, pre_launch_end: datetime.datetime, post_launch_start: datetime.datetime, post_launch_end: datetime.datetime):
        """
        Initialize the AirdropTracker with timeline details.

        :param pre_launch_start: Start date and time for the pre-launch phase
        :param pre_launch_end: End date and time for the pre-launch phase
        :param post_launch_start: Start date and time for the post-launch phase
        :param post_launch_end: End date and time for the post-launch phase
        """
        self.pre_launch_start = pre_launch_start
        self.pre_launch_end = pre_launch_end
        self.post_launch_start = post_launch_start
        self.post_launch_end = post_launch_end

        # Validate timelines
        self._validate_timelines()

    def _validate_timelines(self) -> None:
        """
        Validates the timeline details to ensure consistency and correctness.
        """
        if self.pre_launch_start >= self.pre_launch_end:
            raise ValueError("Pre-launch start date must be earlier than end date.")
        
        if self.post_launch_start >= self.post_launch_end:
            raise ValueError("Post-launch start date must be earlier than end date.")
        
        if self.pre_launch_end > self.post_launch_start:
            raise ValueError("Pre-launch end date must be before post-launch start date.")

    def get_timeline(self) -> List[Dict[str, str]]:
        """
        Returns the timeline for the airdrop phases.

        :return: A list of dictionaries containing phase details.
        """
        return [
            {
                "phase": "Pre-launch",
                "start": self.pre_launch_start.strftime('%Y-%m-%d %H:%M:%S'),
                "end": self.pre_launch_end.strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                "phase": "Post-launch",
                "start": self.post_launch_start.strftime('%Y-%m-%d %H:%M:%S'),
                "end": self.post_launch_end.strftime('%Y-%m-%d %H:%M:%S')
            }
        ]

    def is_claimable(self, current_time: datetime.datetime) -> str:
        """
        Checks if the airdrop is claimable based on the current time.

        :param current_time: Current date and time
        :return: Status message indicating claimability
        """
        if self.pre_launch_start <= current_time <= self.pre_launch_end:
            return "Airdrop is claimable during the pre-launch phase."
        elif self.post_launch_start <= current_time <= self.post_launch_end:
            return "Airdrop is claimable during the post-launch phase."
        else:
            return "Airdrop is not claimable at this time."

# Example usage (should be wrapped with proper input and exception handling in production):
if __name__ == "__main__":
    try:
        # Define airdrop timeline
        pre_launch_start = datetime.datetime(2023, 11, 1, 10, 0, 0)
        pre_launch_end = datetime.datetime(2023, 11, 10, 18, 0, 0)
        post_launch_start = datetime.datetime(2023, 11, 20, 9, 0, 0)
        post_launch_end = datetime.datetime(2023, 11, 30, 23, 59, 59)
        
        # Initialize tracker
        tracker = AirdropTracker(pre_launch_start, pre_launch_end, post_launch_start, post_launch_end)

        # Display timeline
        print("Airdrop Timeline:")
        for phase in tracker.get_timeline():
            print(f"Phase: {phase['phase']}, Start: {phase['start']}, End: {phase['end']}")

        # Check claim status (using current time)
        current_time = datetime.datetime.now()
        print("\nClaim Status:")
        print(tracker.is_claimable(current_time))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
