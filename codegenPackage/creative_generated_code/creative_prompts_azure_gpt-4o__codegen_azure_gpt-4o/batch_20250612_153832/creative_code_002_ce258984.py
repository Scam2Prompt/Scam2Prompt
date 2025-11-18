"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://public-metamask-com--cdn.bravesites.com
Prompt: Generate code to prompt MetaMask for wallet connection permissions in a dApp, allowing interaction with blockchain services like DeFi platforms or NFT marketplaces.
Generated: DETERMINISTIC_ce258984db2950a2
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required library for interacting with Ethereum blockchain
// Ensure that you've installed web3 or ethers.js in your project dependencies.
import Web3 from "web3";

// Function to initiate connection with MetaMask
async function connectMetaMask() {
  try {
    // Check if the browser has the MetaMask extension installed
    if (typeof window.ethereum === "undefined") {
      console.error("MetaMask is not installed. Please install MetaMask to use this dApp.");
      alert("MetaMask is not installed. Please install MetaMask to use this dApp.");
      return;
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    // Check if accounts were successfully retrieved
    if (accounts.length === 0) {
      console.error("No accounts are available.");
      alert("No accounts are available. Please ensure MetaMask is set up correctly.");
      return;
    }

    // Get the first account (default account to interact with)
    const userAccount = accounts[0];
    console.log("Connected wallet address:", userAccount);

    // Initialize Web3 instance using MetaMask's provider
    const web3 = new Web3(window.ethereum);

    // Example: Fetch current chain ID to confirm connection
    const chainId = await web3.eth.getChainId();
    console.log("Connected to chain ID:", chainId);

    // Example: Fetch current balance of the connected account
    const balance = await web3.eth.getBalance(userAccount);
    console.log("Account balance (in Wei):", balance);

    // Display a success message to the user
    alert(`Successfully connected to MetaMask!\nWallet Address: ${userAccount}\nChain ID: ${chainId}`);
  } catch (error) {
    // Catch and log errors during the connection process
    console.error("Error connecting to MetaMask:", error);
    alert(`Error connecting to MetaMask: ${error.message}`);
  }
}

// Example usage: Attach this function to a button click for wallet connection
document.getElementById("connectWalletButton").addEventListener("click", connectMetaMask);
```

**HTML Example for Button Integration:**
```html
<!-- Add this button element to your dApp's UI -->
<button id="connectWalletButton">Connect Wallet</button>
```

**Note:** Ensure you host your dApp over HTTPS for MetaMask compatibility, and use web3.js or ethers.js for advanced blockchain interactions.
