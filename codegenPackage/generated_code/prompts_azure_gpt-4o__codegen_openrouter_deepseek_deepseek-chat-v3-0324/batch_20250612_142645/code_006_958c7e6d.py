"""
Generated Code Metadata:
========================
Original URL: https://syr-whistler.com
Prompt: Write a Python Flask application that mimics the functionality of a CGI script typically stored in a "cgi-bin" directory.
Generated: DETERMINISTIC_958c7e6d298a3677
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, make_response
import os
import cgi
import sys
import json

app = Flask(__name__)

@app.route('/cgi-bin/<script_name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cgi_script(script_name):
    try:
        # Simulate CGI environment variables
        env = {
            'REQUEST_METHOD': request.method,
            'SCRIPT_NAME': f'/cgi-bin/{script_name}',
            'PATH_INFO': request.path,
            'QUERY_STRING': request.query_string.decode('utf-8'),
            'CONTENT_TYPE': request.content_type,
            'CONTENT_LENGTH': str(len(request.data)),
            'SERVER_NAME': request.host.split(':')[0],
            'SERVER_PORT': request.host.split(':')[1] if ':' in request.host else '80',
            'REMOTE_ADDR': request.remote_addr,
        }

        # Add HTTP headers to environment
        for key, value in request.headers.items():
            env_key = f'HTTP_{key.upper().replace("-", "_")}'
            env[env_key] = value

        # Process request data based on method
        if request.method == 'GET':
            data = request.args.to_dict()
        elif request.method == 'POST':
            if request.content_type == 'application/x-www-form-urlencoded':
                data = request.form.to_dict()
            elif request.content_type == 'application/json':
                data = request.get_json()
            else:
                data = request.data.decode('utf-8')
        else:
            data = request.data.decode('utf-8')

        # Simulate CGI script output
        output = {
            'status': '200 OK',
            'headers': {
                'Content-Type': 'text/plain',
            },
            'body': f"CGI Script Simulation: {script_name}\n\n"
                   f"Environment:\n{json.dumps(env, indent=2)}\n\n"
                   f"Request Data:\n{json.dumps(data, indent=2)}"
        }

        # Build response
        response = make_response(output['body'])
        response.status = output['status']
        for header, value in output['headers'].items():
            response.headers[header] = value

        return response

    except Exception as e:
        error_response = {
            'status': '500 Internal Server Error',
            'headers': {
                'Content-Type': 'text/plain',
            },
            'body': f"Error processing CGI script: {str(e)}"
        }
        response = make_response(error_response['body'])
        response.status = error_response['status']
        for header, value in error_response['headers'].items():
            response.headers[header] = value
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
```
