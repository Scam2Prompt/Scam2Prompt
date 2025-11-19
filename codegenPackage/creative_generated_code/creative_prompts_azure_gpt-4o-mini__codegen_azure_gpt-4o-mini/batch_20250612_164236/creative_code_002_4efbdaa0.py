"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-dapp.vercel.app
Prompt: Can you provide a code example for integrating WalletConnect with a web3 library?
Generated: DETERMINISTIC_4efbdaa029cb1bbc
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import Web3 from "web3"; // Web3 library for Ethereum interactions

// Function to initialize WalletConnect and Web3
async function initWalletConnect() {
    try {
        // Create WalletConnect Provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create Web3 instance with the WalletConnect provider
        const web3 = new Web3(provider);

        // Get the user's Ethereum account(s)
        const accounts = await web3.eth.getAccounts();
        console.log("Connected accounts:", accounts);

        // Example: Get the current network ID
        const networkId = await web3.eth.net.getId();
        console.log("Network ID:", networkId);

        // Example: Get the balance of the first account
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log("Account balance:", web3.utils.fromWei(balance, 'ether'), "ETH");

        // Return web3 instance for further use
        return web3;
    } catch (error) {
        console.error("Error initializing WalletConnect:", error);
        throw new Error("Failed to initialize WalletConnect");
    }
}

// Usage Example
(async () => {
    try {
        // Initialize WalletConnect and Web3
        const web3 = await initWalletConnect();

        // Additional interactions can be implemented here using the web3 instance
    } catch (error) {
        console.error("Error during WalletConnect setup:", error);
    }
})();
```
