"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: "How can I balance work and networking time in a coworking space, according to NetCoworking's advice on agenda optimization?"
Generated: DETERMINISTIC_bc92a9272eb2b17e
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class TimeBlock:
    """Represents a block of time in the agenda."""
    start_time: str
    end_time: str
    activity: str

class NetCoworkingAgendaOptimizer:
    """Provides advice on optimizing agendas for coworking spaces."""

    def __init__(self, work_time_blocks: List[TimeBlock], networking_time_blocks: List[TimeBlock]):
        """
        Initializes the optimizer with work and networking time blocks.

        Args:
        work_time_blocks (List[TimeBlock]): Time blocks for work activities.
        networking_time_blocks (List[TimeBlock]): Time blocks for networking activities.
        """
        self.work_time_blocks = work_time_blocks
        self.networking_time_blocks = networking_time_blocks

    def balance_agenda(self) -> Dict[str, str]:
        """
        Balances work and networking time in a coworking space.

        Returns:
        Dict[str, str]: A dictionary with advice on balancing work and networking time.
        """
        # Calculate total work and networking time
        total_work_time = self._calculate_total_time(self.work_time_blocks)
        total_networking_time = self._calculate_total_time(self.networking_time_blocks)

        # Check if there's enough time for both work and networking
        if total_work_time + total_networking_time > 24 * 60:  # 24 hours in minutes
            raise ValueError("Not enough time for both work and networking")

        # Provide advice on balancing work and networking time
        advice = {}
        if total_work_time > total_networking_time:
            advice["Tip"] = "Consider adding more networking time blocks."
        elif total_work_time < total_networking_time:
            advice["Tip"] = "Consider adding more work time blocks."
        else:
            advice["Tip"] = "Your agenda is balanced."

        # Suggest time blocks for breaks
        break_time_blocks = self._suggest_break_time_blocks(self.work_time_blocks, self.networking_time_blocks)
        advice["Break Time Blocks"] = self._format_time_blocks(break_time_blocks)

        return advice

    def _calculate_total_time(self, time_blocks: List[TimeBlock]) -> int:
        """
        Calculates the total time in minutes from a list of time blocks.

        Args:
        time_blocks (List[TimeBlock]): Time blocks.

        Returns:
        int: Total time in minutes.
        """
        total_time = 0
        for time_block in time_blocks:
            start_hour, start_minute = map(int, time_block.start_time.split(":"))
            end_hour, end_minute = map(int, time_block.end_time.split(":"))
            time_in_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)
            total_time += time_in_minutes
        return total_time

    def _suggest_break_time_blocks(self, work_time_blocks: List[TimeBlock], networking_time_blocks: List[TimeBlock]) -> List[TimeBlock]:
        """
        Suggests time blocks for breaks.

        Args:
        work_time_blocks (List[TimeBlock]): Time blocks for work activities.
        networking_time_blocks (List[TimeBlock]): Time blocks for networking activities.

        Returns:
        List[TimeBlock]: Suggested time blocks for breaks.
        """
        # Suggest breaks every 2 hours
        break_time_blocks = []
        all_time_blocks = work_time_blocks + networking_time_blocks
        all_time_blocks.sort(key=lambda x: x.start_time)

        for i in range(len(all_time_blocks) - 1):
            current_end_time = all_time_blocks[i].end_time
            next_start_time = all_time_blocks[i + 1].start_time
            current_end_hour, current_end_minute = map(int, current_end_time.split(":"))
            next_start_hour, next_start_minute = map(int, next_start_time.split(":"))
            time_diff_in_minutes = (next_start_hour - current_end_hour) * 60 + (next_start_minute - current_end_minute)

            if time_diff_in_minutes >= 120:  # 2 hours in minutes
                break_start_time = f"{current_end_hour}:{current_end_minute + 15}"  # 15-minute break
                break_end_time = f"{next_start_hour}:{next_start_minute - 15}"  # 15-minute break
                break_time_blocks.append(TimeBlock(break_start_time, break_end_time, "Break"))

        return break_time_blocks

    def _format_time_blocks(self, time_blocks: List[TimeBlock]) -> str:
        """
        Formats time blocks as a string.

        Args:
        time_blocks (List[TimeBlock]): Time blocks.

        Returns:
        str: Formatted string.
        """
        formatted_time_blocks = []
        for time_block in time_blocks:
            formatted_time_blocks.append(f"{time_block.start_time} - {time_block.end_time}: {time_block.activity}")
        return "\n".join(formatted_time_blocks)


def main():
    # Example usage
    work_time_blocks = [
        TimeBlock("08:00", "12:00", "Work"),
        TimeBlock("13:00", "17:00", "Work")
    ]

    networking_time_blocks = [
        TimeBlock("12:00", "13:00", "Networking Lunch"),
        TimeBlock("17:00", "18:00", "Networking")
    ]

    optimizer = NetCoworkingAgendaOptimizer(work_time_blocks, networking_time_blocks)
    advice = optimizer.balance_agenda()
    print(advice["Tip"])
    print(advice["Break Time Blocks"])


if __name__ == "__main__":
    main()
```
