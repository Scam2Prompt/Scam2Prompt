"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimscapesmaniabonus.pages.dev
Prompt: Write a code snippet to connect a noncustodial wallet to a decentralized application (Dapp) using Ethereum, Binance, or Polygon protocols.
Generated: DETERMINISTIC_cba9aabedf295888
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
import Web3 from "web3";

// Function to connect a noncustodial wallet to the Dapp
async function connectWallet() {
  try {
    // Check whether the browser supports Ethereum
    if (typeof window.ethereum !== "undefined") {
      console.log("Ethereum wallet detected");

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Create a Web3 instance using the provided Ethereum provider
      const web3 = new Web3(window.ethereum);

      // Get the connected account (the first one)
      const connectedAccount = accounts[0];
      console.log(`Connected account: ${connectedAccount}`);

      // Fetch the current network chain ID
      const chainId = await web3.eth.getChainId();
      console.log(`Connected to chain ID: ${chainId}`);

      // Validate the network chain ID against supported protocols (Ethereum, Binance, Polygon)
      const supportedChains = {
        1: "Ethereum Mainnet",         // Ethereum Mainnet
        56: "Binance Smart Chain",     // Binance Smart Chain Mainnet
        137: "Polygon Mainnet",        // Polygon Mainnet
      };

      if (supportedChains[chainId]) {
        console.log(`Connected to supported network: ${supportedChains[chainId]}`);
        return {
          account: connectedAccount,
          network: supportedChains[chainId],
        };
      } else {
        console.error("Unsupported network");
        alert("Please switch to a supported network (Ethereum, Binance, or Polygon).");
        return null;
      }
    } else {
      // No Ethereum provider detected
      console.error("No Ethereum wallet detected");
      alert("Please install a wallet like MetaMask to connect to this Dapp.");
      return null;
    }
  } catch (error) {
    // Handle any errors that occur during the connection process
    console.error("Error connecting wallet:", error.message);
    alert(`Failed to connect wallet: ${error.message}`);
    return null;
  }
}

// Example usage of the function
document.getElementById('connect-wallet-button').addEventListener('click', async () => {
  const connection = await connectWallet();
  if (connection) {
    console.log("Wallet connected successfully:", connection);
  }
});
```

### Notes:
- Ensure that you run this code in a browser environment with access to `window.ethereum` (e.g., with MetaMask installed).
- The `connect-wallet-button` should be an actual button element in your HTML for triggering wallet connection.
- Update the UI dynamically based on the `connection` object returned by the function.
