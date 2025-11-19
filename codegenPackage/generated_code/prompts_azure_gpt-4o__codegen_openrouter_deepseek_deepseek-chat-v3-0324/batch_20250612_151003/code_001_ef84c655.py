"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Generate code to calculate the total voting power percentage for each Clearpool oracle based on the provided CPOOL staking data.
Generated: DETERMINISTIC_ef84c655d9a4712d
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict

def calculate_voting_power(staking_data):
    """
    Calculate the total voting power percentage for each Clearpool oracle based on CPOOL staking data.
    
    Args:
        staking_data (list): List of dictionaries containing staking data for each oracle.
                            Each dictionary should have 'oracle_address' and 'staked_amount' keys.
    
    Returns:
        dict: A dictionary with oracle addresses as keys and their voting power percentages as values.
    """
    if not staking_data:
        raise ValueError("Staking data cannot be empty")
    
    total_staked = 0
    oracle_stakes = defaultdict(int)
    
    # Calculate total staked amount and individual oracle stakes
    for entry in staking_data:
        if not isinstance(entry, dict):
            raise ValueError("Each staking data entry must be a dictionary")
        
        if 'oracle_address' not in entry or 'staked_amount' not in entry:
            raise ValueError("Each staking data entry must contain 'oracle_address' and 'staked_amount'")
        
        try:
            staked_amount = float(entry['staked_amount'])
        except (ValueError, TypeError):
            raise ValueError("Staked amount must be a numeric value")
        
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative")
        
        oracle_address = entry['oracle_address']
        oracle_stakes[oracle_address] += staked_amount
        total_staked += staked_amount
    
    if total_staked <= 0:
        raise ValueError("Total staked amount must be greater than zero")
    
    # Calculate voting power percentages
    voting_power = {}
    for oracle, stake in oracle_stakes.items():
        voting_power[oracle] = (stake / total_staked) * 100
    
    return voting_power

def load_staking_data_from_file(file_path):
    """
    Load staking data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing staking data.
    
    Returns:
        list: List of staking data entries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Invalid data format: expected a list of staking entries")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the input file")

def main():
    try:
        # Example usage
        staking_data = [
            {"oracle_address": "0x123...", "staked_amount": "1000"},
            {"oracle_address": "0x456...", "staked_amount": "2000"},
            {"oracle_address": "0x123...", "staked_amount": "500"},
            {"oracle_address": "0x789...", "staked_amount": "2500"}
        ]
        
        voting_power = calculate_voting_power(staking_data)
        print("Voting Power Percentages:")
        for oracle, percentage in voting_power.items():
            print(f"{oracle}: {percentage:.2f}%")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
