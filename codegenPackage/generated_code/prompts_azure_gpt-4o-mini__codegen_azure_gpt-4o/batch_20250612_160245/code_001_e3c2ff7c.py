"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Write a code snippet that demonstrates how to use WalletConnect to connect wallets to DApps as described in the Dapp Starter documentation.
Generated: DETERMINISTIC_e3c2ff7cfabfde71
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import WalletConnect dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to initialize WalletConnect and connect a wallet
async function connectWallet() {
  try {
    // Create a WalletConnect provider instance
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Enable the provider (this will prompt the user to connect their wallet)
    await provider.enable();

    // Create a Web3 instance using the WalletConnect provider
    const web3 = new Web3(provider);

    // Get the connected accounts
    const accounts = await web3.eth.getAccounts();

    // Log the connected account(s)
    console.log("Connected account(s):", accounts);

    // Example: Get the current chain ID
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);

    // Handle provider events (e.g., disconnect, accountsChanged, chainChanged)
    provider.on("disconnect", (error) => {
      console.log("Wallet disconnected:", error);
    });

    provider.on("accountsChanged", (accounts) => {
      console.log("Accounts changed:", accounts);
    });

    provider.on("chainChanged", (chainId) => {
      console.log("Chain changed:", chainId);
    });

    // Return the Web3 instance and connected accounts for further use
    return { web3, accounts };
  } catch (error) {
    // Handle errors (e.g., user rejected connection, network issues)
    console.error("Error connecting wallet:", error);
    throw error; // Rethrow the error for further handling
  }
}

// Example usage of the connectWallet function
(async () => {
  try {
    const { web3, accounts } = await connectWallet();
    console.log("Wallet successfully connected!");
    // You can now interact with the blockchain using the web3 instance
  } catch (error) {
    console.error("Failed to connect wallet:", error);
  }
})();
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID. Ensure you have installed the required dependencies (`@walletconnect/web3-provider` and `web3`) in your project using npm or yarn.
