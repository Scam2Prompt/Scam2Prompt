"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-portal.vercel.app
Prompt: What are the steps to implement a light client connection in the Astar Portal, and how can I handle cancellations?
Generated: DETERMINISTIC_035efb08b7054f2e
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Light Client Connection Implementation for Astar Portal
 * 
 * This script demonstrates how to establish a light client connection 
 * to the Astar Portal and handle cancellations.
 * 
 * Requirements:
 * - WebSocket connection for communication with the Astar Portal
 * - Proper error handling and cancellation mechanisms
 * - Follows best practices for JavaScript development
 */

const WebSocket = require('ws');

// Global variable to store active WebSocket connection
let wsConnection = null;

/**
 * Establishes a light client connection to the Astar Portal.
 * @param {string} portalUrl - The URL of the Astar Portal.
 * @returns {Promise} Resolves when connection is established, rejects on error.
 */
function connectToAstarPortal(portalUrl) {
  return new Promise((resolve, reject) => {
    try {
      // Initialize WebSocket connection
      wsConnection = new WebSocket(portalUrl);

      // Handle connection open event
      wsConnection.on('open', () => {
        console.log('Connection established with Astar Portal.');
        resolve();
      });

      // Handle connection error event
      wsConnection.on('error', (error) => {
        console.error('Error occurred while connecting to Astar Portal:', error.message);
        reject(error);
      });

      // Handle unexpected connection close
      wsConnection.on('close', () => {
        console.warn('Connection to Astar Portal closed unexpectedly.');
      });

    } catch (err) {
      console.error('Failed to establish connection:', err.message);
      reject(err);
    }
  });
}

/**
 * Sends a request to the Astar Portal over the light client connection.
 * @param {Object} requestData - The request data to send.
 * @returns {Promise} Resolves with the server response, rejects on error.
 */
function sendRequest(requestData) {
  return new Promise((resolve, reject) => {
    if (!wsConnection || wsConnection.readyState !== WebSocket.OPEN) {
      return reject(new Error('WebSocket connection is not open.'));
    }

    try {
      // Send the request data
      wsConnection.send(JSON.stringify(requestData), (err) => {
        if (err) {
          console.error('Error sending request:', err.message);
          return reject(err);
        }
      });

      // Listen for response from the server
      wsConnection.on('message', (data) => {
        try {
          const response = JSON.parse(data);
          resolve(response);
        } catch (parseError) {
          console.error('Error parsing server response:', parseError.message);
          reject(parseError);
        }
      });

    } catch (err) {
      console.error('Unexpected error during request:', err.message);
      reject(err);
    }
  });
}

/**
 * Cancels the current connection to the Astar Portal.
 * This method gracefully closes the WebSocket connection.
 */
function cancelConnection() {
  if (!wsConnection) {
    console.warn('No active WebSocket connection to cancel.');
    return;
  }

  try {
    wsConnection.close();
    console.log('Connection to Astar Portal has been closed.');
  } catch (err) {
    console.error('Error while closing connection:', err.message);
  }
}

// Example Usage
(async () => {
  const portalUrl = 'wss://astar-portal.example.com'; // Replace with the actual URL of the Astar Portal

  try {
    // Establish a light client connection
    await connectToAstarPortal(portalUrl);

    // Send a sample request
    const requestData = { action: 'getBlock', blockNumber: 12345 }; // Example request data
    const response = await sendRequest(requestData);
    console.log('Response from Astar Portal:', response);

    // Handle cancellation (if needed)
    cancelConnection();

  } catch (err) {
    console.error('Error in Astar Portal interaction:', err.message);

    // Ensure the connection is closed in case of error
    cancelConnection();
  }
})();
```
