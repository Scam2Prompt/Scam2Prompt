"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth.net
Prompt: What are the steps to integrate a cryptocurrency wallet connection using WalletConnect in a project like Common Wealth?
Generated: DETERMINISTIC_114151f0ad56971f
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to initialize WalletConnect and connect to a cryptocurrency wallet
async function connectWallet() {
  try {
    // Step 1: Configure WalletConnect provider
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
    });

    // Step 2: Enable the provider (shows QR code to connect wallet)
    await provider.enable();

    // Step 3: Create a Web3 instance using the WalletConnect provider
    const web3 = new Web3(provider);

    // Step 4: Get the connected wallet's accounts
    const accounts = await web3.eth.getAccounts();

    // Step 5: Log the connected wallet address
    console.log("Connected Wallet Address:", accounts[0]);

    // You can now use `web3` for further interactions such as sending transactions, querying balances, etc.

    // Example: Fetch balance of the connected wallet
    const balance = await web3.eth.getBalance(accounts[0]);
    console.log("Wallet Balance (in Wei):", balance);

    // Example: Convert balance to Ether for better readability
    const balanceInEth = web3.utils.fromWei(balance, "ether");
    console.log("Wallet Balance (in Ether):", balanceInEth);

    return {
      provider,
      web3,
      walletAddress: accounts[0],
      balanceInEth,
    };
  } catch (error) {
    console.error("Error connecting wallet:", error.message);
    throw new Error("Failed to connect to wallet. Please try again.");
  }
}

// Function to disconnect the wallet
async function disconnectWallet(provider) {
  try {
    // Step 1: Disconnect WalletConnect provider
    if (provider && provider.disconnect) {
      await provider.disconnect();
      console.log("Wallet disconnected successfully.");
    } else {
      console.log("No provider found to disconnect.");
    }
  } catch (error) {
    console.error("Error disconnecting wallet:", error.message);
    throw new Error("Failed to disconnect wallet. Please try again.");
  }
}

// Usage Example
(async () => {
  try {
    // Connect the wallet
    const walletDetails = await connectWallet();
    console.log("Wallet Details:", walletDetails);

    // Disconnect the wallet (optional, e.g., on user logout)
    // await disconnectWallet(walletDetails.provider);
  } catch (error) {
    console.error("Error:", error.message);
  }
})();
```

**Note:**
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- Ensure you have installed the required dependencies (`@walletconnect/web3-provider` and `web3`) by running:
  ```
  npm install @walletconnect/web3-provider web3
  ```
