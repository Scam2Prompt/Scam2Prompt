"""
Generated Code Metadata:
========================
Original URL: https://io-ultra-net.vercel.app
Prompt: Create a code example for integrating a crypto wallet with a Dapp, enabling mobile wallet/extension connectivity and resolving common integration/migration issues.
Generated: DETERMINISTIC_151f864adfe7829e
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DApp Wallet Integration Example
// Supports WalletConnect, MetaMask, and other EIP-1193 compatible wallets

import { ethers } from 'ethers';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Web3Modal from 'web3modal';

// Configuration
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura ID
    }
  }
};

const web3Modal = new Web3Modal({
  network: 'mainnet', // Optional - defaults to 'mainnet'
  cacheProvider: true, // Optional - enables wallet reconnection
  providerOptions // Required
});

// Wallet state
let provider;
let signer;
let currentAccount = null;
let chainId = null;

// DOM Elements
const connectButton = document.getElementById('connect-button');
const accountDisplay = document.getElementById('account-display');
const chainDisplay = document.getElementById('chain-display');
const signMessageButton = document.getElementById('sign-message-button');
const sendTxButton = document.getElementById('send-tx-button');

// Event Listeners
connectButton.addEventListener('click', connectWallet);
signMessageButton.addEventListener('click', signMessage);
sendTxButton.addEventListener('click', sendTransaction);

// Initialize
async function init() {
  if (web3Modal.cachedProvider) {
    await connectWallet();
  }
  setupEventListeners();
}

// Connect wallet handler
async function connectWallet() {
  try {
    provider = await web3Modal.connect();
    await setupProvider(provider);
    updateUI();
  } catch (error) {
    console.error('Could not connect to wallet:', error);
    resetState();
  }
}

// Setup provider and event listeners
async function setupProvider(provider) {
  const web3Provider = new ethers.providers.Web3Provider(provider);
  signer = web3Provider.getSigner();
  
  // Get initial account and chain
  const accounts = await web3Provider.listAccounts();
  currentAccount = accounts[0];
  chainId = (await web3Provider.getNetwork()).chainId;

  // Subscribe to accounts change
  provider.on('accountsChanged', (accounts) => {
    currentAccount = accounts[0] || null;
    updateUI();
  });

  // Subscribe to chain change
  provider.on('chainChanged', (newChainId) => {
    chainId = parseInt(newChainId, 16);
    updateUI();
  });

  // Subscribe to disconnect
  provider.on('disconnect', (code, reason) => {
    console.log('Wallet disconnected:', reason);
    resetState();
  });
}

// Update UI based on wallet state
function updateUI() {
  if (currentAccount) {
    accountDisplay.textContent = `${currentAccount.substring(0, 6)}...${currentAccount.substring(38)}`;
    chainDisplay.textContent = `Chain ID: ${chainId}`;
    connectButton.textContent = 'Connected';
    signMessageButton.disabled = false;
    sendTxButton.disabled = false;
  } else {
    accountDisplay.textContent = 'Not connected';
    chainDisplay.textContent = 'Chain ID: -';
    connectButton.textContent = 'Connect Wallet';
    signMessageButton.disabled = true;
    sendTxButton.disabled = true;
  }
}

// Reset wallet state
function resetState() {
  currentAccount = null;
  chainId = null;
  updateUI();
}

// Sign message example
async function signMessage() {
  if (!signer || !currentAccount) return;
  
  try {
    const message = 'Hello from DApp!';
    const signature = await signer.signMessage(message);
    console.log('Message signed:', signature);
    alert(`Signature: ${signature}`);
  } catch (error) {
    console.error('Error signing message:', error);
    alert('Failed to sign message');
  }
}

// Send transaction example
async function sendTransaction() {
  if (!signer || !currentAccount) return;
  
  try {
    const tx = {
      to: '0x0000000000000000000000000000000000000000',
      value: ethers.utils.parseEther('0.01')
    };
    
    const txResponse = await signer.sendTransaction(tx);
    console.log('Transaction sent:', txResponse.hash);
    alert(`Transaction sent: ${txResponse.hash}`);
  } catch (error) {
    console.error('Error sending transaction:', error);
    alert('Failed to send transaction');
  }
}

// Setup event listeners for wallet changes
function setupEventListeners() {
  window.addEventListener('load', async () => {
    if (window.ethereum) {
      try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
      } catch (error) {
        console.error('User denied account access');
      }
    }
  });
}

// Initialize the app
init();
```
