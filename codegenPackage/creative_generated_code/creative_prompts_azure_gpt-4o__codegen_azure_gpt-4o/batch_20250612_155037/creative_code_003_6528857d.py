"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Write a script in JavaScript or TypeScript to interact with Hyperlane's APIs for sending cross-chain messages. Include examples of initializing the API and sending a message.
Generated: DETERMINISTIC_6528857de2660fce
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hyperlane.xyz": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```typescript
// Import required modules
import axios from 'axios';

// Hyperlane API Configuration
const HYPERLANE_API_BASE_URL = 'https://api.hyperlane.xyz';
const API_TIMEOUT = 10000; // Timeout in milliseconds

// Interface for message payload
interface MessagePayload {
  destinationChain: string; // Target chain (e.g., "polygon", "avalanche")
  recipient: string;        // Recipient address on the destination chain
  message: string;          // Message you want to send
}

// Initialize the Hyperlane API client
const hyperlaneClient = axios.create({
  baseURL: HYPERLANE_API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to send a cross-chain message
async function sendCrossChainMessage(payload: MessagePayload): Promise<void> {
  try {
    // Validate the payload
    if (!payload.destinationChain || !payload.recipient || !payload.message) {
      throw new Error('Invalid payload: destinationChain, recipient, and message are required.');
    }

    // Construct POST request body
    const requestBody = {
      destinationChain: payload.destinationChain,
      recipient: payload.recipient,
      message: payload.message,
    };

    // Make API call to send the message
    const response = await hyperlaneClient.post('/send-message', requestBody);

    // Log success response
    console.log('Message sent successfully:', response.data);
  } catch (error) {
    // Handle errors
    if (axios.isAxiosError(error)) {
      console.error('API error:', error.response?.data || error.message);
    } else {
      console.error('Unexpected error:', error.message);
    }
    throw error; // Re-throw the error for upstream handling
  }
}

// Example usage of the sendCrossChainMessage function
(async () => {
  const examplePayload: MessagePayload = {
    destinationChain: 'polygon',
    recipient: '0xRecipientAddressHere',
    message: 'Hello from Hyperlane!',
  };

  try {
    console.log('Sending cross-chain message...');
    await sendCrossChainMessage(examplePayload);
    console.log('Message sent successfully.');
  } catch (error) {
    console.error('Failed to send message:', error.message);
  }
})();
```
