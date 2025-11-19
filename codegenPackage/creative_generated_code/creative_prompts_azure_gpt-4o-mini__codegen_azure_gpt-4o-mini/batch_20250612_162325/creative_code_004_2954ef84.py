"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orca-2-git-tmoc-modify-liquidity-modals-2-orca-so.vercel.app
Prompt: How do I implement auto-buy functionality for ORCA tokens using the Orca liquidity modals?
Generated: DETERMINISTIC_2954ef84f92328f3
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Orca, Network } from '@orca-so/sdk';

// Configuration for the Solana connection and Orca
const NETWORK = Network.MAINNET; // Choose the network
const ORCA_POOL_ID = 'YourPoolId'; // Replace with your actual pool ID
const ORCA_TOKEN_MINT = 'YourTokenMint'; // Replace with the mint address of the ORCA token
const USER_WALLET = 'YourWalletAddress'; // Replace with the user's wallet address
const PRIVATE_KEY = 'YourPrivateKey'; // Replace with the user's private key (keep it safe)

// Initialize the connection to the Solana blockchain
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Async function to perform the auto-buy
async function autoBuyOrcaTokens(amountIn) {
    try {
        // Initialize Orca SDK
        const orca = Orca.getOrca(connection, NETWORK);
        
        // Fetch the pool
        const orcaPool = orca.getPool(ORCA_POOL_ID);
        
        // Check if the user has enough funds
        const userBalance = await connection.getTokenAccountBalance(new PublicKey(ORCA_TOKEN_MINT));
        if (userBalance.value.uiAmount < amountIn) {
            throw new Error(`Insufficient balance: ${userBalance.value.uiAmount} available, ${amountIn} required.`);
        }

        // Define the transaction for buying ORCA tokens
        const transaction = await orcaPool.getQuote(amountIn, orcaPool.getQuoteToken());
        
        // Construct the transaction instruction
        const instructions = await transaction.buildTransaction();

        // Sign and send the transaction
        const { signature } = await connection.sendTransaction(instructions, [PRIVATE_KEY], { skipPreflight: false });

        // Confirm the transaction
        await connection.confirmTransaction(signature, 'confirmed');
        console.log(`Transaction successful with signature: ${signature}`);
    } catch (error) {
        console.error('An error occurred while trying to auto-buy ORCA tokens:', error.message);
    }
}

// Example usage
autoBuyOrcaTokens(1.0); // Example to buy 1 ORCA token
```

**Note**: 
- Replace placeholder values for `YourPoolId`, `YourTokenMint`, `YourWalletAddress`, and `YourPrivateKey` with valid data.
- Ensure that the private key is handled securely and not hardcoded in production code.
- This code is a simplified example and may require further adjustments based on the specific Orca SDK version and the actual implementation context.
