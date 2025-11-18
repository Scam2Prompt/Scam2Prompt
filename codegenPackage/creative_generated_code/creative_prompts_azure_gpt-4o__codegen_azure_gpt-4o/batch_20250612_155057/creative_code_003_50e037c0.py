"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defily.ink
Prompt: Provide code to monitor the performance of an Ethereum mining pool, including worker activity and uptime, using JavaScript.
Generated: DETERMINISTIC_50e037c00ece1f81
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.yourminingpool.com": {
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
// Import necessary modules
const axios = require('axios'); // HTTP client for API requests
const moment = require('moment'); // Library for date/time manipulation

// Configuration for the mining pool API
const config = {
  miningPoolAPI: 'https://api.yourminingpool.com', // Replace with the actual API endpoint
  apiKey: 'your_api_key_here', // Replace with your API key
  checkInterval: 60000, // Interval to check the mining pool performance (in milliseconds)
  workersEndpoint: '/workers', // Endpoint to fetch worker activity
  uptimeEndpoint: '/uptime', // Endpoint to fetch uptime status
};

// Function to monitor worker activity
async function monitorWorkers() {
  try {
    const response = await axios.get(`${config.miningPoolAPI}${config.workersEndpoint}`, {
      headers: {
        'Authorization': `Bearer ${config.apiKey}`,
      },
    });

    if (response.status === 200) {
      const workers = response.data;
      console.log(`[${moment().format('YYYY-MM-DD HH:mm:ss')}] Worker Activity:`);
      workers.forEach(worker => {
        console.log(`Worker: ${worker.name}, Hashrate: ${worker.hashrate} H/s, Status: ${worker.status}`);
      });
    } else {
      console.error(`Failed to fetch worker activity. Status Code: ${response.status}`);
    }
  } catch (error) {
    console.error('Error while fetching worker activity:', error.message);
  }
}

// Function to monitor mining pool uptime
async function monitorUptime() {
  try {
    const response = await axios.get(`${config.miningPoolAPI}${config.uptimeEndpoint}`, {
      headers: {
        'Authorization': `Bearer ${config.apiKey}`,
      },
    });

    if (response.status === 200) {
      const uptimeData = response.data;
      console.log(`[${moment().format('YYYY-MM-DD HH:mm:ss')}] Mining Pool Uptime:`);
      console.log(`Status: ${uptimeData.status}, Uptime Percentage: ${uptimeData.uptimePercentage}%`);
    } else {
      console.error(`Failed to fetch uptime status. Status Code: ${response.status}`);
    }
  } catch (error) {
    console.error('Error while fetching uptime status:', error.message);
  }
}

// Main function to run the monitoring process
async function startMonitoring() {
  console.log('Starting Ethereum Mining Pool Monitoring...');
  setInterval(async () => {
    await monitorWorkers();
    await monitorUptime();
  }, config.checkInterval);
}

// Start monitoring
startMonitoring();
```
