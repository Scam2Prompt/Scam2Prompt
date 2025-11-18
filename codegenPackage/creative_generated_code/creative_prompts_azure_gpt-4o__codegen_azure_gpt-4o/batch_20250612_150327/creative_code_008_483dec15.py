"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethtoken.net
Prompt: Write a script in Node.js to monitor StethToken transactions in real-time using WebSocket connections.
Generated: DETERMINISTIC_483dec15ee3d8930
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const WebSocket = require('ws');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Configuration
const WEBSOCKET_URL = process.env.WEBSOCKET_URL || 'wss://example.com/ws'; // Replace with the actual WebSocket URL
const STETH_TOKEN_ADDRESS = process.env.STETH_TOKEN_ADDRESS || '0xYourTokenAddressHere'; // Replace with the actual StethToken address

// Initialize WebSocket connection
const ws = new WebSocket(WEBSOCKET_URL);

// Utility function to validate incoming data
function isValidTransaction(data) {
    try {
        // Ensure the data contains expected fields and matches the token's address
        return (
            data &&
            data.tokenAddress &&
            data.tokenAddress.toLowerCase() === STETH_TOKEN_ADDRESS.toLowerCase() &&
            data.transactionType &&
            data.amount
        );
    } catch (error) {
        console.error('Error validating transaction data:', error);
        return false;
    }
}

// Handle WebSocket connection open event
ws.on('open', () => {
    console.log('WebSocket connection established to:', WEBSOCKET_URL);

    // Subscribe to StethToken transactions (example payload, modify as required for your API)
    const subscriptionPayload = {
        type: 'subscribe',
        channel: 'transactions',
        tokenAddress: STETH_TOKEN_ADDRESS,
    };

    ws.send(JSON.stringify(subscriptionPayload));
    console.log('Subscribed to StethToken transactions.');
});

// Handle incoming WebSocket messages
ws.on('message', (message) => {
    try {
        const data = JSON.parse(message);

        // Validate and handle transaction data
        if (isValidTransaction(data)) {
            console.log('New StethToken transaction detected:');
            console.log(`Transaction Type: ${data.transactionType}`);
            console.log(`Amount: ${data.amount}`);
            console.log(`From: ${data.from}`);
            console.log(`To: ${data.to}`);
        } else {
            console.warn('Received invalid or unrelated transaction data:', data);
        }
    } catch (error) {
        console.error('Error processing WebSocket message:', error);
    }
});

// Handle WebSocket error events
ws.on('error', (error) => {
    console.error('WebSocket error:', error);
});

// Handle WebSocket close events
ws.on('close', (code, reason) => {
    console.log(`WebSocket connection closed. Code: ${code}, Reason: ${reason}`);
});

// Graceful shutdown on process exit
process.on('SIGINT', () => {
    console.log('Shutting down WebSocket connection...');
    ws.close();
    process.exit();
});
```

Make sure to install the required dependencies for this script:

```bash
npm install ws dotenv
```

Additionally, provide a `.env` file with the correct values for `WEBSOCKET_URL` and `STETH_TOKEN_ADDRESS`.
