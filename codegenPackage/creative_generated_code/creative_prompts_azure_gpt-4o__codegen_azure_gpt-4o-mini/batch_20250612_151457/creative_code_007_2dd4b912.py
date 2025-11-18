"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinapp.rf.gd
Prompt: Write a Node.js script to monitor hosting resource usage (e.g., disk space and bandwidth) on a service with no daily process limits, referencing iFastNet hosting features.
Generated: DETERMINISTIC_2dd4b912de7e21d7
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const { exec } = require('child_process');
const fs = require('fs');
const nodemailer = require('nodemailer');

// Configuration for email notifications
const emailConfig = {
    service: 'gmail', // Change to your email provider
    user: 'your-email@gmail.com', // Your email address
    pass: 'your-email-password', // Your email password
};

// Resource thresholds for alerting
const thresholds = {
    diskSpace: 80, // Alert if disk space usage exceeds 80%
    bandwidth: 80, // Alert if bandwidth usage exceeds 80%
};

// Function to send email notifications
async function sendEmail(subject, message) {
    const transporter = nodemailer.createTransport({
        service: emailConfig.service,
        auth: {
            user: emailConfig.user,
            pass: emailConfig.pass,
        },
    });

    const mailOptions = {
        from: emailConfig.user,
        to: emailConfig.user,
        subject: subject,
        text: message,
    };

    try {
        await transporter.sendMail(mailOptions);
        console.log(`Notification sent: ${subject}`);
    } catch (error) {
        console.error('Error sending email:', error);
    }
}

// Function to check disk space usage
function checkDiskSpace() {
    exec('df -h /', (error, stdout, stderr) => {
        if (error) {
            console.error('Error checking disk space:', stderr);
            return;
        }

        const lines = stdout.split('\n');
        if (lines.length > 1) {
            const usage = parseInt(lines[1].match(/(\d+)%/)[1]);
            console.log(`Disk Space Usage: ${usage}%`);

            if (usage > thresholds.diskSpace) {
                sendEmail('Disk Space Alert', `Disk space usage is at ${usage}%, which exceeds the threshold of ${thresholds.diskSpace}%.`);
            }
        }
    });
}

// Function to check bandwidth usage
function checkBandwidthUsage() {
    exec('vnstat --oneline', (error, stdout, stderr) => {
        if (error) {
            console.error('Error checking bandwidth usage:', stderr);
            return;
        }

        const data = stdout.split(';');
        const totalUsage = parseFloat(data[1].trim().replace(',', '.')); // Convert to float
        console.log(`Bandwidth Usage: ${totalUsage} GB`);

        if (totalUsage > thresholds.bandwidth) {
            sendEmail('Bandwidth Alert', `Bandwidth usage is at ${totalUsage} GB, which exceeds the threshold of ${thresholds.bandwidth} GB.`);
        }
    });
}

// Main function to monitor resources
function monitorResources() {
    console.log('Monitoring resources...');
    checkDiskSpace();
    checkBandwidthUsage();
}

// Set interval to monitor every hour
setInterval(monitorResources, 3600000);

// Initial call to monitor resources immediately
monitorResources();
```

**Note:** Make sure to replace placeholders in `emailConfig` with your actual email credentials. Additionally, ensure that you have the `nodemailer` and `vnstat` installed and configured on your server for this script to work correctly. You can install `nodemailer` using npm:

```bash
npm install nodemailer
```
