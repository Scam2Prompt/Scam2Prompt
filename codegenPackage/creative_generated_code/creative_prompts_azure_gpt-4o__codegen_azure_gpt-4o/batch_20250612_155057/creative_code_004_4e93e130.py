"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeext.bravesites.com
Prompt: Write code to securely import an existing wallet into MetaMask using a recovery phrase. Include steps for ensuring the recovery phrase is handled locally and not transmitted externally.
Generated: DETERMINISTIC_4e93e13078849ba9
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code to securely import an existing wallet into MetaMask using a recovery phrase. Note: MetaMask is a browser extension and wallet software that operates locally within the browser. This code illustrates how to interact with MetaMask's API securely. The recovery phrase should only be handled locally with proper precautions.

```javascript
// Import the ethers.js library for wallet operations
const { Wallet } = require('ethers');

// Function to securely import an existing wallet into MetaMask using a recovery phrase
async function importWalletToMetaMask(recoveryPhrase) {
  try {
    // Validate that the recovery phrase is a non-empty string
    if (typeof recoveryPhrase !== 'string' || recoveryPhrase.trim() === '') {
      throw new Error('Invalid recovery phrase provided.');
    }

    // Locally create a wallet instance using the recovery phrase
    const wallet = Wallet.fromMnemonic(recoveryPhrase);

    // Ensure wallet creation was successful
    if (!wallet || !wallet.address) {
      throw new Error('Failed to create wallet from the recovery phrase.');
    }

    console.log(`Wallet created locally. Address: ${wallet.address}`);

    // Check if MetaMask is available in the browser (window.ethereum)
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed in the browser.');
    }

    // Request MetaMask to connect to the user's wallet
    const accounts = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });

    console.log(`MetaMask connected. Accounts: ${accounts}`);

    // Warning: MetaMask does not allow programmatic importing of private keys/mnemonics.
    // Users must manually import the recovery phrase into MetaMask via the MetaMask UI.
    console.warn(
      'You must manually import your recovery phrase into MetaMask via the MetaMask extension. This cannot be automated for security reasons.'
    );

    // Return the wallet address as confirmation
    return wallet.address;
  } catch (error) {
    // Log and handle errors gracefully
    console.error('Error importing wallet into MetaMask:', error.message);
    throw error;
  }
}

// Usage example
(async () => {
  try {
    // Replace with your actual recovery phrase
    const recoveryPhrase = 'your 12 or 24 word mnemonic phrase goes here';

    const walletAddress = await importWalletToMetaMask(recoveryPhrase);
    console.log(`Wallet successfully imported. Address: ${walletAddress}`);
  } catch (error) {
    console.error('Failed to import wallet:', error.message);
  }
})();
```

### Important Notes:
1. **Security**: Ensure you never share or transmit the recovery phrase outside of your local machine. This code assumes the recovery phrase is securely provided to it.
2. **MetaMask Limitations**: MetaMask does not support programmatically importing wallets for security reasons. Users must manually input their recovery phrase via the MetaMask UI.
3. **Error Handling**: The code includes error handling to cover common issues like invalid recovery phrases or missing MetaMask installations.
4. **Dependencies**: Install ethers.js (`npm install ethers`) before running this code.
