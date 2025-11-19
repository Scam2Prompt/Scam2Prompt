"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinahotelcorfu.com
Prompt: Generate a booking system API that allows users to check availability for luxury deluxe rooms at Marina Boutique Hotel in Moraitika, Corfu.
Generated: DETERMINISTIC_9a1461df7229e7a3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample data representing room availability
# Structure: {"date": "YYYY-MM-DD", "available_rooms": int}
availability_data = [
    {"date": "2023-10-01", "available_rooms": 5},
    {"date": "2023-10-02", "available_rooms": 3},
    {"date": "2023-10-03", "available_rooms": 0},
    # Additional dates can be added here
]

@app.route('/check_availability', methods=['GET'])
def check_availability():
    """
    Endpoint to check availability for luxury deluxe rooms at Marina Boutique Hotel.
    Expects 'date' as a query parameter in the format 'YYYY-MM-DD'.
    Returns the number of available rooms and relevant information.
    """
    try:
        # Retrieve the date from query parameters
        date = request.args.get('date')
        if not date:
            return jsonify({"error": "Missing 'date' query parameter."}), 400
        
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'."}), 400
        
        # Search for availability on the requested date
        for record in availability_data:
            if record['date'] == date:
                return jsonify({
                    "date": date,
                    "available_rooms": record['available_rooms'],
                    "hotel_name": "Marina Boutique Hotel",
                    "location": "Moraitika, Corfu"
                }), 200
        
        # If no matching record is found, return 0 availability
        return jsonify({
            "date": date,
            "available_rooms": 0,
            "hotel_name": "Marina Boutique Hotel",
            "location": "Moraitika, Corfu"
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
