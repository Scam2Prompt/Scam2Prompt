"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Generate a step-by-step tutorial for integrating deBridge's cross-chain bridging functionality into a Solana-based DeFi protocol.
Generated: DETERMINISTIC_f854a105b9a58a2c
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { deBridge } = require('@debridge-finance/sdk');

// Configuration for connecting to Solana
const SOLANA_NETWORK = 'mainnet-beta'; // Change to 'devnet' for testing
const SOLANA_RPC_URL = clusterApiUrl(SOLANA_NETWORK);

// Initialize Solana connection
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');

/**
 * Function to bridge tokens from one blockchain to another using deBridge
 * @param {string} sourceToken - The address of the source token
 * @param {string} targetToken - The address of the target token
 * @param {number} amount - The amount of tokens to bridge
 * @param {string} recipient - The recipient's address on the target chain
 */
async function bridgeTokens(sourceToken, targetToken, amount, recipient) {
    try {
        // Validate inputs
        if (!PublicKey.isOnCurve(sourceToken) || !PublicKey.isOnCurve(targetToken)) {
            throw new Error('Invalid token address.');
        }
        if (amount <= 0) {
            throw new Error('Amount must be greater than zero.');
        }
        if (!PublicKey.isOnCurve(recipient)) {
            throw new Error('Invalid recipient address.');
        }

        // Initialize deBridge SDK
        const deb = new deBridge.DeBridge({
            network: SOLANA_NETWORK,
            connection: connection,
        });

        // Check balance of the source token
        const balance = await connection.getTokenAccountBalance(new PublicKey(sourceToken));
        if (balance.value.uiAmount < amount) {
            throw new Error('Insufficient balance.');
        }

        // Initiate the bridging process
        const tx = await deb.bridge({
            from: sourceToken,
            to: targetToken,
            amount,
            recipient,
        });

        console.log('Bridging transaction successful: ', tx);
        return tx;

    } catch (error) {
        // Handle errors and log them
        console.error('Error during token bridging: ', error.message);
        throw error; // Rethrow error after logging
    }
}

// Example usage
(async () => {
    const sourceToken = 'sourceTokenAddress';
    const targetToken = 'targetTokenAddress';
    const amount = 10; // Amount to bridge
    const recipient = 'recipientAddress';

    try {
        const txResult = await bridgeTokens(sourceToken, targetToken, amount, recipient);
        console.log('Bridging result: ', txResult);
    } catch (error) {
        console.error('Bridging failed: ', error.message);
    }
})();
```
