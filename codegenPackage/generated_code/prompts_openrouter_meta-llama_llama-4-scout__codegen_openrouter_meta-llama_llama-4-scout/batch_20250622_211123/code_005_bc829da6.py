"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a GGPLAY platform integration guide, detailing how to incorporate GXT and EXP utilities and use cases into a WEB3 gaming application.
Generated: DETERMINISTIC_bc829da68e3a2169
Batch ID: 20250622_211123
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.ggplay.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * GGPLAY Platform Integration Guide
 * 
 * This library provides a comprehensive guide on integrating GXT and EXP utilities
 * into a WEB3 gaming application.
 * 
 * @author [Your Name]
 * @version 1.0.0
 */

// Import required libraries
const Web3 = require('web3');
const axios = require('axios');

// Define constants
const GGPLAY_API_URL = 'https://api.ggplay.com';
const GXT_CONTRACT_ADDRESS = '0xGXT_CONTRACT_ADDRESS';
const EXP_CONTRACT_ADDRESS = '0xEXP_CONTRACT_ADDRESS';

/**
 * Initialize the GGPLAY platform integration
 * 
 * @param {string} apiKey - GGPLAY API key
 * @param {string} apiSecret - GGPLAY API secret
 */
function initGGPLAY(apiKey, apiSecret) {
    // Set API credentials
    axios.defaults.headers.common['Authorization'] = `Bearer ${apiKey}`;
    axios.defaults.headers.common['Content-Type'] = 'application/json';

    // Initialize Web3
    const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));
    return { web3, axios };
}

/**
 * Get GXT balance
 * 
 * @param {string} userAddress - User Ethereum address
 * @param {object} ggplay - GGPLAY platform integration object
 * @returns {Promise<number>} GXT balance
 */
async function getGXTBalance(userAddress, ggplay) {
    try {
        // Call GXT contract
        const gxtContract = new ggplay.web3.eth.Contract(GXT_ABI, GXT_CONTRACT_ADDRESS);
        const balance = await gxtContract.methods.balanceOf(userAddress).call();
        return balance;
    } catch (error) {
        console.error('Error getting GXT balance:', error);
        throw error;
    }
}

/**
 * Get EXP balance
 * 
 * @param {string} userAddress - User Ethereum address
 * @param {object} ggplay - GGPLAY platform integration object
 * @returns {Promise<number>} EXP balance
 */
async function getEXPBalance(userAddress, ggplay) {
    try {
        // Call EXP contract
        const expContract = new ggplay.web3.eth.Contract(EXP_ABI, EXP_CONTRACT_ADDRESS);
        const balance = await expContract.methods.balanceOf(userAddress).call();
        return balance;
    } catch (error) {
        console.error('Error getting EXP balance:', error);
        throw error;
    }
}

/**
 * Transfer GXT
 * 
 * @param {string} fromAddress - Sender Ethereum address
 * @param {string} toAddress - Recipient Ethereum address
 * @param {number} amount - GXT amount to transfer
 * @param {object} ggplay - GGPLAY platform integration object
 * @returns {Promise<string>} Transaction hash
 */
async function transferGXT(fromAddress, toAddress, amount, ggplay) {
    try {
        // Call GXT contract
        const gxtContract = new ggplay.web3.eth.Contract(GXT_ABI, GXT_CONTRACT_ADDRESS);
        const tx = await gxtContract.methods.transfer(toAddress, amount).send({ from: fromAddress });
        return tx.transactionHash;
    } catch (error) {
        console.error('Error transferring GXT:', error);
        throw error;
    }
}

/**
 * Transfer EXP
 * 
 * @param {string} fromAddress - Sender Ethereum address
 * @param {string} toAddress - Recipient Ethereum address
 * @param {number} amount - EXP amount to transfer
 * @param {object} ggplay - GGPLAY platform integration object
 * @returns {Promise<string>} Transaction hash
 */
async function transferEXP(fromAddress, toAddress, amount, ggplay) {
    try {
        // Call EXP contract
        const expContract = new ggplay.web3.eth.Contract(EXP_ABI, EXP_CONTRACT_ADDRESS);
        const tx = await expContract.methods.transfer(toAddress, amount).send({ from: fromAddress });
        return tx.transactionHash;
    } catch (error) {
        console.error('Error transferring EXP:', error);
        throw error;
    }
}

// Define ABI for GXT and EXP contracts
const GXT_ABI = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [
            {
                "name": "owner",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false
    },
    {
        "inputs": [
            {
                "name": "from",
                "type": "address"
            },
            {
                "name": "to",
                "type": "address"
            },
            {
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "to",
                "type": "address"
            },
            {
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

const EXP_ABI = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [
            {
                "name": "owner",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false
    },
    {
        "inputs": [
            {
                "name": "from",
                "type": "address"
            },
            {
                "name": "to",
                "type": "address"
            },
            {
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "to",
                "type": "address"
            },
            {
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

// Example usage
async function main() {
    try {
        const apiKey = 'YOUR_API_KEY';
        const apiSecret = 'YOUR_API_SECRET';
        const ggplay = initGGPLAY(apiKey, apiSecret);
        const userAddress = '0xUSER_ADDRESS';

        const gxtBalance = await getGXTBalance(userAddress, ggplay);
        console.log(`GXT balance: ${gxtBalance}`);

        const expBalance = await getEXPBalance(userAddress, ggplay);
        console.log(`EXP balance: ${expBalance}`);

        const fromAddress = '0xFROM_ADDRESS';
        const toAddress = '0xTO_ADDRESS';
        const amount = 100;

        const gxtTxHash = await transferGXT(fromAddress, toAddress, amount, ggplay);
        console.log(`GXT transfer tx hash: ${gxtTxHash}`);

        const expTxHash = await transferEXP(fromAddress, toAddress, amount, ggplay);
        console.log(`EXP transfer tx hash: ${expTxHash}`);
    } catch (error) {
        console.error('Error:', error);
