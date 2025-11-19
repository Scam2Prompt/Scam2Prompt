"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radyamswap.godaddysites.com
Prompt: What are the steps to swap tokens on Raydium Swap, and how can I minimize slippage during the transaction?
Generated: DETERMINISTIC_2921656d8e9067a9
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const { Connection, clusterApiUrl, PublicKey, Keypair } = require('@solana/web3.js');
const { TokenInstructions, Token } = require('@solana/spl-token');
const { swap, getSwapInfo, getMinOutAmount } = require('@raydium-io/raydium-sdk');

(async () => {
    // Set up connection to Solana cluster
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

    // Define user wallet and tokens
    const userWallet = Keypair.generate(); // Replace with user's wallet
    const fromTokenMint = new PublicKey('<FROM_TOKEN_MINT_ADDRESS>'); // Replace with the mint address of the token to swap from
    const toTokenMint = new PublicKey('<TO_TOKEN_MINT_ADDRESS>'); // Replace with the mint address of the token to swap to
    const amountIn = 1000000; // Amount of the fromToken to swap (in the smallest unit, e.g., lamports)

    // Fetch the swap information
    const swapInfo = await getSwapInfo(connection, fromTokenMint, toTokenMint);
    if (!swapInfo) throw new Error('Swap information could not be retrieved.');

    // Calculate minimum output amount to minimize slippage
    const slippage = 0.01; // Define slippage percentage (1%)
    const minOutAmount = await getMinOutAmount(amountIn, swapInfo, slippage);

    // Prepare the swap transaction
    const transaction = await swap({
        connection,
        userWallet,
        fromTokenMint,
        toTokenMint,
        amountIn,
        minOutAmount,
        slippage
    });

    // Sign and send the transaction
    try {
        const signature = await connection.sendTransaction(transaction, [userWallet]);
        console.log(`Transaction successful with signature: ${signature}`);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
})();
```

**Note:** 
- Replace `<FROM_TOKEN_MINT_ADDRESS>` and `<TO_TOKEN_MINT_ADDRESS>` with actual addresses of the tokens you wish to swap.
- This code assumes you have already set up the necessary dependencies and environment to run a Node.js application with Solana and Raydium SDKs.
- Ensure proper wallet handling and security practices are in place for production usage.
