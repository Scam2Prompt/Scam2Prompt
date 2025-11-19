"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Implement a monitoring script in Node.js that checks the number of peers and alerts when the queue length exceeds a certain threshold on the Arweave network.
Generated: DETERMINISTIC_6a5f85a95933a3a8
Batch ID: 20250612_160306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net/peers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const axios = require('axios'); // For making HTTP requests
const nodemailer = require('nodemailer'); // For sending email alerts
const schedule = require('node-schedule'); // For scheduling periodic checks

// Configuration for the monitoring script
const config = {
    arweaveAPI: 'https://arweave.net/peers', // Arweave API endpoint to fetch peers
    peerThreshold: 50, // Threshold for the number of peers
    alertEmail: {
        service: 'gmail', // Email service provider
        user: 'your-email@gmail.com', // Your email address
        pass: 'your-email-password' // Your email password (consider using environment variables for security)
    },
    checkInterval: '*/5 * * * *' // Cron schedule for every 5 minutes
};

// Create a transporter for sending email alerts
const transporter = nodemailer.createTransport({
    service: config.alertEmail.service,
    auth: {
        user: config.alertEmail.user,
        pass: config.alertEmail.pass
    }
});

// Function to check the number of peers on the Arweave network
async function checkPeers() {
    try {
        const response = await axios.get(config.arweaveAPI);
        const peerCount = response.data.length; // Get the number of peers from the response

        console.log(`Current number of peers: ${peerCount}`);

        // Check if the number of peers exceeds the threshold
        if (peerCount > config.peerThreshold) {
            console.warn(`Alert: Number of peers (${peerCount}) exceeded the threshold (${config.peerThreshold}).`);
            sendAlert(peerCount);
        }
    } catch (error) {
        console.error('Error fetching peer data:', error.message);
    }
}

// Function to send an alert email when the peer threshold is exceeded
function sendAlert(peerCount) {
    const mailOptions = {
        from: config.alertEmail.user,
        to: config.alertEmail.user, // Send alert to the same email
        subject: 'Arweave Network Alert',
        text: `Alert: The number of peers (${peerCount}) has exceeded the threshold (${config.peerThreshold}).`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.error('Error sending email:', error.message);
        }
        console.log('Alert email sent:', info.response);
    });
}

// Schedule the peer check at defined intervals
schedule.scheduleJob(config.checkInterval, () => {
    console.log('Checking the number of peers on the Arweave network...');
    checkPeers();
});

// Initial check on script start
checkPeers();
```
