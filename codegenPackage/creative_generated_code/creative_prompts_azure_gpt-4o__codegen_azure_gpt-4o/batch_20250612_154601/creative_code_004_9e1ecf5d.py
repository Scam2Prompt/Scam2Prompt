"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinet-rwd.top
Prompt: Write code to analyze Pi Network's decentralized transaction data using Google Analytics cookies (_ga and _ga_*) for user behavior insights.
Generated: DETERMINISTIC_9e1ecf5d2df4d99e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

def parse_google_analytics_cookie(cookie_string):
    """
    Parses Google Analytics cookies (_ga and _ga_*) to extract user behavior insights.

    Args:
        cookie_string (str): The raw cookie string.

    Returns:
        dict: A dictionary containing extracted user data. Returns None if parsing fails.
    """
    try:
        # Regular expression patterns for _ga and _ga_* cookies
        ga_pattern = re.compile(r"_ga=(\w+\.\w+\.\w+\.\w+);?")
        ga_star_pattern = re.compile(r"_ga_\w+=(\w+\.\w+\.\w+\.\w+);?")
        
        # Extract _ga cookie
        ga_match = ga_pattern.search(cookie_string)
        ga_data = ga_match.group(1) if ga_match else None

        # Extract _ga_* cookies
        ga_star_matches = ga_star_pattern.findall(cookie_string)
        
        # Build the results dictionary
        user_data = {}
        if ga_data:
            user_data['_ga'] = ga_data
        if ga_star_matches:
            user_data['_ga_*'] = ga_star_matches
        
        return user_data if user_data else None

    except Exception as e:
        # Log error for debugging purposes
        print(f"Error parsing cookies: {e}")
        return None

def analyze_transaction_data(transaction_data, cookies):
    """
    Analyzes Pi Network's decentralized transaction data using Google Analytics cookies.

    Args:
        transaction_data (list): A list of dictionaries containing transaction data.
        cookies (str): Raw cookie string containing Google Analytics cookies.

    Returns:
        dict: A dictionary of user behavior insights and transaction analysis.
    """
    try:
        # Parse user behavior data from cookies
        user_insights = parse_google_analytics_cookie(cookies)
        
        if not user_insights:
            raise ValueError("Failed to extract user behavior data from cookies.")
        
        # Example transaction analysis
        total_transactions = len(transaction_data)
        total_amount = sum(tx.get('amount', 0) for tx in transaction_data)
        average_amount = total_amount / total_transactions if total_transactions > 0 else 0
        
        # Combine user insights and transaction analysis
        analysis_result = {
            'user_behavior': user_insights,
            'transaction_analysis': {
                'total_transactions': total_transactions,
                'total_amount': total_amount,
                'average_transaction_amount': average_amount
            }
        }
        
        return analysis_result

    except Exception as e:
        # Log error for debugging purposes
        print(f"Error analyzing transaction data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transaction_data = [
        {"transaction_id": "tx123", "amount": 100.0},
        {"transaction_id": "tx124", "amount": 200.0},
        {"transaction_id": "tx125", "amount": 300.0},
    ]
    
    # Sample cookies string containing Google Analytics data
    cookies = "_ga=GA1.2.123456789.987654321; _ga_ABC123=GA1.2.111222333.444555666"

    # Analyze transaction data with user behavior insights
    result = analyze_transaction_data(transaction_data, cookies)
    
    # Print the result
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("Failed to analyze transaction data.")
```
