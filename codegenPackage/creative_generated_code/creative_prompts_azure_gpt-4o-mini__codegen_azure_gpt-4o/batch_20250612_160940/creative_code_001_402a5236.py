"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a script using Web3.js to facilitate the purchase of ALIEN tokens during the presale, ensuring the transaction caps at 0.1 ETH increments.
Generated: DETERMINISTIC_402a5236a6a445bc
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
require('dotenv').config(); // Load environment variables from a .env file

// Load configurations from environment variables
const INFURA_URL = process.env.INFURA_URL; // Infura node URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key
const PRESALE_CONTRACT_ADDRESS = process.env.PRESALE_CONTRACT_ADDRESS; // Presale contract address
const TOKEN_ABI = require('./AlienTokenAbi.json'); // ABI of the ALIEN token presale contract

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Function to purchase ALIEN tokens
async function purchaseAlienTokens(ethAmount) {
  try {
    // Ensure the ETH amount does not exceed the cap (0.1 ETH increments only)
    if (ethAmount <= 0 || ethAmount > 0.1 || ethAmount % 0.1 !== 0) {
      console.error('ETH amount must be in increments of 0.1 and not exceed 0.1 ETH.');
      return;
    }

    // Get wallet account address from private key
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    web3.eth.accounts.wallet.add(account);

    // Instantiate the presale contract
    const presaleContract = new web3.eth.Contract(TOKEN_ABI, PRESALE_CONTRACT_ADDRESS);

    // Get current gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Create the transaction object
    const tx = {
      from: account.address, // Sender address
      to: PRESALE_CONTRACT_ADDRESS, // Presale contract address
      value: web3.utils.toWei(ethAmount.toString(), 'ether'), // Convert ETH amount to Wei
      gas: 200000, // Gas limit
      gasPrice: gasPrice, // Current gas price
      data: presaleContract.methods.buyTokens().encodeABI(), // Encoded ABI for the buyTokens function
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    // Log the receipt for confirmation
    console.log('Transaction successful:', receipt);

  } catch (error) {
    // Handle errors
    console.error('An error occurred during the transaction:', error.message);
  }
}

// Example usage
(async () => {
  const ethAmountToSpend = 0.1; // Specify the ETH amount to spend
  await purchaseAlienTokens(ethAmountToSpend); // Purchase ALIEN tokens
})();
```

**Notes:**
1. Create a `.env` file to securely store your `INFURA_URL`, `PRIVATE_KEY`, and `PRESALE_CONTRACT_ADDRESS`.
2. Save the `AlienTokenAbi.json` file containing the contract's ABI in the same directory as the script.
3. Ensure you have installed the `web3` and `dotenv` packages, using `npm install web3 dotenv`.
