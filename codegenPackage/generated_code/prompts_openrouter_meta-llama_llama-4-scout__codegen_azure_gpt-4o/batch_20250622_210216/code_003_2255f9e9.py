"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Generate a code example for a decentralized application (dApp) that utilizes the Data Ownership Protocol (DOP) for private transactions and selective disclosure of token holdings.
Generated: DETERMINISTIC_2255f9e9bc462764
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and dependencies
const Web3 = require('web3'); // Web3.js for Ethereum interaction
const DOP = require('data-ownership-protocol'); // Hypothetical DOP library
const dotenv = require('dotenv'); // For environment variable management

// Load environment variables from .env file
dotenv.config();

// Initialize Web3 instance
const web3 = new Web3(process.env.INFURA_URL); // Replace with your Ethereum node provider URL

// Load user's private key and wallet address from environment variables
const privateKey = process.env.PRIVATE_KEY; // User's private key
const walletAddress = process.env.WALLET_ADDRESS; // User's wallet address

// Initialize DOP instance
const dop = new DOP({
  network: 'mainnet', // Specify the network (e.g., mainnet, testnet)
  web3Provider: web3.currentProvider, // Use Web3 provider for DOP
});

// Function to send a private transaction using DOP
async function sendPrivateTransaction(receiverAddress, amount) {
  try {
    // Validate input parameters
    if (!web3.utils.isAddress(receiverAddress)) {
      throw new Error('Invalid receiver address');
    }
    if (amount <= 0) {
      throw new Error('Amount must be greater than zero');
    }

    // Create a private transaction using DOP
    const privateTx = await dop.createPrivateTransaction({
      sender: walletAddress,
      receiver: receiverAddress,
      amount: web3.utils.toWei(amount.toString(), 'ether'), // Convert amount to Wei
    });

    // Sign the transaction with the user's private key
    const signedTx = await web3.eth.accounts.signTransaction(privateTx, privateKey);

    // Send the signed transaction to the blockchain
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Transaction successful:', receipt);
  } catch (error) {
    console.error('Error sending private transaction:', error.message);
  }
}

// Function to selectively disclose token holdings using DOP
async function discloseTokenHoldings(tokenAddress, recipientAddress) {
  try {
    // Validate input parameters
    if (!web3.utils.isAddress(tokenAddress)) {
      throw new Error('Invalid token address');
    }
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }

    // Fetch token holdings using DOP
    const tokenHoldings = await dop.getTokenHoldings({
      walletAddress: walletAddress,
      tokenAddress: tokenAddress,
    });

    // Create a disclosure package
    const disclosurePackage = await dop.createDisclosurePackage({
      data: tokenHoldings,
      recipient: recipientAddress,
    });

    console.log('Disclosure package created:', disclosurePackage);
  } catch (error) {
    console.error('Error disclosing token holdings:', error.message);
  }
}

// Example usage
(async () => {
  // Send a private transaction
  await sendPrivateTransaction('0xReceiverAddressHere', 0.1); // Replace with actual receiver address and amount

  // Disclose token holdings
  await discloseTokenHoldings('0xTokenAddressHere', '0xRecipientAddressHere'); // Replace with actual token and recipient addresses
})();
```

**Note:** This code assumes the existence of a hypothetical `data-ownership-protocol` (DOP) library. Replace placeholders (e.g., `INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`, etc.) with actual values. Ensure the DOP library is properly installed and configured for your environment.
