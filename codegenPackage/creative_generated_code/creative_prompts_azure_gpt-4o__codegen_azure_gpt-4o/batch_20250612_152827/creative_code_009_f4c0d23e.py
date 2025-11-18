"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain-app.pages.dev
Prompt: Write a JavaScript function to interact with the PulseChain websocket endpoint `ws.pulsechain.com` to monitor real-time block updates.
Generated: DETERMINISTIC_f4c0d23ea1afec05
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function connects to the PulseChain WebSocket endpoint to monitor real-time block updates.
 * It handles reconnection on errors and provides a clean API to process incoming block data.
 */

// URL of the PulseChain WebSocket endpoint
const PULSECHAIN_WS_URL = "wss://ws.pulsechain.com";

/**
 * Connects to the PulseChain WebSocket and listens for real-time block updates.
 * @param {function} onBlockUpdate - Callback function to handle received block data.
 */
function monitorPulseChainBlocks(onBlockUpdate) {
  // Ensure the provided callback is valid
  if (typeof onBlockUpdate !== "function") {
    throw new Error("onBlockUpdate must be a function.");
  }

  let socket = null;
  let reconnectTimeout = null;

  /**
   * Function to establish a WebSocket connection.
   */
  function connectWebSocket() {
    console.log("Connecting to PulseChain WebSocket...");

    try {
      socket = new WebSocket(PULSECHAIN_WS_URL);

      // Event: Connection opened
      socket.onopen = () => {
        console.log("Connected to PulseChain WebSocket.");
      };

      // Event: Receiving a message (block update)
      socket.onmessage = (event) => {
        try {
          const blockData = JSON.parse(event.data);
          onBlockUpdate(blockData); // Execute callback with parsed block data
        } catch (error) {
          console.error("Error parsing block data:", error);
        }
      };

      // Event: Connection closed
      socket.onclose = (event) => {
        console.warn(`WebSocket closed: ${event.reason}. Reconnecting...`);
        reconnect();
      };

      // Event: Error encountered
      socket.onerror = (error) => {
        console.error("WebSocket error:", error);
        socket.close(); // Force close on error
      };
    } catch (err) {
      console.error("Failed to connect to WebSocket:", err);
      reconnect();
    }
  }

  /**
   * Function to handle reconnection logic.
   */
  function reconnect() {
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
    }

    // Attempt to reconnect after a delay
    reconnectTimeout = setTimeout(() => {
      connectWebSocket();
    }, 5000); // Reconnect after 5 seconds
  }

  /**
   * Function to gracefully stop monitoring block updates.
   */
  function stopMonitoring() {
    if (socket) {
      console.log("Stopping WebSocket monitoring...");
      socket.close();
    }

    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
    }
  }

  // Start the WebSocket connection
  connectWebSocket();

  // Return a handle to stop monitoring
  return {
    stop: stopMonitoring,
  };
}

// Example usage:
const monitorHandle = monitorPulseChainBlocks((blockData) => {
  console.log("Received block update:", blockData);
});

// To stop monitoring:
// monitorHandle.stop();
```
