"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesla-promo.epizy.com
Prompt: Write Node.js code to monitor bandwidth usage on a hosting service with unlimited bandwidth and modern cPanel features.
Generated: DETERMINISTIC_c7c86cddecef428c
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const fs = require('fs');
const path = require('path');
const os = require('os');
const express = require('express');
const { exec } = require('child_process');

// Create an Express app
const app = express();

// Configuration
const PORT = process.env.PORT || 3000; // Port for the server
const LOG_FILE = path.join(__dirname, 'bandwidth.log'); // Log file to record bandwidth usage

// Middleware to parse JSON requests
app.use(express.json());

// Function to log bandwidth usage
function logBandwidthUsage(usage) {
    const logEntry = `${new Date().toISOString()} - Bandwidth Usage: ${usage} bytes\n`;
    fs.appendFile(LOG_FILE, logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
}

// Function to monitor bandwidth
function monitorBandwidth() {
    exec("vnstat --json", (err, stdout, stderr) => {
        if (err) {
            console.error('Error executing vnstat command:', stderr);
            return;
        }
        
        try {
            const data = JSON.parse(stdout);
            const bandwidthUsage = data.interfaces[0].traffic; // Assuming monitoring the first interface
            const totalUsage = bandwidthUsage.rx + bandwidthUsage.tx; // Total RX + TX

            logBandwidthUsage(totalUsage);
        } catch (parseErr) {
            console.error('Error parsing JSON data:', parseErr);
        }
    });
}

// Endpoint to fetch current bandwidth usage
app.get('/bandwidth', (req, res) => {
    exec("vnstat --json", (err, stdout, stderr) => {
        if (err) {
            console.error('Error executing vnstat command:', stderr);
            return res.status(500).send('Error retrieving bandwidth usage');
        }
        
        try {
            const data = JSON.parse(stdout);
            const currentUsage = data.interfaces[0].traffic; // Assuming monitoring the first interface
            res.json(currentUsage);
        } catch (parseErr) {
            console.error('Error parsing JSON data:', parseErr);
            res.status(500).send('Error processing data');
        }
    });
});

// Start monitoring bandwidth at regular intervals
setInterval(monitorBandwidth, 60000); // Monitor every minute

// Start the Express server
app.listen(PORT, () => {
    console.log(`Bandwidth monitoring server running on port ${PORT}`);
});
```

**Note:** This code assumes you have `vnstat` installed on your system for bandwidth monitoring. Make sure to run it with necessary permissions to access the network interface data.
