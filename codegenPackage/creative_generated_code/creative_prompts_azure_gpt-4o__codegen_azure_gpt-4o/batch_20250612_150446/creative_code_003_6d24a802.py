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

def categorize_token_launches(token_data):
    """
    Parses and categorizes token launch data into "live," "upcoming," and "test" categories.

    Args:
        token_data (list of dict): List of token launch details, 
                                   where each dict includes 'name', 'launch_date', and 'type'.
                                   Example: [{'name': 'Token A', 'launch_date': '2023-10-12', 'type': 'live'}, ...]

    Returns:
        dict: Categorized token launches with keys "live", "upcoming", and "test".
              Example: {'live': [...], 'upcoming': [...], 'test': [...]}
    """
    # Initialize categories
    categorized_data = {
        "live": [],
        "upcoming": [],
        "test": []
    }

    # Get the current date for comparison
    current_date = datetime.datetime.now().date()

    # Validate and process each token entry
    for token in token_data:
        try:
            # Extract and validate required fields
            name = token.get('name', '').strip()
            launch_date_str = token.get('launch_date', '').strip()
            token_type = token.get('type', '').strip().lower()

            # Ensure all required fields are present
            if not name or not launch_date_str or not token_type:
                raise ValueError(f"Missing required fields in token data: {token}")

            # Parse the launch_date
            launch_date = datetime.datetime.strptime(launch_date_str, '%Y-%m-%d').date()

            # Categorize based on token type and launch_date
            if token_type == "live":
                categorized_data["live"].append(token)
            elif token_type == "upcoming" and launch_date > current_date:
                categorized_data["upcoming"].append(token)
            elif token_type == "test":
                categorized_data["test"].append(token)
            else:
                # Handle invalid type or date mismatch
                raise ValueError(f"Invalid token type or launch date mismatch for token: {token}")

        except Exception as e:
            # Log or handle errors (in production, consider logging to a file or monitoring system)
            print(f"Error processing token data: {e}")

    return categorized_data


# Example usage:
if __name__ == "__main__":
    # Sample token launch data
    token_data = [
        {"name": "Token A", "launch_date": "2023-10-12", "type": "live"},
        {"name": "Token B", "launch_date": "2023-11-01", "type": "upcoming"},
        {"name": "Token C", "launch_date": "2023-09-30", "type": "test"},
        {"name": "Token D", "launch_date": "", "type": "live"},  # Invalid entry
    ]

    # Categorize tokens
    categorized_tokens = categorize_token_launches(token_data)

    # Display categorized data
    print("Categorized Token Launches:")
    for category, tokens in categorized_tokens.items():
        print(f"{category.capitalize()}: {tokens}")
```
