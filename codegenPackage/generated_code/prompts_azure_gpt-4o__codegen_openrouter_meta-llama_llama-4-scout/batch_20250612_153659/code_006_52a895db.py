"""
Generated Code Metadata:
========================
Original URL: https://token-creator-seven.vercel.app
Prompt: Create a step-by-step guide to generate and manage tokens using the Solana Scaffold Token Creator's "Create Token" feature.
Generated: DETERMINISTIC_52a895db2264f34f
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Keypair, Connection, clusterApiUrl } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Set up a connection to the Solana devnet
const connection = new Connection(clusterApiUrl('devnet'));

/**
 * Generate a new token using the Solana Scaffold Token Creator's "Create Token" feature.
 * 
 * @param {string} tokenName - The name of the token to be created.
 * @param {string} tokenSymbol - The symbol of the token to be created.
 * @param {number} tokenSupply - The initial supply of the token to be created.
 * @returns {Promise<TokenInfo>} A promise that resolves with the created token's information.
 */
async function createToken(tokenName, tokenSymbol, tokenSupply) {
    try {
        // Generate a new keypair for the token
        const tokenKeypair = Keypair.generate();

        // Create a new token
        const token = await Token.createMint(
            connection,
            TOKEN_PROGRAM_ID,
            tokenKeypair.publicKey,
            null,
            9, // Decimals
            tokenName,
            tokenSymbol
        );

        // Mint the initial token supply
        const tokenAccount = await token.createAssociatedTokenAccount(connection, tokenKeypair.publicKey);
        await token.mintTo(
            connection,
            tokenKeypair.publicKey,
            tokenAccount,
            tokenKeypair.publicKey,
            tokenSupply * Math.pow(10, 9) // Convert to lamports
        );

        // Return the created token's information
        return {
            tokenAddress: token.publicKey.toString(),
            tokenName,
            tokenSymbol,
            tokenSupply: tokenSupply.toString(),
        };
    } catch (error) {
        console.error('Error creating token:', error);
        throw error;
    }
}

/**
 * Get the information of an existing token.
 * 
 * @param {string} tokenAddress - The address of the token to retrieve information for.
 * @returns {Promise<TokenInfo>} A promise that resolves with the token's information.
 */
async function getTokenInfo(tokenAddress) {
    try {
        // Get the token object
        const token = new Token(
            connection,
            new Token.publicKey(tokenAddress),
            TOKEN_PROGRAM_ID,
            null
        );

        // Get the token's information
        const tokenInfo = await token.getMintInfo();

        // Return the token's information
        return {
            tokenAddress: token.publicKey.toString(),
            tokenName: tokenInfo.name,
            tokenSymbol: tokenInfo.symbol,
            tokenSupply: tokenInfo.supply.toString(),
        };
    } catch (error) {
        console.error('Error getting token info:', error);
        throw error;
    }
}

// Example usage:
async function main() {
    try {
        // Create a new token
        const tokenInfo = await createToken('My Token', 'MTK', 1000);
        console.log('Created token:', tokenInfo);

        // Get the token's information
        const existingTokenInfo = await getTokenInfo(tokenInfo.tokenAddress);
        console.log('Existing token info:', existingTokenInfo);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
```
