"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Write code to configure MetaMask Snaps for extending wallet functionality with third-party features.
Generated: DETERMINISTIC_689a4fae58ccf8fd
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import { OnRpcRequestHandler } from '@metamask/snaps-utils';
import { snap } from '@metamask/snaps';

// Define the Snap's configuration
const SNAP_ID = 'your-snap-id'; // Replace with your Snap ID

/**
 * The main handler for the Snap's RPC requests.
 * @param {Object} request - The RPC request object containing method and params.
 * @returns {Promise<any>} - The result of the Snap's operation.
 */
export const onRpcRequest: OnRpcRequestHandler = async ({ request }) => {
    switch (request.method) {
        case 'getBalance':
            return await getBalance(request.params);
        case 'getTransactionHistory':
            return await getTransactionHistory(request.params);
        default:
            throw new Error('Method not found');
    }
};

/**
 * Fetch the balance for a given address.
 * @param {string} address - The Ethereum address to fetch the balance for.
 * @returns {Promise<string>} - The balance of the specified address.
 */
const getBalance = async (address) => {
    try {
        // Validate input
        if (!isValidAddress(address)) {
            throw new Error('Invalid Ethereum address');
        }

        // Call an external API or use a blockchain provider to get the balance
        const balance = await snap.request({
            method: 'eth_getBalance',
            params: [address, 'latest'],
        });

        // Convert balance from Wei to Ether
        return parseFloat(balance) / 1e18; 
    } catch (error) {
        console.error('Error fetching balance:', error);
        throw new Error('Failed to fetch balance');
    }
};

/**
 * Get the transaction history for a given address.
 * @param {string} address - The Ethereum address to fetch transaction history for.
 * @returns {Promise<Array>} - The transaction history of the specified address.
 */
const getTransactionHistory = async (address) => {
    try {
        // Validate input
        if (!isValidAddress(address)) {
            throw new Error('Invalid Ethereum address');
        }

        // Implement logic to fetch transaction history (dummy data for example)
        const transactions = await fetchTransactionHistoryFromAPI(address);

        return transactions;
    } catch (error) {
        console.error('Error fetching transaction history:', error);
        throw new Error('Failed to fetch transaction history');
    }
};

/**
 * Validate Ethereum address format.
 * @param {string} address - The Ethereum address to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
const isValidAddress = (address) => {
    return /^0x[a-fA-F0-9]{40}$/.test(address);
};

/**
 * Placeholder function to simulate fetching transaction history.
 * In production, this should call a blockchain explorer API or similar service.
 * @param {string} address - The Ethereum address to fetch transactions for.
 * @returns {Promise<Array>} - An array of transaction objects.
 */
const fetchTransactionHistoryFromAPI = async (address) => {
    // Simulating API response
    return [
        { txHash: '0x123...', to: address, from: '0xabc...', value: '0.1', timestamp: Date.now() },
        { txHash: '0x456...', to: address, from: '0xdef...', value: '0.2', timestamp: Date.now() },
    ];
};

// Set the Snap's configuration
snap.init({
    onRpcRequest,
    snapId: SNAP_ID,
    // Additional configurations can be added here
});
```

This code provides a basic structure for a MetaMask Snap that allows users to fetch their Ethereum balance and transaction history. It includes input validation, error handling, and documentation for clarity.
