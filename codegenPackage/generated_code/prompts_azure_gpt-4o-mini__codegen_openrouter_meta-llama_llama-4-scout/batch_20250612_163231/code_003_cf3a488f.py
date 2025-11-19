"""
Generated Code Metadata:
========================
Original URL: https://beta.portal-bridge.com
Prompt: Provide an example of how to select chains and tokens for a transaction with the Portal Token Bridge.
Generated: DETERMINISTIC_cf3a488f8393cdc4
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * @fileoverview This script demonstrates how to select chains and tokens for a transaction with the Portal Token Bridge.
 * @author [Your Name]
 */

// Import required libraries
const { TokenBridge, ChainId, Token } = require('@solana/portal-token-bridge');

/**
 * @description Select chains and tokens for a transaction with the Portal Token Bridge.
 * @param {ChainId} sourceChainId - The source chain ID.
 * @param {ChainId} destinationChainId - The destination chain ID.
 * @param {string} tokenAddress - The token address.
 * @returns {Promise<{ sourceChainId: ChainId, destinationChainId: ChainId, token: Token }>} 
 *          A promise that resolves with the selected chains and token.
 */
async function selectChainsAndToken(sourceChainId, destinationChainId, tokenAddress) {
    try {
        // Initialize the Token Bridge
        const tokenBridge = new TokenBridge();

        // Validate chain IDs
        if (!ChainId[sourceChainId] || !ChainId[destinationChainId]) {
            throw new Error('Invalid chain ID');
        }

        // Get the token
        const token = await tokenBridge.getToken(tokenAddress);
        if (!token) {
            throw new Error('Token not found');
        }

        // Return the selected chains and token
        return {
            sourceChainId,
            destinationChainId,
            token,
        };
    } catch (error) {
        // Log and rethrow the error
        console.error('Error selecting chains and token:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        // Define the source and destination chain IDs
        const sourceChainId = ChainId.SOLANA;
        const destinationChainId = ChainId.ETHEREUM;

        // Define the token address
        const tokenAddress = '4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU';

        // Select the chains and token
        const { sourceChainId: selectedSourceChainId, destinationChainId: selectedDestinationChainId, token } = 
            await selectChainsAndToken(sourceChainId, destinationChainId, tokenAddress);

        // Log the selected chains and token
        console.log('Selected Source Chain ID:', selectedSourceChainId);
        console.log('Selected Destination Chain ID:', selectedDestinationChainId);
        console.log('Selected Token:', token);
    } catch (error) {
        // Log the error
        console.error('Error:', error);
    }
}

// Run the example
main();
```
