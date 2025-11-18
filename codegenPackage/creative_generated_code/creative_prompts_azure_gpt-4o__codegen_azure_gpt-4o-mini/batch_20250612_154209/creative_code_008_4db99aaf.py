"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: Write a Node.js script to monitor bandwidth usage on a hosting service that offers unlimited bandwidth and modern cPanel.
Generated: DETERMINISTIC_4db99aaf802d2dba
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const http = require('http');
const fs = require('fs');
const os = require('os');

// Configuration for monitoring
const MONITOR_INTERVAL = 60000; // Monitor every minute
const LOG_FILE = 'bandwidth_usage.log';

// Function to get current network usage
const getNetworkUsage = () => {
    const networkInterfaces = os.networkInterfaces();
    let totalBytesReceived = 0;
    let totalBytesSent = 0;

    // Iterate over network interfaces and accumulate data
    for (const interface in networkInterfaces) {
        const addresses = networkInterfaces[interface];
        addresses.forEach(addr => {
            if (addr.family === 'IPv4') {
                totalBytesReceived += addr.rx_bytes || 0; // Received bytes
                totalBytesSent += addr.tx_bytes || 0;     // Sent bytes
            }
        });
    }

    return { received: totalBytesReceived, sent: totalBytesSent };
};

// Function to log bandwidth usage to file
const logBandwidthUsage = (usage) => {
    const logEntry = `${new Date().toISOString()} - Received: ${usage.received} bytes, Sent: ${usage.sent} bytes\n`;
    fs.appendFile(LOG_FILE, logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
};

// Main function to monitor bandwidth
const monitorBandwidth = () => {
    setInterval(() => {
        try {
            const usage = getNetworkUsage();
            logBandwidthUsage(usage);
        } catch (error) {
            console.error('Error monitoring bandwidth:', error);
        }
    }, MONITOR_INTERVAL);
};

// Start the bandwidth monitoring
monitorBandwidth();
console.log(`Bandwidth monitoring started. Logging to ${LOG_FILE} every ${MONITOR_INTERVAL / 1000} seconds.`);
```

Make sure you have the necessary permissions to run this script and write to the specified log file. Additionally, adapt the network interface byte retrieval as per your system and environment, as this implementation assumes a generic structure.
