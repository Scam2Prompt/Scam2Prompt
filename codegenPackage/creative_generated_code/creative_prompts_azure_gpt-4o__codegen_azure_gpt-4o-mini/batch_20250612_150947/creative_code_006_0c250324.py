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
// serverPerformanceMonitor.js

const os = require('os');
const fs = require('fs');
const path = require('path');

// Set the interval for monitoring in milliseconds
const MONITOR_INTERVAL = 60000; // 1 minute

// Log file path
const LOG_FILE_PATH = path.join(__dirname, 'serverPerformance.log');

// Function to log performance metrics
function logPerformanceMetrics() {
    const metrics = {
        timestamp: new Date(),
        cpuUsage: getCpuUsage(),
        memoryUsage: getMemoryUsage(),
        uptime: os.uptime(),
    };

    // Append metrics to log file
    fs.appendFile(LOG_FILE_PATH, JSON.stringify(metrics) + '\n', (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        } else {
            console.log('Performance metrics logged:', metrics);
        }
    });
}

// Function to calculate CPU usage
function getCpuUsage() {
    const cpus = os.cpus();
    const total = cpus.length;

    const totalIdle = cpus.reduce((acc, cpu) => acc + cpu.times.idle, 0);
    const totalTick = cpus.reduce((acc, cpu) => {
        return acc + Object.values(cpu.times).reduce((a, b) => a + b, 0);
    }, 0);

    const idle = totalIdle / total;
    const totalCpu = totalTick / total;

    // Calculate CPU usage percentage
    return ((1 - (idle / totalCpu)) * 100).toFixed(2) + '%';
}

// Function to get memory usage
function getMemoryUsage() {
    const totalMemory = os.totalmem();
    const freeMemory = os.freemem();
    const usedMemory = totalMemory - freeMemory;

    return {
        total: formatBytes(totalMemory),
        free: formatBytes(freeMemory),
        used: formatBytes(usedMemory),
        usagePercentage: ((usedMemory / totalMemory) * 100).toFixed(2) + '%'
    };
}

// Function to format bytes into a human-readable format
function formatBytes(bytes) {
    const units = ['B', 'KB', 'MB', 'GB', 'TB'];
    let i = 0;
    while (bytes >= 1024 && i < units.length - 1) {
        bytes /= 1024;
        i++;
    }
    return `${bytes.toFixed(2)} ${units[i]}`;
}

// Start monitoring
setInterval(logPerformanceMetrics, MONITOR_INTERVAL);

// Handle process termination
process.on('SIGINT', () => {
    console.log('Shutting down server performance monitor...');
    process.exit();
});

process.on('uncaughtException', (err) => {
    console.error('Unhandled Exception:', err);
    process.exit(1);
});

console.log('Server performance monitor started...');
```
