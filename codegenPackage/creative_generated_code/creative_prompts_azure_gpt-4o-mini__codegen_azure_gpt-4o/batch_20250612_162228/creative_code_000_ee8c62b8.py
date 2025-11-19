"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dog-68c.pages.dev
Prompt: Generate a code snippet to interact with the DOG token presale smart contract using Web3.js.
Generated: DETERMINISTIC_ee8c62b83827e9e0
Batch ID: 20250612_162228
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
// Import Web3.js and required libraries
const Web3 = require('web3');

// Define the provider (e.g., Infura, Alchemy, or local node)
const providerURL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your provider URL
const web3 = new Web3(new Web3.providers.HttpProvider(providerURL));

// Define the smart contract ABI and address
const contractABI = [
  // Replace with the actual ABI of the DOG token presale smart contract
  {
    "constant": true,
    "inputs": [],
    "name": "getPresaleRate",
    "outputs": [{ "name": "", "type": "uint256" }],
    "payable": false,
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "amount", "type": "uint256" }],
    "name": "buyTokens",
    "outputs": [],
    "payable": true,
    "type": "function"
  }
];
const contractAddress = '0xYourContractAddressHere'; // Replace with the actual contract address

// Instantiate the contract
const presaleContract = new web3.eth.Contract(contractABI, contractAddress);

// Define the wallet and private key (DO NOT expose your private key publicly)
const walletAddress = '0xYourWalletAddressHere'; // Replace with your wallet address
const privateKey = 'YourPrivateKeyHere'; // Replace with your private key securely

// Function to get the presale rate
async function getPresaleRate() {
  try {
    const rate = await presaleContract.methods.getPresaleRate().call();
    console.log(`Current presale rate: ${rate}`);
    return rate;
  } catch (error) {
    console.error('Error fetching presale rate:', error);
    throw error;
  }
}

// Function to buy tokens
async function buyTokens(amountInETH) {
  try {
    const value = web3.utils.toWei(amountInETH.toString(), 'ether'); // Convert ETH to Wei
    const txData = presaleContract.methods.buyTokens(amountInETH).encodeABI();

    // Prepare transaction object
    const tx = {
      from: walletAddress,
      to: contractAddress,
      value: value,
      gas: 200000, // Estimate appropriate gas limit
      data: txData,
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

    // Send the signed transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction successful!', receipt);
  } catch (error) {
    console.error('Error purchasing tokens:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Fetch and log the presale rate
    await getPresaleRate();

    // Buy tokens (example: 0.1 ETH)
    await buyTokens(0.1);
  } catch (error) {
    console.error('An error occurred:', error);
  }
})();
```
