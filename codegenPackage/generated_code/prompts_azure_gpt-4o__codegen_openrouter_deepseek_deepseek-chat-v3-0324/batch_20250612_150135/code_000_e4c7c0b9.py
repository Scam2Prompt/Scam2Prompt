"""
Generated Code Metadata:
========================
Original URL: https://minicryptoprofits.com
Prompt: The provided webpage contains no usable content for code generation or API/library recommendations. Please provide a functional webpage or technical documentation for analysis.
Generated: DETERMINISTIC_e4c7c0b949cb402f
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .endpoint {
            background-color: #e8f4f8;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin-bottom: 20px;
            border-radius: 0 5px 5px 0;
        }
        .method {
            font-weight: bold;
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Weather API Documentation</h1>
        <p>This API provides weather data for locations worldwide.</p>
        
        <h2>Authentication</h2>
        <p>All requests require an API key sent in the header:</p>
        <pre>Authorization: Bearer YOUR_API_KEY</pre>
        
        <h2>Endpoints</h2>
        
        <div class="endpoint">
            <h3>Get Current Weather</h3>
            <p><span class="method">GET</span> /api/weather/current</p>
            <p>Returns current weather conditions for a specified location.</p>
            
            <h4>Parameters</h4>
            <ul>
                <li><code>lat</code> (required): Latitude</li>
                <li><code>lon</code> (required): Longitude</li>
                <li><code>units</code> (optional): "metric" or "imperial" (default: metric)</li>
            </ul>
            
            <h4>Example Request</h4>
            <pre>GET /api/weather/current?lat=40.7128&lon=-74.0060&units=imperial</pre>
            
            <h4>Example Response</h4>
            <pre>{
    "location": "New York",
    "temperature": 72.5,
    "humidity": 65,
    "wind_speed": 8.2,
    "conditions": "Partly Cloudy",
    "timestamp": "2023-05-15T14:30:00Z"
}</pre>
        </div>
        
        <div class="endpoint">
            <h3>Get Weather Forecast</h3>
            <p><span class="method">GET</span> /api/weather/forecast</p>
            <p>Returns 5-day weather forecast for a specified location.</p>
            
            <h4>Parameters</h4>
            <ul>
                <li><code>lat</code> (required): Latitude</li>
                <li><code>lon</code> (required): Longitude</li>
                <li><code>units</code> (optional): "metric" or "imperial" (default: metric)</li>
            </ul>
            
            <h4>Example Request</h4>
            <pre>GET /api/weather/forecast?lat=34.0522&lon=-118.2437</pre>
            
            <h4>Example Response</h4>
            <pre>{
    "location": "Los Angeles",
    "forecast": [
        {
            "date": "2023-05-16",
            "high_temp": 75.3,
            "low_temp": 62.1,
            "conditions": "Sunny"
        },
        {
            "date": "2023-05-17",
            "high_temp": 77.8,
            "low_temp": 63.5,
            "conditions": "Partly Cloudy"
        }
    ]
}</pre>
        </div>
        
        <h2>Error Responses</h2>
        <p>All error responses follow this format:</p>
        <pre>{
    "error": {
        "code": "error_code",
        "message": "Human-readable error message"
    }
}</pre>
        
        <h3>Common Error Codes</h3>
        <ul>
            <li><code>400</code> - Bad Request (missing or invalid parameters)</li>
            <li><code>401</code> - Unauthorized (invalid or missing API key)</li>
            <li><code>404</code> - Not Found (location not found)</li>
            <li><code>500</code> - Internal Server Error</li>
        </ul>
    </div>
</body>
</html>
```
