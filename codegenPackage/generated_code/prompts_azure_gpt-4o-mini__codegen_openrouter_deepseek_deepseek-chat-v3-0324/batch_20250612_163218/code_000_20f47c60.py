"""
Generated Code Metadata:
========================
Original URL: https://aidsupport.rf.gd
Prompt: Generate a Python script that utilizes Node.js support for a web application hosted on iFastNet.
Generated: DETERMINISTIC_20f47c60d493fac8
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

def check_node_installed():
    """Check if Node.js is installed and available in the system path."""
    try:
        subprocess.run(["node", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def run_node_script(script_path, args=None):
    """
    Execute a Node.js script with optional arguments.
    
    Args:
        script_path (str): Path to the Node.js script.
        args (list, optional): List of arguments to pass to the script.
    
    Returns:
        tuple: (success: bool, output: str, error: str)
    """
    if not os.path.exists(script_path):
        return False, None, f"Script not found: {script_path}"
    
    try:
        command = ["node", script_path]
        if args:
            command.extend(args)
        
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        return True, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

@app.route('/run-node', methods=['POST'])
def handle_node_request():
    """
    Endpoint to execute a Node.js script.
    Expects JSON payload with 'script_path' and optional 'args'.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    script_path = data.get("script_path")
    args = data.get("args", [])
    
    if not script_path:
        return jsonify({"error": "Missing 'script_path'"}), 400
    
    success, output, error = run_node_script(script_path, args)
    
    if not success:
        return jsonify({"error": error}), 500
    
    return jsonify({"output": output})

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    node_installed = check_node_installed()
    return jsonify({
        "status": "healthy",
        "node_installed": node_installed
    })

if __name__ == '__main__':
    if not check_node_installed():
        print("Error: Node.js is not installed or not in the system path.")
        sys.exit(1)
    
    app.run(host='0.0.0.0', port=5000)
```
