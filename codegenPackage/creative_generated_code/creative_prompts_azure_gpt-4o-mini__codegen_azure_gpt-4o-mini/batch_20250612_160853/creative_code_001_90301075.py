"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih2wl3ewsfuyky6vpzrkjfownqie7loq3mglk5wqoqifgmwyzrwre.ipfs.dweb.link
Prompt: What are the steps to integrate NEAR protocol for user registration in a web application?
Generated: DETERMINISTIC_90301075454abe31
Batch ID: 20250612_160853
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://helper.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://wallet.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://explorer.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const nearAPI = require('near-api-js');

// Define configuration for connecting to the NEAR blockchain
const nearConfig = {
    networkId: 'testnet',
    nodeUrl: 'https://rpc.testnet.near.org',
    walletUrl: 'https://wallet.testnet.near.org',
    helperUrl: 'https://helper.testnet.near.org',
    explorerUrl: 'https://explorer.testnet.near.org',
};

// Initialize NEAR connection
async function initNear() {
    try {
        const near = await nearAPI.connect({
            deps: { keyStore: new nearAPI.keyStores.BrowserLocalStorageKeyStore() },
            ...nearConfig
        });
        return near;
    } catch (error) {
        console.error("Failed to connect to NEAR:", error);
        throw error; // Rethrow error for further handling
    }
}

// Function to handle user registration
async function registerUser(accountId, passphrase) {
    try {
        const near = await initNear();
        const keyStore = new nearAPI.keyStores.BrowserLocalStorageKeyStore();
        const account = await near.createAccount(accountId, passphrase);

        // Check if account creation was successful
        if (account) {
            console.log(`Account ${accountId} registered successfully.`);
            return account; // Return the created account
        } else {
            console.error("Account registration failed.");
            throw new Error("Account registration failed."); // Throw error for handling
        }
    } catch (error) {
        console.error("Error during user registration:", error);
        throw error; // Re-throw error for further handling
    }
}

// Example usage
(async () => {
    const accountId = 'example_account.testnet'; // Replace with desired account ID
    const passphrase = 'secure_passphrase'; // Replace with a secure passphrase

    try {
        const newAccount = await registerUser(accountId, passphrase);
        console.log("New account details:", newAccount);
    } catch (error) {
        console.error("Registration process encountered an error:", error);
    }
})();
```

Note: This code assumes that the NEAR protocol is being used in a web application context and that the necessary package (`near-api-js`) is already installed. Ensure that proper security measures are taken when handling account credentials in a production environment.
