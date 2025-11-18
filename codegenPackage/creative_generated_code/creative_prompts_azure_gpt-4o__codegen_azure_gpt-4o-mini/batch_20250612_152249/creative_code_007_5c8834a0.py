"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Write a script to enable push notifications for Web3Inbox on a mobile browser, including steps to add the app to the home screen.
Generated: DETERMINISTIC_5c8834a0fbf6f54d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Web3Inbox Push Notifications Setup

// Check if the service worker feature is supported
if ('serviceWorker' in navigator && 'PushManager' in window) {
    // Register the service worker
    navigator.serviceWorker.register('service-worker.js')
        .then(function(registration) {
            console.log('Service Worker registered with scope:', registration.scope);
            initializePushNotifications(registration);
        })
        .catch(function(error) {
            console.error('Service Worker registration failed:', error);
        });
} else {
    console.warn('Push messaging is not supported in this browser.');
}

/**
 * Initializes push notifications after service worker registration
 * @param {ServiceWorkerRegistration} registration - The service worker registration object
 */
function initializePushNotifications(registration) {
    // Request permission to send push notifications
    Notification.requestPermission().then(function(permission) {
        if (permission === 'granted') {
            console.log('Notification permission granted.');
            subscribeUserToPush(registration);
        } else {
            console.warn('Unable to get permission to notify.');
        }
    }).catch(function(error) {
        console.error('Permission request error:', error);
    });
}

/**
 * Subscribes the user to push notifications
 * @param {ServiceWorkerRegistration} registration - The service worker registration object
 */
function subscribeUserToPush(registration) {
    const applicationServerKey = urlB64ToUint8Array('<Your-VAPID-Public-Key>'); // Replace with your VAPID public key
    registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: applicationServerKey
    }).then(function(subscription) {
        console.log('User is subscribed:', subscription);
        // Send subscription to the server for storing
        sendSubscriptionToServer(subscription);
    }).catch(function(error) {
        console.error('Failed to subscribe the user: ', error);
    });
}

/**
 * Converts a base64 string to a Uint8Array
 * @param {string} base64String - Base64 string to be converted
 * @returns {Uint8Array} - Converted Uint8Array
 */
function urlB64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/-/g, '+')
        .replace(/_/g, '/');
    const rawData = window.atob(base64);
    return new Uint8Array([...Array(rawData.length)].map((_, i) => rawData.charCodeAt(i)));
}

/**
 * Sends the subscription object to the server
 * @param {PushSubscription} subscription - The push subscription object
 */
function sendSubscriptionToServer(subscription) {
    // Replace with your server endpoint
    fetch('/api/save-subscription', {
        method: 'POST',
        body: JSON.stringify(subscription),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(response) {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    }).then(function(data) {
        console.log('Subscription saved successfully:', data);
    }).catch(function(error) {
        console.error('Error saving subscription:', error);
    });
}

// Instructions to add the app to the home screen
// 1. Open the Web3Inbox application in your mobile browser.
// 2. Tap the browser menu (usually represented by three dots).
// 3. Select "Add to Home Screen" from the options.
// 4. Confirm the action and the app will be added to your home screen.
```

**Note:** Replace `<Your-VAPID-Public-Key>` with your actual VAPID public key. Additionally, ensure that the server endpoint `/api/save-subscription` exists and is set up to handle the incoming subscription data.
