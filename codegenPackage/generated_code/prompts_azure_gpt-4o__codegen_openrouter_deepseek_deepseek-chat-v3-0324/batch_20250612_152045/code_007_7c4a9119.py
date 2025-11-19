"""
Generated Code Metadata:
========================
Original URL: https://webogram.org
Prompt: Generate code to implement end-to-end encryption for messages sent through the Telegram Web client.
Generated: DETERMINISTIC_7c4a9119ae76ab23
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Telegram Web End-to-End Encryption Implementation

// Import required libraries
const crypto = require('crypto');
const { subtle } = require('crypto').webcrypto;

// Key management class
class KeyManager {
    constructor() {
        this.keyPair = null;
        this.sharedSecret = null;
        this.peerPublicKey = null;
    }

    // Generate ECDH key pair
    async generateKeyPair() {
        try {
            this.keyPair = await subtle.generateKey(
                {
                    name: "ECDH",
                    namedCurve: "P-256",
                },
                true,
                ["deriveKey", "deriveBits"]
            );
            return this.keyPair;
        } catch (error) {
            console.error("Key generation failed:", error);
            throw error;
        }
    }

    // Import peer's public key
    async importPeerPublicKey(keyData) {
        try {
            this.peerPublicKey = await subtle.importKey(
                "jwk",
                keyData,
                {
                    name: "ECDH",
                    namedCurve: "P-256",
                },
                true,
                []
            );
            return this.peerPublicKey;
        } catch (error) {
            console.error("Public key import failed:", error);
            throw error;
        }
    }

    // Derive shared secret
    async deriveSharedSecret() {
        if (!this.keyPair || !this.peerPublicKey) {
            throw new Error("Key pair or peer public key not available");
        }

        try {
            this.sharedSecret = await subtle.deriveBits(
                {
                    name: "ECDH",
                    public: this.peerPublicKey,
                },
                this.keyPair.privateKey,
                256
            );
            return this.sharedSecret;
        } catch (error) {
            console.error("Shared secret derivation failed:", error);
            throw error;
        }
    }
}

// Encryption/Decryption class
class MessageCrypto {
    constructor() {
        this.keyManager = new KeyManager();
        this.ivLength = 12; // AES-GCM IV length
    }

    // Initialize with key exchange
    async initialize(peerPublicKey) {
        try {
            await this.keyManager.generateKeyPair();
            await this.keyManager.importPeerPublicKey(peerPublicKey);
            await this.keyManager.deriveSharedSecret();
        } catch (error) {
            console.error("Initialization failed:", error);
            throw error;
        }
    }

    // Encrypt message
    async encryptMessage(message) {
        if (!this.keyManager.sharedSecret) {
            throw new Error("Shared secret not available");
        }

        try {
            // Generate random IV
            const iv = crypto.randomBytes(this.ivLength);
            
            // Derive encryption key from shared secret
            const encryptionKey = await subtle.importKey(
                "raw",
                this.keyManager.sharedSecret,
                { name: "AES-GCM" },
                false,
                ["encrypt"]
            );

            // Convert message to ArrayBuffer
            const encoder = new TextEncoder();
            const messageBuffer = encoder.encode(message);

            // Encrypt message
            const ciphertext = await subtle.encrypt(
                {
                    name: "AES-GCM",
                    iv: iv,
                    tagLength: 128,
                },
                encryptionKey,
                messageBuffer
            );

            // Combine IV and ciphertext
            const encryptedData = new Uint8Array(iv.length + ciphertext.byteLength);
            encryptedData.set(iv, 0);
            encryptedData.set(new Uint8Array(ciphertext), iv.length);

            return encryptedData;
        } catch (error) {
            console.error("Encryption failed:", error);
            throw error;
        }
    }

    // Decrypt message
    async decryptMessage(encryptedData) {
        if (!this.keyManager.sharedSecret) {
            throw new Error("Shared secret not available");
        }

        try {
            // Extract IV and ciphertext
            const iv = encryptedData.slice(0, this.ivLength);
            const ciphertext = encryptedData.slice(this.ivLength);

            // Derive decryption key from shared secret
            const decryptionKey = await subtle.importKey(
                "raw",
                this.keyManager.sharedSecret,
                { name: "AES-GCM" },
                false,
                ["decrypt"]
            );

            // Decrypt message
            const plaintext = await subtle.decrypt(
                {
                    name: "AES-GCM",
                    iv: iv,
                    tagLength: 128,
                },
                decryptionKey,
                ciphertext
            );

            // Convert to string
            const decoder = new TextDecoder();
            return decoder.decode(plaintext);
        } catch (error) {
            console.error("Decryption failed:", error);
            throw error;
        }
    }

    // Export public key for sharing
    async exportPublicKey() {
        if (!this.keyManager.keyPair) {
            throw new Error("Key pair not generated");
        }

        try {
            return await subtle.exportKey(
                "jwk",
                this.keyManager.keyPair.publicKey
            );
        } catch (error) {
            console.error("Public key export failed:", error);
            throw error;
        }
    }
}

// Telegram Web Client Integration
class TelegramWebClient {
    constructor() {
        this.crypto = new MessageCrypto();
        this.peerPublicKey = null;
    }

    // Initialize encryption with peer
    async initializeEncryption(peerPublicKey) {
        try {
            this.peerPublicKey = peerPublicKey;
            await this.crypto.initialize(peerPublicKey);
            return await this.crypto.exportPublicKey();
        } catch (error) {
            console.error("Encryption initialization failed:", error);
            throw error;
        }
    }

    // Send encrypted message
    async sendMessage(message) {
        try {
            const encryptedMessage = await this.crypto.encryptMessage(message);
            // In a real implementation, this would send to Telegram's servers
            return encryptedMessage;
        } catch (error) {
            console.error("Message sending failed:", error);
            throw error;
        }
    }

    // Receive and decrypt message
    async receiveMessage(encryptedMessage) {
        try {
            const decryptedMessage = await this.crypto.decryptMessage(encryptedMessage);
            return decryptedMessage;
        } catch (error) {
            console.error("Message receiving failed:", error);
            throw error;
        }
    }
}

// Example usage
(async () => {
    try {
        const client1 = new TelegramWebClient();
        const client2 = new TelegramWebClient();

        // Simulate key exchange
        const client1PublicKey = await client1.crypto.exportPublicKey();
        const client2PublicKey = await client2.crypto.exportPublicKey();

        await client1.initializeEncryption(client2PublicKey);
        await client2.initializeEncryption(client1PublicKey);

        // Send and receive message
        const originalMessage = "Hello, secure Telegram!";
        const encrypted = await client1.sendMessage(originalMessage);
        const decrypted = await client2.receiveMessage(encrypted);

        console.log("Original:", originalMessage);
        console.log("Decrypted:", decrypted);
    } catch (error) {
        console.error("Example failed:", error);
    }
})();
```
