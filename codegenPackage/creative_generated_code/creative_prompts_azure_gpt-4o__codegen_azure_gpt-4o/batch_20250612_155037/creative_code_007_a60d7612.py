"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Create a Node.js script to monitor the $WING presale address for incoming transactions and log the amount of ETH or USDT raised in real-time.
Generated: DETERMINISTIC_a60d7612580e5938
Batch ID: 20250612_155037
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
const ethers = require('ethers');

// Set up environment variables
require('dotenv').config();

const INFURA_API_URL = process.env.INFURA_API_URL; // Infura URL for connecting to Ethereum blockchain
const PRESALE_ADDRESS = process.env.PRESALE_ADDRESS; // Address of the $WING presale contract
const USDT_CONTRACT_ADDRESS = process.env.USDT_CONTRACT_ADDRESS; // Address of the USDT token contract

// Validate environment variables
if (!INFURA_API_URL || !PRESALE_ADDRESS || !USDT_CONTRACT_ADDRESS) {
  console.error('Error: Missing required environment variables.');
  process.exit(1);
}

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_API_URL));

// ABI of the USDT contract (simplified for balanceOf function)
const ERC20_ABI = [
  {
    constant: true,
    inputs: [{ name: '_owner', type: 'address' }],
    name: 'balanceOf',
    outputs: [{ name: 'balance', type: 'uint256' }],
    type: 'function',
  },
];

// Initialize contract instance for USDT
const usdtContract = new web3.eth.Contract(ERC20_ABI, USDT_CONTRACT_ADDRESS);

// Variables to track raised amounts
let totalETHRaised = 0;
let totalUSDTRaised = 0;

// Function to fetch and log presale balances
async function monitorPresale() {
  try {
    // Fetch the current balance of ETH in the presale address
    const ethBalanceWei = await web3.eth.getBalance(PRESALE_ADDRESS);
    const ethBalance = web3.utils.fromWei(ethBalanceWei, 'ether');

    // Fetch the current balance of USDT in the presale address
    const usdtBalanceRaw = await usdtContract.methods.balanceOf(PRESALE_ADDRESS).call();
    const usdtBalance = ethers.utils.formatUnits(usdtBalanceRaw, 6); // USDT uses 6 decimals

    console.log(`Presale Monitoring Update (Address: ${PRESALE_ADDRESS})`);
    console.log(`ETH Raised: ${ethBalance} ETH`);
    console.log(`USDT Raised: ${usdtBalance} USDT`);

    // Update tracked amounts
    totalETHRaised = parseFloat(ethBalance);
    totalUSDTRaised = parseFloat(usdtBalance);
  } catch (error) {
    console.error('Error occurred while monitoring presale:', error.message);
  }
}

// Monitor presale balances at regular intervals
const MONITOR_INTERVAL = 10000; // 10 seconds

console.log('Starting presale monitoring...');
setInterval(monitorPresale, MONITOR_INTERVAL);
```

### Notes:
1. **Environment Variable Setup**: Ensure `INFURA_API_URL`, `PRESALE_ADDRESS`, and `USDT_CONTRACT_ADDRESS` are defined in a `.env` file.
   ```
   INFURA_API_URL=<Your_Infura_Endpoint>
   PRESALE_ADDRESS=<Presale_Contract_Address>
   USDT_CONTRACT_ADDRESS=<USDT_Contract_Address>
   ```

2. Install required packages:
   ```bash
   npm install web3 ethers dotenv
   ```

This script continuously monitors the $WING presale address for ETH and USDT balances and logs the raised amounts in real-time. It handles errors gracefully and follows best practices.
