"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anamalika.com
Prompt: Develop an API endpoint that returns a list of the best natural oils for hair care, including زيت الثوم الاسود and زيت الارغان, as discussed on the webpage.
Generated: DETERMINISTIC_e2d0a16286aedefc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Define the list of natural oils for hair care
natural_oils = [
    {"name": "زيت الثوم الأسود", "benefits": "Promotes hair growth, nourishes scalp"},
    {"name": "زيت الأرجان", "benefits": "Moisturizes hair, reduces frizz, strengthens hair"}
]

@app.route('/api/hair-care-oils', methods=['GET'])
def get_hair_care_oils():
    """
    API Endpoint: /api/hair-care-oils
    Method: GET
    Description: Returns a list of the best natural oils for hair care.
    """
    try:
        # Return the list of oils as JSON
        return jsonify({"status": "success", "data": natural_oils}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
