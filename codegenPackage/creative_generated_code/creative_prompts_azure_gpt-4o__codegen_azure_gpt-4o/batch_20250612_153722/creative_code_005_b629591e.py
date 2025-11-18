"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pisapopa.pages.dev
Prompt: Create a backend service in Node.js to manage app notifications and retry mechanisms, inspired by the TonPlace app's features.
Generated: DETERMINISTIC_b629591e7665a804
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework to create the HTTP service
const bodyParser = require('body-parser'); // Middleware to parse incoming request bodies
const { v4: uuidv4 } = require('uuid'); // Generate unique IDs for notifications
const dotenv = require('dotenv'); // Load environment variables from .env file
const axios = require('axios'); // HTTP client for external retry mechanisms

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Notification storage (In-memory for simplicity; consider a database in production)
const notifications = {};

// Retry settings
const MAX_RETRIES = 3;
const RETRY_DELAY = 5000; // 5 seconds

/**
 * Send notification to a user.
 * Simulates external notification delivery and retry mechanism.
 * @param {string} notificationId - ID of the notification
 */
async function sendNotification(notificationId) {
  const notification = notifications[notificationId];

  if (!notification) {
    console.error(`Notification ID ${notificationId} not found.`);
    return;
  }

  try {
    // Simulating external delivery (Replace with actual delivery logic, e.g., an external API)
    const response = await axios.post(notification.deliveryEndpoint, {
      userId: notification.userId,
      message: notification.message,
    });

    if (response.status === 200) {
      notification.status = 'delivered';
      console.log(`Notification ${notificationId} delivered successfully.`);
    } else {
      throw new Error(`Failed delivery with status code: ${response.status}`);
    }
  } catch (error) {
    console.error(`Error delivering notification ${notificationId}:`, error.message);

    // Retry mechanism
    if (notification.retryCount < MAX_RETRIES) {
      notification.retryCount += 1;
      console.log(`Retrying notification ${notificationId} in ${RETRY_DELAY}ms...`);

      setTimeout(() => sendNotification(notificationId), RETRY_DELAY);
    } else {
      notification.status = 'failed';
      console.error(`Max retries reached for notification ${notificationId}. Marking as failed.`);
    }
  }
}

// POST endpoint to create a new notification
app.post('/notifications', (req, res) => {
  const { userId, message, deliveryEndpoint } = req.body;

  // Validate request body
  if (!userId || !message || !deliveryEndpoint) {
    return res.status(400).json({ error: 'Missing required fields: userId, message, deliveryEndpoint' });
  }

  // Create new notification
  const notificationId = uuidv4();
  notifications[notificationId] = {
    id: notificationId,
    userId,
    message,
    deliveryEndpoint,
    status: 'pending',
    retryCount: 0,
  };

  // Attempt to send the notification
  sendNotification(notificationId);

  res.status(201).json({ notificationId, status: 'pending' });
});

// GET endpoint to retrieve notification status
app.get('/notifications/:id', (req, res) => {
  const { id } = req.params;

  const notification = notifications[id];
  if (!notification) {
    return res.status(404).json({ error: 'Notification not found' });
  }

  res.json({ id, status: notification.status, retryCount: notification.retryCount });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Notification service running on port ${PORT}`);
});
```
