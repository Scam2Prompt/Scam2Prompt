"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://982e0a97.web3-site.pages.dev
Prompt: Generate code to sign and send transactions using Web3.js, incorporating best practices from freeCodeCamp's Web3 content.
Generated: DETERMINISTIC_53bbdb41b28e531b
Batch ID: 20250612_150927
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import the required libraries
const Web3 = require('web3');
const { Transaction } = require('ethereumjs-tx').Transaction; // For creating Ethereum transactions
const Common = require('ethereumjs-common').default; // For Ethereum network configurations
require('dotenv').config(); // For loading environment variables from a .env file

// Initialize Web3 with an Infura or Alchemy provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Account and private key from environment variables
const account = process.env.ACCOUNT_ADDRESS;
const privateKey = Buffer.from(process.env.PRIVATE_KEY, 'hex');

// Function to send a signed transaction
async function sendSignedTransaction(to, value, gasLimit = 21000, gasPrice = '20000000000') {
    try {
        // Get the nonce for the account
        const nonce = await web3.eth.getTransactionCount(account, 'pending');

        // Create the transaction object
        const txParams = {
            nonce: web3.utils.toHex(nonce),
            gasLimit: web3.utils.toHex(gasLimit),
            gasPrice: web3.utils.toHex(gasPrice), // in wei
            to: to,
            value: web3.utils.toHex(web3.utils.toWei(value.toString(), 'ether')), // convert value to wei
            chainId: 1 // Mainnet chain ID
        };

        // Create the transaction using ethereumjs-tx
        const customCommon = Common.forCustomChain(
            'mainnet',
            {
                chainId: 1,
                networkId: 1,
            },
            'petersburg' // Use the appropriate EIP-155 network
        );

        const transaction = new Transaction(txParams, { chain: 'mainnet', hardfork: 'petersburg' });

        // Sign the transaction with the private key
        transaction.sign(privateKey);

        // Serialize the transaction
        const serializedTx = transaction.serialize().toString('hex');

        // Send the signed transaction
        const receipt = await web3.eth.sendSignedTransaction('0x' + serializedTx);

        console.log('Transaction successful with hash:', receipt.transactionHash);
        
        return receipt; // Return the receipt for further processing if needed
    } catch (error) {
        console.error('Error sending transaction:', error.message);
        throw error; // Rethrow the error after logging
    }
}

// Example use case - sending 0.1 ETH to a specified address
const recipientAddress = '0xRecipientAddressHere'; // Replace with the actual recipient address
const amountToSend = 0.1; // Amount in ETH

// Execute the transaction
sendSignedTransaction(recipientAddress, amountToSend)
    .then(receipt => console.log('Transaction Receipt:', receipt))
    .catch(err => console.error('Transaction failed:', err));
```

Make sure to create a `.env` file in the same directory as the script with the following contents:
```
INFURA_URL='https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
ACCOUNT_ADDRESS='YOUR_ACCOUNT_ADDRESS'
PRIVATE_KEY='YOUR_PRIVATE_KEY'
```

**Note:** Always handle your private keys securely and never expose them in your code or public repositories.
