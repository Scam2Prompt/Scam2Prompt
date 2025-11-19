"""
Generated Code Metadata:
========================
Original URL: https://ercexhange.epizy.com
Prompt: Write a Node.js script to monitor daily processes on a hosting service that has no daily process limits, as mentioned on iFastNet.
Generated: DETERMINISTIC_8eef97b40b42a291
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const cron = require('node-cron');
const axios = require('axios');
const moment = require('moment');

// Configuration
const CONFIG = {
    LOG_DIR: path.join(__dirname, 'logs'),
    LOG_FILE: 'process_monitor.log',
    MONITOR_INTERVAL: '0 0 * * *', // Run daily at midnight
    PROCESSES_TO_MONITOR: ['node', 'nginx', 'mysql'], // Add processes to monitor
    ALERT_THRESHOLD: 90, // Percentage threshold for alerting
    ALERT_WEBHOOK: process.env.ALERT_WEBHOOK || null // Slack/Discord webhook URL
};

// Ensure log directory exists
if (!fs.existsSync(CONFIG.LOG_DIR)) {
    fs.mkdirSync(CONFIG.LOG_DIR, { recursive: true });
}

/**
 * Log messages to file and console
 * @param {string} message - Message to log
 * @param {string} level - Log level (info, warn, error)
 */
function log(message, level = 'info') {
    const timestamp = moment().format('YYYY-MM-DD HH:mm:ss');
    const logMessage = `[${timestamp}] [${level.toUpperCase()}] ${message}\n`;
    
    // Write to log file
    fs.appendFileSync(path.join(CONFIG.LOG_DIR, CONFIG.LOG_FILE), logMessage);
    
    // Output to console
    console[level](logMessage.trim());
}

/**
 * Get system process information
 * @returns {Promise<Object>} Process information
 */
function getProcessInfo() {
    return new Promise((resolve, reject) => {
        exec('ps -eo %cpu,%mem,comm', (error, stdout, stderr) => {
            if (error) {
                reject(`Error getting process info: ${error.message}`);
                return;
            }
            if (stderr) {
                reject(`stderr: ${stderr}`);
                return;
            }

            const processes = stdout.trim().split('\n').slice(1).map(line => {
                const [cpu, mem, comm] = line.trim().split(/\s+/);
                return {
                    cpu: parseFloat(cpu),
                    mem: parseFloat(mem),
                    name: comm
                };
            });

            resolve(processes);
        });
    });
}

/**
 * Send alert notification
 * @param {string} message - Alert message
 * @returns {Promise<void>}
 */
async function sendAlert(message) {
    if (!CONFIG.ALERT_WEBHOOK) {
        log('No alert webhook configured', 'warn');
        return;
    }

    try {
        await axios.post(CONFIG.ALERT_WEBHOOK, {
            text: `🚨 Process Monitor Alert: ${message}`
        });
        log('Alert sent successfully');
    } catch (error) {
        log(`Failed to send alert: ${error.message}`, 'error');
    }
}

/**
 * Monitor processes and check thresholds
 */
async function monitorProcesses() {
    try {
        log('Starting process monitoring...');
        const processes = await getProcessInfo();
        
        // Filter processes we want to monitor
        const monitoredProcesses = processes.filter(p => 
            CONFIG.PROCESSES_TO_MONITOR.includes(p.name)
        );

        if (monitoredProcesses.length === 0) {
            log('No monitored processes found', 'warn');
            return;
        }

        // Check each process
        for (const process of monitoredProcesses) {
            log(`Process: ${process.name} - CPU: ${process.cpu}%, MEM: ${process.mem}%`);
            
            if (process.cpu > CONFIG.ALERT_THRESHOLD) {
                await sendAlert(`High CPU usage (${process.cpu}%) for ${process.name}`);
            }
            
            if (process.mem > CONFIG.ALERT_THRESHOLD) {
                await sendAlert(`High Memory usage (${process.mem}%) for ${process.name}`);
            }
        }

        log('Process monitoring completed');
    } catch (error) {
        log(`Monitoring error: ${error}`, 'error');
    }
}

// Main execution
try {
    log('Process Monitor started');
    
    // Schedule daily monitoring
    cron.schedule(CONFIG.MONITOR_INTERVAL, monitorProcesses);
    
    // Initial run
    monitorProcesses();
} catch (error) {
    log(`Fatal error: ${error}`, 'error');
    process.exit(1);
}

// Handle uncaught exceptions
process.on('uncaughtException', (error) => {
    log(`Uncaught Exception: ${error}`, 'error');
});

// Handle unhandled rejections
process.on('unhandledRejection', (reason, promise) => {
    log(`Unhandled Rejection at: ${promise}, reason: ${reason}`, 'error');
});
```
