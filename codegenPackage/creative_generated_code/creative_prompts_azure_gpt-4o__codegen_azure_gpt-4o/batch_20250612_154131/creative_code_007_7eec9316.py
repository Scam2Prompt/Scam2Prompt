"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorta.finance
Prompt: Explain how to use WalletConnect to enable multi-wallet support for a platform similar to Sorta Finance.
Generated: DETERMINISTIC_7eec9316a718eac3
Batch ID: 20250612_154131
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import necessary modules from WalletConnect SDK
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// A utility class to handle multi-wallet connections using WalletConnect
class WalletManager {
  constructor() {
    // To store active provider and Web3 instance
    this.provider = null;
    this.web3 = null;
  }
  
  /**
   * Initialize WalletConnect provider and enable multi-wallet support.
   */
  async initializeWalletConnect() {
    try {
      // Set up WalletConnect provider with supported chain IDs
      this.provider = new WalletConnectProvider({
        rpc: {
          1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Mainnet RPC URL
          4: "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Rinkeby RPC URL
        },
        qrcode: true, // Display QR code for wallet connection
        chainId: 1, // Default to Ethereum Mainnet
      });

      // Listen for connection events and handle them
      this.provider.on("connect", (info) => {
        console.log("Wallet connected:", info);
      });

      // Listen for disconnection events and handle them
      this.provider.on("disconnect", (error) => {
        console.error("Wallet disconnected:", error);
        this.cleanup();
      });

      // Listen for account changes and handle them
      this.provider.on("accountsChanged", (accounts) => {
        console.log("Accounts changed:", accounts);
      });

      // Listen for chain changes and handle them
      this.provider.on("chainChanged", (chainId) => {
        console.log("Chain ID changed:", chainId);
      });
    } catch (error) {
      console.error("Error initializing WalletConnect:", error);
      throw new Error("Failed to initialize WalletConnect");
    }
  }

  /**
   * Connect to a wallet using WalletConnect.
   */
  async connectWallet() {
    try {
      // Enable WalletConnect provider to get user accounts
      await this.provider.enable();

      // Initialize Web3 with the WalletConnect provider
      this.web3 = new Web3(this.provider);

      // Fetch connected accounts
      const accounts = await this.web3.eth.getAccounts();
      console.log("Connected accounts:", accounts);

      // Fetch connected chain ID
      const chainId = await this.web3.eth.getChainId();
      console.log("Connected chain ID:", chainId);

      return { accounts, chainId };
    } catch (error) {
      console.error("Error connecting wallet:", error);
      throw new Error("Failed to connect wallet");
    }
  }

  /**
   * Disconnect the wallet and clean up resources.
   */
  async disconnectWallet() {
    try {
      if (this.provider) {
        await this.provider.disconnect(); // Disconnect WalletConnect provider
        this.cleanup(); // Cleanup local resources
        console.log("Wallet successfully disconnected.");
      }
    } catch (error) {
      console.error("Error disconnecting wallet:", error);
      throw new Error("Failed to disconnect wallet");
    }
  }

  /**
   * Clean up resources when disconnecting.
   */
  cleanup() {
    this.provider = null;
    this.web3 = null;
  }
}

// Example usage of WalletManager
(async () => {
  // Create an instance of WalletManager
  const walletManager = new WalletManager();

  try {
    // Initialize WalletConnect
    await walletManager.initializeWalletConnect();

    // Connect to wallet
    const { accounts, chainId } = await walletManager.connectWallet();
    console.log("Wallet connected with accounts:", accounts, "on chain:", chainId);

    // Perform operations with the wallet and Web3 instance here...

    // After operations, disconnect the wallet
    await walletManager.disconnectWallet();
  } catch (error) {
    console.error("An error occurred:", error);
  }
})();
```

**Note:**
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- Ensure you install the necessary dependencies (`@walletconnect/web3-provider` and `web3`) using a package manager such as npm or yarn:
  ```bash
  npm install @walletconnect/web3-provider web3
  ```
