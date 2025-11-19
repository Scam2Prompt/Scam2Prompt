"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-preview.mynearwallet.com
Prompt: How can I implement JavaScript to enable features in MyNearWallet?
Generated: DETERMINISTIC_aa73af3e0d10de23
Batch ID: 20250612_155235
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
  "https://explorer.testnet.near.org": {
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
  "https://rpc.testnet.near.org": {
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
/**
 * JavaScript code for enabling features in MyNearWallet.
 * This example demonstrates connecting to the NEAR blockchain,
 * enabling wallet login, checking wallet balance, and sending NEAR tokens.
 * 
 * Requirements:
 * - Include the NEAR JavaScript SDK in your project.
 * - Replace placeholder values with your actual contract/account details.
 */

// Import required methods from the NEAR JavaScript SDK
const nearAPI = require('near-api-js');

// Configuration for the NEAR network (Testnet in this example)
const config = {
  networkId: 'testnet',
  nodeUrl: 'https://rpc.testnet.near.org',
  walletUrl: 'https://wallet.testnet.near.org',
  helperUrl: 'https://helper.testnet.near.org',
  explorerUrl: 'https://explorer.testnet.near.org',
  keyStore: new nearAPI.keyStores.BrowserLocalStorageKeyStore(),
};

// Initialize connection to the NEAR blockchain
async function initNear() {
  try {
    const near = await nearAPI.connect(config);
    const walletConnection = new nearAPI.WalletConnection(near);
    return { near, walletConnection };
  } catch (error) {
    console.error('Error initializing NEAR:', error);
    throw error; // Re-throw error for external handling if needed
  }
}

// Login to MyNearWallet
async function login(walletConnection) {
  if (!walletConnection.isSignedIn()) {
    walletConnection.requestSignIn(
      'your-contract-name.testnet', // Replace with your NEAR contract name
      'MyNearWallet App', // App name displayed to the user
    );
  } else {
    console.log('Already logged in:', walletConnection.getAccountId());
  }
}

// Logout from MyNearWallet
function logout(walletConnection) {
  walletConnection.signOut();
  console.log('Logged out successfully!');
}

// Get account balance
async function getBalance(walletConnection) {
  try {
    const account = walletConnection.account();
    const balance = await account.getAccountBalance();
    console.log(`Balance for ${account.accountId}:`, balance);
    return balance;
  } catch (error) {
    console.error('Error fetching account balance:', error);
    throw error;
  }
}

// Send NEAR tokens
async function sendTokens(walletConnection, receiverId, amount) {
  try {
    const account = walletConnection.account();
    const result = await account.sendMoney(receiverId, nearAPI.utils.format.parseNearAmount(amount));
    console.log(`Successfully sent ${amount} NEAR to ${receiverId}:`, result);
    return result;
  } catch (error) {
    console.error('Error sending tokens:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const { near, walletConnection } = await initNear();

    // Login process
    await login(walletConnection);

    if (walletConnection.isSignedIn()) {
      console.log('Logged in as:', walletConnection.getAccountId());

      // Fetch balance
      const balance = await getBalance(walletConnection);

      // Send tokens (replace with actual receiver ID and amount)
      await sendTokens(walletConnection, 'receiver-account.testnet', '0.1');
    } else {
      console.log('User is not logged in.');
    }
  } catch (error) {
    console.error('Error during wallet operations:', error);
  }
})();
```

Note: Ensure that the `near-api-js` package is installed in your project to execute this code. Use the command `npm install near-api-js` to install it. Adjust configuration values based on your NEAR account and environment (e.g. Testnet/Mainnet).
