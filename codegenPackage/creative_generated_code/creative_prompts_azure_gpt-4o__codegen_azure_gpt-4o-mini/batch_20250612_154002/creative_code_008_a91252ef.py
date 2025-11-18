"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwp.com
Prompt: Write a script to monitor Ethereum blockchain events, such as token transfers or liquidity pool updates, using JavaScript.
Generated: DETERMINISTIC_a91252ef69671ba9
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3'); // Library to interact with Ethereum blockchain
const { Contract } = require('web3-eth-contract'); // Contract class for interacting with smart contracts
const dotenv = require('dotenv'); // Library to load environment variables from a .env file

// Load environment variables from .env file
dotenv.config();

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.WebsocketProvider(process.env.INFURA_WS_URL));

// Ethereum smart contract ABI and address for monitoring
const ERC20_ABI = [
    // Minimal ABI to get Transfer events
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
    }
];

// Replace with the token contract address you want to monitor
const TOKEN_CONTRACT_ADDRESS = process.env.TOKEN_CONTRACT_ADDRESS;

// Initialize the contract
const tokenContract = new Contract(ERC20_ABI, TOKEN_CONTRACT_ADDRESS);

// Function to handle Transfer events
const handleTransferEvent = (error, event) => {
    if (error) {
        console.error(`Error receiving event: ${error.message}`);
        return;
    }
    
    // Log the transfer details
    console.log(`Transfer Event Detected: 
        From: ${event.returnValues.from}
        To: ${event.returnValues.to}
        Value: ${web3.utils.fromWei(event.returnValues.value, 'ether')} ETH
    `);
};

// Function to start monitoring events
const startMonitoring = async () => {
    try {
        // Subscribe to Transfer events
        tokenContract.events.Transfer({}, handleTransferEvent)
            .on('error', (error) => {
                console.error(`Error in event subscription: ${error.message}`);
            });
        
        console.log('Monitoring Transfer events...');
    } catch (error) {
        console.error(`Failed to start monitoring: ${error.message}`);
    }
};

// Start the event monitoring process
startMonitoring();
```

Make sure to create a `.env` file containing the following variables:

```
INFURA_WS_URL=wss://mainnet.infura.io/ws/v3/YOUR_INFURA_PROJECT_ID
TOKEN_CONTRACT_ADDRESS=YOUR_TOKEN_CONTRACT_ADDRESS
```

Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID and `YOUR_TOKEN_CONTRACT_ADDRESS` with the Ethereum token contract address you wish to monitor. This script will log all Transfer events from the specified ERC20 token contract.
