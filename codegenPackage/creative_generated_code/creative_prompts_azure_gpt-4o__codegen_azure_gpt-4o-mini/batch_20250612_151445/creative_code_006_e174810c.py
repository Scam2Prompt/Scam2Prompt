"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-ethereums-trustswallet-com.html-5.me
Prompt: Generate a Node.js script to monitor bandwidth usage on a hosting service with unlimited bandwidth and no daily hit limit, such as iFastNet.
Generated: DETERMINISTIC_e174810cbc88daf2
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const http = require('http');
const os = require('os');
const fs = require('fs');
const path = require('path');

// Define constants
const LOG_FILE = path.join(__dirname, 'bandwidth_log.json');
const MONITOR_INTERVAL = 60000; // Monitor every minute

// Bandwidth usage tracker
let previousBytesReceived = 0;
let previousBytesSent = 0;

// Function to log data to a JSON file
const logData = (data) => {
    // Ensuring the log file exists
    if (!fs.existsSync(LOG_FILE)) {
        fs.writeFileSync(LOG_FILE, JSON.stringify([]));
    }

    // Read existing logs
    const logs = JSON.parse(fs.readFileSync(LOG_FILE));

    // Append new log entry
    logs.push(data);

    // Write back to the log file
    fs.writeFileSync(LOG_FILE, JSON.stringify(logs, null, 2));
};

// Function to monitor bandwidth usage
const monitorBandwidth = () => {
    // Get network interfaces
    const interfaces = os.networkInterfaces();

    // Initialize counters
    let totalBytesReceived = 0;
    let totalBytesSent = 0;

    // Iterate over all interfaces
    for (const iface in interfaces) {
        for (const netInfo of interfaces[iface]) {
            // Skip internal (loopback) addresses
            if (netInfo.family === 'IPv4' && !netInfo.internal) {
                totalBytesReceived += netInfo.rx; // Bytes received
                totalBytesSent += netInfo.tx; // Bytes sent
            }
        }
    }

    // Calculate the difference since the last check
    const bytesReceived = totalBytesReceived - previousBytesReceived;
    const bytesSent = totalBytesSent - previousBytesSent;

    // Log the current usage
    logData({
        timestamp: new Date().toISOString(),
        bytesReceived,
        bytesSent
    });

    // Update previous values for the next check
    previousBytesReceived = totalBytesReceived;
    previousBytesSent = totalBytesSent;
};

// Handle potential errors
try {
    // Start the bandwidth monitoring at defined intervals
    setInterval(monitorBandwidth, MONITOR_INTERVAL);
} catch (error) {
    console.error('Error occurred during bandwidth monitoring:', error);
}
```
