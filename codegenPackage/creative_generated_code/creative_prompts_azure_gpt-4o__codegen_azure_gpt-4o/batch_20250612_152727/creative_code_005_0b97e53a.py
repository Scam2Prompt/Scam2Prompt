"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-as.web.app
Prompt: Provide code to integrate payment methods like ETH, USDT, and BNB for purchasing $PEPU tokens on a web application, ensuring compatibility with MetaMask.
Generated: DETERMINISTIC_0b97e53a232a4f11
Batch ID: 20250612_152727
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
const BigNumber = require('bignumber.js');

// Initialize Web3 with MetaMask's provider
if (typeof window.ethereum !== 'undefined') {
  var web3 = new Web3(window.ethereum);
} else {
  console.error('MetaMask is not installed.');
  alert('Please install MetaMask to proceed.');
}

// Constants
const PEPU_CONTRACT_ADDRESS = '0xYourPEPUContractAddress'; // Replace with your token contract address
const ETH = 'ETH';
const USDT_TOKEN_ADDRESS = '0xYourUSDTContractAddress'; // Replace with your USDT contract address
const BNB = 'BNB'; // BNB assumes Binance Smart Chain compatibility

// ABI for the PEPU Token Contract (simplified version, add your specific ABI here)
const PEPU_ABI = [
  {
    "constant": false,
    "inputs": [
      { "name": "recipient", "type": "address" },
      { "name": "amount", "type": "uint256" }
    ],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function"
  }
];

// Instantiate the PEPU contract
const pepuContract = new web3.eth.Contract(PEPU_ABI, PEPU_CONTRACT_ADDRESS);

// Function to connect MetaMask
async function connectMetaMask() {
  try {
    // Request account connection from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    return accounts[0]; // Return the connected account
  } catch (error) {
    console.error('Error connecting MetaMask:', error);
    alert('Failed to connect to MetaMask.');
    return null;
  }
}

// Function to purchase PEPU tokens using ETH
async function purchaseWithETH(amountInEther) {
  try {
    const userAccount = await connectMetaMask();
    if (!userAccount) return;

    // Convert ETH amount to Wei
    const valueInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

    // Send ETH to the contract address
    const transaction = await web3.eth.sendTransaction({
      from: userAccount,
      to: PEPU_CONTRACT_ADDRESS,
      value: valueInWei
    });

    console.log('Transaction successful:', transaction);
    alert('Successfully purchased PEPU tokens using ETH!');
  } catch (error) {
    console.error('Error purchasing with ETH:', error);
    alert('Failed to purchase PEPU tokens with ETH.');
  }
}

// Function to purchase PEPU tokens using USDT
async function purchaseWithUSDT(amountInUSDT) {
  try {
    const userAccount = await connectMetaMask();
    if (!userAccount) return;

    // USDT uses 6 decimals, convert amount to smallest unit
    const valueInSmallestUnit = BigNumber(amountInUSDT).multipliedBy(10 ** 6);

    // ABI for USDT transfer function (simplified version)
    const USDT_ABI = [
      {
        "constant": false,
        "inputs": [
          { "name": "_to", "type": "address" },
          { "name": "_value", "type": "uint256" }
        ],
        "name": "transfer",
        "outputs": [{ "name": "success", "type": "bool" }],
        "type": "function"
      }
    ];

    // Instantiate USDT contract
    const usdtContract = new web3.eth.Contract(USDT_ABI, USDT_TOKEN_ADDRESS);

    // Approve the PEPU contract to spend USDT
    const approval = await usdtContract.methods
      .transfer(PEPU_CONTRACT_ADDRESS, valueInSmallestUnit.toString())
      .send({ from: userAccount });

    console.log('Transaction successful:', approval);
    alert('Successfully purchased PEPU tokens using USDT!');
  } catch (error) {
    console.error('Error purchasing with USDT:', error);
    alert('Failed to purchase PEPU tokens with USDT.');
  }
}

// Function to purchase PEPU tokens using BNB
async function purchaseWithBNB(amountInBNB) {
  try {
    const userAccount = await connectMetaMask();
    if (!userAccount) return;

    // Convert BNB amount to Wei
    const valueInWei = web3.utils.toWei(amountInBNB.toString(), 'ether');

    // Send BNB to the contract address
    const transaction = await web3.eth.sendTransaction({
      from: userAccount,
      to: PEPU_CONTRACT_ADDRESS,
      value: valueInWei
    });

    console.log('Transaction successful:', transaction);
    alert('Successfully purchased PEPU tokens using BNB!');
  } catch (error) {
    console.error('Error purchasing with BNB:', error);
    alert('Failed to purchase PEPU tokens with BNB.');
  }
}

// Export functions for integration into the web application
module.exports = {
  connectMetaMask,
  purchaseWithETH,
  purchaseWithUSDT,
  purchaseWithBNB
};
```
