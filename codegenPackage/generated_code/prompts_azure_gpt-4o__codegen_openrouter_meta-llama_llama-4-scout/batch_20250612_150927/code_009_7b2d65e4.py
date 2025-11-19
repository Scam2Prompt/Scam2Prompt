"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Write a TypeScript script using the Solend SDK to initialize a lending market, deposit collateral, and withdraw liquidity in a single transaction.
Generated: DETERMINISTIC_7b2d65e469d40214
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries
import { SolendClient, Reserve, AssetType } from '@solendprotocol/solend-sdk';
import { clusterApiUrl, Connection } from '@solana/web3.js';

// Set up Solend client and Solana connection
const solendClient = new SolendClient();
const connection = new Connection(clusterApiUrl('devnet'));

// Set up keypair and addresses
// Replace with your own keypair and addresses
const keypair = solendClient.createKeypair('your_private_key');
const userAddress = keypair.publicKey;
const solendProgramId = solendClient.programId;

// Initialize lending market, deposit collateral, and withdraw liquidity in a single transaction
async function lendingMarketTransaction() {
    try {
        // Initialize lending market
        const reserveAddress = await solendClient.initializeLendingMarket({
            lendingMarketAuthority: solendProgramId,
            reserve: {
                address: userAddress,
                collateralMint: '4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU', // USDC mint address
                collateralDecimals: 6,
                assetType: AssetType.COLLATERAL,
            },
        });

        // Deposit collateral
        const depositAmount = 1000; // Deposit 1000 USDC
        const depositTx = await solendClient.deposit({
            user: userAddress,
            reserve: reserveAddress,
            amount: depositAmount,
        });

        // Withdraw liquidity
        const withdrawAmount = 500; // Withdraw 500 USDC
        const withdrawTx = await solendClient.withdraw({
            user: userAddress,
            reserve: reserveAddress,
            amount: withdrawAmount,
        });

        // Create a single transaction with all instructions
        const transaction = solendClient.createTransaction();
        transaction.add(depositTx.instructions[0]);
        transaction.add(withdrawTx.instructions[0]);

        // Sign and send the transaction
        const signedTransaction = await solendClient.signTransaction(transaction, keypair);
        const txid = await connection.sendTransaction(signedTransaction);

        console.log(`Transaction successful: ${txid}`);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Run the lending market transaction
lendingMarketTransaction();
```
