"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Generate code to interact with the Polkadot blockchain using the Polkadot.js library.
Generated: DETERMINISTIC_46883456a7946ccc
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to connect to the Polkadot blockchain
async function connectToPolkadot() {
  try {
    // Define the WebSocket endpoint for the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create an API instance connected to the Polkadot network
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot blockchain.');

    return api; // Return the API instance for further interaction
  } catch (error) {
    console.error('Error connecting to the Polkadot blockchain:', error);
    throw error; // Rethrow the error for proper handling
  }
}

// Function to fetch the latest block number
async function getLatestBlockNumber(api) {
  try {
    // Retrieve the latest block header
    const latestHeader = await api.rpc.chain.getHeader();

    console.log(`Latest block number: ${latestHeader.number}`);

    return latestHeader.number; // Return the block number
  } catch (error) {
    console.error('Error fetching the latest block number:', error);
    throw error; // Rethrow the error for proper handling
  }
}

// Function to fetch account balance
async function getAccountBalance(api, address) {
  try {
    // Retrieve the account balance using the address
    const { data: { free: balance } } = await api.query.system.account(address);

    console.log(`Balance for ${address}: ${balance.toHuman()}`);

    return balance; // Return the balance
  } catch (error) {
    console.error(`Error fetching balance for address ${address}:`, error);
    throw error; // Rethrow the error for proper handling
  }
}

// Main function to demonstrate usage
async function main() {
  try {
    // Connect to the Polkadot blockchain
    const api = await connectToPolkadot();

    // Fetch the latest block number
    await getLatestBlockNumber(api);

    // Replace with a valid Polkadot address to fetch its balance
    const address = '12D3KooWJ...'; // Example address (replace with a real one)
    await getAccountBalance(api, address);

    // Disconnect from the API when done
    await api.disconnect();
    console.log('Disconnected from the Polkadot blockchain.');
  } catch (error) {
    console.error('An error occurred in the main function:', error);
  }
}

// Execute the main function
main();
```

This code is ready to interact with the Polkadot blockchain using the Polkadot.js library. Replace the example address with a valid Polkadot address to fetch its balance. Ensure you have the `@polkadot/api` library installed in your project (`npm install @polkadot/api`) before running the code.
