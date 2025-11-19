"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: Write a function in JavaScript to monitor collateral levels in Venus Protocol and trigger alerts if the liquidation threshold is approached.
Generated: DETERMINISTIC_7badc7daa3057158
Batch ID: 20250612_155048
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-webhook-url.com/alert": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
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
const ethers = require('ethers');
const axios = require('axios');

// Venus Protocol contract addresses and ABI
const VENUS_COMPTROLLER_ADDRESS = '0xfD36E2c2a6789Db23113685031d7F16329158384';
const VENUS_COMPTROLLER_ABI = [
  'function markets(address) view returns (bool, uint256, bool)',
  'function getAccountLiquidity(address) view returns (uint256, uint256, uint256)'
];

// Configuration
const RPC_URL = 'https://bsc-dataseed.binance.org/';
const LIQUIDATION_THRESHOLD_PERCENT = 90; // Alert when collateral reaches 90% of liquidation threshold
const POLL_INTERVAL_MS = 60000; // Check every minute
const ALERT_WEBHOOK_URL = 'https://your-webhook-url.com/alert'; // Replace with your webhook

// Initialize provider and contract
const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
const comptroller = new ethers.Contract(
  VENUS_COMPTROLLER_ADDRESS,
  VENUS_COMPTROLLER_ABI,
  provider
);

/**
 * Monitor collateral levels for a given address
 * @param {string} walletAddress - The wallet address to monitor
 */
async function monitorCollateral(walletAddress) {
  try {
    // Get account liquidity data
    const [error, liquidity, shortfall] = await comptroller.getAccountLiquidity(walletAddress);
    
    if (error.toString() !== '0') {
      throw new Error(`Error fetching liquidity: ${error}`);
    }

    // Calculate collateral utilization percentage
    const collateralUtilization = (shortfall * 100) / (liquidity + shortfall);
    
    if (collateralUtilization >= LIQUIDATION_THRESHOLD_PERCENT) {
      await triggerAlert(walletAddress, collateralUtilization, liquidity, shortfall);
    }

    console.log(`Collateral utilization for ${walletAddress}: ${collateralUtilization.toFixed(2)}%`);
  } catch (error) {
    console.error(`Error monitoring collateral for ${walletAddress}:`, error);
  }
}

/**
 * Trigger alert when liquidation threshold is approached
 * @param {string} walletAddress 
 * @param {number} utilization 
 * @param {ethers.BigNumber} liquidity 
 * @param {ethers.BigNumber} shortfall 
 */
async function triggerAlert(walletAddress, utilization, liquidity, shortfall) {
  const alertMessage = {
    text: `🚨 Venus Protocol Liquidation Alert 🚨`,
    fields: [
      { title: 'Wallet Address', value: walletAddress, short: true },
      { title: 'Collateral Utilization', value: `${utilization.toFixed(2)}%`, short: true },
      { title: 'Liquidity', value: ethers.utils.formatUnits(liquidity, 18), short: true },
      { title: 'Shortfall', value: ethers.utils.formatUnits(shortfall, 18), short: true },
      { title: 'Threshold', value: `${LIQUIDATION_THRESHOLD_PERCENT}%`, short: true },
      { title: 'Time', value: new Date().toISOString(), short: true }
    ]
  };

  try {
    await axios.post(ALERT_WEBHOOK_URL, alertMessage);
    console.log(`Alert sent for ${walletAddress}`);
  } catch (error) {
    console.error('Failed to send alert:', error);
  }
}

/**
 * Start monitoring for multiple addresses
 * @param {string[]} addresses - Array of wallet addresses to monitor
 */
function startMonitoring(addresses) {
  console.log('Starting Venus Protocol collateral monitoring...');
  
  // Initial check
  addresses.forEach(monitorCollateral);
  
  // Set up periodic checks
  const intervalId = setInterval(() => {
    addresses.forEach(monitorCollateral);
  }, POLL_INTERVAL_MS);

  // Return function to stop monitoring
  return () => {
    clearInterval(intervalId);
    console.log('Monitoring stopped');
  };
}

module.exports = {
  monitorCollateral,
  startMonitoring
};
```
