"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Write a code snippet to enable push notifications in a web application using XMTP.
Generated: DETERMINISTIC_e89ef6d83709f921
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Client } from '@xmtp/xmtp-js'; // Import XMTP client
import { ethers } from 'ethers'; // Import ethers for wallet management

// Function to initialize XMTP client and enable push notifications
async function enablePushNotifications() {
    try {
        // Create a new Ethereum provider (e.g., MetaMask)
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Request account access from the user
        await provider.send("eth_requestAccounts", []);

        // Get the signer (the user's wallet)
        const signer = provider.getSigner();
        
        // Create the XMTP client
        const client = await Client.create(signer);
        
        // Check if the client is ready
        if (!client) {
            throw new Error("Failed to create XMTP client");
        }

        // Enable push notifications
        const pushNotificationOptions = {
            // Customize options as needed
            onMessage: (message) => {
                console.log("New message received:", message);
                // Handle the received message (e.g., display a notification)
                displayNotification(message);
            },
            onError: (error) => {
                console.error("Push notification error:", error);
            }
        };

        // Subscribe to new messages
        client.onNewMessage(pushNotificationOptions.onMessage);
        console.log("Push notifications enabled successfully");
        
    } catch (error) {
        // Handle errors gracefully
        console.error("Error enabling push notifications:", error);
        alert("Unable to enable push notifications. Please check the console for more details.");
    }
}

// Function to display browser notifications
function displayNotification(message) {
    // Check if the browser supports notifications
    if (!("Notification" in window)) {
        console.error("This browser does not support desktop notifications.");
        return;
    }

    // Request permission to show notifications
    if (Notification.permission !== "granted") {
        Notification.requestPermission();
    }

    // Create and show the notification
    new Notification("New Message", {
        body: message.content, // Extract content from the message
        icon: "icon.png" // Optional: Replace with your own icon
    });
}

// Call the function to enable push notifications
enablePushNotifications();
```
