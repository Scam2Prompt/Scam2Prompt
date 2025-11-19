"""
Generated Code Metadata:
========================
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a code snippet to configure Web3Modal with multiple wallet providers in a Web3 application.
Generated: DETERMINISTIC_c7b52eddfd69fad4
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import Web3Modal from "web3modal";
import WalletConnectProvider from "@walletconnect/web3-provider";
import Torus from "@toruslabs/torus-embed";
import Authereum from "authereum";
import Fortmatic from "fortmatic";
import Portis from "@portis/web3";

// Web3Modal configuration
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    },
  },
  torus: {
    package: Torus,
  },
  authereum: {
    package: Authereum,
  },
  fortmatic: {
    package: Fortmatic,
    options: {
      key: "YOUR_FORTMATIC_KEY", // Replace with your Fortmatic API key
    },
  },
  portis: {
    package: Portis,
    options: {
      id: "YOUR_PORTIS_ID", // Replace with your Portis ID
    },
  },
  // Add other wallet providers here
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // Optional - cache provider for better UX
  providerOptions, // Required
  theme: "dark", // Optional - change modal theme
});

// Function to connect wallet
async function connectWallet() {
  try {
    const provider = await web3Modal.connect();
    return provider;
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw error;
  }
}

// Function to clear cached provider and disconnect
function disconnectWallet() {
  web3Modal.clearCachedProvider();
}

// Example usage
async function init() {
  try {
    const provider = await connectWallet();
    console.log("Connected with provider:", provider);
    // Initialize your web3 instance here
  } catch (error) {
    console.error("Initialization failed:", error);
  }
}

// Initialize on page load or button click
// init();
```
