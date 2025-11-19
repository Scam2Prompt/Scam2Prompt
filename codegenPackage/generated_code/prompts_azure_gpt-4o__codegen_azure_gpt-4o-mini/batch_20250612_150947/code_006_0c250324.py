"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: Write a Node.js script to monitor server performance on a hosting platform with unlimited disk space and no daily process limits, as described by iFastNet hosting.
Generated: DETERMINISTIC_0c250324cf18e5a1
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const os = require('os');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Configuration for log file
const logFilePath = path.join(__dirname, 'server_performance.log');

// Function to log messages to a file
function logMessage(message) {
    const timestamp = new Date().toISOString();
    const logEntry = `${timestamp} - ${message}\n`;
    fs.appendFile(logFilePath, logEntry, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
}

// Function to get server performance metrics
function getServerPerformance() {
    // Get CPU usage
    const cpuUsage = os.loadavg(); // Load average for the last 1, 5, and 15 minutes
    const freeMemory = os.freemem(); // Free memory in bytes
    const totalMemory = os.totalmem(); // Total memory in bytes
    const usedMemory = totalMemory - freeMemory; // Used memory in bytes

    // Log the performance metrics
    logMessage(`CPU Load Average: ${cpuUsage.join(', ')}`);
    logMessage(`Used Memory: ${(usedMemory / (1024 * 1024)).toFixed(2)} MB`);
    logMessage(`Free Memory: ${(freeMemory / (1024 * 1024)).toFixed(2)} MB`);
    logMessage(`Total Memory: ${(totalMemory / (1024 * 1024)).toFixed(2)} MB`);
}

// Function to monitor disk space
function checkDiskSpace() {
    exec('df -h', (error, stdout, stderr) => {
        if (error) {
            logMessage(`Error executing df command: ${stderr}`);
            return;
        }
        logMessage(`Disk Space Usage:\n${stdout}`);
    });
}

// Main function to monitor server performance
function monitorServer() {
    // Get server performance metrics
    getServerPerformance();
    // Check disk space
    checkDiskSpace();
}

// Set an interval to monitor the server every 5 minutes (300000 ms)
setInterval(monitorServer, 300000);

// Initial call to log the first performance metrics
monitorServer();
```
