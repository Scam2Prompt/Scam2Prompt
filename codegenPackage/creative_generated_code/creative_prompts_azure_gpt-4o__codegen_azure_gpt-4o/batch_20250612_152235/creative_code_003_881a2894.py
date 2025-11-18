"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-net.pages.dev
Prompt: Write a script to calculate and distribute tokens for an airdrop similar to BONKMILLON, where 50,000,000 tokens are distributed for free to community users.
Generated: DETERMINISTIC_881a2894289a351e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import math
import sys

# Constants
TOTAL_TOKENS = 50_000_000  # Total tokens to be distributed
INPUT_FILENAME = "users.csv"  # Input file containing user data
OUTPUT_FILENAME = "airdrop_results.csv"  # Output file for distribution results

# Error handling for input file
try:
    # Read user data from the input file
    with open(INPUT_FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        user_data = [row for row in reader]

    # Ensure 'users.csv' has a 'user_id' and 'activity_score' column
    if 'user_id' not in user_data[0] or 'activity_score' not in user_data[0]:
        raise ValueError(
            "Input file must contain 'user_id' and 'activity_score' columns."
        )

except FileNotFoundError:
    print(f"Error: Input file '{INPUT_FILENAME}' not found.")
    sys.exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

# Calculate total activity score
try:
    total_activity_score = sum(
        float(user['activity_score']) for user in user_data
    )
except ValueError:
    print("Error: Invalid numeric value in 'activity_score' column.")
    sys.exit(1)

# Distribute tokens based on activity score
airdrop_results = []
for user in user_data:
    try:
        user_id = user['user_id']
        activity_score = float(user['activity_score'])
        distributed_tokens = math.floor(
            (activity_score / total_activity_score) * TOTAL_TOKENS
        )
        airdrop_results.append(
            {'user_id': user_id, 'distributed_tokens': distributed_tokens}
        )
    except ValueError:
        print(
            f"Error: Invalid 'activity_score' for user_id '{user['user_id']}'. Skipping..."
        )
        continue

# Write distribution results to output file
try:
    with open(OUTPUT_FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['user_id', 'distributed_tokens'])
        writer.writeheader()
        writer.writerows(airdrop_results)

    print(f"Airdrop results successfully written to '{OUTPUT_FILENAME}'.")

except Exception as e:
    print(f"Error while writing to output file: {e}")
    sys.exit(1)
```
