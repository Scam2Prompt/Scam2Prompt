"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-layer-auth.pages.dev
Prompt: Generate code to integrate BONK token transactions into a Solana-based decentralized application (dApp), leveraging the multi-chain wormhole support mentioned on the BONK Layer Auth site.
Generated: DETERMINISTIC_4ab6416a5704e982
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and libraries
const web3 = require('@solana/web3.js'); // Solana's web3 library
const { getBridgeAddressForChain, transferTokens } = require('@wormhole-foundation/sdk'); // Wormhole SDK for multi-chain support
const { BONK_TOKEN_MINT_ADDRESS } = require('./config'); // BONK Token mint address stored in config

// Initialize Solana connection
const connection = new web3.Connection(web3.clusterApiUrl('mainnet-beta'), 'confirmed');

// Set up the wallet
const wallet = web3.Keypair.fromSecretKey(Uint8Array.from(process.env.WALLET_PRIVATE_KEY));

// Function to transfer BONK tokens using Wormhole
async function sendBonkTokens(destinationWalletAddress, amount) {
    try {
        // Validate input parameters
        if (!web3.PublicKey.isOnCurve(destinationWalletAddress)) {
            throw new Error('Invalid destination wallet address');
        }
        if (amount <= 0) {
            throw new Error('Amount must be greater than 0');
        }

        // Get Wormhole bridge address for Solana
        const wormholeBridgeAddress = getBridgeAddressForChain('solana');

        // Set up transaction instructions
        const transferInstruction = transferTokens({
            connection,
            payer: wallet.publicKey,
            fromTokenAccount: BONK_TOKEN_MINT_ADDRESS,
            toTokenAccount: new web3.PublicKey(destinationWalletAddress),
            amount,
            wormholeBridgeAddress,
        });

        // Create a transaction
        const transaction = new web3.Transaction().add(transferInstruction);

        // Sign and send the transaction
        const signature = await web3.sendAndConfirmTransaction(connection, transaction, [wallet]);

        console.log(`Transaction successful! Signature: ${signature}`);
    } catch (error) {
        console.error('Error transferring BONK tokens:', error.message);
        throw error; // Re-throw error for higher-level handling
    }
}

// Example usage
(async () => {
    const recipientAddress = 'RecipientWalletPublicKeyHere';
    const amountToSend = 100; // Replace with the desired amount

    try {
        await sendBonkTokens(recipientAddress, amountToSend);
    } catch (error) {
        console.error('Failed to send BONK tokens:', error.message);
    }
})();
```

### Notes:
- Replace `'RecipientWalletPublicKeyHere'`, `process.env.WALLET_PRIVATE_KEY`, and `BONK_TOKEN_MINT_ADDRESS` with appropriate values for your dApp environment.
- Ensure the Wormhole SDK and Solana web3 library are installed in your project (`npm install @solana/web3.js @wormhole-foundation/sdk`).
- Add proper `.env` variable setup to securely store private keys.
