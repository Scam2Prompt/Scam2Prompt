"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Write code to implement a push notification system for PWAs, including handling edge cases where iOS versions below 17.2 fail to deliver notifications.
Generated: DETERMINISTIC_aa1fa90317b9a109
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PushNotificationService.js
const webpush = require('web-push');
const vapidKeys = require('./vapidKeys.json');

/**
 * Initializes the push notification service with VAPID keys.
 */
class PushNotificationService {
  constructor() {
    // Initialize VAPID keys for push notifications
    webpush.setVapidDetails(
      'mailto:your_email@example.com',
      vapidKeys.publicKey,
      vapidKeys.privateKey
    );
  }

  /**
   * Subscribes a user to push notifications.
   * @param {object} subscription - The subscription object from the browser.
   * @returns {Promise} A promise that resolves when the subscription is saved.
   */
  async subscribeUser(subscription) {
    try {
      // Save the subscription to your database or server-side storage
      await this.saveSubscription(subscription);
      return subscription;
    } catch (error) {
      console.error('Error subscribing user:', error);
      throw error;
    }
  }

  /**
   * Saves a subscription to your database or server-side storage.
   * @param {object} subscription - The subscription object from the browser.
   * @returns {Promise} A promise that resolves when the subscription is saved.
   */
  async saveSubscription(subscription) {
    // Implement database or storage logic to save the subscription
    // For demonstration purposes, a simple in-memory storage is used
    if (!this.subscriptions) {
      this.subscriptions = [];
    }
    this.subscriptions.push(subscription);
  }

  /**
   * Sends a push notification to a subscribed user.
   * @param {string} subscription - The subscription object from the browser.
   * @param {object} notification - The notification payload.
   * @returns {Promise} A promise that resolves when the notification is sent.
   */
  async sendNotification(subscription, notification) {
    try {
      // Handle edge case for iOS versions below 17.2
      if (process.env.NODE_ENV === 'production' && this.isIOSBelow172(subscription)) {
        console.log('iOS version below 17.2 detected, using legacy notification payload');
        return this.sendLegacyNotification(subscription, notification);
      }

      // Send the notification using web-push
      const result = await webpush.sendNotification(subscription, JSON.stringify(notification));
      console.log('Notification sent:', result);
      return result;
    } catch (error) {
      console.error('Error sending notification:', error);
      throw error;
    }
  }

  /**
   * Checks if the subscription is from an iOS device with a version below 17.2.
   * @param {object} subscription - The subscription object from the browser.
   * @returns {boolean} True if the subscription is from an iOS device with a version below 17.2.
   */
  isIOSBelow172(subscription) {
    // Implement logic to detect iOS version from the subscription object
    // For demonstration purposes, assume the user agent is available
    const userAgent = subscription.userAgent;
    return userAgent.includes('iPhone') && this.getiOSVersion(userAgent) < 17.2;
  }

  /**
   * Extracts the iOS version from a user agent string.
   * @param {string} userAgent - The user agent string.
   * @returns {number} The iOS version.
   */
  getiOSVersion(userAgent) {
    const iosVersionMatch = userAgent.match(/OS (\d+(?:_\d+)*)/);
    if (iosVersionMatch) {
      const version = iosVersionMatch[1].split('_').map(Number);
      return version[0] + version[1] / 100;
    }
    return 0;
  }

  /**
   * Sends a legacy notification payload for iOS versions below 17.2.
   * @param {object} subscription - The subscription object from the browser.
   * @param {object} notification - The notification payload.
   * @returns {Promise} A promise that resolves when the notification is sent.
   */
  async sendLegacyNotification(subscription, notification) {
    // Implement logic to send a legacy notification payload
    // For demonstration purposes, assume a simple payload is used
    const legacyPayload = {
      title: notification.title,
      message: notification.message,
    };
    // Send the legacy notification using web-push
    const result = await webpush.sendNotification(subscription, JSON.stringify(legacyPayload));
    console.log('Legacy notification sent:', result);
    return result;
  }

  /**
   * Unsubscribes a user from push notifications.
   * @param {object} subscription - The subscription object from the browser.
   * @returns {Promise} A promise that resolves when the subscription is deleted.
   */
  async unsubscribeUser(subscription) {
    try {
      // Delete the subscription from your database or server-side storage
      await this.deleteSubscription(subscription);
      return subscription;
    } catch (error) {
      console.error('Error unsubscribing user:', error);
      throw error;
    }
  }

  /**
   * Deletes a subscription from your database or server-side storage.
   * @param {object} subscription - The subscription object from the browser.
   * @returns {Promise} A promise that resolves when the subscription is deleted.
   */
  async deleteSubscription(subscription) {
    // Implement database or storage logic to delete the subscription
    // For demonstration purposes, a simple in-memory storage is used
    if (this.subscriptions) {
      this.subscriptions = this.subscriptions.filter((sub) => sub !== subscription);
    }
  }
}

module.exports = PushNotificationService;
```

```javascript
// server.js
const express = require('express');
const PushNotificationService = require('./PushNotificationService');

const app = express();
app.use(express.json());

const pushNotificationService = new PushNotificationService();

// Handle subscription requests
app.post('/subscribe', async (req, res) => {
  try {
    const subscription = req.body;
    const result = await pushNotificationService.subscribeUser(subscription);
    res.status(201).json(result);
  } catch (error) {
    console.error('Error subscribing user:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Handle notification requests
app.post('/notify', async (req, res) => {
  try {
    const subscription = req.body.subscription;
    const notification = req.body.notification;
    const result = await pushNotificationService.sendNotification(subscription, notification);
    res.status(201).json(result);
  } catch (error) {
    console.error('Error sending notification:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Handle unsubscription requests
app.post('/unsubscribe', async (req, res) => {
  try {
    const subscription = req.body;
    const result = await pushNotificationService.unsubscribeUser(subscription);
    res.status(200).json(result);
  } catch (error) {
    console.error('Error unsubscribing user:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

```json
// vapidKeys.json
{
  "publicKey": "YOUR_PUBLIC_VAPID_KEY",
  "privateKey": "YOUR_PRIVATE_VAPID_KEY"
}
```
