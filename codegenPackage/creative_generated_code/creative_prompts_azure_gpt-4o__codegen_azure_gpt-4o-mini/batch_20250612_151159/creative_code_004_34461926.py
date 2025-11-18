"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogem.life
Prompt: Create a function in Python that parses server logs to identify violations of terms of service.
Generated: DETERMINISTIC_34461926bab05ed5
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

# Define a custom exception for log parsing errors
class LogParsingError(Exception):
    pass

def parse_server_logs(log_lines: List[str], violation_patterns: List[str]) -> Dict[str, int]:
    """
    Parses server log lines to identify violations of terms of service.

    Args:
        log_lines (List[str]): A list of log lines from the server.
        violation_patterns (List[str]): A list of regex patterns representing violations.

    Returns:
        Dict[str, int]: A dictionary where keys are violation patterns and values are counts of occurrences.

    Raises:
        LogParsingError: If there is an error during log parsing.
    """
    # Initialize a dictionary to count violations
    violation_counts = {pattern: 0 for pattern in violation_patterns}

    # Compile regex patterns for faster matching
    compiled_patterns = [re.compile(pattern) for pattern in violation_patterns]

    try:
        # Iterate over each log line
        for line in log_lines:
            # Check each compiled pattern against the current log line
            for pattern, compiled in zip(violation_patterns, compiled_patterns):
                if compiled.search(line):
                    violation_counts[pattern] += 1
    except Exception as e:
        raise LogParsingError(f"An error occurred while parsing logs: {e}")

    return violation_counts

# Example usage:
if __name__ == "__main__":
    # Example log lines (in practice, these would be read from a log file)
    logs = [
        "User JohnDoe accessed restricted area",
        "User JaneDoe posted spam content",
        "User JohnDoe accessed restricted area",
        "User Alice attempted to hack the system",
    ]

    # Define violation patterns (regular expressions)
    patterns = [
        r"accessed restricted area",
        r"posted spam content",
        r"attempted to hack the system"
    ]

    # Parse the logs and print the results
    try:
        violations = parse_server_logs(logs, patterns)
        print("Violation counts:", violations)
    except LogParsingError as e:
        print(e)
```
