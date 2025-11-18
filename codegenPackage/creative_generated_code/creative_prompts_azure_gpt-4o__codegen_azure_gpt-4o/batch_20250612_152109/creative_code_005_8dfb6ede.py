"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Create a JavaScript function to connect a crypto wallet to the BTCETF presale widget, allowing users to purchase tokens using ETH or BNB.
Generated: DETERMINISTIC_8dfb6ede4a6c37b3
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Connect Wallet and Purchase Tokens Functionality
// This script is designed to connect a user's crypto wallet to the BTCETF presale widget
// It allows the user to purchase tokens using ETH or BNB.

// Ensure you have web3.js or ethers.js installed and properly configured in your application.

/**
 * Connect Wallet and Handle Token Purchase
 * @param {string} tokenType - The type of token used for purchase ('ETH' or 'BNB').
 * @param {number} amount - The amount of tokens to purchase, specified in cryptocurrency.
 * @returns {Promise<void>}
 */
async function connectWalletAndPurchaseToken(tokenType, amount) {
  try {
    // Validate token type
    if (tokenType !== 'ETH' && tokenType !== 'BNB') {
      throw new Error('Invalid token type. Only ETH or BNB are accepted.');
    }

    // Validate amount
    if (isNaN(amount) || amount <= 0) {
      throw new Error('Invalid amount. Please provide a positive number.');
    }

    // Check if the browser has an Ethereum-compatible wallet (e.g., MetaMask)
    if (typeof window.ethereum === 'undefined') {
      alert('No crypto wallet detected. Please install MetaMask or another Ethereum-compatible wallet.');
      return;
    }

    // Request account access from the user's wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0]; // Get the user's wallet address

    // Log the connected wallet address
    console.log(`Connected wallet address: ${userAddress}`);

    // Set up Web3 provider
    const web3 = new Web3(window.ethereum);

    // Define the BTCETF presale contract address and ABI
    const presaleContractAddress = '0xYourPresaleContractAddressHere'; // Replace with the actual contract address
    const presaleContractABI = [
      // Replace with the actual ABI. This is a placeholder example.
      {
        "constant": false,
        "inputs": [
          { "name": "amount", "type": "uint256" }
        ],
        "name": "purchaseTokens",
        "outputs": [],
        "type": "function"
      }
    ];

    // Instantiate the presale contract
    const presaleContract = new web3.eth.Contract(presaleContractABI, presaleContractAddress);

    // Calculate the amount in Wei (smallest denomination) for the transaction
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Determine the payment method (ETH or BNB) and execute the transaction
    const transactionParams = {
      from: userAddress,
      value: amountInWei // Send ETH/BNB as the value
    };

    console.log(`Initiating token purchase with ${tokenType}...`);
    await presaleContract.methods.purchaseTokens(amountInWei).send(transactionParams);

    // Confirm the transaction
    alert(`Token purchase successful! You have purchased ${amount} BTCETF tokens using ${tokenType}.`);

  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred:', error);
    alert(`Error: ${error.message}`);
  }
}

// Example usage:
// connectWalletAndPurchaseToken('ETH', 0.1);
```
