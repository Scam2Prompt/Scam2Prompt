"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lsooo.pages.dev
Prompt: Suggest best practices for integrating WalletConnect into a web3 app, referencing the guidelines and resources mentioned on the WalletConnect website.
Generated: DETERMINISTIC_9f34542f13c80cf3
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries for WalletConnect and Web3
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import Web3 from "web3"; // Web3 library for interacting with Ethereum

// Define a function to initialize WalletConnect
async function initializeWalletConnect() {
    try {
        // Create a WalletConnect Provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create a Web3 instance using the WalletConnect provider
        const web3 = new Web3(provider);

        // Fetch and log the user's accounts
        const accounts = await web3.eth.getAccounts();
        console.log("Connected accounts:", accounts);

        // You can now interact with the Ethereum blockchain using the web3 instance
        // e.g., getting the balance of the first account
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log("Account balance:", web3.utils.fromWei(balance, "ether"), "ETH");

        // Handle events for session disconnection
        provider.on("disconnect", (code, reason) => {
            console.log("Disconnected:", code, reason);
        });

    } catch (error) {
        // Proper error handling
        console.error("Failed to connect to WalletConnect:", error);
    }
}

// Call the function to initialize WalletConnect
initializeWalletConnect();
```
