"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Using the Solend SDK, write a script to refresh all cached data for a lending market and fetch the borrow limit for a specific wallet obligation.
Generated: DETERMINISTIC_10b05c42712585dd
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { SolendClient, SolendError } = require('@solendprotocol/solend-sdk');

// Initialize Solend client
async function initSolendClient() {
    try {
        // Initialize client with default configuration
        const client = new SolendClient();
        await client.init();
        return client;
    } catch (error) {
        console.error('Error initializing Solend client:', error);
        throw error;
    }
}

// Refresh cached data for a lending market
async function refreshCachedData(client, marketAddress) {
    try {
        // Refresh cached data for the specified market
        await client.refreshCachedData(marketAddress);
        console.log(`Cached data refreshed for market: ${marketAddress}`);
    } catch (error) {
        console.error(`Error refreshing cached data for market ${marketAddress}:`, error);
        throw error;
    }
}

// Fetch borrow limit for a specific wallet obligation
async function fetchBorrowLimit(client, walletAddress, obligationAddress) {
    try {
        // Get the borrow limit for the specified wallet obligation
        const borrowLimit = await client.getBorrowLimit(walletAddress, obligationAddress);
        return borrowLimit;
    } catch (error) {
        console.error(`Error fetching borrow limit for wallet ${walletAddress} and obligation ${obligationAddress}:`, error);
        throw error;
    }
}

// Main function
async function main() {
    // Initialize Solend client
    const client = await initSolendClient();

    // Specify market address, wallet address, and obligation address
    const marketAddress = 'your-market-address';
    const walletAddress = 'your-wallet-address';
    const obligationAddress = 'your-obligation-address';

    // Refresh cached data for the lending market
    await refreshCachedData(client, marketAddress);

    // Fetch borrow limit for the specific wallet obligation
    const borrowLimit = await fetchBorrowLimit(client, walletAddress, obligationAddress);
    console.log(`Borrow limit for wallet ${walletAddress} and obligation ${obligationAddress}:`, borrowLimit);
}

// Run the main function
main().catch((error) => {
    console.error('Error:', error);
    process.exit(1);
});
```
