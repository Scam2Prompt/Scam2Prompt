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
// notification.js

// Check for browser compatibility for notifications
if (!('Notification' in window)) {
    console.error('This browser does not support desktop notifications.');
} else if (Notification.permission === 'denied') {
    console.warn('Notification permissions are denied. Unable to send notifications.');
} else {
    // Function to request permission for notifications
    const requestNotificationPermission = async () => {
        try {
            const permission = await Notification.requestPermission();
            if (permission === 'granted') {
                console.log('Notification permission granted.');
                // Proceed to enable notifications
                enableNotifications();
            } else {
                console.warn('Notification permission denied.');
            }
        } catch (error) {
            console.error('Error requesting notification permission:', error);
        }
    };

    // Function to enable sending notifications
    const enableNotifications = () => {
        // Example notification data
        const notificationData = {
            title: 'AI Waifu Update',
            body: 'You have a new message from your AI Waifu!',
            icon: 'icon.png' // Replace with your notification icon path
        };

        // Create and display a new notification
        const showNotification = () => {
            const notification = new Notification(notificationData.title, {
                body: notificationData.body,
                icon: notificationData.icon
            });

            // Close notification after 5 seconds
            setTimeout(() => {
                notification.close();
            }, 5000);

            // Optional: add click event to the notification
            notification.onclick = () => {
                console.log('Notification clicked!');
                // Handle the notification click (e.g., open the app)
                window.focus();
            };
        };

        // Show notification on a specific event (e.g., a message received)
        // This is just an example, replace it with your actual event.
        document.addEventListener('messageReceived', showNotification);
    };

    // Request permission for notifications on page load
    document.addEventListener('DOMContentLoaded', () => {
        if (Notification.permission === 'default') {
            requestNotificationPermission();
        } else if (Notification.permission === 'granted') {
            enableNotifications();
        }
    });
}
```

### Note:
- Ensure you replace `'icon.png'` with the path to your actual notification icon.
- This script assumes that there is an event `messageReceived` that triggers notifications; you should implement this event in your AI application to suit your needs.
