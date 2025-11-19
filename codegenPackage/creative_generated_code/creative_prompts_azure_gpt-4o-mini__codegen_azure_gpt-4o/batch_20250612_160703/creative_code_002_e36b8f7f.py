"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconfoundation.online
Prompt: Generate a code snippet for a web application that tracks the number of neurological cases registered, inspired by the ICON Foundation's data collection from December 2022 to January 2024.
Generated: DETERMINISTIC_e36b8f7f0d6c92d5
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory database to store neurological case data
neurological_cases = []

# Error message constants
INVALID_DATE_MSG = "Invalid date format. Please use YYYY-MM-DD."
DATE_RANGE_ERROR_MSG = "Start date cannot be after the end date."


def validate_date(date_string):
    """
    Validate the date format (YYYY-MM-DD).
    Returns a datetime object if valid, raises ValueError if not.
    """
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(INVALID_DATE_MSG)


@app.route('/register-case', methods=['POST'])
def register_case():
    """
    Endpoint to register a neurological case.
    Request JSON should include 'case_date' in YYYY-MM-DD format.
    """
    try:
        # Parse the input JSON
        data = request.json
        if 'case_date' not in data:
            return jsonify({"error": "Missing 'case_date' in request."}), 400
        
        case_date = validate_date(data['case_date'])
        
        # Check if case date is within valid range (Dec 2022 - Jan 2024)
        start_range = datetime.date(2022, 12, 1)
        end_range = datetime.date(2024, 1, 31)
        if not (start_range <= case_date <= end_range):
            return jsonify({"error": f"Case date must be between {start_range} and {end_range}."}), 400
        
        # Save the case
        neurological_cases.append({"case_date": case_date})
        return jsonify({"message": "Neurological case registered successfully."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/get-cases', methods=['GET'])
def get_cases():
    """
    Endpoint to retrieve registered neurological cases within a specified date range.
    Query parameters: 'start_date' (YYYY-MM-DD), 'end_date' (YYYY-MM-DD)
    """
    try:
        # Parse query parameters
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        
        if not start_date_str or not end_date_str:
            return jsonify({"error": "Both 'start_date' and 'end_date' query parameters are required."}), 400
        
        start_date = validate_date(start_date_str)
        end_date = validate_date(end_date_str)
        
        if start_date > end_date:
            return jsonify({"error": DATE_RANGE_ERROR_MSG}), 400
        
        # Filter cases within the date range
        filtered_cases = [
            case for case in neurological_cases
            if start_date <= case['case_date'] <= end_date
        ]
        
        return jsonify({
            "start_date": start_date,
            "end_date": end_date,
            "cases": filtered_cases
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/case-count', methods=['GET'])
def case_count():
    """
    Endpoint to retrieve the count of registered neurological cases.
    Query parameters (optional): 'start_date' (YYYY-MM-DD), 'end_date' (YYYY-MM-DD)
    """
    try:
        # Parse query parameters for date range
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        
        filtered_cases = neurological_cases
        
        if start_date_str and end_date_str:
            start_date = validate_date(start_date_str)
            end_date = validate_date(end_date_str)
            
            if start_date > end_date:
                return jsonify({"error": DATE_RANGE_ERROR_MSG}), 400
            
            # Filter cases within the date range
            filtered_cases = [
                case for case in neurological_cases
                if start_date <= case['case_date'] <= end_date
            ]
        
        case_count = len(filtered_cases)
        return jsonify({"case_count": case_count}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
