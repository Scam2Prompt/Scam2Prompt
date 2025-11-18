"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmtp-subscribe-push-demo.vercel.app
Prompt: Provide a code example for integrating XMTP into a web app to handle push notifications, referencing the setup used in the XMTP Subscribe Push Demo.
Generated: DETERMINISTIC_00a4597f161d21ac
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies from XMTP and other libraries
import { Client } from '@xmtp/xmtp-js';
import { getFirebaseMessagingToken, sendPushNotification } from './firebaseUtils'; // Utility functions for Firebase setup
import { initializeApp } from 'firebase/app';
import { getMessaging, onMessage } from 'firebase/messaging';

// Firebase configuration (replace with your actual Firebase project config)
const firebaseConfig = {
  apiKey: 'YOUR_FIREBASE_API_KEY',
  authDomain: 'YOUR_FIREBASE_AUTH_DOMAIN',
  projectId: 'YOUR_FIREBASE_PROJECT_ID',
  storageBucket: 'YOUR_FIREBASE_STORAGE_BUCKET',
  messagingSenderId: 'YOUR_FIREBASE_MESSAGING_SENDER_ID',
  appId: 'YOUR_FIREBASE_APP_ID',
};

// Initialize Firebase app
const firebaseApp = initializeApp(firebaseConfig);
const messaging = getMessaging(firebaseApp);

/**
 * Initialize XMTP client and subscribe to push notifications for incoming messages.
 * @param {string} walletPrivateKey - The private key for the wallet used to connect to XMTP.
 */
async function initializeXMTPandPushNotifications(walletPrivateKey) {
  try {
    // Create an XMTP client using the wallet's private key
    const xmtpClient = await Client.create(walletPrivateKey);

    // Check if the client is initialized correctly
    if (!xmtpClient) throw new Error('Failed to initialize XMTP client.');

    console.log('XMTP client initialized successfully.');

    // Retrieve Firebase messaging token
    const firebaseToken = await getFirebaseMessagingToken(messaging);
    console.log('Firebase messaging token:', firebaseToken);

    // Subscribe to XMTP conversations and listen for incoming messages
    for await (const conversation of xmtpClient.conversations.stream()) {
      console.log(`Listening to conversation with: ${conversation.peerAddress}`);

      for await (const message of conversation.streamMessages()) {
        console.log(`New message from ${conversation.peerAddress}: ${message.content}`);

        // Send a push notification for the incoming XMTP message
        await sendPushNotification(firebaseToken, {
          title: 'New Message Received',
          body: `From: ${conversation.peerAddress}`,
        });
      }
    }
  } catch (error) {
    console.error('Error initializing XMTP or push notifications:', error);
  }
}

// Listen for Firebase push notifications in the browser
onMessage(messaging, (payload) => {
  console.log('Push notification received:', payload);
});

/**
 * Example usage of the XMTP and Firebase integration.
 */
(async () => {
  // Replace this with the actual wallet private key
  const walletPrivateKey = 'YOUR_WALLET_PRIVATE_KEY';

  // Initialize XMTP and push notifications
  await initializeXMTPandPushNotifications(walletPrivateKey);
})();
```
