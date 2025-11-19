"""
Generated Code Metadata:
========================
Original URL: https://web3-dapp.vercel.app
Prompt: Provide an example of handling wallet connection errors using Web3Modal in a Web3 project.
Generated: DETERMINISTIC_e75d2a046f71c6ed
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import { Web3Modal } from '@web3modal/standalone';
import { ethers } from 'ethers';

// Web3Modal configuration
const web3Modal = new Web3Modal({
  projectId: 'YOUR_PROJECT_ID', // Replace with your WalletConnect project ID
  walletConnectVersion: 2,
  themeMode: 'light',
  themeVariables: {
    '--w3m-font-family': 'Arial, sans-serif',
    '--w3m-accent-color': '#3b82f6',
  },
});

// Function to handle wallet connection
async function connectWallet() {
  try {
    // Open Web3Modal and get the provider
    const provider = await web3Modal.openModal();

    // Create ethers provider
    const ethersProvider = new ethers.BrowserProvider(provider);

    // Get user's accounts
    const accounts = await ethersProvider.listAccounts();
    if (accounts.length === 0) {
      throw new Error('No accounts found');
    }

    // Get network details
    const network = await ethersProvider.getNetwork();
    
    return {
      provider: ethersProvider,
      account: accounts[0],
      network
    };
  } catch (error) {
    // Handle specific error cases
    if (error.code === 'USER_CLOSED_MODAL') {
      console.warn('User closed the modal without connecting');
      throw new Error('Connection cancelled by user');
    } else if (error.code === 'SESSION_DISCONNECTED') {
      console.error('Session disconnected:', error);
      throw new Error('Wallet session disconnected');
    } else if (error.message.includes('No accounts found')) {
      console.error('No accounts found in wallet');
      throw new Error('No accounts found in connected wallet');
    } else if (error.message.includes('Unsupported chain')) {
      console.error('Unsupported chain:', error);
      throw new Error('Connected to unsupported network');
    } else {
      console.error('Unknown connection error:', error);
      throw new Error('Failed to connect wallet');
    }
  } finally {
    // Always close the modal when done
    web3Modal.closeModal();
  }
}

// Example usage
async function handleConnect() {
  try {
    const walletData = await connectWallet();
    console.log('Connected wallet:', walletData);
    // Proceed with your application logic
  } catch (error) {
    // Display user-friendly error message
    alert(`Error connecting wallet: ${error.message}`);
  }
}

// Event listener for connect button
document.getElementById('connectButton')?.addEventListener('click', handleConnect);
```
