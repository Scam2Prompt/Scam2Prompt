"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Write a TypeScript code snippet using the `@solendprotocol/solend-sdk` to initialize a Solend market with parameters and metadata, and then read on-chain accounts for reserve data and cache.
Generated: DETERMINISTIC_5479399bec4825b6
Batch ID: 20250622_211342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
// Import required libraries
import { SolendClient, ReserveData, ReserveCache } from '@solendprotocol/solend-sdk';
import { Connection, PublicKey } from '@solana/web3.js';

// Define constants
const SOLEND_PROGRAM_ID = new PublicKey('So1n...'); // Replace with actual Solend program ID
const RESERVE_PUBKEY = new PublicKey(' reserve...'); // Replace with actual reserve public key
const SOLANA_RPC_URL = 'https://api.devnet.solana.com'; // Replace with actual Solana RPC URL

// Initialize Solend client
async function initSolendClient(): Promise<SolendClient> {
    const connection = new Connection(SOLANA_RPC_URL);
    return new SolendClient(connection, SOLEND_PROGRAM_ID);
}

// Initialize Solend market with parameters and metadata
async function initSolendMarket(solendClient: SolendClient): Promise<void> {
    try {
        // Define market parameters
        const marketParams = {
            // Add market parameters here
            // Example:
            loanToValueRatio: 0.5,
            liquidationBonus: 0.05,
            liquidationPenalty: 0.1,
        };

        // Define market metadata
        const marketMetadata = {
            // Add market metadata here
            // Example:
            name: 'My Solend Market',
            description: 'This is my Solend market',
        };

        // Initialize market
        // Note: This might not be a real method, check @solendprotocol/solend-sdk documentation
        // await solendClient.initializeMarket(marketParams, marketMetadata);
    } catch (error) {
        console.error('Error initializing Solend market:', error);
        throw error;
    }
}

// Read on-chain accounts for reserve data and cache
async function readReserveData(solendClient: SolendClient): Promise<void> {
    try {
        // Get reserve data
        const reserveData: ReserveData = await solendClient.getReserveData(RESERVE_PUBKEY);
        console.log('Reserve data:', reserveData);

        // Get reserve cache
        const reserveCache: ReserveCache = await solendClient.getReserveCache(RESERVE_PUBKEY);
        console.log('Reserve cache:', reserveCache);
    } catch (error) {
        console.error('Error reading reserve data:', error);
        throw error;
    }
}

// Main function
async function main(): Promise<void> {
    try {
        // Initialize Solend client
        const solendClient = await initSolendClient();

        // Initialize Solend market
        await initSolendMarket(solendClient);

        // Read on-chain accounts for reserve data and cache
        await readReserveData(solendClient);
    } catch (error) {
        console.error('Error:', error);
        process.exit(1);
    }
}

// Run main function
main();
```
