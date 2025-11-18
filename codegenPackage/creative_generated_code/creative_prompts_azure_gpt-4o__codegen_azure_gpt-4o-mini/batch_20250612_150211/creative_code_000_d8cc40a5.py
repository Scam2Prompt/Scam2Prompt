"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Write a script using the MetaMask API to connect a wallet and verify ownership by signing a message, as described in the $YE Token presale process.
Generated: DETERMINISTIC_d8cc40a59b84f5f3
Batch ID: 20250612_150211
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

// Create a class to handle wallet connection and message signing
class WalletConnector {
    constructor() {
        // Initialize Web3
        this.web3 = null;
        this.accounts = [];
    }

    // Method to connect to MetaMask
    async connectWallet() {
        try {
            // Check if MetaMask is installed
            if (typeof window.ethereum === 'undefined') {
                throw new Error('MetaMask is not installed. Please install it to use this feature.');
            }

            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.accounts = accounts;
            this.web3 = new Web3(window.ethereum);

            console.log('Wallet connected:', this.accounts[0]);
        } catch (error) {
            console.error('Error connecting to wallet:', error.message);
            alert('Connection failed: ' + error.message);
        }
    }

    // Method to sign a message
    async signMessage(message) {
        try {
            if (this.accounts.length === 0) {
                throw new Error('Please connect your wallet first.');
            }

            // Sign the provided message with the connected account
            const signature = await this.web3.eth.personal.sign(message, this.accounts[0], '');
            console.log('Message signed:', signature);

            return signature;
        } catch (error) {
            console.error('Error signing message:', error.message);
            alert('Signing failed: ' + error.message);
        }
    }

    // Method to verify the signed message
    verifyMessage(message, signature) {
        try {
            // Recover the signer address from the signature
            const signer = this.web3.eth.accounts.recover(message, signature);
            console.log('Signer Address:', signer);

            // Check if the signer address matches the connected wallet
            const isOwner = signer.toLowerCase() === this.accounts[0].toLowerCase();
            console.log('Ownership verification result:', isOwner);

            return isOwner;
        } catch (error) {
            console.error('Error verifying message:', error.message);
            alert('Verification failed: ' + error.message);
        }
    }
}

// Example usage
(async () => {
    const walletConnector = new WalletConnector();
    await walletConnector.connectWallet(); // Connect to wallet

    const message = "Please sign this message to verify ownership of your wallet.";
    const signature = await walletConnector.signMessage(message); // Sign message

    // Verify ownership
    const isOwner = walletConnector.verifyMessage(message, signature);
    if (isOwner) {
        console.log('Ownership verified successfully!');
    } else {
        console.log('Ownership verification failed.');
    }
})();
```
