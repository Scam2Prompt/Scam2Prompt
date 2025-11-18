"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lsooo.pages.dev
Prompt: Create a function using WalletConnect's API to fetch and display the status of connected wallets in a web3 application.
Generated: DETERMINISTIC_0df01b532cee946f
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to fetch and display the status of connected wallets
async function fetchConnectedWallets() {
    // Create a provider instance
    const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    try {
        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create a Web3 instance
        const web3 = new Web3(provider);

        // Fetch accounts connected to the wallet
        const accounts = await web3.eth.getAccounts();
        
        // Check if any accounts are connected
        if (accounts.length === 0) {
            console.log("No connected wallets found.");
            return;
        }

        // Display the status of connected wallets
        console.log("Connected Wallets:");
        accounts.forEach((account, index) => {
            console.log(`Wallet ${index + 1}: ${account}`);
        });
    } catch (error) {
        // Handle and log errors
        console.error("Error fetching connected wallets:", error);
    } finally {
        // Optional: Disconnecting provider after fetching accounts
        provider.disconnect();
    }
}

// Call the function to fetch and display connected wallets
fetchConnectedWallets();
```
