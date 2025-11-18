"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Generate an API endpoint for retrieving presale statistics, including total tokens sold, amount raised, and remaining tokens, as displayed on the GoodEgg presale page.
Generated: DETERMINISTIC_01cc1b9c0d0df920
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

# Mock data for presale statistics
presale_data = {
    "total_tokens": 1000000,  # Total tokens available for presale
    "tokens_sold": 450000,   # Tokens sold so far
    "token_price_usd": Decimal("0.50"),  # Price per token in USD
}

@app.route('/api/presale-stats', methods=['GET'])
def get_presale_stats():
    """
    API endpoint to retrieve presale statistics.
    
    Returns a JSON object containing:
    - total_tokens_sold: Total tokens sold during the presale
    - amount_raised_usd: Total amount raised during the presale
    - remaining_tokens: Tokens left for sale
    """
    try:
        # Calculate amount raised and remaining tokens
        tokens_sold = presale_data.get("tokens_sold", 0)
        token_price = presale_data.get("token_price_usd", Decimal("0.0"))
        total_tokens = presale_data.get("total_tokens", 0)
        
        # Ensure the data is valid
        if tokens_sold > total_tokens or tokens_sold < 0:
            raise ValueError("Invalid presale data: tokens_sold exceeds total_tokens or is negative.")
        
        # Perform calculations
        amount_raised_usd = tokens_sold * token_price
        remaining_tokens = total_tokens - tokens_sold

        # Return presale statistics as JSON
        return jsonify({
            "total_tokens_sold": tokens_sold,
            "amount_raised_usd": float(amount_raised_usd),  # Convert Decimal to float for JSON serialization
            "remaining_tokens": remaining_tokens
        }), 200
    except (ValueError, InvalidOperation) as e:
        # Handle calculation or data errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
