"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogetest3.vercel.app
Prompt: What are the steps to implement the "Connect Wallet" feature for a decentralized application like Dogetest3?
Generated: DETERMINISTIC_5a500a21de51661c
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from "web3";

// Define constants
const supportedNetworks = [1, 3, 4, 5, 42]; // Mainnet, Ropsten, Rinkeby, Goerli, Kovan (Example networks)
let web3; // Instance of Web3
let userAddress = ""; // Store the connected wallet address

/**
 * Function to detect if MetaMask or any Ethereum provider is installed
 * @returns {boolean} True if provider is available, false otherwise
 */
function isWalletAvailable() {
  return typeof window.ethereum !== "undefined";
}

/**
 * Connect Wallet Function
 * This function connects to the user's wallet using MetaMask or supported Ethereum provider
 */
async function connectWallet() {
  try {
    // Check if Ethereum provider is available
    if (!isWalletAvailable()) {
      alert("No Ethereum provider detected. Please install MetaMask or a compatible wallet.");
      return;
    }

    // Initialize Web3 instance
    web3 = new Web3(window.ethereum);

    // Request wallet connection (will prompt MetaMask or compatible wallet UI)
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    // Get the first account (user's wallet address)
    userAddress = accounts[0];
    console.log("Connected Wallet Address:", userAddress);

    // Check if the connected network is supported
    const networkId = await web3.eth.net.getId();
    if (!supportedNetworks.includes(networkId)) {
      alert(`Unsupported network. Please switch to a supported network.`);
      return;
    }

    // Successfully connected - Perform any additional logic post-connection
    alert(`Wallet connected successfully! Address: ${userAddress}`);
  } catch (error) {
    // Handle errors during connection
    console.error("Error connecting wallet:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

/**
 * Disconnect Wallet Function
 * This function disconnects the user's wallet
 */
function disconnectWallet() {
  userAddress = ""; // Reset user address
  web3 = null; // Reset Web3 instance
  alert("Wallet disconnected successfully.");
}

/**
 * Event Listener for Network Changes
 * Ensures the app behaves correctly when the user switches networks
 */
function setupNetworkChangeListener() {
  if (window.ethereum) {
    window.ethereum.on("chainChanged", () => {
      window.location.reload(); // Reload the page to handle network change
    });
  }
}

/**
 * Event Listener for Account Changes
 * Detects when user changes their account in the wallet
 */
function setupAccountChangeListener() {
  if (window.ethereum) {
    window.ethereum.on("accountsChanged", (accounts) => {
      if (accounts.length > 0) {
        userAddress = accounts[0];
        alert(`Wallet address changed! New address: ${userAddress}`);
        console.log("New Wallet Address:", userAddress);
      } else {
        disconnectWallet(); // Handle case where user disconnects their wallet
      }
    });
  }
}

// Example usage: Call connectWallet on button click
document.getElementById("connectWalletButton").addEventListener("click", connectWallet);
document.getElementById("disconnectWalletButton").addEventListener("click", disconnectWallet);

// Setup listeners for network and account changes
setupNetworkChangeListener();
setupAccountChangeListener();
```

**Note**: Ensure you have buttons with IDs `connectWalletButton` and `disconnectWalletButton` in your HTML for this example to work.
