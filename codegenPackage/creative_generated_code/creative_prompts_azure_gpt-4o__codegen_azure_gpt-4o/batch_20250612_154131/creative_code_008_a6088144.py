"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fivefootgaming.com
Prompt: Write Python code to analyze server logs from a LiteSpeed Web Server, such as the one hosting fivefootgaming.com, for gaming-related traffic patterns.
Generated: DETERMINISTIC_a6088144fada7ec3
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os
import sys
from collections import Counter

def analyze_server_logs(log_file_path):
    """
    Analyzes LiteSpeed server logs for gaming-related traffic patterns.

    Args:
        log_file_path (str): Path to the LiteSpeed server log file.

    Returns:
        dict: Dictionary containing analysis results.
    """
    # Define gaming-related patterns to look for in the logs
    gaming_patterns = [
        r'\bgame\b',  # Matches the word "game"
        r'\bgaming\b',  # Matches the word "gaming"
        r'\bplay\b',  # Matches the word "play"
        r'\bscore\b',  # Matches the word "score"
        r'\bwin\b'  # Matches the word "win"
    ]

    try:
        # Check if log file exists
        if not os.path.exists(log_file_path):
            raise FileNotFoundError(f"Log file not found: {log_file_path}")

        # Initialize counters for analysis
        total_lines = 0
        gaming_related_lines = 0
        gaming_word_frequency = Counter()

        # Open and read the log file line by line
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                total_lines += 1

                # Check if the line contains any gaming-related patterns
                if any(re.search(pattern, line, re.IGNORECASE) for pattern in gaming_patterns):
                    gaming_related_lines += 1

                    # Extract and count individual gaming-related words
                    for pattern in gaming_patterns:
                        matches = re.findall(pattern, line, re.IGNORECASE)
                        gaming_word_frequency.update(map(str.lower, matches))

        # Calculate the percentage of gaming-related lines
        gaming_percentage = (gaming_related_lines / total_lines) * 100 if total_lines > 0 else 0

        # Return analysis results as a dictionary
        return {
            "total_lines": total_lines,
            "gaming_related_lines": gaming_related_lines,
            "gaming_percentage": gaming_percentage,
            "gaming_word_frequency": dict(gaming_word_frequency)
        }

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    log_file = "litespeed_server.log"  # Replace with the actual path to your LiteSpeed server log file

    # Perform the analysis
    results = analyze_server_logs(log_file)

    # Display the results
    print("\n=== Server Log Analysis Results ===")
    print(f"Total Lines Processed: {results['total_lines']}")
    print(f"Gaming-Related Lines: {results['gaming_related_lines']}")
    print(f"Percentage of Gaming Traffic: {results['gaming_percentage']:.2f}%")
    print("Gaming Word Frequency:")
    for word, count in results['gaming_word_frequency'].items():
        print(f"  {word}: {count}")
```
