"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Provide code examples for building a dapp with infinite scalability using Infura x Linea integration, as outlined in Consensys' article.
Generated: DETERMINISTIC_667ee3e847630deb
Batch ID: 20250612_153812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://linea.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

I'll provide a basic example of a decentralized application (dapp) using Infura and Linea for infinite scalability. I'll be using JavaScript, Web3.js, and Ethers.js for this example.

**package.json**
```json
{
  "name": "infura-linea-dapp",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "web3": "^1.8.0",
    "ethers": "^5.4.1"
  }
}
```

**index.js**
```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Infura project ID
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';

// Linea RPC URL
const LINEA_RPC_URL = 'https://linea.infura.io/v3/YOUR_INFURA_PROJECT_ID';

// Create a new Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider(LINEA_RPC_URL));

// Create a new Ethers provider
const ethersProvider = new ethers.providers.JsonRpcProvider(LINEA_RPC_URL);

// Define a contract ABI
const contractAbi = [
  {
    "inputs": [],
    "name": "getMessage",
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
        "internalType": "string",
        "name": "_message",
        "type": "string"
      }
    ],
    "name": "setMessage",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Define a contract address
const contractAddress = '0x...';

// Create a new contract instance
const contract = new web3.eth.Contract(contractAbi, contractAddress);

// Create a new ethers contract instance
const ethersContract = new ethers.Contract(contractAddress, contractAbi, ethersProvider);

// Define an async function to get the message
async function getMessage() {
  try {
    const message = await contract.methods.getMessage().call();
    console.log(`Message: ${message}`);
  } catch (error) {
    console.error(`Error getting message: ${error.message}`);
  }
}

// Define an async function to set the message
async function setMessage(message) {
  try {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];
    await contract.methods.setMessage(message).send({ from: account });
    console.log(`Message set: ${message}`);
  } catch (error) {
    console.error(`Error setting message: ${error.message}`);
  }
}

// Define an async function using ethers to get the message
async function getMessageEthers() {
  try {
    const message = await ethersContract.getMessage();
    console.log(`Message (ethers): ${message}`);
  } catch (error) {
    console.error(`Error getting message (ethers): ${error.message}`);
  }
}

// Define an async function using ethers to set the message
async function setMessageEthers(message) {
  try {
    const signer = await new ethers.Wallet('YOUR_PRIVATE_KEY', ethersProvider);
    const tx = await ethersContract.connect(signer).setMessage(message);
    await tx.wait();
    console.log(`Message set (ethers): ${message}`);
  } catch (error) {
    console.error(`Error setting message (ethers): ${error.message}`);
  }
}

// Call the functions
async function main() {
  await getMessage();
  await setMessage('Hello, world!');
  await getMessageEthers();
  await setMessageEthers('Hello, world! (ethers)');
}

main();
```
