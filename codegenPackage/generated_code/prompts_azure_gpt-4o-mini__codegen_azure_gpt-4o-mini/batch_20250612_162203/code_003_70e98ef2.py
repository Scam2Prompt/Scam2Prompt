"""
Generated Code Metadata:
========================
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Generate a sample JavaScript code for integrating XMTP push notifications into a web app.
Generated: DETERMINISTIC_70e98ef2abc3db48
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Client } from '@xmtp/xmtp-js';

// Define a function to initialize the XMTP client
async function initializeXmtpClient() {
    try {
        // Create a new XMTP client instance
        const client = await Client.create();
        console.log('XMTP client initialized successfully.');

        return client;
    } catch (error) {
        console.error('Error initializing XMTP client:', error);
        throw new Error('Failed to initialize XMTP client');
    }
}

// Define a function to subscribe to push notifications
async function subscribeToNotifications(client) {
    try {
        // Subscribe to incoming messages
        client.onMessage(async (message) => {
            console.log('New message received:', message);
            // Handle the incoming message (e.g., display a notification)
            displayNotification(message);
        });

        console.log('Subscribed to notifications successfully.');
    } catch (error) {
        console.error('Error subscribing to notifications:', error);
        throw new Error('Failed to subscribe to notifications');
    }
}

// Function to display a notification
function displayNotification(message) {
    // Check if the browser supports notifications
    if ('Notification' in window) {
        // Request permission to show notifications
        Notification.requestPermission().then((permission) => {
            if (permission === 'granted') {
                // Create and display the notification
                new Notification('New Message', {
                    body: message.content,
                    icon: 'icon.png' // Path to an icon image
                });
            }
        });
    } else {
        console.warn('This browser does not support desktop notifications.');
    }
}

// Main function to run the application
async function main() {
    try {
        // Initialize the XMTP client
        const xmtpClient = await initializeXmtpClient();

        // Subscribe to notifications
        await subscribeToNotifications(xmtpClient);
    } catch (error) {
        console.error('Error in main function:', error);
    }
}

// Run the main function when the window loads
window.onload = main;
```
