"""
Generated Code Metadata:
========================
Original URL: https://help-community.42web.io
Prompt: Write a Node.js script to monitor daily processes on a hosting service with no daily process limit, like iFastNet.
Generated: DETERMINISTIC_901f0ce860a14879
Batch ID: 20250612_151513
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

// Configuration
const config = {
    logDirectory: './logs',
    maxLogFiles: 30,
    processesToMonitor: ['httpd', 'mysqld', 'node'], // Add processes to monitor
    checkInterval: '*/5 * * * *', // Every 5 minutes
    alertThreshold: 90, // CPU usage percentage threshold
    emailAlert: {
        enabled: false,
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-password'
        },
        to: 'admin@example.com'
    }
};

// Ensure log directory exists
if (!fs.existsSync(config.logDirectory)) {
    fs.mkdirSync(config.logDirectory, { recursive: true });
}

// Rotate logs to prevent excessive growth
function rotateLogs() {
    fs.readdir(config.logDirectory, (err, files) => {
        if (err) {
            console.error('Error reading log directory:', err);
            return;
        }

        if (files.length >= config.maxLogFiles) {
            files.sort((a, b) => {
                return fs.statSync(path.join(config.logDirectory, a)).mtime.getTime() - 
                       fs.statSync(path.join(config.logDirectory, b)).mtime.getTime();
            });

            const filesToDelete = files.length - config.maxLogFiles;
            for (let i = 0; i < filesToDelete; i++) {
                fs.unlink(path.join(config.logDirectory, files[i]), (err) => {
                    if (err) console.error('Error deleting old log file:', err);
                });
            }
        }
    });
}

// Get current timestamp for logging
function getTimestamp() {
    return new Date().toISOString();
}

// Log monitoring data
function logData(data) {
    const timestamp = getTimestamp();
    const logFile = path.join(config.logDirectory, `monitor-${new Date().toISOString().split('T')[0]}.log`);
    const logEntry = `${timestamp} - ${JSON.stringify(data)}\n`;

    fs.appendFile(logFile, logEntry, (err) => {
        if (err) console.error('Error writing to log file:', err);
    });
}

// Check system processes
function checkProcesses() {
    exec('ps aux', (error, stdout, stderr) => {
        if (error) {
            console.error('Error checking processes:', error);
            return;
        }

        const processes = stdout.split('\n');
        const monitoredProcesses = {};

        config.processesToMonitor.forEach(processName => {
            const matchingProcesses = processes.filter(line => line.includes(processName));
            monitoredProcesses[processName] = matchingProcesses.length;
        });

        // Check CPU usage
        exec("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'", 
            (cpuError, cpuStdout, cpuStderr) => {
                if (cpuError) {
                    console.error('Error checking CPU usage:', cpuError);
                    return;
                }

                const cpuUsage = parseFloat(cpuStdout.trim());
                const data = {
                    processes: monitoredProcesses,
                    cpuUsage: cpuUsage,
                    timestamp: getTimestamp()
                };

                logData(data);

                // Check for alerts
                if (cpuUsage > config.alertThreshold) {
                    const alertMessage = `High CPU usage detected: ${cpuUsage}%`;
                    console.warn(alertMessage);
                    sendAlert(alertMessage);
                }
            });
    });
}

// Send alert notification
function sendAlert(message) {
    if (!config.emailAlert.enabled) return;

    const nodemailer = require('nodemailer');
    const transporter = nodemailer.createTransport({
        service: config.emailAlert.service,
        auth: config.emailAlert.auth
    });

    const mailOptions = {
        from: config.emailAlert.auth.user,
        to: config.emailAlert.to,
        subject: 'Server Alert',
        text: message
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Error sending alert email:', error);
        } else {
            console.log('Alert email sent:', info.response);
        }
    });
}

// Main execution
console.log('Starting process monitor...');

// Schedule regular checks
cron.schedule(config.checkInterval, () => {
    checkProcesses();
    rotateLogs();
});

// Initial check
checkProcesses();

// Handle process termination
process.on('SIGINT', () => {
    console.log('Shutting down process monitor...');
    process.exit();
});
```
