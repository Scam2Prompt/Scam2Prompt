"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Write a guide on integrating $HEHE token transactions into a decentralized application (dApp) using Web3.js.
Generated: DETERMINISTIC_5a490386e4ad1888
Batch ID: 20250612_153420
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
// Import necessary modules
const Web3 = require('web3');

// Define constants for the dApp
const INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const TOKEN_CONTRACT_ADDRESS = '0xYourHEHETokenAddress'; // Replace with the $HEHE token contract address
const ABI = [/* Token Contract ABI */]; // Replace with the actual ABI of the $HEHE token contract
const PRIVATE_KEY = 'YourPrivateKey'; // Replace with the private key of the wallet sending transactions (Keep secure!)
const RECEIVER_ADDRESS = '0xReceiverWalletAddress'; // Replace with the recipient's wallet address

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Function to get balance of $HEHE token for a given address
const getTokenBalance = async (walletAddress) => {
  try {
    // Create contract instance
    const tokenContract = new web3.eth.Contract(ABI, TOKEN_CONTRACT_ADDRESS);

    // Call the balanceOf() function in the ERC20 contract
    const balance = await tokenContract.methods.balanceOf(walletAddress).call();

    // Convert balance from Wei to a human-readable format
    return web3.utils.fromWei(balance, 'ether');
  } catch (error) {
    console.error('Error fetching token balance:', error.message);
    throw error;
  }
};

// Function to transfer $HEHE tokens to another wallet
const transferTokens = async (toAddress, amount) => {
  try {
    // Create contract instance
    const tokenContract = new web3.eth.Contract(ABI, TOKEN_CONTRACT_ADDRESS);

    // Get the wallet address from the private key
    const senderAddress = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY).address;

    // Convert amount to Wei
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Encode the transfer method call
    const data = tokenContract.methods.transfer(toAddress, amountInWei).encodeABI();

    // Get the current gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Estimate the gas required for the transaction
    const gasLimit = await tokenContract.methods
      .transfer(toAddress, amountInWei)
      .estimateGas({ from: senderAddress });

    // Create a raw transaction object
    const tx = {
      to: TOKEN_CONTRACT_ADDRESS,
      data,
      gasPrice,
      gas: gasLimit,
      nonce: await web3.eth.getTransactionCount(senderAddress),
    };

    // Sign the transaction with the private key
    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    console.log('Transaction successful! Receipt:', receipt);
    return receipt;
  } catch (error) {
    console.error('Error transferring tokens:', error.message);
    throw error;
  }
};

// Example usage
(async () => {
  try {
    const walletAddress = '0xYourWalletAddress'; // Replace with the wallet to check
    const balance = await getTokenBalance(walletAddress);
    console.log(`Balance of $HEHE tokens: ${balance}`);

    const transferAmount = 10; // Replace with the number of tokens to transfer
    const receipt = await transferTokens(RECEIVER_ADDRESS, transferAmount);
    console.log('Transfer complete. Transaction receipt:', receipt);
  } catch (error) {
    console.error('Error in dApp:', error.message);
  }
})();
```

**Notes**:
1. Replace `YOUR_INFURA_PROJECT_ID`, `0xYourHEHETokenAddress`, `YourPrivateKey`, `0xReceiverWalletAddress`, and the ABI array with actual values specific to your project.
2. Keep your private key secure and never expose it in public repositories.
3. Install the required dependencies using `npm install web3`.
4. Make sure your application handles errors gracefully.
