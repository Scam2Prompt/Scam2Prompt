"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercexhange.epizy.com
Prompt: Write a Node.js script to monitor daily processes on a hosting service that has no daily process limits, as mentioned on iFastNet.
Generated: DETERMINISTIC_8eef97b40b42a291
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const fs = require('fs');
const path = require('path');
const os = require('os');
const { exec } = require('child_process');

// Configuration constants
const LOG_DIR = path.join(__dirname, 'logs');
const LOG_FILE = path.join(LOG_DIR, `daily_process_log_${new Date().toISOString().split('T')[0]}.log`);
const CHECK_INTERVAL = 60 * 60 * 1000; // Check every hour
const MAX_LOG_SIZE_MB = 5;

/**
 * Ensure the logs directory exists.
 */
function ensureLogDirectory() {
  if (!fs.existsSync(LOG_DIR)) {
    fs.mkdirSync(LOG_DIR, { recursive: true });
  }
}

/**
 * Log a message to the console and file.
 * @param {string} message - The message to log.
 */
function logMessage(message) {
  const timestamp = new Date().toISOString();
  const logEntry = `[${timestamp}] ${message}\n`;

  console.log(logEntry);

  // Write log to file
  fs.appendFile(LOG_FILE, logEntry, (err) => {
    if (err) {
      console.error(`[ERROR] Failed to write to log file: ${err.message}`);
    }
  });
}

/**
 * Check the log file size and rotate if necessary.
 */
function rotateLogs() {
  fs.stat(LOG_FILE, (err, stats) => {
    if (err && err.code !== 'ENOENT') {
      console.error(`[ERROR] Failed to check log file size: ${err.message}`);
      return;
    }

    if (stats && stats.size > MAX_LOG_SIZE_MB * 1024 * 1024) {
      const rotatedFile = `${LOG_FILE}.bak_${new Date().getTime()}`;
      fs.rename(LOG_FILE, rotatedFile, (renameErr) => {
        if (renameErr) {
          console.error(`[ERROR] Failed to rotate log file: ${renameErr.message}`);
        } else {
          logMessage(`Log file rotated. Old log file: ${rotatedFile}`);
        }
      });
    }
  });
}

/**
 * Monitor server processes and log relevant data.
 */
function monitorProcesses() {
  // Execute a shell command to list all running processes
  exec('ps -aux', (err, stdout, stderr) => {
    if (err) {
      logMessage(`[ERROR] Failed to execute process monitoring command: ${err.message}`);
      return;
    }

    if (stderr) {
      logMessage(`[ERROR] Error output from process monitoring command: ${stderr}`);
      return;
    }

    logMessage('Successfully retrieved process data.');
    logMessage(stdout);
  });

  rotateLogs(); // Ensure logs are rotated periodically
}

/**
 * Start the monitoring service.
 */
function startMonitoring() {
  ensureLogDirectory(); // Ensure the log directory exists

  logMessage('Process monitoring service started.');

  // Monitor processes at regular intervals
  setInterval(() => {
    logMessage('Starting process monitoring check...');
    monitorProcesses();
  }, CHECK_INTERVAL);
}

// Start the monitoring service
startMonitoring();
```
