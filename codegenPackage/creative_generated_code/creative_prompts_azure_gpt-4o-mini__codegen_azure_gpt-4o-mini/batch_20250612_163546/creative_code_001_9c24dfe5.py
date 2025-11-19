"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Write a code snippet to implement WalletConnect for a DApp based on the guidance provided on the Dapp Starter page.
Generated: DETERMINISTIC_9c24dfe5fa5afbc7
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from WalletConnect and ethers.js
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Define a class to handle our DApp's WalletConnect functionality
class WalletConnectDApp {
    constructor() {
        // Initialize provider and signer
        this.provider = null;
        this.signer = null;
        this.walletConnect = null;
    }

    // Method to initialize WalletConnect provider
    async initWalletConnect() {
        // Create a WalletConnect provider
        this.walletConnect = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura Project ID
        });

        // Enable session (triggers QR Code modal)
        await this.walletConnect.enable();

        // Create an ethers provider using the WalletConnect provider
        this.provider = new ethers.providers.Web3Provider(this.walletConnect);
        this.signer = this.provider.getSigner();

        console.log("WalletConnect initialized successfully.");
    }

    // Method to get user's account address
    async getAccount() {
        try {
            const accounts = await this.provider.listAccounts();
            if (accounts.length > 0) {
                return accounts[0]; // Return the first account
            } else {
                throw new Error("No accounts found. Please connect your wallet.");
            }
        } catch (error) {
            console.error("Error retrieving accounts:", error);
            throw error; // Re-throw the error for handling elsewhere
        }
    }

    // Method to sign a message (for demonstration)
    async signMessage(message) {
        try {
            const account = await this.getAccount();
            const signature = await this.signer.signMessage(message);
            return { account, signature };
        } catch (error) {
            console.error("Error signing message:", error);
            throw error; // Re-throw the error for handling elsewhere
        }
    }

    // Method to disconnect the wallet
    async disconnect() {
        if (this.walletConnect) {
            await this.walletConnect.killSession();
            console.log("Wallet disconnected.");
        }
    }
}

// Example usage of the WalletConnectDApp class
(async () => {
    const dApp = new WalletConnectDApp();
    try {
        await dApp.initWalletConnect();
        const account = await dApp.getAccount();
        console.log("Connected account:", account);

        const message = "Hello, WalletConnect!";
        const { signature } = await dApp.signMessage(message);
        console.log("Signed message:", signature);
    } catch (error) {
        console.error("An error occurred in the DApp:", error);
    }
})();
```

Replace `YOUR_INFURA_ID` with your actual Infura project ID for the code to work properly. Ensure that you have the necessary dependencies installed by running:

```bash
npm install @walletconnect/web3-provider ethers
```
