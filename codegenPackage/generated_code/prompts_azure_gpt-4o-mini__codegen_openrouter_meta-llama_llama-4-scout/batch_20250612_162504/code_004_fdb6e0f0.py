"""
Generated Code Metadata:
========================
Original URL: https://matrica21.vercel.app
Prompt: How do I create an event listener for network changes in a decentralized application using Matrica?
Generated: DETERMINISTIC_fdb6e0f040e227e2
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { Network } = require('@matrica/sdk');

/**
 * Creates an event listener for network changes in a decentralized application using Matrica.
 */
class NetworkChangeListener {
  /**
   * Initializes a new instance of the NetworkChangeListener class.
   * @param {Network} network - The Matrica network instance.
   */
  constructor(network) {
    if (!(network instanceof Network)) {
      throw new Error('Invalid network instance');
    }
    this.network = network;
  }

  /**
   * Starts listening for network changes.
   */
  startListening() {
    try {
      // Register event listener for network changes
      this.network.on('change', (newNetworkState) => {
        // Handle network change event
        this.handleNetworkChange(newNetworkState);
      });
    } catch (error) {
      // Log and handle any errors that occur during event listener registration
      console.error('Error starting network change listener:', error);
    }
  }

  /**
   * Stops listening for network changes.
   */
  stopListening() {
    try {
      // Remove event listener for network changes
      this.network.off('change');
    } catch (error) {
      // Log and handle any errors that occur during event listener removal
      console.error('Error stopping network change listener:', error);
    }
  }

  /**
   * Handles a network change event.
   * @param {object} newNetworkState - The new network state.
   */
  handleNetworkChange(newNetworkState) {
    // Implement custom logic to handle network changes
    console.log('Network change detected:', newNetworkState);
  }
}

// Example usage:
async function main() {
  try {
    // Initialize Matrica network instance
    const network = new Network();

    // Create a new network change listener
    const listener = new NetworkChangeListener(network);

    // Start listening for network changes
    listener.startListening();

    // Simulate a network change (for demonstration purposes only)
    network.emit('change', { status: 'online' });
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
