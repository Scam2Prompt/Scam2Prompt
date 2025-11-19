"""
Generated Code Metadata:
========================
Original URL: https://olivedao.finance
Prompt: Write code to integrate a wallet connection feature for a decentralized finance (DeFi) application, similar to the functionality described on the OliveDAO Finance website.
Generated: DETERMINISTIC_e13a98ed3c6efb7d
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';

// Wallet connection configuration
const providerOptions = {
  // Add wallet providers here (e.g., Metamask, WalletConnect, etc.)
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: 'YOUR_INFURA_PROJECT_ID' // Replace with your Infura ID
    }
  }
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions // required
});

// DOM elements
const connectButton = document.getElementById('connect-wallet');
const walletAddressElement = document.getElementById('wallet-address');
const walletBalanceElement = document.getElementById('wallet-balance');

// State variables
let provider;
let signer;
let account;
let chainId;

// Initialize application
async function init() {
  // Check if wallet is already connected
  if (web3Modal.cachedProvider) {
    await connectWallet();
  }
  
  // Set up event listeners
  connectButton.addEventListener('click', async () => {
    if (account) {
      await disconnectWallet();
    } else {
      await connectWallet();
    }
  });
}

// Connect wallet function
async function connectWallet() {
  try {
    // Open wallet connection modal
    const instance = await web3Modal.connect();
    
    // Create Web3 provider and signer
    provider = new ethers.providers.Web3Provider(instance);
    signer = provider.getSigner();
    
    // Get account and chain details
    account = await signer.getAddress();
    chainId = await provider.getNetwork().then(network => network.chainId);
    
    // Update UI
    updateUI();
    
    // Set up event listeners for account/chain changes
    instance.on('accountsChanged', (accounts) => {
      account = accounts[0];
      updateUI();
    });
    
    instance.on('chainChanged', (chainId) => {
      window.location.reload();
    });
    
    // Get and display balance
    await updateBalance();
    
  } catch (error) {
    console.error('Error connecting wallet:', error);
    alert('Failed to connect wallet. Please try again.');
  }
}

// Disconnect wallet function
async function disconnectWallet() {
  try {
    // Clear web3Modal cache
    web3Modal.clearCachedProvider();
    
    // Reset state
    provider = null;
    signer = null;
    account = null;
    chainId = null;
    
    // Update UI
    updateUI();
    
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    alert('Failed to disconnect wallet. Please try again.');
  }
}

// Update wallet balance
async function updateBalance() {
  if (!account || !provider) return;
  
  try {
    const balance = await provider.getBalance(account);
    const formattedBalance = ethers.utils.formatEther(balance);
    walletBalanceElement.textContent = `${parseFloat(formattedBalance).toFixed(4)} ETH`;
  } catch (error) {
    console.error('Error fetching balance:', error);
    walletBalanceElement.textContent = 'Error';
  }
}

// Update UI based on connection state
function updateUI() {
  if (account) {
    // Truncate address for display
    const truncatedAddress = `${account.substring(0, 6)}...${account.substring(account.length - 4)}`;
    walletAddressElement.textContent = truncatedAddress;
    connectButton.textContent = 'Disconnect';
  } else {
    walletAddressElement.textContent = 'Not connected';
    walletBalanceElement.textContent = '0 ETH';
    connectButton.textContent = 'Connect Wallet';
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', init);

// Export for testing or module usage
export {
  connectWallet,
  disconnectWallet,
  provider,
  signer,
  account,
  chainId
};
```
