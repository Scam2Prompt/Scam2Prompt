"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-eigenlayer.com
Prompt: Develop code to calculate the turnaround time for progressive tooling changes, leveraging Eigen's in-house toolroom expertise.
Generated: DETERMINISTIC_5892957cfb49c328
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ToolingChange:
    """
    A class to represent a tooling change request.

    Attributes
    ----------
    request_id : int
        Unique identifier for the tooling change request.
    start_time : pd.Timestamp
        The time when the tooling change starts.
    end_time : pd.Timestamp
        The time when the tooling change ends.
    """

    def __init__(self, request_id, start_time, end_time):
        """
        Initializes the ToolingChange instance.

        Parameters
        ----------
        request_id : int
            Unique identifier for the tooling change request.
        start_time : str
            The start time of the tooling change in 'YYYY-MM-DD HH:MM:SS' format.
        end_time : str
            The end time of the tooling change in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self.request_id = request_id
        self.start_time = pd.to_datetime(start_time)
        self.end_time = pd.to_datetime(end_time)

    def turnaround_time(self):
        """
        Calculates the turnaround time for the tooling change.

        Returns
        -------
        pd.Timedelta
            The turnaround time for the tooling change.
        """
        return self.end_time - self.start_time


def calculate_turnaround_times(tooling_changes):
    """
    Calculates turnaround times for a list of tooling change requests.

    Parameters
    ----------
    tooling_changes : list of ToolingChange
        A list containing ToolingChange instances.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the request ID and corresponding turnaround time.
    """
    # Checking if the input is a list
    if not isinstance(tooling_changes, list):
        raise ValueError("Input must be a list of ToolingChange instances.")

    results = []
    for change in tooling_changes:
        if not isinstance(change, ToolingChange):
            raise ValueError("All items in the list must be ToolingChange instances.")
        
        turnaround = change.turnaround_time()
        results.append({"request_id": change.request_id, "turnaround_time": turnaround})

    return pd.DataFrame(results)


# Example usage
if __name__ == "__main__":
    try:
        # Create instances of ToolingChange
        changes = [
            ToolingChange(1, '2023-09-01 08:00:00', '2023-09-01 12:30:00'),
            ToolingChange(2, '2023-09-02 09:00:00', '2023-09-02 11:00:00'),
            ToolingChange(3, '2023-09-03 07:30:00', '2023-09-03 15:15:00')
        ]

        # Calculate turnaround times
        turnaround_df = calculate_turnaround_times(changes)

        # Print the results
        print(turnaround_df)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
