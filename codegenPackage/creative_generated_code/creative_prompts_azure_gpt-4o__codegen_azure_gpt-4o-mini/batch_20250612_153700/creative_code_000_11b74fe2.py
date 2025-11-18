"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdex.cloud
Prompt: Write code to integrate WalletConnect for connecting decentralized applications (dApps) to multiple wallets, including Metamask, Trust Wallet, and Phantom, using QR code scanning.
Generated: DETERMINISTIC_11b74fe200f406a7
Batch ID: 20250612_153700
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc-mainnet.maticvigil.com/": {
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
import QRCodeModal from "@walletconnect/qrcode-modal";
import Web3 from "web3";

// Check if Web3 is already injected (e.g., by MetaMask)
const web3 = new Web3(window.ethereum || "http://localhost:8545");

// WalletConnect integration function
async function connectWallet() {
    try {
        // Create WalletConnect Provider
        const connector = new WalletConnectProvider({
            // Infura or other RPC URLs can be used here
            rpc: {
                1: "https://mainnet.infura.io/v3/YOUR_INFURA_KEY", // Mainnet
                56: "https://bsc-dataseed.binance.org/", // Binance Smart Chain
                137: "https://rpc-mainnet.maticvigil.com/" // Polygon
            },
            qrcodeModal: QRCodeModal,
        });

        // Check if already connected
        if (!connector.connected) {
            await connector.createSession(); // Create a new session
        }

        // Subscribe to connection
        connector.on("connect", async (error, payload) => {
            if (error) {
                throw error; // Handle connection error
            }

            // Get provided accounts and chainId
            const { accounts, chainId } = payload.params[0];
            console.log("Connected accounts: ", accounts);
            console.log("Connected chain: ", chainId);

            // Set provider for web3 instance
            web3.setProvider(connector);
            // Now you can use web3 to interact with the blockchain
        });

        // Subscribe to session update
        connector.on("session_update", (error, payload) => {
            if (error) {
                throw error; // Handle session update error
            }

            const { accounts, chainId } = payload.params[0];
            console.log("Updated accounts: ", accounts);
            console.log("Updated chain: ", chainId);
        });

        // Subscribe to disconnection
        connector.on("disconnect", (error, payload) => {
            if (error) {
                throw error; // Handle disconnection error
            }
            console.log("Disconnected", payload);
            // Handle disconnection logic here
        });

    } catch (error) {
        console.error("Error connecting to wallet: ", error); // Log any errors
    }
}

// Call the connectWallet function on button click or relevant event
document.getElementById("connect-button").addEventListener("click", connectWallet);
```

Make sure to replace `YOUR_INFURA_KEY` with your actual Infura project key and include proper HTML to create a button with the `id="connect-button"` for the connection trigger.
