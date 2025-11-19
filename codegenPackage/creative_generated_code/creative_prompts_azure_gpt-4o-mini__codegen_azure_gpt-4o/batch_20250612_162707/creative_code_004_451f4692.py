"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-nfts.web.app
Prompt: Explain how to manage wallets and connect different wallets for NFT trading on the Solana network based on the information from sol-nfts.web.app.
Generated: DETERMINISTIC_451f4692d6a577d5
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const { Connection, clusterApiUrl, PublicKey } = require('@solana/web3.js');
const { WalletAdapterNetwork } = require('@solana/wallet-adapter-base');
const {
    WalletAdapter,
    Wallets,
    WalletAdapterReactProvider,
} = require('@solana/wallet-adapter-react');
const {
    PhantomWalletAdapter,
    SolflareWalletAdapter,
    TorusWalletAdapter,
} = require('@solana/wallet-adapter-wallets';

// Establish connection to Solana network (mainnet-beta is used for production)
const network = WalletAdapterNetwork.Mainnet; // Change to 'Devnet' or 'Testnet' for testing environments
const connection = new Connection(clusterApiUrl(network), 'confirmed');

// Initialize wallets supported by the application
const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter(),
    new TorusWalletAdapter(),
];

// Function to connect a wallet
async function connectWallet(walletAdapter) {
    try {
        // Check if the wallet adapter is ready
        if (!walletAdapter.ready) {
            throw new Error('Wallet is not ready. Please ensure it is installed.');
        }

        // Connect to the wallet
        await walletAdapter.connect();
        console.log('Wallet connected successfully.');

        // Retrieve the public key of the connected wallet
        const publicKey = walletAdapter.publicKey;
        console.log('Wallet Public Key:', publicKey.toBase58());
        return publicKey;
    } catch (error) {
        console.error('Error connecting to wallet:', error.message);
        throw error; // Re-throw the error for further handling
    }
}

// Function to disconnect a wallet
async function disconnectWallet(walletAdapter) {
    try {
        // Disconnect the wallet
        await walletAdapter.disconnect();
        console.log('Wallet disconnected successfully.');
    } catch (error) {
        console.error('Error disconnecting wallet:', error.message);
        throw error; // Re-throw the error for further handling
    }
}

// Example usage of wallet connection
(async () => {
    const walletAdapter = wallets[0]; // Select the first wallet (Phantom in this case)

    try {
        // Connect to the wallet
        const publicKey = await connectWallet(walletAdapter);

        // Wallet is connected, proceed with NFT trading logic
        console.log('Proceeding with NFT trading using wallet:', publicKey.toBase58());

        // Example: Fetch account details (replace with actual NFT trading logic)
        const accountInfo = await connection.getAccountInfo(new PublicKey(publicKey));
        console.log('Account Info:', accountInfo);

        // Disconnect the wallet after operations
        await disconnectWallet(walletAdapter);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
