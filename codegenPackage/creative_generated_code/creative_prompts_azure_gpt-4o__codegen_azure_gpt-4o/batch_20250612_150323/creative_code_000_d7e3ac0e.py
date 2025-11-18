"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Write code using the MetaMask SDK to integrate a Web3 wallet into a dapp for Ethereum transactions.
Generated: DETERMINISTIC_d7e3ac0e7fb3d840
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the MetaMask SDK
import { MetaMaskSDK } from '@metamask/sdk';

// Import the ethers library for interacting with Ethereum
import { ethers } from 'ethers';

// Initialize the MetaMask SDK
const options = {
  dappMetadata: {
    name: 'My DApp', // Name of your dApp
  },
};
const MMSDK = new MetaMaskSDK(options);

// Get the Ethereum provider
const ethereum = MMSDK.getProvider();

// Function to connect the user's wallet
async function connectWallet() {
  try {
    // Request wallet connection
    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    
    // Log the connected account(s)
    console.log('Connected account:', accounts[0]);

    return accounts[0]; // Return the connected account
  } catch (error) {
    // Handle errors (e.g., user rejection, no MetaMask installed)
    console.error('Error connecting wallet:', error.message);
    throw new Error('Failed to connect wallet. Please ensure MetaMask is installed.');
  }
}

// Function to send an Ethereum transaction
async function sendTransaction(receiverAddress, amountInEth) {
  try {
    // Ensure the wallet is connected
    const account = await connectWallet();

    // Use ethers.js to create a provider
    const provider = new ethers.providers.Web3Provider(ethereum);

    // Get the signer (account initiating the transaction)
    const signer = provider.getSigner();

    // Parse the amount into Wei (smallest Ethereum denomination)
    const amountInWei = ethers.utils.parseEther(amountInEth);

    // Create the transaction object
    const tx = {
      to: receiverAddress, // Address to send Ether to
      value: amountInWei,  // Amount to send (in Wei)
    };

    // Send the transaction
    const txResponse = await signer.sendTransaction(tx);

    // Wait for the transaction to be mined
    const receipt = await txResponse.wait();

    // Log the transaction receipt
    console.log('Transaction successful:', receipt);

    return receipt; // Return the transaction receipt
  } catch (error) {
    // Handle errors (e.g., insufficient funds, invalid address)
    console.error('Error sending transaction:', error.message);
    throw new Error('Failed to send transaction. Please verify the details and try again.');
  }
}

// Example usage of the functions
(async () => {
  try {
    const connectedAccount = await connectWallet(); // Connect the wallet
    console.log('Wallet connected:', connectedAccount);

    // Replace with the recipient's Ethereum address and amount to send
    const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const amountToSend = '0.01'; // Amount in Ether

    const txReceipt = await sendTransaction(recipientAddress, amountToSend); // Send transaction
    console.log('Transaction receipt:', txReceipt);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

### Notes:
- Replace `'0xRecipientAddressHere'` with the actual Ethereum address of the recipient.
- Ensure `@metamask/sdk` and `ethers` are installed via npm (`npm install @metamask/sdk ethers`) before running the code.
- Make sure MetaMask is installed in the browser where this code is executed.
