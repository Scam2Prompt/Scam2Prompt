"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webrectificationfix.com
Prompt: What are the best practices for building self-custodial wallets for DApps as outlined on WebRectificationFix?
Generated: DETERMINISTIC_d8109ce7d83819eb
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Wallet.js
// A simple implementation of a self-custodial wallet for DApps
// This wallet allows users to manage their private keys and perform transactions securely.

class SelfCustodialWallet {
    constructor() {
        // Initialize wallet properties
        this.privateKey = null;
        this.publicKey = null;
        this.balance = 0;
    }

    /**
     * Generates a new key pair for the wallet.
     * @returns {Object} Contains privateKey and publicKey
     */
    generateKeyPair() {
        try {
            // Using a built-in crypto library to generate keys
            const { generateKeyPairSync } = require('crypto');
            const { publicKey, privateKey } = generateKeyPairSync('ec', {
                namedCurve: 'sect239k1',
            });
            this.privateKey = privateKey.export({ type: 'spki', format: 'pem' });
            this.publicKey = publicKey.export({ type: 'spki', format: 'pem' });
            console.log("Key pair generated successfully.");
        } catch (error) {
            console.error("Error generating key pair:", error);
        }
    }

    /**
     * Sets the balance for the wallet.
     * @param {number} amount - The amount to set the balance.
     */
    setBalance(amount) {
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error("Invalid balance amount. Amount must be a non-negative number.");
        }
        this.balance = amount;
    }

    /**
     * Retrieves the current balance of the wallet.
     * @returns {number} The current balance.
     */
    getBalance() {
        return this.balance;
    }

    /**
     * Initiates a transaction from the wallet.
     * @param {number} amount - The amount to send.
     * @param {string} recipient - The recipient's public key.
     * @throws Will throw an error if the amount exceeds the balance or invalid recipient.
     */
    sendTransaction(amount, recipient) {
        if (amount <= 0) {
            throw new Error("Invalid transaction amount. Amount must be positive.");
        }
        if (amount > this.balance) {
            throw new Error("Insufficient balance for transaction.");
        }
        if (!this.isValidPublicKey(recipient)) {
            throw new Error("Invalid recipient public key.");
        }
        
        // Simulating transaction by deducting from balance
        this.balance -= amount;
        console.log(`Transaction of ${amount} sent to ${recipient}.`);
    }

    /**
     * Validates the format of a public key.
     * @param {string} publicKey - The public key to validate.
     * @returns {boolean} True if public key is valid, otherwise false.
     */
    isValidPublicKey(publicKey) {
        // Basic validation logic for public keys
        return typeof publicKey === 'string' && publicKey.length > 0;
    }
}

// Usage example
try {
    const wallet = new SelfCustodialWallet();
    wallet.generateKeyPair();
    wallet.setBalance(100);
    console.log(`Current balance: ${wallet.getBalance()}`);
    wallet.sendTransaction(30, 'recipient-public-key-example');
    console.log(`New balance: ${wallet.getBalance()}`);
} catch (error) {
    console.error("Error in wallet operation:", error);
}
```
