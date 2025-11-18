"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-box.web.app
Prompt: Write a function to connect and disconnect a Solana-compatible wallet programmatically, as described in the "Connect Wallet" section of the webpage.
Generated: DETERMINISTIC_89339c4bf5a2d3aa
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, Cluster, clusterApiUrl } from '@solana/web3.js';
import Wallet from '@project-serum/sol-wallet-adapter';

class SolanaWalletConnector {
    constructor() {
        // Define Solana network cluster
        this.cluster = 'devnet'; // Can be changed to 'testnet' or 'mainnet-beta'
        this.connection = new Connection(clusterApiUrl(this.cluster), 'confirmed');
        this.wallet = null;
    }

    /**
     * Initializes the wallet connection
     * @param {string} walletAddress - The address of the Solana wallet to connect
     */
    async connectWallet(walletAddress) {
        try {
            // Create a new wallet instance
            this.wallet = new Wallet(walletAddress);
            await this.wallet.connect();

            console.log('Wallet connected:', this.wallet.publicKey.toString());
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            throw new Error('Wallet connection failed');
        }
    }

    /**
     * Disconnects the current wallet
     */
    async disconnectWallet() {
        try {
            if (this.wallet) {
                await this.wallet.disconnect();
                console.log('Wallet disconnected');
                this.wallet = null;
            } else {
                console.warn('No wallet is connected');
            }
        } catch (error) {
            console.error('Failed to disconnect wallet:', error);
            throw new Error('Wallet disconnection failed');
        }
    }
}

// Export the wallet connector for use in other parts of the application
export default SolanaWalletConnector;

// Example usage
// const walletConnector = new SolanaWalletConnector();
// walletConnector.connectWallet('YOUR_WALLET_ADDRESS_HERE');
// walletConnector.disconnectWallet();
```
