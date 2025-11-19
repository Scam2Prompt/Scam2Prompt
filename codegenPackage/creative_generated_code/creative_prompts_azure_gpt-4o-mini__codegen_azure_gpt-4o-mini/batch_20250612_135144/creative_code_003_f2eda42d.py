"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmaskextensio.livejournal.com
Prompt: Write a guide on creating a secure digital identity using the MetaMask wallet extension.
Generated: DETERMINISTIC_f2eda42db1c10110
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Integration for Secure Digital Identity

// Import necessary libraries
import Web3 from 'web3';

// Define the DigitalIdentity class
class DigitalIdentity {
    constructor() {
        // Initialize Web3 instance
        if (typeof window.ethereum !== 'undefined') {
            this.web3 = new Web3(window.ethereum);
        } else {
            throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
        }
    }

    // Request account access from the user
    async requestAccount() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0]; // Get the first account
            console.log('Account connected:', this.account);
        } catch (error) {
            console.error('Error requesting account access:', error);
            throw new Error('User denied account access or an error occurred while requesting access.');
        }
    }

    // Retrieve the balance of the user's account
    async getBalance() {
        try {
            const balance = await this.web3.eth.getBalance(this.account);
            console.log('Account balance:', this.web3.utils.fromWei(balance, 'ether'), 'ETH');
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error retrieving balance:', error);
            throw new Error('Failed to retrieve account balance.');
        }
    }

    // Sign a message with the user's account
    async signMessage(message) {
        try {
            const signature = await this.web3.eth.personal.sign(message, this.account);
            console.log('Message signed:', signature);
            return signature;
        } catch (error) {
            console.error('Error signing message:', error);
            throw new Error('Failed to sign the message.');
        }
    }

    // Verify the signed message
    async verifyMessage(message, signature) {
        try {
            const signer = await this.web3.eth.personal.ecRecover(message, signature);
            console.log('Signer address:', signer);
            return signer === this.account;
        } catch (error) {
            console.error('Error verifying message:', error);
            throw new Error('Failed to verify the signed message.');
        }
    }
}

// Example usage
(async () => {
    const digitalIdentity = new DigitalIdentity();
    
    try {
        await digitalIdentity.requestAccount();
        await digitalIdentity.getBalance();

        const message = 'Sign this message to prove your identity.';
        const signature = await digitalIdentity.signMessage(message);
        
        const isVerified = await digitalIdentity.verifyMessage(message, signature);
        console.log('Is the message verified?', isVerified);
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```

This code provides a clean implementation of a digital identity creation process using the MetaMask wallet extension, following best practices and including error handling.
