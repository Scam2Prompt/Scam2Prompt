"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.web.app
Prompt: Generate a JavaScript function to cancel a Light client connection to the Astar Network.
Generated: DETERMINISTIC_d1ae6c5cb02312c7
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cancels a Light client connection to the Astar Network.
 * 
 * This function assumes the Light client connection is managed via a WebSocket or similar mechanism.
 * It gracefully closes the connection and handles any errors during the process.
 * 
 * @param {WebSocket} connection - The WebSocket connection to the Astar Network.
 * @returns {Promise<void>} - Resolves when the connection is successfully closed.
 */
async function cancelAstarConnection(connection) {
    // Validate the input
    if (!(connection instanceof WebSocket)) {
        throw new Error("Invalid connection object. Expected a WebSocket instance.");
    }

    // Check if the connection is already closed
    if (connection.readyState === WebSocket.CLOSED) {
        console.warn("Connection is already closed.");
        return;
    }

    return new Promise((resolve, reject) => {
        try {
            // Set up event listeners for graceful closure
            connection.onclose = () => {
                console.log("Connection to Astar Network successfully closed.");
                resolve();
            };

            connection.onerror = (error) => {
                console.error("Error occurred while closing the connection:", error);
                reject(error);
            };

            // Close the connection
            console.log("Closing connection to Astar Network...");
            connection.close();
        } catch (error) {
            // Handle unexpected errors
            console.error("Unexpected error while attempting to close the connection:", error);
            reject(error);
        }
    });
}

// Example usage:
// const ws = new WebSocket("wss://astar.network");
// cancelAstarConnection(ws).catch((error) => console.error("Failed to cancel connection:", error));
```
