"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slothanacoin.pages.dev
Prompt: Create a Solana-based script to automate the process of swapping SOL for $SLOTH tokens during the presale, including wallet connection and transaction confirmation.
Generated: DETERMINISTIC_704bf49ad68bcea0
Batch ID: 20250612_145924
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
    clusterApiUrl,
    Keypair,
    PublicKey,
    Transaction,
    SystemProgram,
    sendAndConfirmTransaction,
} = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');
const { WalletAdapterNetwork } = require('@solana/wallet-adapter-base');
const {
    PhantomWalletAdapter,
    SolletWalletAdapter,
} = require('@solana/wallet-adapter-wallets');

// Load environment variables
require('dotenv').config();

// Define constants
const NETWORK = WalletAdapterNetwork.Mainnet;
const SOL_TOKEN_MINT_ADDRESS = 'YOUR_SOL_TOKEN_MINT_ADDRESS';
const SLOTH_TOKEN_MINT_ADDRESS = 'YOUR_SLOTH_TOKEN_MINT_ADDRESS';
const SLOTH_PRESELL_ADDRESS = 'YOUR_SLOTH_PRESELL_CONTRACT_ADDRESS';

// Create a connection to the Solana blockchain
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Initialize wallet adapter (using Phantom as an example)
const wallet = new PhantomWalletAdapter();

// Function to swap SOL for SLOTH tokens
async function swapSolForSloth(amountInSOL) {
    try {
        // Connect the wallet
        await wallet.connect();

        // Get the wallet's public key
        const walletPublicKey = wallet.publicKey;

        // Calculate the amount of SLOTH tokens to receive (mock conversion rate)
        const slothAmount = amountInSOL * 100; // Example rate: 1 SOL = 100 SLOTH tokens

        // Create a transaction to send SOL and receive SLOTH tokens
        const transaction = new Transaction();

        // Create SOL transfer instruction
        const transferInstruction = SystemProgram.transfer({
            fromPubkey: walletPublicKey,
            toPubkey: new PublicKey(SLOTH_PRESELL_ADDRESS),
            lamports: amountInSOL * 1e9, // Convert SOL to lamports
        });

        transaction.add(transferInstruction);

        // Sign and send the transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, {
            signers: [wallet.publicKey],
        });

        console.log('Transaction successful with signature:', signature);
        
        // (Assuming the presale contract handles issuing SLOTH tokens)
        console.log(`You successfully swapped ${amountInSOL} SOL for ${slothAmount} SLOTH tokens.`);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
}

// Example usage: Swap 0.1 SOL for SLOTH tokens
swapSolForSloth(0.1);
```

**Note**: Replace `'YOUR_SOL_TOKEN_MINT_ADDRESS'`, `'YOUR_SLOTH_TOKEN_MINT_ADDRESS'`, and `'YOUR_SLOTH_PRESELL_CONTRACT_ADDRESS'` with the actual addresses before running the code.
