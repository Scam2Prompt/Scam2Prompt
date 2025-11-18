"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Write code to implement a push notification system for PWAs, including handling edge cases where iOS versions below 17.2 fail to deliver notifications.
Generated: DETERMINISTIC_aa1fa90317b9a109
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Service Worker Registration for Push Notifications in a Progressive Web App (PWA)
// The following code handles push notifications and accounts for iOS versions below 17.2.

if ('serviceWorker' in navigator && 'PushManager' in window) {
    // Register the Service Worker
    navigator.serviceWorker.register('/service-worker.js')
        .then((registration) => {
            console.log('Service Worker registered successfully:', registration);

            // Check if Push Notifications are supported
            return registration.pushManager.getSubscription().then((subscription) => {
                if (subscription === null) {
                    // No subscription exists, ask the user for permission
                    return requestPushNotificationPermission(registration);
                } else {
                    console.log('User is already subscribed to push notifications:', subscription);
                }
            });
        })
        .catch((error) => {
            console.error('Service Worker registration failed:', error);
        });
} else {
    console.error('Push Notifications are not supported on this browser.');
}

/**
 * Request permission for Push Notifications and subscribe the user if granted.
 * @param {ServiceWorkerRegistration} registration - The service worker registration object.
 * @returns {Promise<void>}
 */
async function requestPushNotificationPermission(registration) {
    try {
        const permission = await Notification.requestPermission();

        if (permission === 'granted') {
            console.log('Notification permission granted.');

            const subscription = await registration.pushManager.subscribe({
                userVisibleOnly: true, // Ensures notifications are visible to the user
                applicationServerKey: urlBase64ToUint8Array('<YOUR_PUBLIC_VAPID_KEY>') // Replace <YOUR_PUBLIC_VAPID_KEY>
            });

            console.log('Push Notification subscription:', subscription);

            // Send subscription to the server for storage
            await sendSubscriptionToServer(subscription);
        } else {
            console.warn('Notification permission denied.');
        }
    } catch (error) {
        console.error('Error requesting push notification permission:', error);
    }
}

/**
 * Converts a base64 string to a Uint8Array for use with VAPID keys.
 * @param {string} base64String - The base64 string representing the VAPID public key.
 * @returns {Uint8Array}
 */
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

/**
 * Sends the subscription object to the server for storage.
 * @param {PushSubscription} subscription - The push subscription object.
 * @returns {Promise<void>}
 */
async function sendSubscriptionToServer(subscription) {
    try {
        const response = await fetch('/api/save-subscription', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(subscription),
        });

        if (!response.ok) {
            throw new Error(`Failed to send subscription to server: ${response.statusText}`);
        }

        console.log('Subscription saved successfully on the server.');
    } catch (error) {
        console.error('Error saving subscription to the server:', error);
    }
}

/**
 * Detect iOS version and provide feedback if the version does not support Push Notifications (pre-17.2).
 */
function handleIOSCompatibility() {
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;
    if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        const iOSVersionMatch = userAgent.match(/OS (\d+)_/);
        const iOSVersion = iOSVersionMatch ? parseInt(iOSVersionMatch[1], 10) : null;

        if (iOSVersion !== null && iOSVersion < 17) {
            console.warn('Push Notifications are not supported on iOS versions below 17.2.');
            alert('Push Notifications are currently unsupported on your iOS version. Please update your device.');
        }
    }
}

// Run compatibility check for iOS
handleIOSCompatibility();
```
