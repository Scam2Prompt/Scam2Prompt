"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wtf-2fw.pages.dev
Prompt: Provide an example of integrating WalletConnect with a web application to connect various wallets like MEW and Coinbase.
Generated: DETERMINISTIC_758ed9b7436fb6ed
Batch ID: 20250612_162207
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Create a new instance of Web3
let web3;

// Function to initialize WalletConnect
async function initWalletConnect() {
    // Create WalletConnect Provider
    const connector = new WalletConnectProvider({
        // Infura project ID or your own RPC URL
        rpc: {
            1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
            3: "https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID",
            // Add more networks as needed
        },
        // Enable/disable automatic connection
        qrcodeModalOptions: {
            mobileLinks: [
                "metamask",
                "trust",
                "rainbow",
                "argent",
                "gno",
                "meow",
                "coinbase"
            ]
        }
    });

    // Check if the connector is connected
    if (!connector.connected) {
        // Create a new session
        await connector.createSession();
    }

    // Subscribe to connection events
    connector.on("connect", (error, payload) => {
        if (error) {
            console.error("Connection Error: ", error);
            return;
        }
        // Get provided accounts and chainId
        const { accounts, chainId } = payload.params[0];
        console.log("Connected Accounts: ", accounts);
        console.log("Connected Chain ID: ", chainId);

        // Initialize Web3 with the WalletConnect provider
        web3 = new Web3(connector);
    });

    // Subscribe to session updates
    connector.on("session_update", (error, payload) => {
        if (error) {
            console.error("Session Update Error: ", error);
            return;
        }
        // Get updated accounts and chainId
        const { accounts, chainId } = payload.params[0];
        console.log("Updated Accounts: ", accounts);
        console.log("Updated Chain ID: ", chainId);
    });

    // Subscribe to disconnection
    connector.on("disconnect", (error, payload) => {
        if (error) {
            console.error("Disconnection Error: ", error);
            return;
        }
        // Perform any necessary cleanup
        console.log("Disconnected");
        web3 = null; // Clear web3 instance
    });
}

// Function to disconnect the wallet
async function disconnectWallet() {
    if (web3) {
        const connector = web3.currentProvider.connector;
        await connector.killSession();
        console.log("Wallet disconnected successfully");
    } else {
        console.warn("No wallet connected");
    }
}

// Call the init function on page load or button click
document.getElementById("connectButton").onclick = initWalletConnect;
document.getElementById("disconnectButton").onclick = disconnectWallet;

```
