"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Using the Solend SDK, create a script to load reserve data for the USDC token and log the total deposits in Wads format.
Generated: DETERMINISTIC_7668862131c6ed5b
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Solend SDK
const { SolendSDK } = require('@solendprotocol/solend-sdk'); // Ensure you have the SDK installed
const { PublicKey } = require('@solana/web3.js');

// Initialize the Solend SDK
const solend = new SolendSDK();

// Define the USDC token
const USDC_MINT_ADDRESS = new PublicKey('9n4nbM71c4m7XgP8B6K3aYTHoEYF6NyJ8LNNku1t7R4A'); // Replace with actual USDC mint address

async function loadReserveData() {
    try {
        // Fetch reserve data for the USDC token
        const reserveData = await solend.getReserveData(USDC_MINT_ADDRESS);
        
        // Check if reserve data is available
        if (!reserveData) {
            console.error('No reserve data found for USDC.');
            return;
        }

        // Extract total deposits in Wads format (Wads is a scaling factor, typically 10^9)
        const totalDepositsWads = reserveData.totalDeposits.toString(); // toString for easier logging

        // Log the total deposits in Wads
        console.log(`Total Deposits for USDC in Wads: ${totalDepositsWads}`);
    } catch (error) {
        // Handle errors appropriately
        console.error('Error loading reserve data:', error);
    }
}

// Execute the script
loadReserveData();
```

**Note:** Ensure you have the Solend SDK and required dependencies installed in your project to run the script successfully.
