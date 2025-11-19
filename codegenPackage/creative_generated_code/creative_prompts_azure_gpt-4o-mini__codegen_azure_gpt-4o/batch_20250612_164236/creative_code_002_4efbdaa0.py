"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-dapp.vercel.app
Prompt: Can you provide a code example for integrating WalletConnect with a web3 library?
Generated: DETERMINISTIC_4efbdaa029cb1bbc
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers'; // Ethers.js for interacting with Ethereum blockchain
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider

// Asynchronous function to initialize WalletConnect integration
async function connectWallet() {
  try {
    // Initialize WalletConnect provider
    const walletConnectProvider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Enable the provider (opens WalletConnect QR code modal)
    await walletConnectProvider.enable();

    // Create a new instance of ethers.js provider using WalletConnect provider
    const web3Provider = new ethers.providers.Web3Provider(walletConnectProvider);

    // Get the signer instance from the provider (to interact with user's account)
    const signer = web3Provider.getSigner();

    // Get the connected user's wallet address
    const userAddress = await signer.getAddress();
    console.log("Connected wallet address:", userAddress);

    // Example: Fetch the current balance of the connected wallet
    const balance = await web3Provider.getBalance(userAddress);
    console.log("Wallet balance (ETH):", ethers.utils.formatEther(balance));

    // Listen for account or chain changes
    walletConnectProvider.on("accountsChanged", (accounts) => {
      console.log("Accounts changed:", accounts);
    });

    walletConnectProvider.on("chainChanged", (chainId) => {
      console.log("Chain changed:", chainId);
    });

    walletConnectProvider.on("disconnect", (code, reason) => {
      console.log("WalletConnect disconnected:", code, reason);
    });

    // Return the provider and signer for further interactions
    return { web3Provider, signer, userAddress };

  } catch (error) {
    // Handle errors (e.g., user closes modal without connecting)
    console.error("Failed to connect wallet:", error.message);
  }
}

// Connect wallet button handler example
document.getElementById("connectWalletButton").addEventListener("click", async () => {
  const connection = await connectWallet();
  if (connection) {
    console.log("Wallet connected successfully!");
    // You can now use connection.web3Provider and connection.signer for web3 interactions
  } else {
    console.log("Wallet connection failed.");
  }
});
```

**Dependencies:**
- Install the required packages before running the code:
  ```bash
  npm install ethers @walletconnect/web3-provider
  ```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID.
