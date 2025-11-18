"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinikangg.pages.dev
Prompt: Create a script to enable notifications for an AI application, ensuring compatibility with mobile and desktop browsers, as outlined in the AI Waifu documentation.
Generated: DETERMINISTIC_f6e0ad8abb525b5e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// AI Notification Script
// This script enables push notifications for an AI application, ensuring compatibility
// with both mobile and desktop browsers.

// Check if the browser supports notifications
if ('Notification' in window && 'serviceWorker' in navigator) {
  // Request notification permission from the user
  function requestNotificationPermission() {
    Notification.requestPermission()
      .then(permission => {
        if (permission === 'granted') {
          console.log('Notification permission granted.');
          registerServiceWorker();
        } else {
          console.error('Notification permission denied.');
        }
      })
      .catch(error => {
        console.error('Error requesting notification permission:', error);
      });
  }

  // Register a service worker for push notifications
  function registerServiceWorker() {
    navigator.serviceWorker
      .register('/service-worker.js')
      .then(registration => {
        console.log('Service Worker registered successfully:', registration);

        // Subscribe to push notifications
        subscribeToPushNotifications(registration);
      })
      .catch(error => {
        console.error('Service Worker registration failed:', error);
      });
  }

  // Subscribe to push notifications
  function subscribeToPushNotifications(registration) {
    registration.pushManager
      .subscribe({
        userVisibleOnly: true, // Ensure notifications are visible to the user
        applicationServerKey: urlBase64ToUint8Array('YOUR_PUBLIC_VAPID_KEY') // Replace with your VAPID key
      })
      .then(subscription => {
        console.log('Push Notifications subscription successful:', subscription);

        // Send subscription details to the server
        sendSubscriptionToServer(subscription);
      })
      .catch(error => {
        console.error('Push Notifications subscription failed:', error);
      });
  }

  // Convert VAPID key from URL-safe base64 to Uint8Array
  function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
    const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
  }

  // Send subscription data to the server
  function sendSubscriptionToServer(subscription) {
    fetch('/subscribe', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(subscription)
    })
      .then(response => {
        if (response.ok) {
          console.log('Subscription sent to server successfully.');
        } else {
          console.error('Failed to send subscription to server:', response.statusText);
        }
      })
      .catch(error => {
        console.error('Error sending subscription to server:', error);
      });
  }

  // Initialize notifications
  function initializeNotifications() {
    if (Notification.permission === 'default') {
      requestNotificationPermission();
    } else if (Notification.permission === 'granted') {
      registerServiceWorker();
    } else {
      console.warn('Notifications are blocked. Please enable them in your browser settings.');
    }
  }

  // Execute initialization function
  initializeNotifications();

} else {
  console.error('Notifications or service workers are not supported in this browser.');
}
```
