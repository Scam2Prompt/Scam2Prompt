"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: Write code to integrate Hemi’s blockchain with Metamask for asset transfers between Bitcoin and Ethereum networks.
Generated: DETERMINISTIC_aa13dc07ce9d89a4
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Set up the main class for the HemiBlockchainIntegration
class HemiBlockchainIntegration {
    constructor() {
        // Initialize Web3 and Ethereum provider
        this.web3 = new Web3(window.ethereum);
        this.provider = new ethers.providers.Web3Provider(window.ethereum);
    }

    // Function to connect to Metamask
    async connectMetamask() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Unable to connect to Metamask');
        }
    }

    // Function to transfer assets from Bitcoin to Ethereum
    async transferAssets(amount, toAddress, network) {
        // Validate input parameters
        if (!this.validateAmount(amount) || !this.validateAddress(toAddress)) {
            throw new Error('Invalid amount or address');
        }

        try {
            // Check the selected network
            if (network === 'ethereum') {
                // Create a transaction for Ethereum network
                const ethTransaction = {
                    to: toAddress,
                    value: this.web3.utils.toWei(amount.toString(), 'ether'),
                    gas: 21000,
                };

                // Send the transaction
                const accounts = await this.web3.eth.getAccounts();
                const txHash = await this.web3.eth.sendTransaction({ ...ethTransaction, from: accounts[0] });
                console.log('Ethereum Transaction Hash:', txHash);
                return txHash;
            } else if (network === 'bitcoin') {
                // Placeholder for Bitcoin transfer logic (implement Bitcoin transfer logic here)
                console.log('Initiating Bitcoin transfer (implementation required)');
                // Example: Implement Bitcoin transfer using appropriate library
                // const btcTransaction = await this.sendBitcoin(toAddress, amount);
                // return btcTransaction;
            } else {
                throw new Error('Unsupported network');
            }
        } catch (error) {
            console.error('Error during asset transfer:', error);
            throw new Error('Asset transfer failed');
        }
    }

    // Utility function to validate amount
    validateAmount(amount) {
        return amount > 0;
    }

    // Utility function to validate Ethereum address
    validateAddress(address) {
        return this.web3.utils.isAddress(address);
    }
}

// Example usage
(async () => {
    const integration = new HemiBlockchainIntegration();
    try {
        const account = await integration.connectMetamask();
        console.log('Account connected:', account);
        
        // Transfer Ethereum assets
        const txHash = await integration.transferAssets(0.01, '0xRecipientAddressHere', 'ethereum');
        console.log('Transaction successful with hash:', txHash);
        
        // For Bitcoin transfer, uncomment and implement the corresponding logic
        // const btcTxHash = await integration.transferAssets(0.001, 'BitcoinAddressHere', 'bitcoin');
        // console.log('Bitcoin Transaction successful with hash:', btcTxHash);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```

Remember to replace `'0xRecipientAddressHere'` and `'BitcoinAddressHere'` with actual addresses when using the code. Additionally, implement the Bitcoin transfer logic as needed.
