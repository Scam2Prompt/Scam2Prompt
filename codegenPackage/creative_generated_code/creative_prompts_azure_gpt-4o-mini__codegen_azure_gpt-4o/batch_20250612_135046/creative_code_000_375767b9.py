"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: How can I implement WalletConnect in my dApp to enhance user experience and facilitate wallet connections?
Generated: DETERMINISTIC_375767b9526a25c1
Batch ID: 20250612_135046
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
import Web3 from "web3";

// Function to initialize WalletConnect in your dApp
async function initializeWalletConnect() {
  try {
    // Step 1: Configure the WalletConnect provider
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Step 2: Enable the provider (opens WalletConnect QR code modal)
    await provider.enable();

    // Step 3: Create a Web3 instance using the WalletConnect provider
    const web3 = new Web3(provider);

    // Step 4: Get the connected wallet's accounts (address)
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Step 5: (Optional) Get the connected wallet's chain ID
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);

    // Step 6: Use the Web3 instance for further dApp interactions
    // Example: Get the balance of the connected wallet
    const balance = await web3.eth.getBalance(accounts[0]);
    console.log("Wallet balance:", web3.utils.fromWei(balance, "ether"));

    // Step 7: Handle provider events (e.g., disconnect, account change)
    provider.on("disconnect", (code, reason) => {
      console.log("Wallet disconnected:", code, reason);
      // Cleanup or refresh UI
    });

    provider.on("accountsChanged", (newAccounts) => {
      console.log("Accounts changed:", newAccounts);
      // Handle account changes
    });

    provider.on("chainChanged", (newChainId) => {
      console.log("Chain changed:", newChainId);
      // Handle chain changes
    });

    return { provider, web3, accounts, chainId }; // Return initialized objects for further use
  } catch (error) {
    // Handle errors (e.g., user rejects connection, network issues)
    console.error("Error initializing WalletConnect:", error);
    alert("Failed to connect to Wallet. Please try again.");
    return null;
  }
}

// Example usage: Integrating WalletConnect into a button click event
document.getElementById("connect-wallet").addEventListener("click", async () => {
  const walletConnection = await initializeWalletConnect();
  if (walletConnection) {
    console.log("WalletConnect successfully initialized!", walletConnection);
    // Perform additional dApp logic here
  }
});

// Cleanup function to disconnect the WalletConnect session
async function disconnectWalletConnect(provider) {
  if (provider && provider.close) {
    await provider.close();
    console.log("WalletConnect session disconnected.");
  } else {
    console.log("Provider does not support disconnection.");
  }
}
```

### Notes:
- Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID for Ethereum network interactions.
- Ensure you have installed `@walletconnect/web3-provider` and `web3` packages using npm or yarn:
  ```bash
  npm install @walletconnect/web3-provider web3
  ```
- Link the `connect-wallet` button to your HTML file for user interaction:
  ```html
  <button id="connect-wallet">Connect Wallet</button>
  ```
