"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: How can I implement native Solana support in MetaMask to enhance multichain access?
Generated: DETERMINISTIC_310bc51491b7cccb
Batch ID: 20250612_162701
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import Web3 from 'web3';
import { Connection, PublicKey } from '@solana/web3.js';

class MetaMaskSolanaSupport {
    constructor() {
        // Initialize Web3 provider for Ethereum
        this.ethereumWeb3 = new Web3(window.ethereum);
        // Solana connection
        this.solanaConnection = new Connection('https://api.mainnet-beta.solana.com');
    }

    /**
     * Connect to MetaMask and request account access
     * @returns {Promise<String>} - The connected Ethereum account address
     * @throws Will throw an error if the connection fails
     */
    async connectEthereum() {
        try {
            const accounts = await this.ethereumWeb3.eth.requestAccounts();
            return accounts[0];
        } catch (error) {
            console.error("Failed to connect to MetaMask:", error);
            throw new Error('MetaMask connection failed');
        }
    }

    /**
     * Retrieve the balance of a Solana account
     * @param {String} publicKey - The public key of the Solana account
     * @returns {Promise<Number>} - The balance in SOL
     * @throws Will throw an error if the balance retrieval fails
     */
    async getSolanaBalance(publicKey) {
        try {
            const balance = await this.solanaConnection.getBalance(new PublicKey(publicKey));
            return balance / 1000000000; // Convert lamports to SOL
        } catch (error) {
            console.error("Failed to retrieve Solana balance:", error);
            throw new Error('Solana balance retrieval failed');
        }
    }

    /**
     * Get the connected Ethereum account and its corresponding Solana balance
     * @returns {Promise<Object>} - An object containing Ethereum account and Solana balance
     */
    async getAccountInfo() {
        try {
            const ethAccount = await this.connectEthereum();
            // Placeholder Solana public key for demonstration
            const solanaPublicKey = '<YOUR_SOLANA_PUBLIC_KEY>'; 
            const solanaBalance = await this.getSolanaBalance(solanaPublicKey);
            return {
                ethAccount,
                solanaBalance
            };
        } catch (error) {
            console.error("Error while fetching account info:", error);
            throw new Error('Account information retrieval failed');
        }
    }
}

// Example usage
(async () => {
    // Instantiate MetaMaskSolanaSupport
    const metaMaskSolanaSupport = new MetaMaskSolanaSupport();

    try {
        const accountInfo = await metaMaskSolanaSupport.getAccountInfo();
        console.log("Account Info:", accountInfo);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```
Please replace `'<YOUR_SOLANA_PUBLIC_KEY>'` with a valid Solana public key for testing purposes.
