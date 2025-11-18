"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anydurasup.pages.dev
Prompt: Generate JavaScript code to enable WalletConnect functionality for scanning QR codes to connect a DApp, as outlined in the webpage content.
Generated: DETERMINISTIC_9a3818826ff12d44
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import WalletConnect and necessary dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";

// Create a function to initialize WalletConnect functionality
const initializeWalletConnect = async () => {
  try {
    // Create a WalletConnect Provider instance
    const walletConnectProvider = new WalletConnectProvider({
      // Required configuration for WalletConnect
      // Replace with your own Infura Project ID or other RPC endpoint
      rpc: {
        1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
      },
      qrcode: true, // Enable QR code display
    });

    // Subscribe to connection events (optional)
    walletConnectProvider.on("connect", (error, payload) => {
      if (error) {
        console.error("Error during WalletConnect connection", error);
        return;
      }
      console.log("Wallet connected successfully:", payload);
    });

    walletConnectProvider.on("disconnect", (error, payload) => {
      if (error) {
        console.error("Error during WalletConnect disconnection", error);
        return;
      }
      console.log("Wallet disconnected:", payload);
    });

    walletConnectProvider.on("session_update", (payload) => {
      console.log("Session updated:", payload);
    });

    // Enable WalletConnect provider (scans QR code and connects wallet)
    await walletConnectProvider.enable();

    // Log the connected accounts and chain ID
    const accounts = walletConnectProvider.accounts;
    const chainId = walletConnectProvider.chainId;

    console.log("Connected Accounts:", accounts);
    console.log("Connected Chain ID:", chainId);

    // Use the provider in your Web3 instance
    const web3 = new Web3(walletConnectProvider);

    // Example: Fetch the balance of the first connected account
    const balance = await web3.eth.getBalance(accounts[0]);
    console.log(`Balance of account ${accounts[0]}:`, web3.utils.fromWei(balance, "ether"));

    // Return the provider instance for further usage
    return walletConnectProvider;
  } catch (error) {
    console.error("Error initializing WalletConnect:", error);
    throw error; // Rethrow the error for further handling by the caller
  }
};

// Example usage of the initializeWalletConnect function
(async () => {
  try {
    const walletProvider = await initializeWalletConnect();
    console.log("WalletConnect initialized successfully.");
    // Do additional operations with the walletProvider if needed
  } catch (error) {
    console.error("Failed to initialize WalletConnect:", error);
  }
})();
```

Make sure to install the required dependencies (`@walletconnect/web3-provider` and `web3`) by running:
```bash
npm install @walletconnect/web3-provider web3
```

Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID or other RPC endpoint.
