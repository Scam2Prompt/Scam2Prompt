"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a code snippet to configure Web3Modal with multiple wallet providers in a Web3 application.
Generated: DETERMINISTIC_c7b52eddfd69fad4
Batch ID: 20250612_150030
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
// Import necessary dependencies
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';
import CoinbaseWalletSDK from '@coinbase/wallet-sdk';

// Function to configure and initialize Web3Modal
const configureWeb3Modal = () => {
  try {
    // Define provider options for Web3Modal
    const providerOptions = {
      /* WalletConnect configuration */
      walletconnect: {
        package: WalletConnectProvider, // Required
        options: {
          infuraId: "YOUR_INFURA_PROJECT_ID", // Required: Replace with your Infura Project ID
          rpc: {
            1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Replace with your Infura URL for Ethereum Mainnet
          },
        },
      },
      /* Coinbase Wallet configuration */
      coinbasewallet: {
        package: CoinbaseWalletSDK, // Required
        options: {
          appName: "Your App Name", // Required: Replace with your application name
          infuraId: "YOUR_INFURA_PROJECT_ID", // Required: Replace with your Infura Project ID
          rpc: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Replace with your Infura URL for Ethereum Mainnet
          chainId: 1, // Ethereum Mainnet
        },
      },
      /* Add additional wallet providers here if needed */
    };

    // Initialize Web3Modal instance
    const web3Modal = new Web3Modal({
      cacheProvider: true, // Optional: Enables caching to remember selected provider
      providerOptions, // Pass provider options
      theme: "dark", // Optional: Customize theme ("dark" or "light")
    });

    // Return configured Web3Modal instance
    return web3Modal;
  } catch (error) {
    console.error("Error configuring Web3Modal:", error);
    throw new Error("Failed to initialize Web3Modal");
  }
};

// Usage Example
(async () => {
  // Configure Web3Modal
  const web3Modal = configureWeb3Modal();

  // Display Web3Modal to the user for selecting a wallet provider
  try {
    const provider = await web3Modal.connect();
    console.log("Wallet connected successfully!", provider);
    // Perform further actions using the connected provider (e.g., interact with smart contracts)
  } catch (error) {
    console.error("Error connecting wallet:", error);
  }
})();
```

Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID and `"Your App Name"` with the name of your application.
