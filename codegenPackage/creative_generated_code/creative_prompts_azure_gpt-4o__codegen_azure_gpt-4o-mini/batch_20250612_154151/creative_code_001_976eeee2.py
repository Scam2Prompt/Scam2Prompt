"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zip-4t3.pages.dev
Prompt: Generate code that connects to a Solana wallet and executes a token swap between SOL and ORCA using the Orca trade pool API.
Generated: DETERMINISTIC_976eeee27c4fd37e
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const {
    Connection,
    Keypair,
    PublicKey,
    clusterApiUrl,
} = require('@solana/web3.js');

const {
    TokenInstructions,
    TOKEN_PROGRAM_ID,
} = require('@solana/spl-token');

const {
    Orca,
    OrcaPool,
    ORCA_DEVNET_POOL_ID,
    ORCA_MAINNET_POOL_ID,
} = require('@orca-so/sdk');

// Function to swap tokens between SOL and ORCA
async function swapSolToOrca(wallet, amountInSol) {
    try {
        // Establish a connection to the Solana cluster
        const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

        // Initialize Orca with the connection
        const orca = Orca.fetcher(connection);

        // Define the pool for SOL/ORCA on Devnet
        const pool = orca.pool(ORCA_DEVNET_POOL_ID);

        // Calculate the amount of ORCA to receive
        const amountInLamports = amountInSol * Math.pow(10, 9); // Convert SOL to lamports (1 SOL = 10^9 lamports)
        const swapInfo = await pool.getQuote(amountInLamports, TokenInstructions.TOKEN_PROGRAM_ID);

        // Execute the swap
        const transaction = await swapInfo.swap(wallet, amountInLamports);

        // Send the transaction
        const signature = await connection.sendTransaction(transaction, [wallet]);

        // Wait for confirmation
        await connection.confirmTransaction(signature);

        console.log(`Swap successful! Transaction signature: ${signature}`);
    } catch (error) {
        console.error("Error during token swap:", error);
    }
}

// Main function to run the swap operation
async function main() {
    // Load or create a wallet
    const wallet = Keypair.generate(); // Replace with loading an existing wallet

    const amountInSol = 0.1; // Amount of SOL to swap for ORCA

    // Call the swap function
    await swapSolToOrca(wallet, amountInSol);
}

// Execute the main function
main().catch(err => {
    console.error("Error in main function:", err);
});
```

**Note:** Ensure that you have the required libraries installed in your project. You can install them using npm:

```bash
npm install @solana/web3.js @solana/spl-token @orca-so/sdk
``` 

Also, replace `Keypair.generate()` with your actual wallet loading logic if you're using an existing wallet.
