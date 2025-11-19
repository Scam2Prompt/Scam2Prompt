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
const os = require('os');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const moment = require('moment');
const pidusage = require('pidusage');

// Configuration
const LOG_DIRECTORY = './server_monitor_logs';
const LOG_INTERVAL_MS = 60000; // 1 minute
const MAX_LOG_FILES = 30; // Keep last 30 log files
const LOG_FILE_PREFIX = 'server_monitor_';

// Ensure log directory exists
if (!fs.existsSync(LOG_DIRECTORY)) {
    fs.mkdirSync(LOG_DIRECTORY, { recursive: true });
}

/**
 * Get current server performance metrics
 * @returns {Promise<Object>} Performance metrics
 */
async function getPerformanceMetrics() {
    try {
        // Get CPU usage
        const cpuUsage = os.loadavg()[0]; // 1-minute load average
        const cpuCores = os.cpus().length;
        
        // Get memory usage
        const totalMem = os.totalmem();
        const freeMem = os.freemem();
        const usedMem = totalMem - freeMem;
        const memUsagePercent = (usedMem / totalMem) * 100;
        
        // Get disk usage
        const diskStats = await new Promise((resolve, reject) => {
            exec('df -k /', (error, stdout) => {
                if (error) reject(error);
                const lines = stdout.trim().split('\n');
                const values = lines[1].split(/\s+/);
                resolve({
                    total: parseInt(values[1]) * 1024,
                    used: parseInt(values[2]) * 1024,
                    free: parseInt(values[3]) * 1024,
                    percent: parseInt(values[4])
                });
            });
        });
        
        // Get process stats
        const processStats = await pidusage(process.pid);
        
        return {
            timestamp: new Date().toISOString(),
            cpu: {
                load: cpuUsage,
                cores: cpuCores,
                usagePercent: processStats.cpu
            },
            memory: {
                total: totalMem,
                used: usedMem,
                free: freeMem,
                usagePercent: memUsagePercent,
                processUsage: processStats.memory
            },
            disk: diskStats,
            uptime: os.uptime(),
            processUptime: process.uptime()
        };
    } catch (error) {
        console.error('Error collecting performance metrics:', error);
        throw error;
    }
}

/**
 * Log performance metrics to file
 * @param {Object} metrics Performance metrics
 */
function logMetrics(metrics) {
    try {
        const timestamp = moment().format('YYYYMMDD_HHmmss');
        const logFileName = path.join(LOG_DIRECTORY, `${LOG_FILE_PREFIX}${timestamp}.json`);
        
        fs.writeFileSync(logFileName, JSON.stringify(metrics, null, 2));
        console.log(`Metrics logged to ${logFileName}`);
        
        // Clean up old log files
        const logFiles = fs.readdirSync(LOG_DIRECTORY)
            .filter(file => file.startsWith(LOG_FILE_PREFIX))
            .sort()
            .reverse();
        
        if (logFiles.length > MAX_LOG_FILES) {
            const filesToDelete = logFiles.slice(MAX_LOG_FILES);
            filesToDelete.forEach(file => {
                fs.unlinkSync(path.join(LOG_DIRECTORY, file));
                console.log(`Deleted old log file: ${file}`);
            });
        }
    } catch (error) {
        console.error('Error logging metrics:', error);
    }
}

/**
 * Main monitoring function
 */
async function monitorServer() {
    try {
        console.log('Starting server performance monitoring...');
        
        // Initial metrics collection
        const metrics = await getPerformanceMetrics();
        logMetrics(metrics);
        
        // Set up periodic monitoring
        setInterval(async () => {
            try {
                const metrics = await getPerformanceMetrics();
                logMetrics(metrics);
            } catch (error) {
                console.error('Error during periodic monitoring:', error);
            }
        }, LOG_INTERVAL_MS);
        
    } catch (error) {
        console.error('Failed to start server monitoring:', error);
        process.exit(1);
    }
}

// Start monitoring
monitorServer();

// Handle process termination
process.on('SIGINT', () => {
    console.log('\nServer monitoring stopped by user');
    process.exit();
});

process.on('uncaughtException', (error) => {
    console.error('Uncaught exception:', error);
    process.exit(1);
});

process.on('unhandledRejection', (error) => {
    console.error('Unhandled rejection:', error);
    process.exit(1);
});
```
