"""
Generated Code Metadata:
========================
Original URL: https://cave.fi
Prompt: How can I notify users about maintenance mode in a web application, similar to the approach used by CAVE?
Generated: DETERMINISTIC_710669ebc4417db2
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify, make_response
import time
from functools import wraps

app = Flask(__name__)

# Maintenance mode configuration
MAINTENANCE_MODE = False
MAINTENANCE_START = None
MAINTENANCE_END = None
MAINTENANCE_MESSAGE = "We're currently undergoing maintenance. Please check back soon."

def check_maintenance(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if MAINTENANCE_MODE:
            # Check if request is API call
            if request.path.startswith('/api/'):
                return jsonify({
                    "status": "maintenance",
                    "message": MAINTENANCE_MESSAGE,
                    "scheduled_end": MAINTENANCE_END
                }), 503
            
            # For regular web requests
            return render_template('maintenance.html', 
                                message=MAINTENANCE_MESSAGE,
                                start_time=MAINTENANCE_START,
                                end_time=MAINTENANCE_END), 503
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@check_maintenance
def home():
    return render_template('index.html')

@app.route('/api/data')
@check_maintenance
def api_data():
    return jsonify({"data": "sample data"})

@app.route('/admin/maintenance', methods=['POST'])
def toggle_maintenance():
    global MAINTENANCE_MODE, MAINTENANCE_START, MAINTENANCE_END
    
    # In a real app, this would have proper authentication
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid request"}), 400
    
    MAINTENANCE_MODE = data.get('enabled', False)
    
    if MAINTENANCE_MODE:
        MAINTENANCE_START = int(time.time())
        MAINTENANCE_END = data.get('estimated_end', MAINTENANCE_START + 3600)  # Default 1 hour
    else:
        MAINTENANCE_START = None
        MAINTENANCE_END = None
    
    return jsonify({
        "status": "success",
        "maintenance_mode": MAINTENANCE_MODE,
        "start_time": MAINTENANCE_START,
        "estimated_end": MAINTENANCE_END
    })

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/maintenance.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Maintenance Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f5f5f5;
        }
        .maintenance-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 30px;
            background: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e74c3c;
        }
        .time-info {
            margin: 20px 0;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <h1>Maintenance in Progress</h1>
        <p>{{ message }}</p>
        
        <div class="time-info">
            {% if start_time %}
                <p>Maintenance started: {{ start_time|datetime }}</p>
            {% endif %}
            {% if end_time %}
                <p>Estimated completion: {{ end_time|datetime }}</p>
            {% endif %}
        </div>
        
        <p>We apologize for the inconvenience. Please try again later.</p>
    </div>
</body>
</html>
```

```javascript
// Client-side check for maintenance mode
function checkMaintenanceStatus() {
    fetch('/api/health')
        .then(response => {
            if (response.status === 503) {
                // Parse maintenance info from response headers or body
                return response.json().then(data => {
                    showMaintenanceNotice(data);
                    return Promise.reject('Maintenance mode active');
                });
            }
            return response.json();
        })
        .catch(error => {
            if (error !== 'Maintenance mode active') {
                console.error('Error checking maintenance status:', error);
            }
        });
}

function showMaintenanceNotice(data) {
    // Create or show maintenance banner
    let banner = document.getElementById('maintenance-banner');
    if (!banner) {
        banner = document.createElement('div');
        banner.id = 'maintenance-banner';
        banner.style.cssText = `
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #e74c3c;
            color: white;
            padding: 15px;
            text-align: center;
            z-index: 9999;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
        `;
        document.body.appendChild(banner);
    }
    
    let message = data.message || 'Maintenance in progress';
    if (data.scheduled_end) {
        const endTime = new Date(data.scheduled_end * 1000);
        message += ` - Estimated completion: ${endTime.toLocaleString()}`;
    }
    
    banner.innerHTML = `
        <strong>Notice:</strong> ${message}
        <button onclick="this.parentElement.style.display='none'" 
                style="margin-left: 15px; background: white; border: none; padding: 3px 8px; border-radius: 3px;">
            Hide
        </button>
    `;
}

// Check periodically (every 5 minutes)
setInterval(checkMaintenanceStatus, 300000);
checkMaintenanceStatus(); // Initial check
```
