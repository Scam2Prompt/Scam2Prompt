"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://echotradeoptions.com
Prompt: Write code to connect a Web3 wallet to a trading platform dashboard for real-time balance tracking, similar to Echo Trade's "Connect Wallet" feature.
Generated: DETERMINISTIC_433b18113c2add78
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import Web3 from 'web3';

// Constants
const supportedNetworks = [1, 3, 4, 5, 42]; // Supported Ethereum networks (Mainnet, Ropsten, Rinkeby, etc.)
const defaultNetwork = 1; // Default to Ethereum Mainnet

// Initialize Web3 instance
let web3;
if (window.ethereum) {
  web3 = new Web3(window.ethereum);
} else {
  console.error('No Ethereum provider found. Please install Metamask or another wallet.');
  alert('No Ethereum wallet detected. Please install Metamask.');
}

// DOM Elements
const connectWalletBtn = document.getElementById('connectWalletBtn');
const walletAddressDisplay = document.getElementById('walletAddress');
const walletBalanceDisplay = document.getElementById('walletBalance');

// Helper Functions

/**
 * Checks if the connected network is supported.
 * @param {number} networkId - The network ID to validate.
 * @returns {boolean} True if the network is supported, otherwise false.
 */
function isSupportedNetwork(networkId) {
  return supportedNetworks.includes(networkId);
}

/**
 * Converts balance from Wei to Ether.
 * @param {string} balanceInWei - Balance in Wei.
 * @returns {string} Balance in Ether.
 */
function convertWeiToEther(balanceInWei) {
  return web3.utils.fromWei(balanceInWei, 'ether');
}

/**
 * Handles wallet connection logic.
 */
async function connectWallet() {
  try {
    // Request wallet connection
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get accounts
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      alert('No accounts found. Please ensure your wallet is connected.');
      return;
    }

    const walletAddress = accounts[0];
    walletAddressDisplay.textContent = `Connected Wallet: ${walletAddress}`;

    // Get current network
    const networkId = await web3.eth.net.getId();
    if (!isSupportedNetwork(networkId)) {
      alert(`Unsupported network. Please switch to a supported network.`);
      walletAddressDisplay.textContent = `Unsupported Network`;
      return;
    }
    
    // Fetch initial balance
    updateBalance(walletAddress);

    // Listen for account and network changes
    listenForWalletEvents();

  } catch (error) {
    console.error('Error connecting wallet:', error);
    alert('Failed to connect wallet. Please try again.');
  }
}

/**
 * Updates the wallet balance in real-time.
 * @param {string} walletAddress - The wallet address to fetch the balance for.
 */
async function updateBalance(walletAddress) {
  try {
    const balance = await web3.eth.getBalance(walletAddress);
    walletBalanceDisplay.textContent = `Balance: ${convertWeiToEther(balance)} ETH`;
  } catch (error) {
    console.error('Error fetching balance:', error);
    walletBalanceDisplay.textContent = `Balance: Error`;
  }
}

/**
 * Listens for wallet-related events such as account or network changes.
 */
function listenForWalletEvents() {
  // Listen for account changes
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      // Wallet disconnected
      walletAddressDisplay.textContent = 'Wallet Disconnected';
      walletBalanceDisplay.textContent = 'Balance: -';
    } else {
      // Update UI with new account
      const newWalletAddress = accounts[0];
      walletAddressDisplay.textContent = `Connected Wallet: ${newWalletAddress}`;
      updateBalance(newWalletAddress);
    }
  });

  // Listen for network changes
  window.ethereum.on('chainChanged', (chainId) => {
    const networkId = parseInt(chainId, 16);
    if (!isSupportedNetwork(networkId)) {
      alert(`Unsupported network. Please switch to a supported network.`);
      walletAddressDisplay.textContent = `Unsupported Network`;
      walletBalanceDisplay.textContent = 'Balance: -';
    } else {
      // Fetch updated balance for the valid network
      web3.eth.getAccounts().then((accounts) => {
        if (accounts.length > 0) {
          updateBalance(accounts[0]);
        }
      });
    }
  });
}

// Attach event listener to the "Connect Wallet" button
connectWalletBtn.addEventListener('click', connectWallet);

// End of script
```
