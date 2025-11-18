"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moca.nexus.beta.coinlist.yachts
Prompt: Create a function to parse and categorize token launch data from MocaList, distinguishing between "live," "upcoming," and "test" launches.
Generated: DETERMINISTIC_6d24a802386562ce
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class TokenLaunch:
    def __init__(self, name: str, start_time: str, end_time: str, status: str):
        self.name = name
        self.start_time = self._parse_time(start_time)
        self.end_time = self._parse_time(end_time)
        self.status = status

    @staticmethod
    def _parse_time(time_str: str) -> datetime.datetime:
        """Parses a time string into a datetime object."""
        try:
            return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            raise ValueError(f"Invalid date format for '{time_str}': {e}")

def categorize_token_launches(launches: List[Dict[str, Any]]) -> Dict[str, List[TokenLaunch]]:
    """
    Categorizes token launches into 'live', 'upcoming', and 'test'.
    
    Args:
        launches (List[Dict[str, Any]]): A list of token launch dictionaries.

    Returns:
        Dict[str, List[TokenLaunch]]: A dictionary with categories as keys and lists of TokenLaunch objects as values.
    """
    categorized_launches = {
        'live': [],
        'upcoming': [],
        'test': []
    }
    
    current_time = datetime.datetime.now()

    for launch_data in launches:
        try:
            launch = TokenLaunch(
                name=launch_data['name'],
                start_time=launch_data['start_time'],
                end_time=launch_data['end_time'],
                status=launch_data['status']
            )
            
            if launch.status.lower() == 'test':
                categorized_launches['test'].append(launch)
            elif launch.start_time <= current_time <= launch.end_time:
                categorized_launches['live'].append(launch)
            elif launch.start_time > current_time:
                categorized_launches['upcoming'].append(launch)

        except KeyError as e:
            print(f"Missing expected key in launch data: {e}")
        except ValueError as e:
            print(f"Error processing launch '{launch_data.get('name', 'unknown')}': {e}")

    return categorized_launches

# Example usage:
if __name__ == "__main__":
    launch_data = [
        {'name': 'Token A', 'start_time': '2023-10-01 10:00:00', 'end_time': '2023-10-01 12:00:00', 'status': 'live'},
        {'name': 'Token B', 'start_time': '2023-10-05 10:00:00', 'end_time': '2023-10-05 12:00:00', 'status': 'upcoming'},
        {'name': 'Token C', 'start_time': '2023-10-01 08:00:00', 'end_time': '2023-10-01 09:00:00', 'status': 'test'},
    ]

    categorized = categorize_token_launches(launch_data)
    print(categorized)
```
