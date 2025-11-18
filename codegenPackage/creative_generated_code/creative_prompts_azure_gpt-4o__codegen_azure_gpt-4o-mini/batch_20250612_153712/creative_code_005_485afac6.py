"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmsetumsklogi.webflow.io
Prompt: Write a function in JavaScript to securely store and retrieve the seed phrase for a Metamask wallet, ensuring encryption is used for storage.
Generated: DETERMINISTIC_485afac699685f7c
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Securely stores and retrieves a seed phrase for a Metamask wallet.
 * Utilizes the Web Crypto API for encryption and decryption.
 */

class SeedPhraseManager {
    constructor() {
        // The algorithm used for encryption
        this.algorithm = {
            name: "AES-GCM",
            length: 256
        };
        // This will hold the encryption key
        this.encryptionKey = null;
    }

    /**
     * Generates a cryptographic key for encryption/decryption
     * @returns {Promise<void>}
     */
    async generateEncryptionKey() {
        this.encryptionKey = await window.crypto.subtle.generateKey(
            this.algorithm,
            true,
            ["encrypt", "decrypt"]
        );
    }

    /**
     * Encrypts the seed phrase
     * @param {string} seedPhrase - The seed phrase to encrypt
     * @returns {Promise<ArrayBuffer>} - The encrypted seed phrase as an ArrayBuffer
     */
    async encryptSeedPhrase(seedPhrase) {
        if (!this.encryptionKey) {
            throw new Error("Encryption key not generated.");
        }

        const iv = window.crypto.getRandomValues(new Uint8Array(12)); // Initialization vector
        const encodedPhrase = new TextEncoder().encode(seedPhrase);
        
        const encrypted = await window.crypto.subtle.encrypt(
            {
                ...this.algorithm,
                iv: iv
            },
            this.encryptionKey,
            encodedPhrase
        );

        // Return the IV and encrypted data for decryption
        return { iv: iv, data: new Uint8Array(encrypted) };
    }

    /**
     * Decrypts the encrypted seed phrase
     * @param {Object} encryptedData - Contains the IV and encrypted data
     * @returns {Promise<string>} - The decrypted seed phrase
     */
    async decryptSeedPhrase(encryptedData) {
        if (!this.encryptionKey) {
            throw new Error("Encryption key not generated.");
        }

        const { iv, data } = encryptedData;

        const decrypted = await window.crypto.subtle.decrypt(
            {
                ...this.algorithm,
                iv: iv
            },
            this.encryptionKey,
            data
        );

        return new TextDecoder().decode(decrypted);
    }

    /**
     * Stores the encrypted seed phrase securely in local storage
     * @param {string} seedPhrase - The seed phrase to store
     * @returns {Promise<void>}
     */
    async storeSeedPhrase(seedPhrase) {
        const encryptedData = await this.encryptSeedPhrase(seedPhrase);
        localStorage.setItem("encryptedSeedPhrase", JSON.stringify(encryptedData));
    }

    /**
     * Retrieves and decrypts the seed phrase from local storage
     * @returns {Promise<string>} - The decrypted seed phrase
     */
    async retrieveSeedPhrase() {
        const encryptedData = localStorage.getItem("encryptedSeedPhrase");
        if (!encryptedData) {
            throw new Error("No seed phrase found in storage.");
        }

        return await this.decryptSeedPhrase(JSON.parse(encryptedData));
    }
}

// Usage example
(async () => {
    const seedPhraseManager = new SeedPhraseManager();
    await seedPhraseManager.generateEncryptionKey();

    const seedPhrase = "example seed phrase for testing";
    await seedPhraseManager.storeSeedPhrase(seedPhrase);

    const retrievedSeedPhrase = await seedPhraseManager.retrieveSeedPhrase();
    console.log("Retrieved Seed Phrase:", retrievedSeedPhrase);
})();
```
