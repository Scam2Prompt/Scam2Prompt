"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-foundation.vercel.app
Prompt: Generate a script to calculate and display the percentage distribution of $ARB tokens to users and DAOs in the Arbitrum ecosystem.
Generated: DETERMINISTIC_7f518514ea89e43a
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from collections import defaultdict

def calculate_distribution(user_data, dao_data, total_tokens):
    """
    Calculate the percentage distribution of tokens to users and DAOs.
    
    Args:
        user_data (dict): Dictionary of user addresses and their token amounts.
        dao_data (dict): Dictionary of DAO addresses and their token amounts.
        total_tokens (int): Total number of tokens to be distributed.
    
    Returns:
        dict: Dictionary containing percentage distributions for users and DAOs.
    """
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than zero")
    
    # Calculate total allocated to users and DAOs
    user_total = sum(user_data.values())
    dao_total = sum(dao_data.values())
    
    # Calculate percentages
    user_percentage = (user_total / total_tokens) * 100
    dao_percentage = (dao_total / total_tokens) * 100
    
    # Calculate individual user percentages
    user_distribution = {
        address: (amount / user_total) * 100
        for address, amount in user_data.items()
    }
    
    # Calculate individual DAO percentages
    dao_distribution = {
        address: (amount / dao_total) * 100
        for address, amount in dao_data.items()
    }
    
    return {
        "overall_distribution": {
            "users": user_percentage,
            "daos": dao_percentage
        },
        "user_distribution": user_distribution,
        "dao_distribution": dao_distribution
    }

def load_data_from_file(filename):
    """
    Load distribution data from a JSON file.
    
    Args:
        filename (str): Path to JSON file containing distribution data.
    
    Returns:
        tuple: (user_data, dao_data, total_tokens)
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return (
                data.get("users", {}),
                data.get("daos", {}),
                data.get("total_tokens", 0)
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in input file")

def display_distribution(results):
    """
    Display the distribution results in a readable format.
    
    Args:
        results (dict): Distribution results from calculate_distribution.
    """
    print("\nARB Token Distribution Report")
    print("=" * 40)
    
    # Overall distribution
    overall = results["overall_distribution"]
    print(f"\nOverall Distribution:")
    print(f"- Users: {overall['users']:.2f}%")
    print(f"- DAOs: {overall['daos']:.2f}%")
    
    # User distribution
    print("\nUser Distribution:")
    for address, percentage in results["user_distribution"].items():
        print(f"- {address[:10]}...: {percentage:.4f}%")
    
    # DAO distribution
    print("\nDAO Distribution:")
    for address, percentage in results["dao_distribution"].items():
        print(f"- {address[:10]}...: {percentage:.4f}%")

def main():
    try:
        # Load data (replace with your actual data file)
        user_data, dao_data, total_tokens = load_data_from_file("distribution_data.json")
        
        # Calculate distribution
        distribution = calculate_distribution(user_data, dao_data, total_tokens)
        
        # Display results
        display_distribution(distribution)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
