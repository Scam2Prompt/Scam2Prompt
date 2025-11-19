"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Generate a sample JavaScript code for integrating XMTP push notifications into a web app.
Generated: DETERMINISTIC_70e98ef2abc3db48
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for XMTP integration (install via npm)
// npm install @xmtp/xmtp-js

import { Client } from '@xmtp/xmtp-js';

// Define the main application class
class XmtpNotificationApp {
    constructor() {
        this.client = null;
        this.initialize();
    }

    // Initialize the XMTP client
    async initialize() {
        try {
            // Connect to the XMTP client
            this.client = await Client.create();
            console.log('XMTP Client initialized successfully.');

            // Subscribe to new messages
            this.listenForMessages();
        } catch (error) {
            console.error('Error initializing XMTP Client:', error);
        }
    }

    // Listen for incoming messages
    listenForMessages() {
        this.client.onMessage(async (message) => {
            console.log('New message received:', message);

            // Display push notification for new messages
            this.showNotification(message);
        });
    }

    // Show a browser notification
    async showNotification(message) {
        // Check if the browser supports notifications
        if (!('Notification' in window)) {
            console.error('This browser does not support desktop notification');
            return;
        }

        // Ask for permission to show notifications
        const permission = await Notification.requestPermission();
        if (permission !== 'granted') {
            console.warn('Notification permission denied');
            return;
        }

        // Create and display the notification
        new Notification('New Message from ' + message.sender, {
            body: message.body,
            icon: 'path/to/icon.png', // Optional icon
        });
    }
}

// Instantiate the application
document.addEventListener('DOMContentLoaded', () => {
    new XmtpNotificationApp();
});
```

Make sure to replace `'path/to/icon.png'` with the actual path to your notification icon. Additionally, ensure that your environment is set up for using ES modules if you are using this import syntax.
