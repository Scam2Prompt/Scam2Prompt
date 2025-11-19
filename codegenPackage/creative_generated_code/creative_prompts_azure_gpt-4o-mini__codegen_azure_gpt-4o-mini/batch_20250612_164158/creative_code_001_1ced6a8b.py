"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-demo.vercel.app
Prompt: Write a code snippet to implement WalletConnect for connecting to a MetaMask wallet in a JavaScript application.
Generated: DETERMINISTIC_1ced6a8b8ecafe7b
Batch ID: 20250612_164158
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

// Define an async function to connect to MetaMask using WalletConnect
async function connectWallet() {
    try {
        // Create a new WalletConnect Provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create a Web3 instance with the WalletConnect provider
        const web3 = new Web3(provider);

        // Get the user's account
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error("No accounts found. Please connect to a wallet.");
        }

        // Log the connected account
        console.log("Connected account:", accounts[0]);

        // You can now interact with the Ethereum blockchain using web3
        // For example, get the balance of the connected account
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log("Account balance:", web3.utils.fromWei(balance, "ether"), "ETH");

        // Return the provider and web3 instance for further usage
        return { provider, web3, account: accounts[0] };

    } catch (error) {
        // Handle errors and log them for debugging
        console.error("Wallet connection error:", error.message);
        alert(`Failed to connect to wallet: ${error.message}`);
    }
}

// Example usage of the connectWallet function
document.getElementById("connect-button").addEventListener("click", connectWallet);
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID and include the necessary HTML to have a button with the ID `connect-button` to trigger the connection.
