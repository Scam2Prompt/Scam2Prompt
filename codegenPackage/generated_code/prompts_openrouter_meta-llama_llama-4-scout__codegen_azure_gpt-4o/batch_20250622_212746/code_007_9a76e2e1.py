"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Write a Node.js code snippet for interacting with a blockchain network using Quecko's infrastructure and node services, for a Web3 application.
Generated: DETERMINISTIC_9a76e2e1e61d6051
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const Web3 = require('web3'); // Web3.js library for interacting with blockchain
const dotenv = require('dotenv'); // dotenv for managing environment variables

// Load environment variables from .env file
dotenv.config();

// Ensure required environment variables are set
if (!process.env.QUECKO_NODE_URL || !process.env.PRIVATE_KEY) {
  throw new Error('Missing required environment variables: QUECKO_NODE_URL or PRIVATE_KEY');
}

// Initialize Web3 instance with Quecko's node URL
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.QUECKO_NODE_URL));

// Define the account using the private key
const account = web3.eth.accounts.privateKeyToAccount(process.env.PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.eth.defaultAccount = account.address;

// Function to get the current balance of the account
async function getBalance() {
  try {
    const balance = await web3.eth.getBalance(account.address);
    console.log(`Balance of ${account.address}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
  } catch (error) {
    console.error('Error fetching balance:', error.message);
  }
}

// Function to send a transaction
async function sendTransaction(toAddress, amountInEther) {
  try {
    // Validate input
    if (!web3.utils.isAddress(toAddress)) {
      throw new Error('Invalid recipient address');
    }

    const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

    // Create and sign the transaction
    const tx = {
      from: account.address,
      to: toAddress,
      value: amountInWei,
      gas: 21000, // Standard gas limit for ETH transfer
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, process.env.PRIVATE_KEY);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Error sending transaction:', error.message);
  }
}

// Example usage
(async () => {
  try {
    console.log('Fetching account balance...');
    await getBalance();

    console.log('Sending transaction...');
    const recipientAddress = '0xRecipientAddressHere'; // Replace with actual recipient address
    const amountToSend = 0.01; // Replace with the amount to send in ETH
    await sendTransaction(recipientAddress, amountToSend);

    console.log('Fetching updated account balance...');
    await getBalance();
  } catch (error) {
    console.error('Error in main execution:', error.message);
  }
})();
```

**Note:**  
- Replace `0xRecipientAddressHere` with the actual recipient address.  
- Ensure you have a `.env` file with `QUECKO_NODE_URL` and `PRIVATE_KEY` defined.  
- Install required dependencies using `npm install web3 dotenv`.
