"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Write code to integrate the WalletConnect Network into a web3 application, ensuring compatibility with WalletConnect's onchain UX ecosystem.
Generated: DETERMINISTIC_3e5ade4b9ec40f0f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { WalletConnectModal } from '@walletconnect/modal';
import { Web3Provider } from '@ethersproject/providers';
import { ethers } from 'ethers';

// Set up WalletConnect project ID
const projectId = 'YOUR_PROJECT_ID';

// Initialize WalletConnect modal
const modal = new WalletConnectModal({
  projectId,
  // Add your chains and methods here
  chains: [1, 137], // Ethereum mainnet and Polygon
  methods: ['eth_sendTransaction', 'eth_requestAccounts'],
  events: ['chainChanged', 'accountsChanged'],
});

// Function to connect to WalletConnect
async function connectToWalletConnect() {
  try {
    // Open the modal for user to select a wallet
    const { connector } = await modal.open();

    // Create a Web3 provider from the connector
    const provider = new Web3Provider(connector);

    // Get the user's accounts
    const accounts = await provider.listAccounts();

    // Get the current chain ID
    const chainId = await provider.getNetwork().then((network) => network.chainId);

    // Handle chain changes
    provider.on('chainChanged', (chainId) => {
      console.log(`Chain changed to ${chainId}`);
      // Update your application state here
    });

    // Handle account changes
    provider.on('accountsChanged', (accounts) => {
      console.log(`Accounts changed to ${accounts}`);
      // Update your application state here
    });

    // Return the Web3 provider
    return provider;
  } catch (error) {
    console.error('Error connecting to WalletConnect:', error);
    throw error;
  }
}

// Function to send a transaction using WalletConnect
async function sendTransaction(provider, to, value) {
  try {
    // Create a new ethers signer from the provider
    const signer = provider.getSigner();

    // Send the transaction
    const tx = await signer.sendTransaction({
      to,
      value: ethers.utils.parseEther(value.toString()),
    });

    // Wait for the transaction to be mined
    await tx.wait();

    console.log(`Transaction sent: ${tx.hash}`);
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    // Connect to WalletConnect
    const provider = await connectToWalletConnect();

    // Send a transaction
    await sendTransaction(provider, '0x...recipient address...', 1.0);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
