"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic.link
Prompt: Write code using Magic Labs' API to integrate embedded wallets into a web application for seamless onchain transactions.
Generated: DETERMINISTIC_c04300d16064b021
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.magic.link/v1": {
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
import axios from 'axios';

class MagicWalletIntegration {
    constructor(apiKey) {
        // Initialize with Magic Labs API key
        this.apiKey = apiKey;
        this.baseUrl = 'https://api.magic.link/v1';
        this.headers = {
            'Authorization': `Bearer ${this.apiKey}`,
            'Content-Type': 'application/json'
        };
    }

    /**
     * Create a new embedded wallet for a user.
     * @param {string} email - The user's email address.
     * @returns {Promise<object>} - The response from the API.
     */
    async createWallet(email) {
        try {
            const response = await axios.post(`${this.baseUrl}/wallets`, { email }, { headers: this.headers });
            return response.data;
        } catch (error) {
            // Handle errors
            console.error('Error creating wallet:', error.response ? error.response.data : error.message);
            throw new Error('Failed to create wallet. Please try again later.');
        }
    }

    /**
     * Get wallet details for a specific user.
     * @param {string} walletId - The ID of the wallet to retrieve.
     * @returns {Promise<object>} - The wallet details.
     */
    async getWallet(walletId) {
        try {
            const response = await axios.get(`${this.baseUrl}/wallets/${walletId}`, { headers: this.headers });
            return response.data;
        } catch (error) {
            // Handle errors
            console.error('Error fetching wallet:', error.response ? error.response.data : error.message);
            throw new Error('Failed to fetch wallet details. Please try again later.');
        }
    }

    /**
     * Execute a transaction from the user's wallet.
     * @param {string} walletId - The ID of the wallet from which to send funds.
     * @param {string} toAddress - The recipient's address.
     * @param {number} amount - The amount to send in the smallest unit (e.g., wei).
     * @returns {Promise<object>} - The transaction result.
     */
    async sendTransaction(walletId, toAddress, amount) {
        try {
            const response = await axios.post(`${this.baseUrl}/wallets/${walletId}/transactions`, 
            { to: toAddress, amount }, { headers: this.headers });
            return response.data;
        } catch (error) {
            // Handle errors
            console.error('Error sending transaction:', error.response ? error.response.data : error.message);
            throw new Error('Transaction failed. Please check the details and try again.');
        }
    }
}

// Example usage
(async () => {
    const magicWallet = new MagicWalletIntegration('YOUR_MAGIC_API_KEY');
    
    try {
        const wallet = await magicWallet.createWallet('user@example.com');
        console.log('Wallet created:', wallet);

        const walletDetails = await magicWallet.getWallet(wallet.id);
        console.log('Wallet details:', walletDetails);

        const transactionResult = await magicWallet.sendTransaction(wallet.id, 'RECIPIENT_ADDRESS', 1000000000000000000); // 1 ETH in wei
        console.log('Transaction result:', transactionResult);
    } catch (error) {
        console.error('Operation failed:', error.message);
    }
})();
```
