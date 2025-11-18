"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-website1.pages.dev
Prompt: Write code to integrate a "Connect Wallet" feature for a crypto-native fund platform, ensuring compatibility with open and permissionless crypto networks as described by Innodapter ApS.
Generated: DETERMINISTIC_16f4e74ff8a4ea96
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Constants for supported networks
const SUPPORTED_NETWORKS = {
  ethereum: {
    chainId: '0x1', // Mainnet
    networkName: 'Ethereum Mainnet',
  },
  polygon: {
    chainId: '0x89', // Polygon Mainnet
    networkName: 'Polygon Mainnet',
  },
};

// Initialize web3 instance
let web3;

// DOM elements for wallet actions
const connectButton = document.getElementById('connectWallet');
const walletAddressDisplay = document.getElementById('walletAddress');
const networkDisplay = document.getElementById('network');

// Error handling utility
function handleError(error) {
  console.error('Error:', error.message || error);
  alert('An error occurred: ' + (error.message || error));
}

// Connect Wallet function
async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not detected. Please install MetaMask to continue.');
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const walletAddress = accounts[0];

    // Initialize web3 with the connected provider
    web3 = new Web3(window.ethereum);

    // Get the current network
    const chainId = await web3.eth.getChainId();
    const networkInfo = Object.values(SUPPORTED_NETWORKS).find((network) => network.chainId === '0x' + chainId.toString(16));

    if (!networkInfo) {
      throw new Error('Unsupported network. Please switch to a supported network.');
    }

    // Update UI
    walletAddressDisplay.textContent = `Wallet Address: ${walletAddress}`;
    networkDisplay.textContent = `Network: ${networkInfo.networkName}`;
    connectButton.textContent = 'Wallet Connected';

    // Add event listener for account changes
    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length > 0) {
        walletAddressDisplay.textContent = `Wallet Address: ${accounts[0]}`;
      } else {
        walletAddressDisplay.textContent = 'Wallet Address: Not Connected';
        connectButton.textContent = 'Connect Wallet';
      }
    });

    // Add event listener for network changes
    window.ethereum.on('chainChanged', (chainId) => {
      const updatedNetworkInfo = Object.values(SUPPORTED_NETWORKS).find((network) => network.chainId === chainId);
      if (updatedNetworkInfo) {
        networkDisplay.textContent = `Network: ${updatedNetworkInfo.networkName}`;
      } else {
        networkDisplay.textContent = 'Network: Unsupported';
      }
    });
  } catch (error) {
    handleError(error);
  }
}

// Event listener for Connect Wallet button
connectButton.addEventListener('click', connectWallet);

// Ensure the DOM elements exist in your HTML:
// <button id="connectWallet">Connect Wallet</button>
// <div id="walletAddress">Wallet Address: Not Connected</div>
// <div id="network">Network: Not Connected</div>
```

**Note:** This code assumes that `index.html` includes the necessary UI elements (`connectWallet`, `walletAddress`, and `network`). Additionally, the script uses the MetaMask provider (`window.ethereum`) to connect to open and permissionless crypto networks. Ensure you have MetaMask installed and set up correctly in your browser for testing.
