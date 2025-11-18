"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantomwallet.io
Prompt: Generate a step-by-step guide for creating a Fantom wallet using JavaScript, including password encryption for the keystore file.
Generated: DETERMINISTIC_2b4881c34a187242
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const fs = require('fs');
const crypto = require('crypto');
const { v4: uuidv4 } = require('uuid');

// Function to create a Fantom wallet
function createFantomWallet(password) {
    // Generate a random private key
    const privateKey = crypto.randomBytes(32).toString('hex');
    
    // Create a wallet object
    const wallet = {
        version: 3,
        id: uuidv4(),
        address: generateAddress(privateKey),
        crypto: {
            cipher: 'aes-128-ctr',
            ciphertext: '',
            cipherparams: {
                iv: '',
            },
            kdf: 'scrypt',
            kdfparams: {
                dklen: 32,
                salt: crypto.randomBytes(32).toString('hex'),
                n: 262144,
                r: 8,
                p: 1,
            },
            mac: '',
        },
    };

    // Encrypt the private key and store in the wallet
    const encryptedKey = encryptPrivateKey(privateKey, password, wallet.crypto.kdfparams.salt);
    wallet.crypto.ciphertext = encryptedKey.ciphertext;
    wallet.crypto.cipherparams.iv = encryptedKey.iv;
    wallet.crypto.mac = encryptedKey.mac;

    // Convert wallet object to JSON
    const walletJson = JSON.stringify(wallet, null, 2);

    // Save the keystore file
    const fileName = `FantomWallet_${wallet.id}.json`;
    fs.writeFileSync(fileName, walletJson);

    console.log(`Wallet created and stored as ${fileName}`);
}

// Function to generate an Ethereum-like address from a private key
function generateAddress(privateKey) {
    const keccak256 = require('js-sha3').keccak_256;
    return '0x' + keccak256(Buffer.from(privateKey, 'hex')).slice(24);
}

// Function to encrypt the private key
function encryptPrivateKey(privateKey, password, salt) {
    try {
        const iv = crypto.randomBytes(16);
        const derivedKey = crypto.scryptSync(password, Buffer.from(salt, 'hex'), 32);
        const cipher = crypto.createCipheriv('aes-128-ctr', derivedKey.slice(0, 16), iv);
        
        let ciphertext = cipher.update(privateKey, 'hex', 'hex');
        ciphertext += cipher.final('hex');

        const mac = crypto.createHmac('sha256', derivedKey).update(Buffer.from(ciphertext, 'hex')).digest('hex');

        return {
            ciphertext: ciphertext,
            iv: iv.toString('hex'),
            mac: mac,
        };
    } catch (error) {
        console.error('Error encrypting the private key:', error);
        throw new Error('Encryption failed');
    }
}

// Example usage - replace 'your_password' with a secure password
const password = 'your_password';
createFantomWallet(password);
```

Make sure to replace `'your_password'` with a secure password when using the script. This code creates a Fantom wallet, encrypts the private key, and saves the wallet in a keystore file.
