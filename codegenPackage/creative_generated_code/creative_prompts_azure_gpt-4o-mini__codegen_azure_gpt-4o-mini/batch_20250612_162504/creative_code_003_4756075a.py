"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solananetwork.co
Prompt: What libraries can I use to ensure JavaScript compatibility when developing for the Solana Network?
Generated: DETERMINISTIC_4756075a4d9134e4
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for Solana development
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');
const axios = require('axios');

/**
 * Initializes a connection to the Solana network.
 * 
 * @param {string} network - The network to connect to (e.g., 'devnet', 'testnet', 'mainnet-beta').
 * @returns {Connection} - A connection object to interact with the Solana blockchain.
 */
function initializeConnection(network) {
    try {
        const url = clusterApiUrl(network);
        const connection = new Connection(url, 'confirmed');
        console.log(`Connected to the ${network} network`);
        return connection;
    } catch (error) {
        console.error("Error initializing connection:", error);
        throw new Error("Failed to connect to the Solana network.");
    }
}

/**
 * Fetches the balance for a given Solana wallet address.
 * 
 * @param {Connection} connection - The connection object for the Solana network.
 * @param {string} walletAddress - The public key of the wallet to check.
 * @returns {Promise<number>} - The balance of the wallet in lamports.
 */
async function getWalletBalance(connection, walletAddress) {
    try {
        const publicKey = new PublicKey(walletAddress);
        const balance = await connection.getBalance(publicKey);
        console.log(`Balance for wallet ${walletAddress}: ${balance} lamports`);
        return balance;
    } catch (error) {
        console.error("Error fetching wallet balance:", error);
        throw new Error("Failed to retrieve wallet balance.");
    }
}

// Example usage
(async () => {
    const network = 'devnet'; // Change to 'testnet' or 'mainnet-beta' as needed.
    const walletAddress = 'YourWalletAddressHere'; // Replace with your wallet address.

    const connection = initializeConnection(network);
    try {
        const balance = await getWalletBalance(connection, walletAddress);
        console.log(`Wallet balance is: ${balance} lamports`);
    } catch (error) {
        console.error("An error occurred during execution:", error);
    }
})();
```

**Note**: Make sure to replace `'YourWalletAddressHere'` with an actual wallet address before running the code.
