"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Write a JavaScript function to display real-time updates of ETH deposits and wallet addresses participating in a token presale, inspired by the DOG token presale webpage.
Generated: DETERMINISTIC_3b0308d6b758bc6e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to display real-time updates of ETH deposits and wallet addresses
// participating in a token presale.

const WebSocket = require('ws'); // Import WebSocket for real-time updates

// Presale WebSocket URL (replace with actual endpoint)
const PRESALE_WS_URL = 'wss://example-presale-websocket-url';

// HTML Elements for displaying data (Assumes these exist in your HTML)
const depositsListElement = document.getElementById('deposits-list');
const participantsCountElement = document.getElementById('participants-count');

// Initialize WebSocket connection
function initializePresaleUpdates() {
  const ws = new WebSocket(PRESALE_WS_URL);

  // Event: Connection opened
  ws.onopen = () => {
    console.log('Connected to the presale WebSocket server.');
    // Optionally, send a subscription message if required by the server
    // ws.send(JSON.stringify({ action: 'subscribe', channel: 'eth-deposits' }));
  };

  // Event: Message received
  ws.onmessage = (event) => {
    try {
      // Parse incoming data
      const data = JSON.parse(event.data);

      // Validate data structure
      if (!data.walletAddress || !data.depositAmount) {
        console.warn('Invalid data format received:', data);
        return;
      }

      // Update the deposits list
      updateDepositsList(data.walletAddress, data.depositAmount);

      // Update participants count
      updateParticipantsCount(data.totalParticipants);
    } catch (error) {
      console.error('Error processing WebSocket message:', error);
    }
  };

  // Event: Connection closed
  ws.onclose = () => {
    console.warn('WebSocket connection closed. Reconnecting...');
    // Retry connection after a delay
    setTimeout(initializePresaleUpdates, 5000);
  };

  // Event: Error occurred
  ws.onerror = (error) => {
    console.error('WebSocket encountered an error:', error);
  };
}

// Function to update the deposits list
function updateDepositsList(walletAddress, depositAmount) {
  const listItem = document.createElement('li');
  listItem.textContent = `Wallet: ${walletAddress}, Deposit: ${depositAmount} ETH`;
  depositsListElement.appendChild(listItem);
}

// Function to update the participants count
function updateParticipantsCount(totalParticipants) {
  participantsCountElement.textContent = `Total Participants: ${totalParticipants}`;
}

// Start the WebSocket connection
initializePresaleUpdates();
```
