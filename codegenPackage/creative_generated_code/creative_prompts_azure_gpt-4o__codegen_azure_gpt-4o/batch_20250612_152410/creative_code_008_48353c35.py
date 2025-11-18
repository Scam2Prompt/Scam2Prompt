"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://judgeai.web.app
Prompt: Generate code to integrate Judge AI's reporting and plugin features into a user-friendly interface for crypto contract security analysis.
Generated: DETERMINISTIC_48353c35cac43a09
Batch ID: 20250612_152410
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.judge-ai.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import requests
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configuration for Judge AI API
JUDGE_AI_API_BASE_URL = "https://api.judge-ai.com"
JUDGE_AI_API_KEY = "your_api_key_here"  # Replace with your actual API key

# Error-response helper function
def error_response(message, status_code=400):
    return jsonify({"success": False, "error": message}), status_code

# Endpoint to analyze crypto contract
@app.route('/analyze_contract', methods=['POST'])
def analyze_contract():
    try:
        # Extract contract data from the request
        contract_data = request.json.get("contract_data", None)
        if not contract_data:
            return error_response("Missing 'contract_data' in request.")
        
        # Call Judge AI's reporting feature for security analysis
        response = requests.post(
            f"{JUDGE_AI_API_BASE_URL}/report",
            headers={"Authorization": f"Bearer {JUDGE_AI_API_KEY}"},
            json={"contract": contract_data}
        )
        
        # Handle response errors
        if response.status_code != 200:
            return error_response(f"Judge AI API error: {response.json().get('error', 'Unknown error')}", response.status_code)
        
        # Parse and return the analysis result
        analysis_result = response.json()
        return jsonify({"success": True, "analysis": analysis_result})
    
    except Exception as e:
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

# Endpoint to integrate Judge AI plugins
@app.route('/integrate_plugin', methods=['POST'])
def integrate_plugin():
    try:
        # Extract plugin details from the request
        plugin_name = request.json.get("plugin_name", None)
        plugin_config = request.json.get("plugin_config", None)
        if not plugin_name or not plugin_config:
            return error_response("Missing 'plugin_name' or 'plugin_config' in request.")
        
        # Call Judge AI's plugin integration feature
        response = requests.post(
            f"{JUDGE_AI_API_BASE_URL}/plugins/integrate",
            headers={"Authorization": f"Bearer {JUDGE_AI_API_KEY}"},
            json={"plugin_name": plugin_name, "plugin_config": plugin_config}
        )
        
        # Handle response errors
        if response.status_code != 200:
            return error_response(f"Judge AI API error: {response.json().get('error', 'Unknown error')}", response.status_code)
        
        # Parse and return the plugin integration result
        integration_result = response.json()
        return jsonify({"success": True, "integration": integration_result})
    
    except Exception as e:
        return error_response(f"An unexpected error occurred: {str(e)}", 500)

# Main application entry point
if __name__ == '__main__':
    # Start the Flask server
    app.run(host='0.0.0.0', port=5000, debug=False)
```
