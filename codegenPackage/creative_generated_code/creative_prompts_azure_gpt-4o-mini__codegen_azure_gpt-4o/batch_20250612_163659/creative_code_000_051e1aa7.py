"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opsecmigrationlive.pages.dev
Prompt: Write a code snippet to connect a noncustodial wallet to a decentralized application (Dapp) using Ethereum or Binance Smart Chain.
Generated: DETERMINISTIC_051e1aa79f22c140
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from "web3";

// Function to connect a noncustodial wallet to a DApp
async function connectWallet() {
  try {
    // Check if the user's browser supports Ethereum (MetaMask or similar wallets)
    if (typeof window.ethereum !== "undefined") {
      // Request the user to connect their wallet
      await window.ethereum.request({ method: "eth_requestAccounts" });
      
      // Initialize web3 instance
      const web3 = new Web3(window.ethereum);

      // Get the user's wallet address
      const accounts = await web3.eth.getAccounts();

      // Log the connected wallet address
      console.log("Connected wallet address:", accounts[0]);

      // Detect the currently connected network (Ethereum or Binance Smart Chain)
      const chainId = await web3.eth.getChainId();
      console.log("Connected network chain ID:", chainId);

      // Perform chain-specific logic (optional)
      if (chainId === 1) {
        console.log("Connected to Ethereum Mainnet");
      } else if (chainId === 56) {
        console.log("Connected to Binance Smart Chain Mainnet");
      } else {
        console.log("Connected to an unsupported network");
      }

      // Return the wallet address and chain ID for application use
      return { walletAddress: accounts[0], chainId };
    } else {
      // No wallet provider found
      throw new Error(
        "No Ethereum-compatible browser extension detected. Please install MetaMask or a similar wallet."
      );
    }
  } catch (error) {
    // Error handling
    console.error("Error connecting wallet:", error.message);
    alert("Error connecting wallet: " + error.message);
    return null;
  }
}

// Example usage of the function
connectWallet()
  .then((result) => {
    if (result) {
      console.log("Wallet successfully connected:", result);
    }
  })
  .catch((error) => {
    console.error("Failed to connect wallet:", error);
  });
```
