"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impolitede.web.app
Prompt: Generate a Node.js script to automate the process of connecting to a Phantom wallet and claiming DUST tokens from DustLabs.
Generated: DETERMINISTIC_60bea9a89f947f48
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { PhantomWalletAdapter } = require('@solana/wallet-adapter-phantom');
const { Connection, PublicKey, Transaction, clusterApiUrl } = require('@solana/web3.js');
const { TokenInstructions } = require('@solana/spl-token');
const { WalletNotConnectedError } = require('@solana/wallet-adapter-base');

// Define constants
const DUST_LABS_ADDRESS = 'YOUR_DUST_LABS_ADDRESS'; // Replace with actual Dust Labs address
const DUST_TOKEN_MINT = 'YOUR_DUST_TOKEN_MINT_ADDRESS'; // Replace with actual DUST token mint address
const NETWORK = 'mainnet-beta'; // Set to the desired network: 'devnet', 'testnet', or 'mainnet-beta'

// Initialize Phantom wallet adapter
const wallet = new PhantomWalletAdapter();

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

/**
 * Function to check wallet connection
 */
async function checkWalletConnection() {
    if (!wallet.connected) {
        throw new WalletNotConnectedError();
    }
}

/**
 * Function to claim DUST tokens
 */
async function claimDustTokens() {
    try {
        // Check wallet connection
        await checkWalletConnection();

        // Fetch current wallet public key
        const publicKey = wallet.publicKey;

        // Create instruction for claiming DUST tokens
        const tx = new Transaction().add(
            TokenInstructions.transfer({
                source: publicKey,
                destination: new PublicKey(DUST_LABS_ADDRESS),
                amount: 1, // Specify amount to claim
                mint: new PublicKey(DUST_TOKEN_MINT),
                owner: publicKey,
            })
        );

        // Send transaction
        const signature = await connection.sendTransaction(tx, [wallet], {
            skipPreflight: false,
            preflightCommitment: 'confirmed',
        });

        // Confirm transaction
        await connection.confirmTransaction(signature, 'confirmed');

        console.log('Successfully claimed DUST tokens:', signature);
    } catch (error) {
        console.error('Error claiming DUST tokens:', error);
    }
}

/**
 * Main function to execute the script
 */
(async () => {
    try {
        // Connect wallet
        await wallet.connect();

        // Claim DUST tokens
        await claimDustTokens();
    } catch (error) {
        console.error('Error in main execution:', error);
    } finally {
        // Disconnect wallet
        if (wallet.connected) {
            await wallet.disconnect();
        }
    }
})();
```

**Note:** Ensure to replace `YOUR_DUST_LABS_ADDRESS` and `YOUR_DUST_TOKEN_MINT_ADDRESS` with the actual addresses required for claiming tokens. Make sure the Phantom wallet extension is installed and properly configured in your browser for connection.
