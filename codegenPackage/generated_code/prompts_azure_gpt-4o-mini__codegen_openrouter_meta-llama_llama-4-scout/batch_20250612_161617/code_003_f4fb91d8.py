"""
Generated Code Metadata:
========================
Original URL: https://matrica11.vercel.app
Prompt: Provide an example of how to handle events in a multi-network blockchain application.
Generated: DETERMINISTIC_f4fb91d8fb9e5762
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EventManager.js
/**
 * EventManager class to handle events in a multi-network blockchain application.
 */
class EventManager {
  /**
   * Constructor to initialize the event manager.
   */
  constructor() {
    // Map to store event listeners
    this.listeners = new Map();
  }

  /**
   * Adds an event listener for a specific event.
   * @param {string} event - The event to listen for.
   * @param {function} callback - The callback function to execute when the event is emitted.
   */
  on(event, callback) {
    if (typeof callback !== 'function') {
      throw new Error('Callback must be a function');
    }

    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }

    this.listeners.get(event).push(callback);
  }

  /**
   * Removes an event listener for a specific event.
   * @param {string} event - The event to remove the listener for.
   * @param {function} callback - The callback function to remove.
   */
  off(event, callback) {
    if (!this.listeners.has(event)) {
      return;
    }

    const listeners = this.listeners.get(event);
    const index = listeners.indexOf(callback);

    if (index !== -1) {
      listeners.splice(index, 1);
    }
  }

  /**
   * Emits an event and executes all registered callback functions.
   * @param {string} event - The event to emit.
   * @param {...any} args - Arguments to pass to the callback functions.
   */
  emit(event, ...args) {
    if (!this.listeners.has(event)) {
      return;
    }

    this.listeners.get(event).forEach((callback) => {
      try {
        callback(...args);
      } catch (error) {
        console.error(`Error handling event ${event}:`, error);
      }
    });
  }
}

// BlockchainNetwork.js
/**
 * BlockchainNetwork class to simulate a blockchain network.
 */
class BlockchainNetwork {
  /**
   * Constructor to initialize the blockchain network.
   * @param {string} name - The name of the blockchain network.
   */
  constructor(name) {
    this.name = name;
    this.eventManager = new EventManager();
  }

  /**
   * Adds a transaction to the blockchain network.
   * @param {string} transaction - The transaction to add.
   */
  addTransaction(transaction) {
    // Simulate adding a transaction to the blockchain network
    this.eventManager.emit('transactionAdded', transaction);
  }

  /**
   * Adds an event listener for a specific event.
   * @param {string} event - The event to listen for.
   * @param {function} callback - The callback function to execute when the event is emitted.
   */
  on(event, callback) {
    this.eventManager.on(event, callback);
  }

  /**
   * Removes an event listener for a specific event.
   * @param {string} event - The event to remove the listener for.
   * @param {function} callback - The callback function to remove.
   */
  off(event, callback) {
    this.eventManager.off(event, callback);
  }
}

// MultiNetworkBlockchainApp.js
/**
 * MultiNetworkBlockchainApp class to simulate a multi-network blockchain application.
 */
class MultiNetworkBlockchainApp {
  /**
   * Constructor to initialize the multi-network blockchain application.
   */
  constructor() {
    this.networks = new Map();
  }

  /**
   * Adds a blockchain network to the application.
   * @param {BlockchainNetwork} network - The blockchain network to add.
   */
  addNetwork(network) {
    this.networks.set(network.name, network);
  }

  /**
   * Gets a blockchain network by name.
   * @param {string} name - The name of the blockchain network.
   * @returns {BlockchainNetwork} The blockchain network instance.
   */
  getNetwork(name) {
    return this.networks.get(name);
  }
}

// Example usage
function main() {
  const app = new MultiNetworkBlockchainApp();

  const network1 = new BlockchainNetwork('Network 1');
  const network2 = new BlockchainNetwork('Network 2');

  app.addNetwork(network1);
  app.addNetwork(network2);

  // Add event listeners
  network1.on('transactionAdded', (transaction) => {
    console.log(`Transaction added to ${network1.name}: ${transaction}`);
  });

  network2.on('transactionAdded', (transaction) => {
    console.log(`Transaction added to ${network2.name}: ${transaction}`);
  });

  // Add transactions to the blockchain networks
  network1.addTransaction('Transaction 1');
  network2.addTransaction('Transaction 2');

  // Remove event listener
  const callback = (transaction) => {
    console.log(`Transaction added to ${network1.name}: ${transaction}`);
  };
  network1.on('transactionAdded', callback);
  network1.off('transactionAdded', callback);
  network1.addTransaction('Transaction 3');
}

main();
```
