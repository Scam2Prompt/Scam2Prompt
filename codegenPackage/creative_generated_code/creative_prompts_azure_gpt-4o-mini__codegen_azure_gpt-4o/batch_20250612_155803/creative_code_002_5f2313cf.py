"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercsz.com
Prompt: Can you provide code snippets for integrating JavaScript with Ethereum smart contracts in a DeFi context?
Generated: DETERMINISTIC_5f2313cfea5ff09d
Batch ID: 20250612_155803
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
// Import required libraries
const Web3 = require('web3');

// Connect to Ethereum blockchain via an Infura node (or any other provider)
const INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// ABI (Application Binary Interface) for the smart contract
// Replace this with the ABI of your Ethereum smart contract
const contractABI = [
  // Example ABI
  {
    "constant": true,
    "inputs": [{ "name": "_address", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "balance", "type": "uint256" }],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address (replace with the actual deployed contract address)
const contractAddress = '0xYourSmartContractAddressHere';

// Initialize contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to fetch token balance of a user
async function getBalance(userAddress) {
  try {
    // Validate Ethereum address
    if (!web3.utils.isAddress(userAddress)) {
      throw new Error('Invalid Ethereum address');
    }

    // Call the smart contract function `balanceOf` to fetch the balance
    const balance = await contract.methods.balanceOf(userAddress).call();

    // Convert balance to human-readable format (optional, if token has decimals)
    // Replace "18" with the token's decimal places if applicable
    const readableBalance = web3.utils.fromWei(balance, 'ether');

    return readableBalance; // Returns balance as a string
  } catch (error) {
    console.error('Error fetching balance:', error.message);
    throw error; // Re-throw error for further handling
  }
}

// Example usage of the above function
(async () => {
  const userAddress = '0xYourEthereumAddressHere'; // Replace with an actual user address
  try {
    const balance = await getBalance(userAddress);
    console.log(`Balance of ${userAddress}: ${balance} tokens`);
  } catch (error) {
    console.error('Failed to retrieve token balance:', error.message);
  }
})();

// Function to send tokens to another address
async function transferTokens(fromAddress, privateKey, toAddress, amount) {
  try {
    // Validate Ethereum addresses
    if (!web3.utils.isAddress(fromAddress) || !web3.utils.isAddress(toAddress)) {
      throw new Error('Invalid Ethereum address');
    }

    // Convert amount to Wei (assuming tokens have 18 decimals)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Build transaction object
    const tx = {
      from: fromAddress,
      to: contractAddress,
      gas: 200000, // Estimate gas limit (may need to adjust based on the contract)
      data: contract.methods.transfer(toAddress, amountInWei).encodeABI() // Encoded data for transfer function
    };

    // Sign transaction with the sender's private key
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

    // Send transaction to the blockchain
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Transaction successful:', receipt.transactionHash);
  } catch (error) {
    console.error('Error during token transfer:', error.message);
    throw error; // Re-throw error for further handling
  }
}

// Example usage of token transfer
(async () => {
  const senderAddress = '0xYourSenderAddressHere'; // Replace with sender's address
  const senderPrivateKey = 'YourPrivateKeyHere'; // Replace with sender's private key
  const recipientAddress = '0xRecipientAddressHere'; // Replace with recipient's address
  const transferAmount = '10'; // Amount to transfer (e.g., 10 tokens)

  try {
    await transferTokens(senderAddress, senderPrivateKey, recipientAddress, transferAmount);
  } catch (error) {
    console.error('Failed to transfer tokens:', error.message);
  }
})();
```
