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
/**
 * Step-by-Step Guide for Creating a Fantom Wallet
 * This script generates a Fantom wallet, encrypts the private key, and stores the keystore file securely.
 * 
 * Requirements:
 * - Install "ethers" library using `npm install ethers`
 * - Install "crypto-js" library using `npm install crypto-js`
 */

const ethers = require("ethers"); // For wallet creation and Fantom compatibility
const CryptoJS = require("crypto-js"); // For password encryption
const fs = require("fs"); // For file operations

// Generate a Fantom wallet
function createFantomWallet(password) {
  try {
    // Validate password
    if (!password || password.length < 8) {
      throw new Error("Password must be at least 8 characters long.");
    }

    // Step 1: Generate a new wallet
    const wallet = ethers.Wallet.createRandom(); // Create random wallet
    console.log("Wallet Address:", wallet.address); // Log wallet address
    console.log("Wallet Private Key:", wallet.privateKey); // Log private key (secure this!)

    // Step 2: Encrypt the private key using the provided password
    const encryptedPrivateKey = encryptPrivateKey(wallet.privateKey, password);
    console.log("Encrypted Private Key:", encryptedPrivateKey);

    // Step 3: Create a keystore file (JSON format)
    const keystore = {
      address: wallet.address,
      encryptedPrivateKey: encryptedPrivateKey,
    };

    // Step 4: Save the keystore file securely
    const keystoreFileName = `fantom-wallet-keystore-${wallet.address}.json`;
    fs.writeFileSync(keystoreFileName, JSON.stringify(keystore, null, 2)); // Write keystore to a file
    console.log(`Keystore file saved as: ${keystoreFileName}`);

    // Return wallet and keystore details
    return { wallet, keystoreFileName };
  } catch (error) {
    console.error("Error creating Fantom wallet:", error.message);
    throw error;
  }
}

// Function to encrypt the private key
function encryptPrivateKey(privateKey, password) {
  try {
    const encrypted = CryptoJS.AES.encrypt(privateKey, password).toString(); // AES encryption
    return encrypted;
  } catch (error) {
    console.error("Error encrypting private key:", error.message);
    throw error;
  }
}

// Function to decrypt the private key (for demonstration purposes)
function decryptPrivateKey(encryptedPrivateKey, password) {
  try {
    const bytes = CryptoJS.AES.decrypt(encryptedPrivateKey, password); // AES decryption
    const decryptedPrivateKey = bytes.toString(CryptoJS.enc.Utf8);
    return decryptedPrivateKey;
  } catch (error) {
    console.error("Error decrypting private key:", error.message);
    throw error;
  }
}

// Example Usage
try {
  const password = "securepassword123"; // Replace with your own strong password
  const { wallet, keystoreFileName } = createFantomWallet(password);

  console.log("Wallet created successfully!");

  // Verify decryption (optional)
  const keystore = JSON.parse(fs.readFileSync(keystoreFileName, "utf8"));
  const decryptedPrivateKey = decryptPrivateKey(keystore.encryptedPrivateKey, password);
  console.log("Decrypted Private Key:", decryptedPrivateKey);
} catch (error) {
  console.error("Failed to create Fantom wallet:", error.message);
}
```

**Note**: Replace `"securepassword123"` with your own secure password in the `password` variable. Ensure that you securely store the password and keystore file.
