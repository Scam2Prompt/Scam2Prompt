"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-moonbag-org.pages.dev
Prompt: Generate a code snippet to connect a wallet using WalletConnect or MetaMask for the MoonBag cryptocurrency presale.
Generated: DETERMINISTIC_2a94f6ce17b6f3e6
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Code snippet to connect a wallet using WalletConnect or MetaMask
 * for the MoonBag cryptocurrency presale.
 * This example utilizes Web3.js for interacting with the Ethereum blockchain.
 */

import Web3 from 'web3'; // Web3.js library for blockchain interaction
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider

// Configuration
const PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress"; // Replace with MoonBag presale contract address
const CHAIN_ID = 1; // Ethereum Mainnet. Change to the desired chain ID for presale.

// Initialize Web3 instance
let web3;
let currentAccount;

// Function to connect wallet via MetaMask or WalletConnect
async function connectWallet(providerType) {
  try {
    if (providerType === "metamask") {
      // Check if MetaMask is available
      if (typeof window.ethereum === "undefined") {
        throw new Error("MetaMask is not installed. Please install MetaMask to continue.");
      }

      // Request account access
      await window.ethereum.request({ method: "eth_requestAccounts" });
      web3 = new Web3(window.ethereum); // Use MetaMask's provided provider
    } else if (providerType === "walletconnect") {
      // Configure WalletConnect provider
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "YourInfuraID" // Replace with your Infura project ID
      });

      // Enable WalletConnect session
      await walletConnectProvider.enable();
      web3 = new Web3(walletConnectProvider); // Use WalletConnect's provider
    } else {
      throw new Error("Invalid provider type. Use 'metamask' or 'walletconnect'.");
    }

    // Get the current account
    const accounts = await web3.eth.getAccounts();
    currentAccount = accounts[0];
    console.log("Connected account:", currentAccount);

    // Check if the correct chain is selected
    const networkId = await web3.eth.net.getId();
    if (networkId !== CHAIN_ID) {
      throw new Error(`Please switch your wallet to the network with chain ID ${CHAIN_ID}.`);
    }

    console.log("Wallet connected and ready.");
  } catch (error) {
    console.error("Error connecting wallet:", error.message);
  }
}

// Example usage
// Connect via MetaMask
document.getElementById("connectMetaMaskBtn").addEventListener("click", () => {
  connectWallet("metamask");
});

// Connect via WalletConnect
document.getElementById("connectWalletConnectBtn").addEventListener("click", () => {
  connectWallet("walletconnect");
});

// Note: Ensure you have buttons with IDs 'connectMetaMaskBtn' and 'connectWalletConnectBtn' in your HTML.
```

Ensure to replace the placeholders like `YourInfuraID` and `0xYourPresaleContractAddress` with real values for your project. Add proper UI elements (buttons) in your HTML to trigger the wallet connection functionality.
