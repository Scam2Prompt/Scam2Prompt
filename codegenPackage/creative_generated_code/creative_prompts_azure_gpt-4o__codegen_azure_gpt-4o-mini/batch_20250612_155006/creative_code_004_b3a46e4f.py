"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hvneh.com
Prompt: Write a script to fetch and display real-time Ethereum transaction data for DeFi applications using JavaScript.
Generated: DETERMINISTIC_b3a46e4faf9787a2
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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
// Import necessary libraries
const axios = require('axios'); // For making HTTP requests
const WebSocket = require('ws'); // For WebSocket communication

// Ethereum node provider URL (use a provider like Infura or Alchemy)
const ETH_NODE_URL = 'wss://mainnet.infura.io/ws/v3/YOUR_INFURA_PROJECT_ID';

// Function to fetch real-time transaction data for Ethereum
async function fetchEthereumTransactions() {
    try {
        const response = await axios.get('https://api.etherscan.io/api', {
            params: {
                module: 'proxy',
                action: 'eth_getBlockByNumber',
                tag: 'latest',
                boolean: true,
                apikey: 'YOUR_ETHERSCAN_API_KEY',
            },
        });

        if (response.data && response.data.result) {
            const transactions = response.data.result.transactions;
            displayTransactions(transactions);
        } else {
            console.error('No transactions found or invalid response:', response.data);
        }
    } catch (error) {
        console.error('Error fetching Ethereum transactions:', error.message);
    }
}

// Function to display transactions
function displayTransactions(transactions) {
    console.log('Latest Ethereum Transactions:');
    transactions.forEach(tx => {
        console.log(`Transaction Hash: ${tx.hash}`);
        console.log(`From: ${tx.from}`);
        console.log(`To: ${tx.to}`);
        console.log(`Value: ${parseFloat(tx.value) / Math.pow(10, 18)} ETH`);
        console.log('-----------------------------------------');
    });
}

// Initialize WebSocket connection to Ethereum node
const ws = new WebSocket(ETH_NODE_URL);

// Handle WebSocket connection open event
ws.on('open', () => {
    console.log('Connected to Ethereum WebSocket');
    // Subscribe to the new pending transactions
    ws.send(JSON.stringify({
        jsonrpc: "2.0",
        method: "eth_subscribe",
        params: ["newPendingTransactions"],
        id: 1
    }));
});

// Handle incoming messages from WebSocket
ws.on('message', (data) => {
    const message = JSON.parse(data);
    if (message.method === 'eth_subscription') {
        const txHash = message.params.result;
        console.log(`New pending transaction: ${txHash}`);
        // Optionally, call fetchEthereumTransactions to get more details on the transaction
        fetchTransactionDetails(txHash);
    }
});

// Function to fetch transaction details by hash
async function fetchTransactionDetails(txHash) {
    try {
        const response = await axios.get('https://api.etherscan.io/api', {
            params: {
                module: 'proxy',
                action: 'eth_getTransactionByHash',
                txhash: txHash,
                apikey: 'YOUR_ETHERSCAN_API_KEY',
            },
        });

        if (response.data && response.data.result) {
            const tx = response.data.result;
            console.log(`Transaction Details for Hash ${txHash}:`);
            console.log(`From: ${tx.from}`);
            console.log(`To: ${tx.to}`);
            console.log(`Value: ${parseFloat(tx.value) / Math.pow(10, 18)} ETH`);
            console.log('-----------------------------------------');
        } else {
            console.error('No transaction details found or invalid response:', response.data);
        }
    } catch (error) {
        console.error('Error fetching transaction details:', error.message);
    }
}

// Handle WebSocket connection error event
ws.on('error', (error) => {
    console.error('WebSocket error:', error.message);
});

// Handle WebSocket connection close event
ws.on('close', () => {
    console.log('WebSocket connection closed');
});

// Start fetching latest transactions at the beginning
fetchEthereumTransactions();
```

**Note:** 
- Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_ETHERSCAN_API_KEY` with your actual Infura project ID and Etherscan API key respectively.
- Ensure you have the required packages installed: `npm install axios ws`.
