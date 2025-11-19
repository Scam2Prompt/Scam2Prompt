"""
Generated Code Metadata:
========================
Original URL: https://phantom-phantomwallet.github.io
Prompt: Generate a script that demonstrates the security features of Phantom Wallet, focusing on end-to-end encryption and seed phrase management.
Generated: DETERMINISTIC_da5cc7a59e494bfb
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const crypto = require('crypto');
const readline = require('readline');

// Define a class for seed phrase management
class SeedPhraseManager {
  /**
   * Generates a random seed phrase
   * @returns {string[]} - An array of 12 random words
   */
  generateSeedPhrase() {
    // List of words to choose from (BIP39 wordlist)
    const wordlist = [
      'abandon', 'ability', 'able', 'about', 'above', 'accept', 'access', 'accommodate', 'accumulate', 'accurate',
      'achieve', 'acquire', 'across', 'act', 'action', 'actor', 'actress', 'actual', 'adapt', 'add', 'addict',
      // ... (full BIP39 wordlist)
    ];

    // Select 12 random words from the wordlist
    const seedPhrase = [];
    for (let i = 0; i < 12; i++) {
      seedPhrase.push(wordlist[Math.floor(Math.random() * wordlist.length)]);
    }
    return seedPhrase;
  }

  /**
   * Encrypts a seed phrase using a password
   * @param {string[]} seedPhrase - The seed phrase to encrypt
   * @param {string} password - The password to use for encryption
   * @returns {string} - The encrypted seed phrase
   */
  encryptSeedPhrase(seedPhrase, password) {
    // Create a new AES-256-CBC cipher
    const cipher = crypto.createCipheriv('aes-256-cbc', this.deriveKey(password), crypto.randomBytes(16));

    // Convert the seed phrase to a string
    const seedPhraseString = seedPhrase.join(' ');

    // Encrypt the seed phrase
    const encrypted = Buffer.concat([cipher.update(seedPhraseString), cipher.final()]);

    // Return the encrypted seed phrase as a base64-encoded string
    return encrypted.toString('base64');
  }

  /**
   * Decrypts an encrypted seed phrase using a password
   * @param {string} encryptedSeedPhrase - The encrypted seed phrase
   * @param {string} password - The password to use for decryption
   * @returns {string[]} - The decrypted seed phrase
   */
  decryptSeedPhrase(encryptedSeedPhrase, password) {
    // Create a new AES-256-CBC decipher
    const decipher = crypto.createDecipheriv('aes-256-cbc', this.deriveKey(password), Buffer.from(encryptedSeedPhrase, 'base64').slice(0, 16));

    // Decrypt the seed phrase
    const decrypted = Buffer.concat([decipher.update(Buffer.from(encryptedSeedPhrase, 'base64')), decipher.final()]);

    // Convert the decrypted seed phrase back to an array of words
    const seedPhrase = decrypted.toString().split(' ');

    return seedPhrase;
  }

  /**
   * Derives a key from a password using PBKDF2
   * @param {string} password - The password to derive a key from
   * @returns {Buffer} - The derived key
   */
  deriveKey(password) {
    // Use PBKDF2 with SHA-256 to derive a key
    const salt = crypto.randomBytes(16);
    const key = crypto.pbkdf2Sync(password, salt, 100000, 32, 'sha256');

    return key;
  }
}

// Define a class for end-to-end encryption
class EndToEndEncryption {
  /**
   * Generates a new key pair
   * @returns {{publicKey: string, privateKey: string}} - A new key pair
   */
  generateKeyPair() {
    // Generate a new RSA key pair
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
      modulusLength: 4096,
      publicExponent: 65537,
      publicKeyEncoding: {
        type: 'spki',
        format: 'pem',
      },
      privateKeyEncoding: {
        type: 'pkcs8',
        format: 'pem',
      },
    });

    return { publicKey, privateKey };
  }

  /**
   * Encrypts a message using a public key
   * @param {string} message - The message to encrypt
   * @param {string} publicKey - The public key to use for encryption
   * @returns {string} - The encrypted message
   */
  encryptMessage(message, publicKey) {
    // Create a new RSA cipher
    const cipher = crypto.publicEncrypt({
      key: publicKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    }, Buffer.from(message));

    // Return the encrypted message as a base64-encoded string
    return cipher.toString('base64');
  }

  /**
   * Decrypts an encrypted message using a private key
   * @param {string} encryptedMessage - The encrypted message
   * @param {string} privateKey - The private key to use for decryption
   * @returns {string} - The decrypted message
   */
  decryptMessage(encryptedMessage, privateKey) {
    // Create a new RSA decipher
    const decipher = crypto.privateDecrypt({
      key: privateKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    }, Buffer.from(encryptedMessage, 'base64'));

    // Return the decrypted message
    return decipher.toString();
  }
}

// Main function
async function main() {
  const seedPhraseManager = new SeedPhraseManager();
  const endToEndEncryption = new EndToEndEncryption();

  // Generate a new seed phrase
  const seedPhrase = seedPhraseManager.generateSeedPhrase();
  console.log('Seed Phrase:', seedPhrase);

  // Encrypt the seed phrase using a password
  const password = 'mysecretpassword';
  const encryptedSeedPhrase = seedPhraseManager.encryptSeedPhrase(seedPhrase, password);
  console.log('Encrypted Seed Phrase:', encryptedSeedPhrase);

  // Decrypt the encrypted seed phrase
  const decryptedSeedPhrase = seedPhraseManager.decryptSeedPhrase(encryptedSeedPhrase, password);
  console.log('Decrypted Seed Phrase:', decryptedSeedPhrase);

  // Generate a new key pair
  const keyPair = endToEndEncryption.generateKeyPair();
  console.log('Public Key:', keyPair.publicKey);
  console.log('Private Key:', keyPair.privateKey);

  // Encrypt a message using the public key
  const message = 'Hello, World!';
  const encryptedMessage = endToEndEncryption.encryptMessage(message, keyPair.publicKey);
  console.log('Encrypted Message:', encryptedMessage);

  // Decrypt the encrypted message
  const decryptedMessage = endToEndEncryption.decryptMessage(encryptedMessage, keyPair.privateKey);
  console.log('Decrypted Message:', decryptedMessage);
}

// Run the main function
main();
```
