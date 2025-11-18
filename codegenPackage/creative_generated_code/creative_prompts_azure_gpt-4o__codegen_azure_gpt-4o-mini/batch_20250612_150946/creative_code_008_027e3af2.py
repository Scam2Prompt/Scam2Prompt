"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carreiras.oportunidadesevagas.com
Prompt: Recommend a library or framework for building a financial calculator tool inspired by the "Investimentos Inteligentes Potencializa as Finanças da sua Empresa" section, and provide a code example.
Generated: DETERMINISTIC_027e3af2e245f201
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Define a simple financial calculator for investment returns
class FinancialCalculator:
    @staticmethod
    def calculate_investment_return(principal, rate, time):
        """
        Calculate the future value of an investment.

        Parameters:
        principal (float): The initial amount of money invested.
        rate (float): The annual interest rate (as a decimal).
        time (float): The time in years the money is invested for.

        Returns:
        float: The future value of the investment.
        """
        try:
            # Future Value formula: FV = P * (1 + r)^t
            future_value = principal * (1 + rate) ** time
            return future_value
        except Exception as e:
            print(f"Error calculating investment return: {e}")
            return None

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    API endpoint to calculate investment returns.
    Expects JSON payload with 'principal', 'rate', and 'time' fields.
    """
    try:
        data = request.get_json()
        principal = float(data.get('principal'))
        rate = float(data.get('rate'))
        time = float(data.get('time'))

        # Calculate the future value using the FinancialCalculator
        future_value = FinancialCalculator.calculate_investment_return(principal, rate, time)

        if future_value is not None:
            return jsonify({"future_value": future_value}), 200
        else:
            return jsonify({"error": "Calculation error"}), 500

    except ValueError as ve:
        return jsonify({"error": f"Invalid input: {ve}"}), 400
    except Exception as e:
        return jsonify({"error": f"Server error: {e}"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
