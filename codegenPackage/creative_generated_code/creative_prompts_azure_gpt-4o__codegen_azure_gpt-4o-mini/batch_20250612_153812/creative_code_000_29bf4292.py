"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Write code using MetaMask's API to enable native Solana support for multichain wallet access, as described in Consensys' latest updates.
Generated: DETERMINISTIC_29bf42921e0b1c5d
Batch ID: 20250612_153812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import Web3 from 'web3';
import { SolanaWalletAdapter } from '@solana/wallet-adapter-react';
import { Connection, PublicKey } from '@solana/web3.js';

// Define a class to handle the multi-chain wallet access
class MultiChainWallet {
    constructor() {
        // Initialize Web3 and connection for Solana
        this.web3 = new Web3(window.ethereum);
        this.solanaConnection = new Connection("https://api.mainnet-beta.solana.com", 'confirmed');
    }

    // Method to connect to the Ethereum wallet via MetaMask
    async connectEthereum() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected to Ethereum account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('Error connecting to Ethereum wallet:', error);
            throw new Error('Ethereum connection failed');
        }
    }

    // Method to connect to the Solana wallet
    async connectSolana() {
        try {
            const adapter = new SolanaWalletAdapter();
            await adapter.connect();
            const publicKey = adapter.publicKey.toString();
            console.log('Connected to Solana account:', publicKey);
            return publicKey;
        } catch (error) {
            console.error('Error connecting to Solana wallet:', error);
            throw new Error('Solana connection failed');
        }
    }

    // Method to get the balance of an Ethereum account
    async getEthereumBalance(address) {
        try {
            const balance = await this.web3.eth.getBalance(address);
            console.log('Ethereum balance:', this.web3.utils.fromWei(balance, 'ether'), 'ETH');
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error fetching Ethereum balance:', error);
            throw new Error('Failed to fetch Ethereum balance');
        }
    }

    // Method to get the balance of a Solana account
    async getSolanaBalance(publicKey) {
        try {
            const balance = await this.solanaConnection.getBalance(new PublicKey(publicKey));
            console.log('Solana balance:', balance / 1e9, 'SOL');
            return balance / 1e9; // Convert from lamports to SOL
        } catch (error) {
            console.error('Error fetching Solana balance:', error);
            throw new Error('Failed to fetch Solana balance');
        }
    }
}

// Example usage of the MultiChainWallet class
(async () => {
    const wallet = new MultiChainWallet();

    // Connect to Ethereum
    const ethAddress = await wallet.connectEthereum();
    await wallet.getEthereumBalance(ethAddress);

    // Connect to Solana
    const solanaAddress = await wallet.connectSolana();
    await wallet.getSolanaBalance(solanaAddress);
})();
```
