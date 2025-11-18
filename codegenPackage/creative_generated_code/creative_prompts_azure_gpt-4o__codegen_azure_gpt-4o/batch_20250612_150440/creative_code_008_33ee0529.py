"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: Provide sample code for connecting a Polkadot wallet to a dApp using the Metamask Snap Polkadot example.
Generated: DETERMINISTIC_33ee05295b2e1632
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { web3Enable, web3Accounts } from '@polkadot/extension-dapp';

// Function to connect a Polkadot wallet to the dApp
async function connectPolkadotWallet() {
  try {
    // Request wallet extensions from the user
    const extensions = await web3Enable('Your DApp Name');

    // Check if the user has Polkadot wallet extensions installed
    if (extensions.length === 0) {
      throw new Error('No Polkadot wallet extensions found. Please install a wallet like Polkadot.js.');
    }

    // Request accounts from the wallet
    const accounts = await web3Accounts();

    // Ensure at least one account is available
    if (accounts.length === 0) {
      throw new Error('No accounts found in the connected Polkadot wallet.');
    }

    // Return the list of accounts
    return accounts;
  } catch (error) {
    // Log and handle errors gracefully
    console.error('Error connecting to Polkadot wallet:', error.message);
    alert(`An error occurred: ${error.message}`);
    return null;
  }
}

// Example usage of `connectPolkadotWallet` function
(async () => {
  const accounts = await connectPolkadotWallet();

  if (accounts) {
    console.log('Connected accounts:', accounts);

    // Select the first account for demonstration purposes
    const selectedAccount = accounts[0];

    console.log('Selected account:', selectedAccount);
    alert(`Connected to account: ${selectedAccount.address}`);
  }
})();
```
