"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Develop a tutorial for creating a Web3-enabled buy widget that allows users to purchase and stake $STARS tokens, similar to the widget described on the Crypto All-Stars website.
Generated: DETERMINISTIC_f114dc60761d3f51
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define constants for the contract ABI and address
const STARS_TOKEN_ABI = [
  {
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const STARS_TOKEN_ADDRESS = '0x...'; // Replace with the actual contract address

// Define constants for the staking contract ABI and address
const STAKING_CONTRACT_ABI = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_stakingToken",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "stakingToken",
    "outputs": [
      {
        "internalType": "contract IERC20",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "userInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "rewardDebt",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "pendingReward",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalStaked",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "stake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "unstake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const STAKING_CONTRACT_ADDRESS = '0x...'; // Replace with the actual contract address

// Create a Web3 instance
const web3 = new Web3(window.ethereum);

// Create a contract instance for the STARS token
const starsTokenContract = new web3.eth.Contract(STARS_TOKEN_ABI, STARS_TOKEN_ADDRESS);

// Create a contract instance for the staking contract
const stakingContract = new web3.eth.Contract(STAKING_CONTRACT_ABI, STAKING_CONTRACT_ADDRESS);

// Function to handle purchase and staking of $STARS tokens
async function purchaseAndStake(amount) {
  try {
    // Get the user's account address
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Approve the staking contract to spend the user's $STARS tokens
    await starsTokenContract.methods.approve(STAKING_CONTRACT_ADDRESS, amount).send({ from: account });

    // Stake the $STARS tokens
    await stakingContract.methods.stake(amount).send({ from: account });
  } catch (error) {
    console.error(error);
  }
}

// Function to handle unstaking of $STARS tokens
async function unstake() {
  try {
    // Get the user's account address
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Unstake the $STARS tokens
    await stakingContract.methods.unstake().send({ from: account });
  } catch (error) {
    console.error(error);
  }
}

// Function to get the user's balance of $STARS tokens
async function getBalance() {
  try {
    // Get the user's account address
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Get the user's balance of $STARS tokens
    const balance = await starsTokenContract.methods.balanceOf(account).call();

    return balance;
  } catch (error) {
    console.error(error);
  }
}

// Function to get the user's staked balance of $STARS tokens
async function getStakedBalance() {
  try {
    // Get the user's account address
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Get the user's staked balance of $STARS tokens
    const userInfo = await stakingContract.methods.userInfo(account).call();
    const stakedBalance = userInfo.amount;

    return stakedBalance;
  } catch (error) {
    console.error(error);
  }
}

// Create a buy widget
const buyWidget = document.createElement('div');
buyWidget.innerHTML = `
  <input id="amount" type="number" placeholder="Enter amount">
  <button id="purchase-and-stake">Purchase and Stake</button>
  <button id="unstake">Unstake</button>
  <p id="balance"></p>
  <p id="staked-balance"></p>
`;

// Add event listeners to the buy widget
document.getElementById('purchase-and-stake').addEventListener('click', async () => {
  const amount = document.getElementById('amount').value;
  await purchaseAndStake(amount);
});

document.getElementById('unstake').addEventListener('click', async () => {
  await unstake();
});

// Update the balance and staked balance displays
async function updateDisplays() {
  const balance = await getBalance();
  document.getElementById('balance').innerText = `Balance: ${balance}`;

  const stakedBalance = await getStakedBalance();
  document.getElementById('staked-balance').innerText = `
