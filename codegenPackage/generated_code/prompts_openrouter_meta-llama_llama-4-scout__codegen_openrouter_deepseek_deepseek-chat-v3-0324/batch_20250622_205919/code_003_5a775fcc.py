"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: "Generate a code example for a basic configuration of Web3Modal using solana as a driving library."
Generated: DETERMINISTIC_5a775fcc4f6d3f7f
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { Web3Modal } from '@web3modal/solana';
import { SolanaWalletConnectors } from '@web3modal/solana-connectors';
import { Connection, clusterApiUrl } from '@solana/web3.js';

// Configuration for Solana network
const solanaConfig = {
  network: 'mainnet-beta', // or 'testnet', 'devnet'
  rpcUrl: clusterApiUrl('mainnet-beta'), // or custom RPC URL
};

// Web3Modal configuration
const web3ModalConfig = {
  projectId: 'YOUR_WALLETCONNECT_PROJECT_ID', // Replace with your WalletConnect project ID
  solanaConfig,
  walletConnectOptions: {
    qrcodeModalOptions: {
      mobileLinks: ['phantom', 'solflare', 'ledger'],
    },
  },
};

// Initialize Web3Modal
const web3Modal = new Web3Modal(web3ModalConfig);

// Function to connect wallet
async function connectWallet() {
  try {
    // Open modal and get selected wallet
    const wallet = await web3Modal.connect();

    // Get provider and signer
    const provider = await web3Modal.getWalletProvider();
    const signer = provider;

    // Create connection to Solana network
    const connection = new Connection(solanaConfig.rpcUrl);

    return { wallet, provider, signer, connection };
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

// Function to disconnect wallet
async function disconnectWallet() {
  try {
    await web3Modal.disconnect();
    console.log('Wallet disconnected');
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Connect wallet
    const { wallet, provider, signer, connection } = await connectWallet();
    console.log('Connected wallet:', wallet);
    console.log('Provider:', provider);
    console.log('Signer:', signer);
    console.log('Connection:', connection);

    // Example: Get wallet balance
    const balance = await connection.getBalance(signer.publicKey);
    console.log('Wallet balance:', balance);

    // Disconnect wallet when done
    await disconnectWallet();
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
