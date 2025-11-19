"""
Generated Code Metadata:
========================
Original URL: https://polkadot-france.fr
Prompt: Provide a code snippet to interact with Kusama's blockchain using the Polkadot.js library, focusing on querying active accounts and transactions as discussed on Polkadot France.
Generated: DETERMINISTIC_b687b0b8d8c2ec32
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from Polkadot.js
import { ApiPromise, WsProvider } from '@polkadot/api';

// Function to initialize the API connection to the Kusama blockchain
async function initKusamaApi() {
    // Define the WebSocket provider for Kusama
    const wsProvider = new WsProvider('wss://kusama-rpc.polkadot.io');

    // Create an instance of the API
    const api = await ApiPromise.create({ provider: wsProvider });

    return api;
}

// Function to query active accounts and their transactions
async function queryActiveAccounts(api) {
    try {
        // Fetch the current block number
        const currentBlock = await api.derive.chain.bestNumber();

        // Fetch the active accounts from the system
        const activeAccounts = await api.query.system.account.entries();

        console.log(`Current Block Number: ${currentBlock.toString()}`);
        console.log('Active Accounts:');

        // Iterate through active accounts and log their details
        for (const [accountId, accountInfo] of activeAccounts) {
            console.log(`Account: ${accountId.toString()}, Balance: ${accountInfo.data.free.toString()}`);
        }

        // Fetch recent transactions for each active account
        for (const [accountId] of activeAccounts) {
            const accountTransactions = await api.query.system.events.at(currentBlock);
            console.log(`Transactions for Account ${accountId.toString()}:`);

            // Filter and log transactions related to the current account
            accountTransactions.forEach(({ event }) => {
                if (event.section === 'system' && event.method === 'ExtrinsicSuccess') {
                    console.log(`- ${event.data.toString()}`);
                }
            });
        }
    } catch (error) {
        console.error('Error querying active accounts and transactions:', error);
    }
}

// Main function to run the script
(async () => {
    const api = await initKusamaApi();
    await queryActiveAccounts(api);

    // Disconnect the API after use
    await api.disconnect();
})();
```
