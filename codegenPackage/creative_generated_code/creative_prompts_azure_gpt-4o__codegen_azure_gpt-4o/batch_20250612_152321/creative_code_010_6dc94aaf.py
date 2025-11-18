"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Write a step-by-step guide for connecting a wallet using MetaMask and purchasing $FROP tokens on the presale widget, including blockchain network selection.
Generated: DETERMINISTIC_6dc94aaf2abccf09
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-step guide for connecting a wallet using MetaMask and purchasing $FROP tokens
 * via a presale widget. This code is written in JavaScript using web3.js.
 * Ensure you have web3.js installed (`npm install web3`) and MetaMask browser extension.
 */

// Import Web3
const Web3 = require('web3');

// Define constants for the blockchain network and token contract
const NETWORK_ID = 1; // Ethereum Mainnet (Change to testnet ID if needed, e.g., 5 for Goerli)
const FROP_TOKEN_ADDRESS = '0xYourFropTokenContractAddressHere'; // Replace with actual token contract address
const PRESALE_WIDGET_ADDRESS = '0xYourPresaleWidgetContractAddressHere'; // Replace with presale widget contract address
const FROP_ABI = []; // Replace with the actual ABI of the $FROP token contract
const PRESALE_WIDGET_ABI = []; // Replace with the actual ABI of the presale widget contract

// Initialize web3 instance
let web3;

// Function to connect MetaMask wallet
async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const selectedAccount = accounts[0]; // Use the first account
    console.log('Connected account:', selectedAccount);

    // Initialize web3 with MetaMask provider
    web3 = new Web3(window.ethereum);

    // Verify network
    const networkId = await web3.eth.net.getId();
    if (networkId !== NETWORK_ID) {
      throw new Error(`Please switch MetaMask to the correct network (Network ID: ${NETWORK_ID}).`);
    }

    return selectedAccount;
  } catch (error) {
    console.error('Error connecting wallet:', error.message);
    throw error;
  }
}

// Function to purchase $FROP tokens via presale widget
async function purchaseFropTokens(account, amountInEther) {
  try {
    // Validate input
    if (!web3.utils.isAddress(account)) {
      throw new Error('Invalid wallet address');
    }
    if (isNaN(amountInEther) || amountInEther <= 0) {
      throw new Error('Invalid purchase amount');
    }

    // Get presale widget contract
    const presaleWidgetContract = new web3.eth.Contract(PRESALE_WIDGET_ABI, PRESALE_WIDGET_ADDRESS);

    // Convert Ether amount to Wei
    const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

    // Send transaction to purchase tokens
    const transaction = await presaleWidgetContract.methods.purchaseTokens().send({
      from: account,
      value: amountInWei, // Ether amount to send
    });

    console.log('Transaction successful! Transaction hash:', transaction.transactionHash);
  } catch (error) {
    console.error('Error purchasing tokens:', error.message);
    throw error;
  }
}

/**
 * Main function to execute the wallet connection and token purchase process.
 */
async function main() {
  try {
    // Connect wallet
    const account = await connectWallet();

    // Specify the amount of Ether to contribute for purchasing $FROP tokens
    const amountInEther = 0.1; // Replace with desired amount

    // Purchase $FROP tokens
    await purchaseFropTokens(account, amountInEther);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Execute the main function
main();

```

### Notes:
- Replace `FROP_ABI` and `PRESALE_WIDGET_ABI` with the actual ABI (JSON interface) for the respective contracts.
- Replace the `FROP_TOKEN_ADDRESS` and `PRESALE_WIDGET_ADDRESS` with the respective contract addresses deployed on the blockchain network.
- Ensure you are using the correct network ID (e.g., Ethereum Mainnet: 1, Rinkeby: 4, Goerli: 5).
- Install `web3.js` using `npm install web3` if not already installed.
