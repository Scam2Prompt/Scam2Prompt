"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorta.finance
Prompt: Explain how to use WalletConnect to enable multi-wallet support for a platform similar to Sorta Finance.
Generated: DETERMINISTIC_7eec9316a718eac3
Batch ID: 20250612_154131
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

// Define a class for WalletConnect integration
class WalletConnectIntegration {
    constructor() {
        // Initialize the provider
        this.provider = null;
        this.web3 = null;
    }

    /**
     * Initialize WalletConnect provider
     * @returns {Promise<void>}
     */
    async initProvider() {
        // Create a WalletConnect Provider
        this.provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
        });

        // Enable session (triggers QR Code modal)
        try {
            await this.provider.enable();
            this.web3 = new Web3(this.provider); // Create Web3 instance with the provider
        } catch (error) {
            console.error("Error enabling WalletConnect provider:", error);
            throw new Error("Could not enable WalletConnect provider");
        }
    }

    /**
     * Get the connected accounts
     * @returns {Promise<string[]>}
     */
    async getAccounts() {
        if (!this.web3) {
            throw new Error("Web3 instance is not initialized. Please call initProvider first.");
        }
        
        try {
            const accounts = await this.web3.eth.getAccounts();
            return accounts;
        } catch (error) {
            console.error("Error fetching accounts:", error);
            throw new Error("Could not fetch accounts");
        }
    }

    /**
     * Send a transaction
     * @param {string} to - The recipient address
     * @param {string|number} value - The amount to send (in wei)
     * @returns {Promise<string>} - Transaction hash
     */
    async sendTransaction(to, value) {
        if (!this.web3) {
            throw new Error("Web3 instance is not initialized. Please call initProvider first.");
        }

        try {
            const accounts = await this.getAccounts();
            const tx = {
                from: accounts[0],
                to: to,
                value: this.web3.utils.toWei(value.toString(), 'ether'), // Convert value to wei
                gas: 2000000, // Set gas limit
            };

            const txHash = await this.web3.eth.sendTransaction(tx);
            return txHash.transactionHash; // Return transaction hash
        } catch (error) {
            console.error("Error sending transaction:", error);
            throw new Error("Transaction failed");
        }
    }

    /**
     * Disconnect the WalletConnect session
     * @returns {Promise<void>}
     */
    async disconnect() {
        if (this.provider) {
            await this.provider.disconnect();
            this.web3 = null; // Reset Web3 instance
        } else {
            console.warn("No provider to disconnect from");
        }
    }
}

// Example usage
(async () => {
    const walletConnect = new WalletConnectIntegration();

    try {
        await walletConnect.initProvider();
        const accounts = await walletConnect.getAccounts();
        console.log("Connected accounts:", accounts);

        // Example: Send a transaction
        const txHash = await walletConnect.sendTransaction("0xRecipientAddress", 0.01);
        console.log("Transaction hash:", txHash);
    } catch (error) {
        console.error("Error in WalletConnect workflow:", error.message);
    } finally {
        await walletConnect.disconnect(); // Clean up
    }
})();
```
