"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbfour-meme.pages.dev
Prompt: Create a JavaScript function to enable users to purchase $FOUR tokens directly from the Binance Smart Chain, ensuring compatibility with the roadmap details mentioned.
Generated: DETERMINISTIC_52bc6c984b9538ef
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries
const Web3 = require('web3'); // For interacting with the Ethereum blockchain.
const BigNumber = require('bignumber.js'); // For handling large numbers.

const web3 = new Web3(window.ethereum); // Connect to the Ethereum provider (MetaMask, for example).

// Define the $FOUR token contract details
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenAddressHere'; // Replace with the actual $FOUR token contract address.
const TOKEN_DECIMALS = 18; // Assuming the token follows the ERC20 standard.
const PURCHASE_AMOUNT = web3.utils.toWei('1', 'ether'); // Amount to purchase, in this case, 1 ETH worth of tokens.

const tokenAbi = [ // Minimal ABI to interact with the token contract
  {
    "constant": false,
    "inputs": [
      {
        "name": "recipient",
        "type": "address"
      },
      {
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function"
  }
];

/**
 * Function to purchase $FOUR tokens.
 * @param {string} recipientAddress - The address where the tokens will be sent.
 */
async function purchaseFourTokens(recipientAddress) {
  try {
    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Create a contract instance
    const tokenContract = new web3.eth.Contract(tokenAbi, TOKEN_CONTRACT_ADDRESS);

    // Get the accounts
    const accounts = await web3.eth.getAccounts();
    const senderAddress = accounts[0];

    // Check if the recipient address is valid
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error('Invalid recipient address');
    }

    // Calculate amount of tokens to buy using current price (dummy example here)
    const tokenAmount = new BigNumber(PURCHASE_AMOUNT).dividedBy(new BigNumber(1).shiftedBy(TOKEN_DECIMALS)); // Replace with actual price logic

    // Make the purchase transaction
    const tx = await tokenContract.methods.transfer(recipientAddress, tokenAmount.toFixed()).send({
      from: senderAddress,
      value: PURCHASE_AMOUNT, // ETH amount sent to purchase the tokens
    });

    console.log('Transaction successful:', tx);
  } catch (error) {
    console.error('Error purchasing tokens:', error.message);
  }
}

// Example usage: Make sure to call this function with a valid recipient address
// purchaseFourTokens('0xRecipientAddressHere');
```
