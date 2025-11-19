"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: Write a code snippet to create walletless dapps using the MetaMask Delegation Toolkit.
Generated: DETERMINISTIC_f3b2ac3dc4de4af0
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Walletless DApp using MetaMask Delegation Toolkit
 * This code snippet demonstrates how to use MetaMask Delegation Toolkit
 * for creating a walletless decentralized application.
 * 
 * Requirements:
 * - Include the MetaMask Delegation Toolkit package in your project (`npm install @metamask/delegation`)
 */

import { createPermissionGrant, createAccessController } from '@metamask/delegation';

/**
 * Initializes a walletless DApp with MetaMask Delegation Toolkit.
 */
async function initializeWalletlessDApp() {
  try {
    // 1. Define the permissions to be granted
    const permissions = {
      eth_accounts: {
        type: 'method',
        description: 'Access to user accounts',
      },
      eth_sendTransaction: {
        type: 'method',
        description: 'Send Ethereum transactions',
      },
    };

    // 2. Create a permission grant object
    const permissionGrant = createPermissionGrant(permissions);

    // 3. Create an access controller using the permission grant
    const accessController = createAccessController(permissionGrant);

    // 4. Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed.');
    }

    // 5. Request accounts from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure MetaMask is unlocked.');
    }

    // 6. Delegate permissions for walletless usage
    const delegated = accessController.delegate({
      from: accounts[0], // Delegator's address
      to: '0xRecipientAddress', // Replace with the recipient address or DApp's address
    });

    console.log('Delegation successful:', delegated);

    // 7. Now the DApp has delegated permissions and can interact without requiring a wallet
  } catch (error) {
    console.error('Error initializing walletless DApp:', error.message);
  }
}

// Call the function to initialize the walletless DApp
initializeWalletlessDApp();
```

Note: Replace `'0xRecipientAddress'` with the actual address that will receive the delegation. Ensure MetaMask and its dependencies are installed correctly in your development environment.
