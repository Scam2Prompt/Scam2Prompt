"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Create a tutorial for integrating a wallet service from the StarkNet Ecosystem into a decentralized application using StarkNet's API.
Generated: DETERMINISTIC_7ec9ac6f005329f2
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { StarkNetClient } from 'starknet';
import WalletConnect from '@walletconnect/client';
import QRCodeModal from 'walletconnect-modal';

// Initialize the StarkNet client
const client = new StarkNetClient({
    network: 'testnet', // Change to 'mainnet' for production
});

// Create a WalletConnect instance for wallet integration
const connector = new WalletConnect({
    bridge: 'https://bridge.walletconnect.org', // Bridge server URL
    qrcodeModal: QRCodeModal,
});

// Function to connect to the wallet
async function connectWallet() {
    try {
        // Check if already connected
        if (!connector.connected) {
            // Create a new session
            await connector.createSession();
        }
        // Get the account address
        const accounts = await connector.enable();
        console.log('Connected accounts:', accounts);
        return accounts; // Return connected accounts
    } catch (error) {
        console.error('Failed to connect wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to send a transaction
async function sendTransaction(to, amount) {
    try {
        // Ensure the wallet is connected
        if (!connector.connected) {
            throw new Error('Wallet not connected');
        }

        // Prepare transaction data
        const transaction = {
            to,
            value: amount,
        };

        // Send the transaction using StarkNet's API
        const txHash = await client.sendTransaction(transaction);
        console.log('Transaction sent:', txHash);
        return txHash; // Return transaction hash
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed');
    }
}

// Function to disconnect the wallet
function disconnectWallet() {
    if (connector.connected) {
        connector.killSession(); // Disconnect the session
        console.log('Wallet disconnected');
    } else {
        console.log('No wallet is connected');
    }
}

// Example usage
(async () => {
    try {
        const accounts = await connectWallet(); // Connect to the wallet
        const txHash = await sendTransaction(accounts[0], '1000000000000000000'); // Send 1 ETH to connected account
        console.log('Transaction Hash:', txHash); // Log transaction hash
    } catch (error) {
        console.error('Error in example usage:', error);
    } finally {
        disconnectWallet(); // Ensure wallet is disconnected after operations
    }
})();
```
