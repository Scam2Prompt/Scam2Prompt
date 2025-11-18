"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Write a script to interact with the Solana blockchain and claim the $Gummy airdrop using the contract address `H7bTHGb5Cvo5fGe5jBDNDPUv8KykQnzyZA3qZ8sH7yxw`.
Generated: DETERMINISTIC_a4273df299c981cb
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { Connection, PublicKey, Keypair, Transaction, SystemProgram, clusterApiUrl } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');
const fetch = require('node-fetch');

// Define constants
const AIRDROP_CONTRACT_ADDRESS = 'H7bTHGb5Cvo5fGe5jBDNDPUv8KykQnzyZA3qZ8sH7yxw';
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for mainnet
const AIRDROP_AMOUNT = 100; // Define the amount to claim

// Generate a new keypair for the wallet
const wallet = Keypair.generate();
console.log(`Generated new wallet: ${wallet.publicKey.toBase58()}`);

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

/**
 * Function to claim the airdrop
 */
async function claimAirdrop() {
    try {
        // Request airdrop from the Solana cluster
        const signature = await connection.requestAirdrop(wallet.publicKey, AIRDROP_AMOUNT);
        
        // Confirm the transaction
        await connection.confirmTransaction(signature);
        console.log(`Airdrop of ${AIRDROP_AMOUNT} lamports confirmed!`);

        // Create token instance
        const token = new Token(connection, new PublicKey(AIRDROP_CONTRACT_ADDRESS), TOKEN_PROGRAM_ID, wallet);

        // Get the associated token address for the wallet
        const tokenAccount = await token.getOrCreateAssociatedAccountInfo(wallet.publicKey);

        // Create a transaction to claim the airdrop
        const transaction = new Transaction().add(
            Token.createMintToInstruction(
                TOKEN_PROGRAM_ID,
                new PublicKey(AIRDROP_CONTRACT_ADDRESS),
                tokenAccount.address,
                wallet.publicKey,
                [],
                AIRDROP_AMOUNT
            )
        );

        // Send transaction
        const txSignature = await connection.sendTransaction(transaction, [wallet]);
        await connection.confirmTransaction(txSignature);
        console.log(`Successfully claimed ${AIRDROP_AMOUNT} $Gummy! Transaction signature: ${txSignature}`);
    } catch (error) {
        console.error('Error claiming airdrop:', error);
    }
}

// Execute the claimAirdrop function
claimAirdrop();
```

**Note:** Make sure to install the necessary packages using npm before running the script:

```bash
npm install @solana/web3.js @solana/spl-token node-fetch
```
