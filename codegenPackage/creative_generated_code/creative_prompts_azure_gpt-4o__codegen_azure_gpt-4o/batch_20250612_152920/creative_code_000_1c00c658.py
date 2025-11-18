"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolitpphxatom.webflow.io
Prompt: Write code to integrate the Phantom Wallet with a Solana-based DeFi application using its API.
Generated: DETERMINISTIC_1c00c658e59ce494
Batch ID: 20250612_152920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js'); // Solana SDK for blockchain interaction
const { PhantomWalletAdapter } = require('@solana/wallet-adapter-wallets'); // Phantom Wallet integration

// Constants
const NETWORK = 'mainnet-beta'; // Use 'mainnet-beta' for production, 'devnet' for testing
const SOLANA_RPC_URL = clusterApiUrl(NETWORK); // RPC URL for network

// Initialize Solana connection
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');

// Function to connect to the Phantom Wallet
async function connectPhantomWallet() {
    try {
        // Create an instance of the Phantom Wallet adapter
        const wallet = new PhantomWalletAdapter();

        // Check if Phantom Wallet is available in the browser
        if (!wallet.ready) {
            throw new Error('Phantom Wallet is not available. Please install it.');
        }

        // Connect to the wallet
        await wallet.connect();

        // Retrieve the wallet's public key
        const publicKey = wallet.publicKey?.toString();
        if (!publicKey) {
            throw new Error('Failed to retrieve public key from Phantom Wallet.');
        }

        console.log(`Connected to Phantom Wallet. Public Key: ${publicKey}`);
        return publicKey;
    } catch (error) {
        console.error('Error connecting to Phantom Wallet:', error.message);
        throw error;
    }
}

// Function to retrieve account balance from the connected wallet
async function getWalletBalance(publicKeyStr) {
    try {
        if (!PublicKey.isOnCurve(new PublicKey(publicKeyStr))) {
            throw new Error('Invalid public key provided.');
        }

        const publicKey = new PublicKey(publicKeyStr);

        // Get wallet balance in lamports
        const balanceLamports = await connection.getBalance(publicKey);

        // Convert lamports to SOL
        const balanceSOL = balanceLamports / 1e9;
        console.log(`Wallet Balance: ${balanceSOL} SOL`);
        return balanceSOL;
    } catch (error) {
        console.error('Error fetching wallet balance:', error.message);
        throw error;
    }
}

// Example of usage
(async () => {
    try {
        console.log('Attempting to connect to Phantom Wallet...');
        const publicKey = await connectPhantomWallet();

        console.log('Fetching wallet balance...');
        const balance = await getWalletBalance(publicKey);

        console.log(`Wallet connected and balance fetched successfully: ${balance} SOL`);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```

### Prerequisites
1. Install the required dependencies:
   ```bash
   npm install @solana/web3.js @solana/wallet-adapter-wallets
   ```
2. Ensure Phantom Wallet browser extension is installed and configured.
