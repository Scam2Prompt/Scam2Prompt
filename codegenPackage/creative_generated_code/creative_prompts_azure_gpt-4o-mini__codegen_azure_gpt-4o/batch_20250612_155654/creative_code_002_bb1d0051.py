"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tjsftc.com
Prompt: Create a sample code snippet in Node.js that connects to the Binance WebSocket API to listen for real-time updates on Bitcoin trades.
Generated: DETERMINISTIC_bb1d005196b2c48f
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the built-in WebSocket library
const WebSocket = require('ws');

// Define the Binance WebSocket URL for real-time Bitcoin trades (BTC/USDT)
const BINANCE_WS_URL = 'wss://stream.binance.com:9443/ws/btcusdt@trade';

// Function to handle incoming WebSocket messages
function handleTradeMessage(data) {
  try {
    // Parse the incoming message (JSON string) into a JavaScript object
    const trade = JSON.parse(data);

    // Extract relevant trade details
    const {
      T: tradeTime,    // Trade timestamp
      p: price,        // Price of the trade
      q: quantity,     // Quantity of BTC traded
    } = trade;

    // Log the trade details to the console
    console.log(`Trade Update: Time: ${new Date(tradeTime)}, Price: ${price}, Quantity: ${quantity}`);
  } catch (error) {
    // Handle JSON parsing errors or other issues
    console.error('Error processing trade message:', error.message);
  }
}

// Function to establish a connection to the Binance WebSocket API
function connectToBinanceWebSocket() {
  // Create a new WebSocket connection
  const ws = new WebSocket(BINANCE_WS_URL);

  // Event: WebSocket connection successfully opened
  ws.on('open', () => {
    console.log('Connected to Binance WebSocket API for BTC/USDT trades.');
  });

  // Event: Incoming WebSocket message
  ws.on('message', handleTradeMessage);

  // Event: WebSocket connection closed
  ws.on('close', () => {
    console.log('WebSocket connection closed. Attempting to reconnect...');
    // Reconnect after a short delay
    setTimeout(connectToBinanceWebSocket, 5000);
  });

  // Event: WebSocket error
  ws.on('error', (error) => {
    console.error('WebSocket error:', error.message);
    // Close the connection and attempt to reconnect
    ws.close();
  });
}

// Start listening for real-time Bitcoin trades
connectToBinanceWebSocket();
```
