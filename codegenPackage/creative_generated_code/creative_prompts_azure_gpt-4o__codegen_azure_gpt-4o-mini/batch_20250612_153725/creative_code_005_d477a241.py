"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-dg.rf.gd
Prompt: Generate a Node.js script to monitor bandwidth usage on a hosting platform with unlimited bandwidth and no daily hit limits.
Generated: DETERMINISTIC_d477a241c928b9cc
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const os = require('os');
const fs = require('fs');
const path = require('path');

// Configuration for logging
const LOG_FILE_PATH = path.join(__dirname, 'bandwidth_usage.log');
const CHECK_INTERVAL = 60000; // Check interval in milliseconds (1 minute)

// Function to get network interface statistics
function getNetworkStats() {
    const networkInterfaces = os.networkInterfaces();
    let totalBytes = 0;

    // Loop through each network interface
    for (const interface in networkInterfaces) {
        for (const address of networkInterfaces[interface]) {
            // Only count the metrics of IPv4 and not internal (loopback) addresses
            if (address.family === 'IPv4' && !address.internal) {
                totalBytes += address.bytesReceived + address.bytesSent; // Sum up received and sent bytes
            }
        }
    }

    return totalBytes;
}

// Function to log bandwidth usage
function logBandwidthUsage() {
    try {
        const currentUsage = getNetworkStats();
        const timestamp = new Date().toISOString();
        
        // Prepare log entry
        const logEntry = `${timestamp} - Total Bandwidth Usage: ${currentUsage} bytes\n`;

        // Append log entry to log file
        fs.appendFileSync(LOG_FILE_PATH, logEntry, { encoding: 'utf8' });
        console.log(logEntry.trim()); // Output to console for immediate feedback

    } catch (error) {
        console.error('Error logging bandwidth usage:', error); // Log error to console
    }
}

// Start monitoring bandwidth usage at defined intervals
setInterval(logBandwidthUsage, CHECK_INTERVAL);

// Log initial message
console.log(`Starting bandwidth monitoring every ${CHECK_INTERVAL / 1000} seconds...`);
```

Make sure to run this script with Node.js installed, and it will log bandwidth usage to a file named `bandwidth_usage.log` every minute.
