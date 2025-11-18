"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Generate code to configure XMTP in a JavaScript app for subscribing to notifications, referencing the XMTP Subscribe Push Demo example.
Generated: DETERMINISTIC_5fe8a9526e643b9d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import { Client } from '@xmtp/xmtp-js';
import { createClient } from 'xmtp';

// Define the main function to set up XMTP client and subscribe to notifications
async function setupXmtp() {
    try {
        // Create an XMTP client instance
        const client = await createClient({
            privateKey: process.env.XMTP_PRIVATE_KEY, // Ensure you have your private key in environment variables
        });

        // Log the client information for debugging
        console.log('XMTP client created successfully:', client);

        // Subscribe to messages
        client.onMessage(async (message) => {
            try {
                // Handle incoming messages
                console.log('New message received:', message);

                // Process the message (this could be customized based on your app's logic)
                await handleIncomingMessage(message);
            } catch (error) {
                console.error('Error handling incoming message:', error);
            }
        });

        // Subscribe to notifications
        client.onNotification((notification) => {
            // Handle incoming notifications
            console.log('New notification received:', notification);
        });

        console.log('Successfully subscribed to notifications and messages.');
    } catch (error) {
        // Handle errors that may occur during initialization
        console.error('Error setting up XMTP:', error);
    }
}

// Function to handle incoming messages
async function handleIncomingMessage(message) {
    // Custom logic to process the incoming message
    // For example, you could store it in a database or update the UI
    console.log('Processing incoming message:', message);
}

// Call the setup function to initiate XMTP configuration
setupXmtp();
```

### Notes:
- Make sure to set the `XMTP_PRIVATE_KEY` environment variable before running this code.
- Customize the `handleIncomingMessage` function to fit your application's needs.
- This code assumes that the necessary XMTP libraries are installed and properly configured in your JavaScript environment.
