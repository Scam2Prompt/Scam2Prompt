"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Write a script using Web3.js to interact with a smart contract that facilitates USDC transfers on the Ethereum blockchain.
Generated: DETERMINISTIC_c051921114c792b5
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const Web3 = require('web3');
require('dotenv').config(); // Load environment variables from a .env file

// Initialize Web3 instance and connect to the Ethereum network
const web3 = new Web3(process.env.INFURA_URL); // Replace INFURA_URL in your .env file with the Infura endpoint

// Load sender's private key from environment variables
const senderPrivateKey = process.env.SENDER_PRIVATE_KEY; // NEVER hardcode private keys in your code
if (!senderPrivateKey) {
  throw new Error("Sender private key is missing in the .env file.");
}

// Define the USDC contract address (mainnet example, replace with testnet address if needed)
const usdcContractAddress = '0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606EB48'; // Replace with the USDC contract address for your chosen network

// Define the ABI of the USDC contract (ERC20 standard ABI subset)
const usdcAbi = [
  {
    "constant": true,
    "inputs": [],
    "name": "name",
    "outputs": [{ "name": "", "type": "string" }],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "symbol",
    "outputs": [{ "name": "", "type": "string" }],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "decimals",
    "outputs": [{ "name": "", "type": "uint8" }],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      { "name": "_to", "type": "address" },
      { "name": "_value", "type": "uint256" }
    ],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function"
  }
];

// Create a contract instance for USDC
const usdcContract = new web3.eth.Contract(usdcAbi, usdcContractAddress);

// Function to transfer USDC
async function transferUSDC(senderAddress, recipientAddress, amount) {
  try {
    // Validate inputs
    if (!web3.utils.isAddress(senderAddress)) {
      throw new Error("Invalid sender address.");
    }
    if (!web3.utils.isAddress(recipientAddress)) {
      throw new Error("Invalid recipient address.");
    }

    // Fetch decimals from the contract to adjust the amount
    const decimals = await usdcContract.methods.decimals().call();
    const adjustedAmount = web3.utils.toBN(amount).mul(web3.utils.toBN(10).pow(web3.utils.toBN(decimals)));

    // Prepare the transaction
    const nonce = await web3.eth.getTransactionCount(senderAddress, 'pending');
    const data = usdcContract.methods.transfer(recipientAddress, adjustedAmount).encodeABI();
    const tx = {
      from: senderAddress,
      to: usdcContractAddress,
      gas: 100000, // Estimate gas limit suitable for transfer
      nonce: nonce,
      data: data
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, senderPrivateKey);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log("Transaction successful:", receipt);
  } catch (error) {
    console.error("Error during USDC transfer:", error.message);
  }
}

// Example usage
(async () => {
  const senderAddress = process.env.SENDER_ADDRESS; // Replace with your sender address
  const recipientAddress = '0xRecipientAddressHere'; // Replace with the actual recipient address
  const amount = 100; // Amount of USDC to transfer (adjust to your needs)

  if (!senderAddress) {
    throw new Error("Sender address is missing in the .env file.");
  }

  await transferUSDC(senderAddress, recipientAddress, amount);
})();
```

**Note:** Before running this script, make sure to install the necessary dependencies (`npm install web3 dotenv`) and configure your `.env` file with `INFURA_URL`, `SENDER_PRIVATE_KEY`, and `SENDER_ADDRESS`. Also, ensure proper security practices when handling private keys and environment variables.
