"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write a code snippet for integrating WalletConnect with a DApp as described on the Dapp Starter page.
Generated: DETERMINISTIC_2678d25edfd0f1f5
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Initialize a WalletConnect Provider
const provider = new WalletConnectProvider({
  infuraId: "YOUR_INFURA_ID", // Required
});

// Function to connect WalletConnect
async function connectWallet() {
  try {
    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Create a Web3 provider with WalletConnect
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Get the signer for transactions
    const signer = web3Provider.getSigner();

    // Retrieve the user's address
    const userAddress = await signer.getAddress();
    console.log("Connected address:", userAddress);

    return { web3Provider, signer, userAddress };
  } catch (error) {
    console.error("Failed to connect to WalletConnect:", error);
    throw new Error("Wallet connection failed");
  }
}

// Function to disconnect WalletConnect
async function disconnectWallet() {
  try {
    // Kill the session
    await provider.disconnect();
    console.log("Wallet disconnected");
  } catch (error) {
    console.error("Failed to disconnect WalletConnect:", error);
  }
}

// Event listener for session updates
provider.on("accountsChanged", (accounts) => {
  console.log("Accounts changed:", accounts);
  // Handle account change
});

provider.on("chainChanged", (chainId) => {
  console.log("Chain changed:", chainId);
  // Handle chain change
});

// Export functions for use in the DApp
export { connectWallet, disconnectWallet };
```

**Note:** Replace `"YOUR_INFURA_ID"` with your actual Infura project ID to connect to the Ethereum network. Make sure to install the required dependencies via npm:

```bash
npm install @walletconnect/web3-provider ethers
```
