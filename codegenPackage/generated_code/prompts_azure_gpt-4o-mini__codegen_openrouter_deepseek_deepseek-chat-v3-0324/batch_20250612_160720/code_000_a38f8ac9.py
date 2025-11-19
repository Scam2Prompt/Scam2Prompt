"""
Generated Code Metadata:
========================
Original URL: https://sweans360.com
Prompt: What are some common practices for handling scheduled maintenance on a web application?
Generated: DETERMINISTIC_a38f8ac95e66b816
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Maintenance mode flag
maintenance_mode = False

# Scheduled maintenance window
scheduled_maintenance = {
    'start_time': None,
    'end_time': None,
    'message': None
}

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

def check_maintenance_window():
    """Check if current time is within maintenance window."""
    now = datetime.utcnow()
    if scheduled_maintenance['start_time'] and scheduled_maintenance['end_time']:
        return scheduled_maintenance['start_time'] <= now <= scheduled_maintenance['end_time']
    return False

@app.before_request
def check_for_maintenance():
    """Middleware to check for maintenance mode before processing requests."""
    if maintenance_mode or check_maintenance_window():
        return jsonify({
            'status': 'maintenance',
            'message': scheduled_maintenance.get('message', 'The application is currently undergoing maintenance.')
        }), 503

@app.route('/admin/maintenance', methods=['POST'])
def set_maintenance():
    """Admin endpoint to enable/disable maintenance mode."""
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    global maintenance_mode
    
    if 'enable' in data:
        maintenance_mode = data['enable']
        logger.info(f"Maintenance mode set to {maintenance_mode}")
        return jsonify({'status': 'success', 'maintenance_mode': maintenance_mode}), 200
    
    return jsonify({'error': 'Invalid request'}), 400

@app.route('/admin/schedule-maintenance', methods=['POST'])
def schedule_maintenance():
    """Admin endpoint to schedule maintenance window."""
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    
    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
        message = data.get('message', 'Scheduled maintenance in progress.')
        
        if end_time <= start_time:
            return jsonify({'error': 'End time must be after start time'}), 400
            
        scheduled_maintenance.update({
            'start_time': start_time,
            'end_time': end_time,
            'message': message
        })
        
        logger.info(f"Scheduled maintenance from {start_time} to {end_time}")
        return jsonify({'status': 'success', 'scheduled_maintenance': scheduled_maintenance}), 200
    
    except (KeyError, ValueError) as e:
        logger.error(f"Error scheduling maintenance: {str(e)}")
        return jsonify({'error': 'Invalid date format or missing parameters'}), 400

@app.route('/status')
def status():
    """Endpoint to check application status."""
    if maintenance_mode or check_maintenance_window():
        return jsonify({
            'status': 'maintenance',
            'message': scheduled_maintenance.get('message', 'The application is currently undergoing maintenance.')
        }), 503
    return jsonify({'status': 'operational'}), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
    finally:
        scheduler.shutdown()
```
