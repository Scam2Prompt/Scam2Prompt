"""
Generated Code Metadata:
========================
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: What are the best practices for integrating Polkadot's JavaScript API into a decentralized application, considering the provided project setup?
Generated: DETERMINISTIC_d37caae70fee5b8e
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from Polkadot's API
import { ApiPromise, WsProvider } from '@polkadot/api';

// Define a function to initialize the Polkadot API
async function initPolkadotApi() {
    // Define the WebSocket provider URL for connecting to the Polkadot network
    const wsProviderUrl = 'wss://rpc.polkadot.io'; // Change this to your desired network

    // Create a new WebSocket provider
    const provider = new WsProvider(wsProviderUrl);

    try {
        // Create an API instance using the provider
        const api = await ApiPromise.create({ provider });

        console.log('Polkadot API initialized successfully');
        return api;
    } catch (error) {
        console.error('Error initializing Polkadot API:', error);
        throw new Error('Failed to initialize Polkadot API');
    }
}

// Define a function to fetch the latest block number
async function fetchLatestBlock(api) {
    try {
        // Retrieve the latest block number from the blockchain
        const lastHeader = await api.rpc.chain.getHeader();
        console.log(`Latest block number: ${lastHeader.number}`);
        return lastHeader.number.toNumber();
    } catch (error) {
        console.error('Error fetching latest block:', error);
        throw new Error('Failed to fetch latest block');
    }
}

// Define a function to send a transaction
async function sendTransaction(api, sender, recipient, amount, signer) {
    try {
        // Create a transfer transaction
        const transfer = api.tx.balances.transfer(recipient, amount);

        // Sign and send the transaction
        const hash = await transfer.signAndSend(sender, { signer });
        console.log('Transaction sent with hash:', hash.toHex());
        return hash;
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw new Error('Failed to send transaction');
    }
}

// Main function to run the application
(async () => {
    // Initialize the Polkadot API
    const api = await initPolkadotApi();

    // Fetch the latest block number
    await fetchLatestBlock(api);

    // Example usage of sendTransaction (replace with actual values)
    // const sender = 'YOUR_SENDER_ADDRESS';
    // const recipient = 'RECIPIENT_ADDRESS';
    // const amount = 1000000000; // Amount in the smallest unit (e.g., Plancks)
    // const signer = YOUR_SIGNER_OBJECT; // Replace with your signer object

    // Uncomment the following line to send a transaction
    // await sendTransaction(api, sender, recipient, amount, signer);
})();
```
