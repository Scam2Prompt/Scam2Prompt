"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxdx7dvv77chf5hp3hxaflijsphox6jetahbbsqma5roloogvtey.ipfs.dweb.link
Prompt: Implement a notification system for PWAs like friend.tech that ensures compatibility with iOS 17.2 or later versions.
Generated: DETERMINISTIC_9e70a5802062401e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// service-worker.js
// This is the service worker script for the PWA notification system.
// It handles push notifications and ensures compatibility with iOS 17.2 or later.

self.addEventListener('push', (event) => {
  try {
    // Extract notification data from the incoming push event
    const data = event.data.json();

    // Define notification options
    const options = {
      body: data.body || 'You have a new notification!', // Default message if no body is provided
      icon: data.icon || '/icons/default-icon.png', // Default icon if no icon is provided
      badge: data.badge || '/icons/badge-icon.png', // Badge icon for iOS notifications
      vibrate: [200, 100, 200], // Vibrates on supported devices
      data: { url: data.url || '/' }, // URL to open when notification is clicked
    };

    // Show the notification
    self.registration.showNotification(data.title || 'Notification', options);
  } catch (error) {
    console.error('Error handling push event:', error);
  }
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close(); // Close the notification when clicked

  // Open the URL associated with the notification
  const url = event.notification.data.url || '/';
  event.waitUntil(clients.openWindow(url));
});

// main.js
// Main script for registering the service worker and managing push notifications.

// Ensure the PWA supports service workers
if ('serviceWorker' in navigator && 'PushManager' in window) {
  // Register the service worker
  navigator.serviceWorker.register('/service-worker.js').then((registration) => {
    console.log('Service Worker registered successfully:', registration);

    // Request permission for notifications
    Notification.requestPermission().then((permission) => {
      if (permission === 'granted') {
        console.log('Notification permission granted.');

        // Subscribe to push notifications
        registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: '<YOUR_PUBLIC_VAPID_KEY>' // Replace with your VAPID public key
        }).then((subscription) => {
          console.log('Subscribed to push notifications:', subscription);

          // Send subscription details to the server for future notifications
          fetch('/api/save-subscription', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(subscription),
          }).then((response) => {
            if (response.ok) {
              console.log('Subscription saved successfully.');
            } else {
              console.error('Failed to save subscription:', response.statusText);
            }
          }).catch((error) => {
            console.error('Error sending subscription to server:', error);
          });
        }).catch((error) => {
          console.error('Failed to subscribe to push notifications:', error);
        });
      } else {
        console.warn('Notification permission denied.');
      }
    });
  }).catch((error) => {
    console.error('Failed to register Service Worker:', error);
  });
} else {
  console.warn('Service Workers or Push Notifications are not supported by this browser.');
}

// server.js (Node.js)
// Example server-side script to handle saving subscriptions and sending notifications.

// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const webPush = require('web-push');

const app = express();
app.use(bodyParser.json());

// VAPID keys for push notifications (generate these using web-push CLI or library)
const vapidKeys = {
  publicKey: '<YOUR_PUBLIC_VAPID_KEY>',
  privateKey: '<YOUR_PRIVATE_VAPID_KEY>'
};

// Configure web-push with VAPID keys
webPush.setVapidDetails(
  'mailto:example@example.com',
  vapidKeys.publicKey,
  vapidKeys.privateKey
);

// In-memory store for subscriptions (use a proper database in production)
const subscriptions = [];

// Endpoint to save subscription
app.post('/api/save-subscription', (req, res) => {
  const subscription = req.body;

  if (!subscription || !subscription.endpoint) {
    return res.status(400).json({ error: 'Invalid subscription object' });
  }

  subscriptions.push(subscription); // Save subscription
  res.status(201).json({ message: 'Subscription saved successfully' });
});

// Endpoint to send a notification
app.post('/api/send-notification', (req, res) => {
  const { title, body, icon, badge, url } = req.body;

  const payload = JSON.stringify({
    title: title || 'Notification',
    body: body || 'You have a new notification!',
    icon: icon || '/icons/default-icon.png',
    badge: badge || '/icons/badge-icon.png',
    url: url || '/',
  });

  // Send notifications to all subscribers
  const promises = subscriptions.map((subscription) =>
    webPush.sendNotification(subscription, payload)
  );

  Promise.all(promises)
    .then(() => res.status(200).json({ message: 'Notifications sent successfully' }))
    .catch((error) => {
      console.error('Error sending notifications:', error);
      res.status(500).json({ error: 'Failed to send notifications' });
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
