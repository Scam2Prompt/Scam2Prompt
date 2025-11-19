"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.ideas2goal.com
Prompt: What are the steps to enable JavaScript for WalletConnect in a web app?
Generated: DETERMINISTIC_4caf544db4bf6c41
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import WalletConnect dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to initialize WalletConnect
async function initializeWalletConnect() {
  try {
    // Step 1: Set up WalletConnect Provider
    const provider = new WalletConnectProvider({
      // WalletConnect options (Optional: customize as needed)
      infuraId: "YOUR_INFURA_PROJECT_ID" // Replace with your Infura Project ID
    });

    // Step 2: Enable the provider (Triggers QR Code for connection in supported wallets)
    await provider.enable();

    // Step 3: Initialize Web3 instance with the WalletConnect provider
    const web3 = new Web3(provider);

    // Step 4: Fetch accounts connected via WalletConnect
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Step 5: Fetch chain ID (Optional: validate the connected chain)
    const chainId = await web3.eth.getChainId();
    console.log("Connected chain ID:", chainId);

    // OPTIONAL: Add listeners for WalletConnect events
    provider.on("disconnect", (code, reason) => {
      console.log(`Wallet disconnected: Code ${code}, Reason: ${reason}`);
      // Handle disconnection logic
    });

    provider.on("accountsChanged", (newAccounts) => {
      console.log("Accounts changed:", newAccounts);
      // Handle account change logic
    });

    provider.on("chainChanged", (newChainId) => {
      console.log("Chain changed:", newChainId);
      // Handle chain change logic
    });

    // Return initialized Web3 instance and provider for further use
    return { web3, provider };

  } catch (error) {
    // Handle errors during initialization
    console.error("Error initializing WalletConnect:", error.message);
    throw new Error("Failed to initialize WalletConnect");
  }
}

// Example usage
initializeWalletConnect()
  .then(({ web3, provider }) => {
    console.log("WalletConnect initialized successfully.");
    // Use web3 and provider for further blockchain interactions
  })
  .catch((error) => {
    console.error("Initialization failed:", error.message);
  });
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID to connect to Ethereum networks. Additionally, you might need to install the required dependencies (`@walletconnect/web3-provider` and `web3`) using npm or yarn:

```bash
npm install @walletconnect/web3-provider web3
```
