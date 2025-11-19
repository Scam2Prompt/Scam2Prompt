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
// Import XMTP SDK
import { Client } from '@xmtp/xmtp-js';

// Function to initialize XMTP client
async function initializeXMTPClient(wallet) {
  try {
    // Create a new XMTP client using the wallet signer
    const xmtpClient = await Client.create(wallet);

    // Ensure the client is connected
    if (!xmtpClient) {
      throw new Error('Failed to initialize XMTP client');
    }

    console.log('XMTP client initialized successfully');
    return xmtpClient;
  } catch (error) {
    console.error('Error initializing XMTP client:', error.message);
    throw error;
  }
}

// Function to listen for incoming messages
async function listenForMessages(xmtpClient) {
  try {
    // Retrieve conversations for the client
    const conversations = await xmtpClient.conversations.list();

    // Iterate through each conversation
    conversations.forEach(async (conversation) => {
      console.log(`Listening to messages from: ${conversation.peerAddress}`);

      // Subscribe to new messages for the conversation
      for await (const message of conversation.streamMessages()) {
        console.log(`New message received from ${conversation.peerAddress}:`, message.content);
        // Add logic here to trigger a push notification
        showPushNotification(conversation.peerAddress, message.content);
      }
    });
  } catch (error) {
    console.error('Error listening for messages:', error.message);
    throw error;
  }
}

// Function to display push notifications
function showPushNotification(peerAddress, messageContent) {
  // Check if the browser supports Notifications API
  if (!('Notification' in window)) {
    console.error('This browser does not support push notifications');
    return;
  }

  // Request notification permission from the user
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      // Display the notification
      new Notification(`Message from ${peerAddress}`, {
        body: messageContent,
      });
    } else {
      console.warn('Push notification permission denied');
    }
  });
}

// Example usage
(async function () {
  try {
    // Replace this with your wallet signer implementation
    const walletSigner = await getWalletSigner(); // A function that retrieves your wallet signer
    const xmtpClient = await initializeXMTPClient(walletSigner);

    // Start listening for incoming XMTP messages
    await listenForMessages(xmtpClient);
  } catch (error) {
    console.error('Error in XMTP integration:', error.message);
  }
})();

// Helper function placeholder to get wallet signer
// Replace this with actual code to retrieve your wallet signer (e.g., MetaMask, WalletConnect, etc.)
async function getWalletSigner() {
  // Example using MetaMask
  if (window.ethereum) {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    return provider.getSigner(accounts[0]);
  } else {
    throw new Error('Ethereum provider not detected');
  }
}
```
