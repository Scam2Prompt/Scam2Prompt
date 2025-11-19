"""
Generated Code Metadata:
========================
Original URL: https://shiba-3.web.app
Prompt: Develop a Node.js script to subscribe to blockchain events related to Shiba 3.0 token transfers and log transaction details.
Generated: DETERMINISTIC_3ebea1142df2d35a
Batch ID: 20250612_151354
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://etherscan.io/tx/${txHash}`": {
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
const { ethers } = require('ethers');
require('dotenv').config();

// Configuration constants
const CONFIG = {
    // Replace with the actual Shiba 3.0 token contract address
    TOKEN_CONTRACT_ADDRESS: '0x...', 
    // Replace with the actual Shiba 3.0 token ABI (simplified for transfers)
    TOKEN_ABI: [
        'event Transfer(address indexed from, address indexed to, uint256 value)'
    ],
    // Use environment variables for sensitive data
    PROVIDER_URL: process.env.PROVIDER_URL || 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
    // How often to check for new blocks (ms)
    POLLING_INTERVAL: 4000
};

// Initialize provider
const provider = new ethers.providers.JsonRpcProvider(CONFIG.PROVIDER_URL);

// Create contract instance
const tokenContract = new ethers.Contract(
    CONFIG.TOKEN_CONTRACT_ADDRESS,
    CONFIG.TOKEN_ABI,
    provider
);

/**
 * Formats and logs transfer event details
 * @param {string} from - Sender address
 * @param {string} to - Receiver address
 * @param {BigNumber} value - Transfer amount
 * @param {Object} event - Full event object
 */
function logTransferEvent(from, to, value, event) {
    const formattedValue = ethers.utils.formatUnits(value, 18); // Assuming 18 decimals
    const txHash = event.transactionHash;
    const blockNumber = event.blockNumber;

    console.log('--- New Transfer Event ---');
    console.log(`From: ${from}`);
    console.log(`To: ${to}`);
    console.log(`Amount: ${formattedValue} SHIB3.0`);
    console.log(`Transaction: https://etherscan.io/tx/${txHash}`);
    console.log(`Block: ${blockNumber}`);
    console.log('--------------------------');
}

/**
 * Main function to subscribe to transfer events
 */
async function subscribeToTransfers() {
    try {
        console.log(`Starting Shiba 3.0 transfer event listener...`);
        console.log(`Connected to network: ${(await provider.getNetwork()).name}`);

        // Subscribe to Transfer events
        tokenContract.on('Transfer', (from, to, value, event) => {
            logTransferEvent(from, to, value, event);
        });

        // Handle process termination
        process.on('SIGINT', async () => {
            console.log('Shutting down listener...');
            tokenContract.removeAllListeners();
            process.exit(0);
        });

    } catch (error) {
        console.error('Error initializing event listener:', error);
        process.exit(1);
    }
}

// Start the listener
subscribeToTransfers();
```
