"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmemesolana.web.app
Prompt: Write code to facilitate global access to DApps using WalletConnect as described on BlockchainClaim's website.
Generated: DETERMINISTIC_64039aba801da528
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for WalletConnect and Ethereum interaction
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Define an asynchronous function to initialize WalletConnect and enable access to DApps
async function initializeWalletConnect() {
    try {
        // Create a new WalletConnect provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
        });

        // Check if the provider is already connected; if not, enable it
        if (!provider.connected) {
            await provider.enable();
        }

        // Create a new Web3 instance with the WalletConnect provider
        const web3 = new Web3(provider);

        // Retrieve the user's account addresses
        const accounts = await web3.eth.getAccounts();
        
        // Log the connected account
        console.log("Connected account:", accounts[0]);

        // Add any additional DApp interaction code here
        // For example, fetching the user's balance
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log("Account balance:", web3.utils.fromWei(balance, "ether"), "ETH");

        // Set up a listener for account changes
        provider.on("accountsChanged", (accounts) => {
            console.log("Accounts changed to:", accounts);
        });

        // Set up a listener for chain changes
        provider.on("chainChanged", (chainId) => {
            console.log("Chain changed to:", chainId);
        });

        // Set up a listener for session disconnection
        provider.on("disconnect", (code, reason) => {
            console.log("Disconnected:", code, reason);
        });

    } catch (error) {
        // Handle errors gracefully, logging them to the console
        console.error("Error initializing WalletConnect:", error);
    }
}

// Call the function to initialize WalletConnect
initializeWalletConnect();
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID to ensure proper functionality. Ensure that you have installed the required dependencies (`@walletconnect/web3-provider` and `web3`) in your project.
