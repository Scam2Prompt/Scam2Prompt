"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Generate a Solend action to deposit a specific amount of SOL into the lending market using the Solend Typescript SDK.
Generated: DETERMINISTIC_d7a6a68eaefb60e7
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Solend, SolendConnection, LendMarket, DepositParams, Wallet } from '@solend/sdk';
import { Keypair, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';

/**
 * Function to deposit SOL into the lending market using the Solend SDK
 * @param wallet - The user's wallet instance
 * @param amount - The amount of SOL to deposit (in lamports)
 * @param marketAddress - The address of the lending market
 */
async function depositSOL(wallet: Wallet, amount: number, marketAddress: string) {
    try {
        // Establish connection to Solana cluster
        const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

        // Initialize Solend SDK
        const solend = new SolendConnection(connection);

        // Load the lending market
        const marketPublicKey = new PublicKey(marketAddress);
        const lendingMarket: LendMarket | null = await solend.getLendingMarket(marketPublicKey);

        if (!lendingMarket) {
            throw new Error('Lending market not found');
        }

        // Prepare deposit parameters
        const depositParams: DepositParams = {
            market: lendingMarket,
            amount: amount, // amount in lamports
            wallet: wallet.publicKey,
        };

        // Create a transaction for the deposit
        const transaction = await solend.createDepositTransaction(depositParams);

        // Send the transaction and confirm it
        const signature = await sendAndConfirmTransaction(connection, transaction, [wallet.keypair]);

        console.log('Deposit successful:', signature);
    } catch (error) {
        console.error('Error depositing SOL:', error);
    }
}

// Example usage
(async () => {
    const userKeypair = Keypair.fromSecretKey(new Uint8Array([/* your secret key */]));
    const userWallet = { publicKey: userKeypair.publicKey, keypair: userKeypair };
    const depositAmount = 1000000000; // 1 SOL in lamports
    const lendingMarketAddress = 'YourLendingMarketAddressHere'; // Replace with the actual market address

    await depositSOL(userWallet, depositAmount, lendingMarketAddress);
})();
```

**Note**: Replace `/* your secret key */` with your actual secret key array and `YourLendingMarketAddressHere` with the actual lending market address you wish to interact with.
