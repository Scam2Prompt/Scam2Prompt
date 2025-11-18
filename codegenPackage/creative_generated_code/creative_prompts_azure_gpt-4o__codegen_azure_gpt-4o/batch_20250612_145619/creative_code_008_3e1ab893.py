"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Generate a code example to enable Ethereum pledge functionality on a mobile browser using Web3.js.
Generated: DETERMINISTIC_3e1ab893e28da7cc
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
import Web3 from 'web3';

// Initialize variables
let web3; // Instance of Web3
let userAccount; // User's Ethereum account

// Smart contract details
const contractAddress = '0xYourSmartContractAddress'; // Replace with your contract address
const contractABI = [ /* ABI Array Here */ ]; // Replace with your contract's ABI

// Initialize Web3 and connect to the user's wallet
async function initializeWeb3() {
  if (window.ethereum) {
    try {
      // Request account access if needed
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Use Ethereum provider
      web3 = new Web3(window.ethereum);

      // Get the user's account
      const accounts = await web3.eth.getAccounts();
      userAccount = accounts[0]; // Use the first account

      console.log('Web3 initialized. User account:', userAccount);
    } catch (error) {
      console.error('User denied account access or other error:', error);
    }
  } else {
    console.error('Ethereum provider not found. Install MetaMask or similar wallet.');
  }
}

// Pledge function to interact with the smart contract
async function pledge(amountInEther) {
  try {
    // Initialize contract instance
    const contract = new web3.eth.Contract(contractABI, contractAddress);

    // Convert amount to Wei
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');

    // Call the pledge function on the contract
    const transaction = await contract.methods.pledge().send({
      from: userAccount,
      value: amountInWei, // Send Ether along with the transaction
    });

    console.log('Pledge successful:', transaction);
  } catch (error) {
    console.error('Pledge failed:', error);
  }
}

// Helper function to attach event listeners to buttons (for UI interaction)
function setupEventListeners() {
  const pledgeButton = document.getElementById('pledgeButton');
  if (pledgeButton) {
    pledgeButton.addEventListener('click', async () => {
      const amount = document.getElementById('pledgeAmount').value;
      if (amount) {
        await pledge(amount);
      } else {
        console.error('Amount is required to make a pledge.');
      }
    });
  }
}

// Initialize the application
async function init() {
  await initializeWeb3();
  setupEventListeners();
}

// Run the initialization when the window loads
window.addEventListener('load', init);
```

### Notes:
- Replace `contractAddress` and `contractABI` with your actual Ethereum smart contract's details.
- Ensure the HTML file includes an input field for `pledgeAmount` and a button with id `pledgeButton`.
- This code assumes the user interacts using a Web3-compatible Ethereum wallet such as MetaMask.
