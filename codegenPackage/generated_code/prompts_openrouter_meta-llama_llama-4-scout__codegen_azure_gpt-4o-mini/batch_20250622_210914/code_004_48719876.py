"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Design a simple UI component for a virtual AI companion, like AI Waifu, that allows users to "Add to Home Screen" and "Enable Notifications".
Generated: DETERMINISTIC_4871987609b2b8a0
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Companion Settings</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        button {
            padding: 10px 15px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            font-size: 16px;
        }
        button:disabled {
            background-color: #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>AI Companion Settings</h2>
        <button id="addToHomeScreen">Add to Home Screen</button>
        <button id="enableNotifications">Enable Notifications</button>
    </div>

    <script>
        // Check if the browser supports service workers and notifications
        if ('serviceWorker' in navigator && 'Notification' in window) {
            // Register service worker
            navigator.serviceWorker.register('service-worker.js')
                .then(() => console.log('Service Worker registered successfully.'))
                .catch(err => console.error('Service Worker registration failed:', err));
        } else {
            console.warn('Service Workers or Notifications are not supported in this browser.');
        }

        // Function to handle "Add to Home Screen" action
        document.getElementById('addToHomeScreen').addEventListener('click', () => {
            if (window.matchMedia('(display-mode: standalone)').matches) {
                alert('This app is already added to the home screen.');
            } else {
                alert('To add this app to your home screen, use the browser menu.');
            }
        });

        // Function to handle "Enable Notifications" action
        document.getElementById('enableNotifications').addEventListener('click', async () => {
            try {
                const permission = await Notification.requestPermission();
                if (permission === 'granted') {
                    alert('Notifications enabled!');
                } else if (permission === 'denied') {
                    alert('Notifications denied. You can enable them in your browser settings.');
                } else {
                    alert('Notifications permission dismissed.');
                }
            } catch (error) {
                console.error('Error requesting notification permission:', error);
                alert('An error occurred while enabling notifications. Please try again.');
            }
        });
    </script>
</body>
</html>
```

```javascript
// service-worker.js
self.addEventListener('push', function(event) {
    const options = {
        body: event.data ? event.data.text() : 'You have a new message from your AI companion!',
        icon: 'icon.png', // Path to your icon
        badge: 'badge.png' // Path to your badge
    };

    event.waitUntil(
        self.registration.showNotification('AI Companion', options)
    );
});
```
