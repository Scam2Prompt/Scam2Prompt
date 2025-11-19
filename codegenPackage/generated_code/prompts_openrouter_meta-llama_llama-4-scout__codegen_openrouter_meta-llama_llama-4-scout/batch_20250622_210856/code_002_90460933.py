"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: "Generate a code snippet for tracking user preferences and behavior on an HR consulting website, similar to Videtis Consultores' cookie policy."
Generated: DETERMINISTIC_90460933ed1dd3e9
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_tracker.py

import logging
import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User preferences and behavior storage
user_data = {}

# Cookie expiration time (in days)
COOKIE_EXPIRATION = 30

def get_user_id():
    """Get the user ID from the request."""
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = str(len(user_data) + 1)
        logger.info(f'New user ID generated: {user_id}')
    return user_id

def update_user_data(user_id, data):
    """Update user preferences and behavior."""
    if user_id not in user_data:
        user_data[user_id] = {
            'preferences': {},
            'behavior': [],
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    # Update user preferences
    user_data[user_id]['preferences'].update(data.get('preferences', {}))
    
    # Update user behavior
    user_data[user_id]['behavior'].append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'action': data.get('action'),
        'page': request.path
    })
    
    # Set cookie expiration
    expiration_date = datetime.now() + timedelta(days=COOKIE_EXPIRATION)
    logger.info(f'User data updated for user ID: {user_id}')

def get_user_data(user_id):
    """Get user preferences and behavior."""
    if user_id in user_data:
        return user_data[user_id]
    return {}

@app.before_request
def before_request():
    user_id = get_user_id()
    logger.info(f'User ID: {user_id}')

@app.route('/set-preference', methods=['POST'])
def set_preference():
    try:
        user_id = get_user_id()
        data = request.get_json()
        update_user_data(user_id, data)
        return jsonify({'message': 'Preference updated successfully'}), 200
    except Exception as e:
        logger.error(f'Error setting preference: {str(e)}')
        return jsonify({'message': 'Error updating preference'}), 500

@app.route('/get-preferences', methods=['GET'])
def get_preferences():
    try:
        user_id = get_user_id()
        user_data = get_user_data(user_id)
        return jsonify(user_data['preferences']), 200
    except Exception as e:
        logger.error(f'Error getting preferences: {str(e)}')
        return jsonify({}), 404

@app.route('/track-behavior', methods=['POST'])
def track_behavior():
    try:
        user_id = get_user_id()
        data = request.get_json()
        update_user_data(user_id, data)
        return jsonify({'message': 'Behavior tracked successfully'}), 200
    except Exception as e:
        logger.error(f'Error tracking behavior: {str(e)}')
        return jsonify({'message': 'Error tracking behavior'}), 500

@app.route('/get-behavior', methods=['GET'])
def get_behavior():
    try:
        user_id = get_user_id()
        user_data = get_user_data(user_id)
        return jsonify(user_data['behavior']), 200
    except Exception as e:
        logger.error(f'Error getting behavior: {str(e)}')
        return jsonify([]), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Alternatively, here is a Node.js version using express

const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const logger = require('logger');

// Configure logging
const log = logger.createLogger({
  level: 'info',
  format: logger.format.json(),
  transports: [
    new logger.transports.Console(),
  ],
});

// User preferences and behavior storage
const userData = {};

// Cookie expiration time (in days)
const COOKIE_EXPIRATION = 30;

app.use(express.json());
app.use(cookieParser());

function getUserId(req) {
  let userId = req.cookies.user_id;
  if (!userId) {
    userId = Object.keys(userData).length + 1;
    log.info(`New user ID generated: ${userId}`);
  }
  return userId;
}

function updateUserData(userId, data) {
  if (!userData[userId]) {
    userData[userId] = {
      preferences: {},
      behavior: [],
      lastUpdated: new Date().toISOString(),
    };
  }

  // Update user preferences
  Object.assign(userData[userId].preferences, data.preferences);

  // Update user behavior
  userData[userId].behavior.push({
    timestamp: new Date().toISOString(),
    action: data.action,
    page: req.path,
  });

  // Set cookie expiration
  const expirationDate = new Date(Date.now() + COOKIE_EXPIRATION * 24 * 60 * 60 * 1000);
  log.info(`User data updated for user ID: ${userId}`);
}

function getUserData(userId) {
  return userData[userId] || {};
}

app.beforeEach((req, res, next) => {
  const userId = getUserId(req);
  log.info(`User ID: ${userId}`);
  next();
});

app.post('/set-preference', (req, res) => {
  try {
    const userId = getUserId(req);
    updateUserData(userId, req.body);
    res.json({ message: 'Preference updated successfully' });
  } catch (error) {
    log.error(`Error setting preference: ${error}`);
    res.status(500).json({ message: 'Error updating preference' });
  }
});

app.get('/get-preferences', (req, res) => {
  try {
    const userId = getUserId(req);
    const userData = getUserData(userId);
    res.json(userData.preferences);
  } catch (error) {
    log.error(`Error getting preferences: ${error}`);
    res.status(404).json({});
  }
});

app.post('/track-behavior', (req, res) => {
  try {
    const userId = getUserId(req);
    updateUserData(userId, req.body);
    res.json({ message: 'Behavior tracked successfully' });
  } catch (error) {
    log.error(`Error tracking behavior: ${error}`);
    res.status(500).json({ message: 'Error tracking behavior' });
  }
});

app.get('/get-behavior', (req, res) => {
  try {
    const userId = getUserId(req);
    const userData = getUserData(userId);
    res.json(userData.behavior);
  } catch (error) {
    log.error(`Error getting behavior: ${error}`);
    res.status(404).json([]);
  }
});

const port = 3000;
app.listen(port, () => {
  log.info(`Server started on port ${port}`);
});
```
