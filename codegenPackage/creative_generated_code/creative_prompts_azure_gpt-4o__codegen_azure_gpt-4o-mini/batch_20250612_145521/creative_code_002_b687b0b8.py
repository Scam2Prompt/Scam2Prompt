"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Provide a code snippet to interact with Kusama's blockchain using the Polkadot.js library, focusing on querying active accounts and transactions as discussed on Polkadot France.
Generated: DETERMINISTIC_b687b0b8d8c2ec32
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Function to initialize the connection to the Kusama blockchain
async function initializeKusamaApi() {
    // Define the WebSocket provider for Kusama
    const provider = new WsProvider('wss://kusama-rpc.polkadot.io');

    // Create the API instance
    const api = await ApiPromise.create({ provider });

    return api;
}

// Function to query active accounts and their transactions
async function queryActiveAccountsAndTransactions(api) {
    try {
        // Fetch the list of active accounts (e.g., using the session module)
        const activeAccounts = await api.query.session.validators();

        console.log('Active Accounts:');
        console.log(activeAccounts.map(account => account.toString()).join('\n'));

        // Loop through each active account and query their transactions
        for (const account of activeAccounts) {
            // Fetch the account's nonce to get the number of transactions sent
            const nonce = await api.query.system.account(account);

            console.log(`Account: ${account.toString()}`);
            console.log(`Transactions Sent: ${nonce.data.nonce.toString()}`);
        }
    } catch (error) {
        console.error('Error querying active accounts and transactions:', error);
    }
}

// Main function to execute the script
async function main() {
    // Initialize the Kusama API
    const api = await initializeKusamaApi();

    // Query active accounts and their transactions
    await queryActiveAccountsAndTransactions(api);

    // Disconnect from the API
    await api.disconnect();
}

// Execute the main function
main().catch(error => {
    console.error('Error in main execution:', error);
});
```
