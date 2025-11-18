"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgn-staking-walletconnect.netlify.app
Prompt: Write code to handle errors when connecting a wallet to an SGN staking dApp using WalletConnect.
Generated: DETERMINISTIC_a3af427234a80597
Batch ID: 20250612_153647
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

// Initialize Web3 and WalletConnect provider
let web3;
let connector;

// Function to connect to wallet using WalletConnect
async function connectWallet() {
    try {
        // Create a connector instance
        connector = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
        });

        // Check if the connector is already connected
        if (!connector.connected) {
            // Create a new session
            await connector.enable();
        }

        // Create a Web3 instance with the connector's provider
        web3 = new Web3(connector);

        console.log("Wallet connected successfully!");
        
        // You can now interact with your staking dApp using web3 instance
    } catch (error) {
        // Handle specific errors during connection
        if (error.message.includes("User rejected the request")) {
            console.error("Connection request was rejected by the user.");
        } else if (error.message.includes("No provider found")) {
            console.error("No wallet provider found. Please install a wallet.");
        } else {
            console.error("An error occurred while connecting the wallet:", error);
        }
    }
}

// Function to disconnect the wallet
async function disconnectWallet() {
    try {
        if (connector) {
            await connector.killSession(); // Terminate the connection
            console.log("Wallet disconnected successfully!");
        }
    } catch (error) {
        console.error("An error occurred while disconnecting the wallet:", error);
    }
}

// Example usage
document.getElementById("connectButton").addEventListener("click", connectWallet);
document.getElementById("disconnectButton").addEventListener("click", disconnectWallet);
```

**Note**: Make sure to replace `"YOUR_INFURA_ID"` with your actual Infura project ID and ensure you have the necessary HTML buttons with IDs `connectButton` and `disconnectButton` for this code to work correctly.
