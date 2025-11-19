"""
Generated Code Metadata:
========================
Original URL: https://zerionwalletextension.blogspot.com
Prompt: Write a tutorial to use the Zerion Wallet Extension for securely signing smart contract transactions in a browser environment.
Generated: DETERMINISTIC_6d691309247d3164
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';
import { ZerionWallet } from '@zerion/wallet-extension-sdk';

// Set up the provider and wallet connection
const provider = new ethers.providers.Web3Provider(window.ethereum);
const zerionWallet = new ZerionWallet(provider);

// Tutorial function to sign a transaction
async function signTransaction() {
  try {
    // Get the user's Ethereum account
    const accounts = await provider.listAccounts();
    const account = accounts[0];

    // Define the contract ABI and address
    const contractAbi = [
      {
        inputs: [],
        name: 'get',
        outputs: [{ internalType: 'uint256', name: '', type: 'uint256' }],
        stateMutability: 'view',
        type: 'function',
      },
      {
        inputs: [{ internalType: 'uint256', name: '_value', type: 'uint256' }],
        name: 'set',
        outputs: [],
        stateMutability: 'nonpayable',
        type: 'function',
      },
    ];
    const contractAddress = '0x...'; // Replace with your contract address

    // Create a contract instance
    const contract = new ethers.Contract(contractAddress, contractAbi, provider);

    // Prepare the transaction
    const tx = await contract.populateTransaction.set(10);

    // Request the user to sign the transaction using Zerion Wallet
    const signedTx = await zerionWallet.signTransaction(tx);

    // Send the signed transaction
    const txReceipt = await provider.sendTransaction(signedTx);

    // Wait for the transaction to be mined
    await txReceipt.wait();

    console.log(`Transaction mined: ${txReceipt.hash}`);
  } catch (error) {
    console.error('Error signing transaction:', error);
  }
}

// Call the tutorial function
signTransaction();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zerion Wallet Extension Tutorial</title>
  <script type="module" src="index.js"></script>
</head>
<body>
  <h1>Zerion Wallet Extension Tutorial</h1>
  <button id="sign-transaction-btn">Sign Transaction</button>
  <script>
    document.getElementById('sign-transaction-btn').addEventListener('click', async () => {
      await signTransaction();
    });
  </script>
</body>
</html>
```
