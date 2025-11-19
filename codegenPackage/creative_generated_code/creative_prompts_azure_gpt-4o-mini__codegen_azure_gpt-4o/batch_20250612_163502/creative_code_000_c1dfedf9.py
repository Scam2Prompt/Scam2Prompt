"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ui-refactor-wallets-to-not-u.swim-ui.pages.dev
Prompt: How can I create a cryptocurrency wallet app using JavaScript instead of plain HTML?
Generated: DETERMINISTIC_c1dfedf9adb913fb
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (Node.js environment)
const crypto = require('crypto'); // For cryptographic operations
const fs = require('fs'); // File system module for saving wallet data
const path = require('path'); // Path module for file management

// Wallet class to encapsulate wallet functionality
class CryptoWallet {
  constructor() {
    this.wallet = null;
  }

  /**
   * Generates a new wallet with a public and private key pair.
   */
  generateWallet() {
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
      modulusLength: 4096, // Key size for enhanced security
      publicKeyEncoding: { type: 'spki', format: 'pem' },
      privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
    });

    this.wallet = { publicKey, privateKey };
    console.log('Wallet generated successfully!');
  }

  /**
   * Saves the wallet to a file securely.
   * @param {string} filePath - File path to save the wallet credentials.
   */
  saveWallet(filePath = './wallet') {
    if (!this.wallet) {
      throw new Error('Wallet not generated yet. Generate a wallet first.');
    }

    // Ensure the directory exists
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // Write the wallet data to files securely
    fs.writeFileSync(`${filePath}_private.pem`, this.wallet.privateKey, { mode: 0o600 });
    fs.writeFileSync(`${filePath}_public.pem`, this.wallet.publicKey, { mode: 0o600 });
    console.log(`Wallet saved to: ${filePath}`);
  }

  /**
   * Loads a wallet from saved files.
   * @param {string} filePath - File path to load the wallet credentials.
   */
  loadWallet(filePath = './wallet') {
    try {
      const privateKey = fs.readFileSync(`${filePath}_private.pem`, 'utf8');
      const publicKey = fs.readFileSync(`${filePath}_public.pem`, 'utf8');
      this.wallet = { privateKey, publicKey };
      console.log('Wallet loaded successfully!');
    } catch (error) {
      console.error('Error loading wallet:', error.message);
      throw new Error('Failed to load wallet files. Ensure the files exist and are accessible.');
    }
  }

  /**
   * Displays the wallet's public key.
   */
  getPublicKey() {
    if (!this.wallet) {
      throw new Error('Wallet not generated or loaded. Generate or load a wallet first.');
    }
    console.log('Public Key:', this.wallet.publicKey);
    return this.wallet.publicKey;
  }
}

// Example usage
try {
  const walletApp = new CryptoWallet();

  // Generate a new wallet
  walletApp.generateWallet();

  // Save the wallet to files
  walletApp.saveWallet('./my_crypto_wallet');

  // Load the wallet from files
  walletApp.loadWallet('./my_crypto_wallet');

  // Display the public key
  walletApp.getPublicKey();
} catch (error) {
  console.error('An error occurred:', error.message);
}
```

Note:
- This code is intended for execution in a Node.js environment, not directly in a browser.
- It uses the `crypto` module to generate RSA key pairs.
- Wallet files are saved securely with restricted file permissions (`0o600`).
- Always handle private keys securely and avoid exposing them publicly.
