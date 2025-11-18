"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Write a Node.js script to monitor server performance on a hosting platform with unlimited disk space and no daily process limits, as described by iFastNet hosting.
Generated: DETERMINISTIC_0c250324cf18e5a1
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Node.js script to monitor server performance on a hosting platform.
 * Assumes hosting with unlimited disk space and no daily process limits, such as iFastNet.
 * The script checks CPU usage, memory usage, and network performance at regular intervals.
 */

const os = require('os');
const fs = require('fs');
const { exec } = require('child_process');

// Monitoring Interval (in milliseconds)
const MONITOR_INTERVAL = 5000; // 5 seconds

// Log file for saving monitoring results
const LOG_FILE = 'server-performance.log';

/**
 * Logs messages to both the console and a log file.
 * @param {string} message - The message to log.
 */
function logMessage(message) {
    const timestamp = new Date().toISOString();
    const logEntry = `[${timestamp}] ${message}`;
    console.log(logEntry);

    // Append log entry to the log file
    fs.appendFile(LOG_FILE, logEntry + '\n', (err) => {
        if (err) {
            console.error('Error writing to log file:', err.message);
        }
    });
}

/**
 * Get CPU usage of the server.
 * @returns {Promise<number>} - CPU usage percentage.
 */
function getCPUUsage() {
    return new Promise((resolve, reject) => {
        exec('top -bn1 | grep "Cpu(s)"', (error, stdout) => {
            if (error) {
                reject(error);
                return;
            }

            try {
                const cpuLine = stdout.trim();
                const usageMatch = cpuLine.match(/(\d+\.\d+)\s+us/); // Extract "us" (user-space CPU usage)
                if (usageMatch && usageMatch[1]) {
                    resolve(parseFloat(usageMatch[1]));
                } else {
                    reject(new Error('Failed to parse CPU usage'));
                }
            } catch (err) {
                reject(err);
            }
        });
    });
}

/**
 * Get memory usage of the server.
 * @returns {{freeMemory: number, totalMemory: number, usedMemoryPercentage: number}}
 */
function getMemoryUsage() {
    const freeMemory = os.freemem();
    const totalMemory = os.totalmem();
    const usedMemoryPercentage = ((totalMemory - freeMemory) / totalMemory) * 100;

    return {
        freeMemory,
        totalMemory,
        usedMemoryPercentage,
    };
}

/**
 * Get network performance metrics.
 * @returns {{networkInterfaces: object}}
 */
function getNetworkPerformance() {
    return {
        networkInterfaces: os.networkInterfaces(),
    };
}

/**
 * Monitor server performance and log results.
 */
async function monitorPerformance() {
    try {
        logMessage('Starting server performance monitoring...');

        const cpuUsage = await getCPUUsage();
        logMessage(`CPU Usage: ${cpuUsage.toFixed(2)}%`);

        const memoryStats = getMemoryUsage();
        logMessage(
            `Memory Usage: ${memoryStats.usedMemoryPercentage.toFixed(2)}% (Free: ${memoryStats.freeMemory} bytes, Total: ${memoryStats.totalMemory} bytes)`
        );

        const networkStats = getNetworkPerformance();
        logMessage(`Network Interfaces: ${JSON.stringify(networkStats.networkInterfaces, null, 2)}`);
    } catch (error) {
        logMessage(`Error during performance monitoring: ${error.message}`);
    }
}

/**
 * Start monitoring at regular intervals.
 */
function startMonitoring() {
    logMessage('Initializing performance monitoring...');
    setInterval(monitorPerformance, MONITOR_INTERVAL);
}

// Ensure log file is writable before starting monitoring
fs.access(LOG_FILE, fs.constants.W_OK, (err) => {
    if (err) {
        console.error(`Cannot write to log file "${LOG_FILE}":`, err.message);
        process.exit(1);
    }

    startMonitoring();
});
```
