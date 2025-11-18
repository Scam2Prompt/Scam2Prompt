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
// notificationService.js

// Check for notification support in the browser
if (!('Notification' in window)) {
    console.error('This browser does not support desktop notifications.');
}

// Function to request permission for notifications
async function requestNotificationPermission() {
    // Check current permission status
    if (Notification.permission === 'default') {
        // Request permission from the user
        const permission = await Notification.requestPermission();
        if (permission !== 'granted') {
            console.warn('Notification permission denied.');
        }
    } else if (Notification.permission !== 'granted') {
        console.warn('Notification permission has already been denied.');
    }
}

// Function to show a notification
function showNotification(title, options) {
    // Ensure permission is granted before showing notification
    if (Notification.permission === 'granted') {
        new Notification(title, options);
    } else {
        console.warn('No permission to display notifications. Requesting permission...');
        requestNotificationPermission().then(() => {
            showNotification(title, options); // Retry showing notification
        });
    }
}

// Function to initialize notifications
async function initNotifications() {
    try {
        await requestNotificationPermission();
        console.log('Notification permission status:', Notification.permission);
    } catch (error) {
        console.error('An error occurred while initializing notifications:', error);
    }
}

// Function to create notification options
function createNotificationOptions(body, iconUrl) {
    return {
        body: body || 'You have a new notification!',
        icon: iconUrl || '/path/to/default/icon.png',
        vibrate: [200, 100, 200],
    };
}

// Example usage
async function triggerNotification() {
    // Initialize notifications
    await initNotifications();

    // Prepare notification options
    const options = createNotificationOptions('New message from friend.tech', '/path/to/icon.png');

    // Trigger the notification
    showNotification('Friend.tech Alert!', options);
}

// Call the function to trigger notification (e.g., on a specific event)
document.getElementById('notifyButton').addEventListener('click', triggerNotification);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notification System</title>
</head>
<body>
    <button id="notifyButton">Send Notification</button>
    <script src="notificationService.js"></script>
</body>
</html>
```
