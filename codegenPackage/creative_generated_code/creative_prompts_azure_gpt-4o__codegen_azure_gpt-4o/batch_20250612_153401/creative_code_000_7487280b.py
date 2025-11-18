"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessepollak-ebv.pages.dev
Prompt: Write code to integrate a "Connect Wallet" feature for a decentralized application, inspired by Jesse Pollak's work on Coinbase Wallet and Base. Include best practices for security and user experience.
Generated: DETERMINISTIC_7487280b5037cd0a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import Web3 from "web3"; // Web3.js for Ethereum blockchain interaction
import detectEthereumProvider from "@metamask/detect-provider"; // Detect MetaMask provider

// Constants
const SUPPORTED_NETWORKS = [1, 137, 56]; // Ethereum Mainnet, Polygon, Binance Smart Chain (example IDs)
const NETWORK_NAMES = {
  1: "Ethereum Mainnet",
  137: "Polygon",
  56: "Binance Smart Chain"
};

// Application State
let web3;
let userAccount = null;

/**
 * Initialize the "Connect Wallet" feature
 * This function detects MetaMask and sets up the required environment
 */
async function initializeWalletConnection() {
  try {
    const provider = await detectEthereumProvider();

    // Check if MetaMask is installed
    if (!provider) {
      alert("MetaMask not detected. Please install MetaMask to use this feature.");
      return;
    }

    // Use the provider with Web3
    web3 = new Web3(provider);

    // Add event listeners for account and network changes
    provider.on("accountsChanged", handleAccountsChanged);
    provider.on("chainChanged", handleNetworkChanged);

    // Prompt user to connect wallet
    await connectWallet();
  } catch (error) {
    console.error("Error initializing wallet:", error);
    alert("An error occurred while initializing the wallet. Please try again.");
  }
}

/**
 * Connect to the user's wallet
 */
async function connectWallet() {
  try {
    const accounts = await web3.eth.requestAccounts(); // Prompt MetaMask connection
    if (accounts.length === 0) {
      alert("No accounts found. Please connect your wallet.");
      return;
    }

    userAccount = accounts[0]; // Save the connected account
    console.log("Wallet connected:", userAccount);

    const networkId = await web3.eth.net.getId(); // Get current network
    if (!SUPPORTED_NETWORKS.includes(networkId)) {
      alert(
        `Unsupported network detected. Please switch to a supported network:\n${SUPPORTED_NETWORKS.map(
          (id) => NETWORK_NAMES[id]
        ).join(", ")}`
      );
      return;
    }

    alert(`Wallet connected successfully to ${NETWORK_NAMES[networkId]}.`);
  } catch (error) {
    console.error("Error connecting wallet:", error);
    alert("An error occurred while connecting the wallet. Please try again.");
  }
}

/**
 * Handle account changes (e.g., user switches accounts in MetaMask)
 * @param {Array<string>} accounts - Updated list of accounts
 */
function handleAccountsChanged(accounts) {
  if (accounts.length === 0) {
    alert("Wallet disconnected. Please connect again.");
    userAccount = null;
    return;
  }

  userAccount = accounts[0];
  console.log("Account changed:", userAccount);
}

/**
 * Handle network changes (e.g., user switches networks in MetaMask)
 * @param {string} chainId - The updated chain ID
 */
async function handleNetworkChanged(chainId) {
  const networkId = parseInt(chainId, 16); // Convert chainId (hex) to integer
  if (!SUPPORTED_NETWORKS.includes(networkId)) {
    alert(
      `Unsupported network detected. Please switch to a supported network:\n${SUPPORTED_NETWORKS.map(
        (id) => NETWORK_NAMES[id]
      ).join(", ")}`
    );
    return;
  }

  console.log(`Network changed to ${NETWORK_NAMES[networkId]}`);
}

/**
 * Disconnect the wallet
 */
function disconnectWallet() {
  userAccount = null;
  alert("Wallet disconnected.");
}

// Example usage: Initialize the wallet connection when the page loads
document.addEventListener("DOMContentLoaded", initializeWalletConnection);

// Button event listeners (example usage)
document.getElementById("connect-wallet-btn").addEventListener("click", connectWallet);
document.getElementById("disconnect-wallet-btn").addEventListener("click", disconnectWallet);

```

### Notes:
1. Make sure your HTML includes buttons with IDs `connect-wallet-btn` and `disconnect-wallet-btn` for the respective functionality to work.
2. Add the required dependencies (`web3`, `@metamask/detect-provider`) to your package.json and install them via npm:
   ```
   npm install web3 @metamask/detect-provider
   ```
