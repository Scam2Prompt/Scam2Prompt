"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Write a code snippet to read on-chain accounts for reserve data using the Solend SDK and log the total deposits for USDC.
Generated: DETERMINISTIC_c6c0438a2de1d40a
Batch ID: 20250612_163243
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Solend SDK and other required libraries
import { Connection } from '@solana/web3.js';
import { getReserveData, ReserveData } from '@solend/sdk';

// Define constants for the Solana network and USDC mint address
const SOLANA_NETWORK = 'https://api.mainnet-beta.solana.com';
const USDC_MINT_ADDRESS = 'A1n4n8K8bY8nXYWQW3on1N1R52KJxW2nwYb5M2uAPtFg'; // Replace with the actual USDC mint address

/**
 * Fetch and log the total deposits for USDC from the Solend protocol.
 */
async function logTotalUSDCDeposits() {
    try {
        // Create a connection to the Solana blockchain
        const connection = new Connection(SOLANA_NETWORK, 'confirmed');

        // Retrieve reserve data for USDC
        const reserveData: ReserveData = await getReserveData(connection, USDC_MINT_ADDRESS);

        // Check if the reserve data is available
        if (reserveData) {
            // Calculate total deposits (in Lamports)
            const totalDeposits = reserveData.totalDeposits.toNumber(); // Convert to a number for easier readability

            // Log the total deposits for USDC
            console.log(`Total deposits for USDC: ${totalDeposits} Lamports`);
        } else {
            console.error('No reserve data found for USDC.');
        }
    } catch (error) {
        // Handle and log any errors that occur during the process
        console.error('Error fetching USDC reserve data:', error);
    }
}

// Execute the function to log total USDC deposits
logTotalUSDCDeposits();
```
