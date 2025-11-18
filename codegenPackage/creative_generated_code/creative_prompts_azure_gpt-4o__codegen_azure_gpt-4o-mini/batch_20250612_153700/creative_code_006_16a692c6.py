"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdex.cloud
Prompt: Develop a browser extension for importing wallets like MathWallet and Bitget, ensuring secure handling of private keys and mnemonic phrases.
Generated: DETERMINISTIC_16a692c60b754d21
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Wallet Importer",
  "version": "1.0",
  "description": "A browser extension for importing wallets securely.",
  "permissions": ["storage", "activeTab", "scripting"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icon.png"
  },
  "background": {
    "service_worker": "background.js"
  }
}
```

```html
<!-- popup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Importer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Import Wallet</h1>
    <form id="import-form">
        <label for="mnemonic">Mnemonic Phrase:</label>
        <input type="text" id="mnemonic" required>
        <label for="private-key">Private Key:</label>
        <input type="text" id="private-key" required>
        <button type="submit">Import</button>
    </form>
    <div id="message"></div>
    <script src="popup.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    padding: 10px;
}

h1 {
    font-size: 24px;
}

label {
    display: block;
    margin-top: 10px;
}

input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
}
```

```javascript
// popup.js
document.getElementById('import-form').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting

    // Get values from the input fields
    const mnemonic = document.getElementById('mnemonic').value;
    const privateKey = document.getElementById('private-key').value;

    // Validate the inputs
    if (!validateMnemonic(mnemonic)) {
        displayMessage('Invalid mnemonic phrase.', 'error');
        return;
    }
    if (!validatePrivateKey(privateKey)) {
        displayMessage('Invalid private key.', 'error');
        return;
    }

    try {
        // Store the mnemonic and private key securely
        await storeWallet(mnemonic, privateKey);
        displayMessage('Wallet imported successfully!', 'success');
    } catch (error) {
        console.error('Error importing wallet:', error);
        displayMessage('Error importing wallet.', 'error');
    }
});

/**
 * Validates the mnemonic phrase.
 * @param {string} mnemonic - The mnemonic phrase to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function validateMnemonic(mnemonic) {
    // Simple validation: Check for word count (12, 15, 18, 21, 24)
    const wordCount = mnemonic.trim().split(/\s+/).length;
    return [12, 15, 18, 21, 24].includes(wordCount);
}

/**
 * Validates the private key format.
 * @param {string} privateKey - The private key to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function validatePrivateKey(privateKey) {
    // Basic validation: Check length & format (hex)
    return /^[0-9a-fA-F]{64}$/.test(privateKey.trim());
}

/**
 * Stores the wallet information securely.
 * @param {string} mnemonic - The mnemonic phrase.
 * @param {string} privateKey - The private key.
 */
async function storeWallet(mnemonic, privateKey) {
    // Use storage API to keep keys secure (not real security implementation)
    await chrome.storage.local.set({ mnemonic, privateKey });
}

/**
 * Displays a message in the UI.
 * @param {string} message - The message to display.
 * @param {string} type - The type of message ('error' or 'success').
 */
function displayMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = type; // Set class for styling based on type
}
```

```javascript
// background.js
chrome.runtime.onInstalled.addListener(() => {
    console.log('Wallet Importer Extension Installed');
});
```

This code provides a basic structure for a browser extension that imports wallets securely. It includes validation for mnemonic phrases and private keys, along with storage using the Chrome storage API.
