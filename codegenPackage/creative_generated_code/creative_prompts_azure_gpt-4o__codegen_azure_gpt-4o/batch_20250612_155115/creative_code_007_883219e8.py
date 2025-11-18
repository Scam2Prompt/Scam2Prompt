"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Generate a JavaScript function to withdraw all profits from an Ethereum account, using the `withdrawAllEth` button functionality described on the webpage.
Generated: DETERMINISTIC_883219e8bb8566b7
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script provides functionality to withdraw all profits from an Ethereum account
 * by interacting with a smart contract via a web3 instance. It assumes the existence 
 * of a button with the ID `withdrawAllEth` on the webpage.
 */

// Ensure web3 is available (e.g., via MetaMask or another provider)
if (typeof window.ethereum === 'undefined') {
  console.error('Ethereum provider not found. Please install MetaMask or another compatible wallet.');
  alert('Ethereum provider not found. Please install MetaMask or another compatible wallet.');
}

// Import Web3 library if needed (Ensure Web3 is included in your project)
// const Web3 = require('web3');

// Smart contract ABI (replace with your contract's ABI)
const contractABI = [
  // Example ABI entry for withdrawAll function
  {
    "constant": false,
    "inputs": [],
    "name": "withdrawAll",
    "outputs": [],
    "type": "function"
  }
];

// Smart contract address (replace with your contract's address)
const contractAddress = '0xYourSmartContractAddressHere';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Withdraw all profits from the user's Ethereum account.
 * It interacts with the smart contract's `withdrawAll` function.
 */
async function withdrawAllProfits() {
  try {
    // Request accounts from the user's wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Check if accounts are available
    if (!accounts || accounts.length === 0) {
      throw new Error('No Ethereum accounts found. Please connect your wallet.');
    }

    const userAccount = accounts[0];

    // Interact with the smart contract to execute the `withdrawAll` function
    const receipt = await contract.methods.withdrawAll().send({ from: userAccount });

    // Log transaction receipt for debugging purposes
    console.log('Transaction successful:', receipt);

    alert('Withdrawal successful!');
  } catch (error) {
    console.error('Error during withdrawal:', error.message);
    alert(`Withdrawal failed: ${error.message}`);
  }
}

// Attach the withdrawAllProfits function to the button
document.getElementById('withdrawAllEth').addEventListener('click', withdrawAllProfits);
```
