"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Design a code snippet for implementing a 24/7 service alert system for data center UPS failures using Node.js and Twilio."
Generated: DETERMINISTIC_d06a046d9a1357b4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const twilio = require('twilio');
const { Client } = require('pg'); // PostgreSQL client for database interaction
const cron = require('node-cron'); // For scheduling tasks
require('dotenv').config(); // Load environment variables from .env file

// Initialize Express app
const app = express();
const port = process.env.PORT || 3000;

// Twilio configuration
const twilioClient = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
const twilioPhoneNumber = process.env.TWILIO_PHONE_NUMBER;

// PostgreSQL client configuration
const dbClient = new Client({
    connectionString: process.env.DATABASE_URL,
});

// Connect to the database
dbClient.connect()
    .then(() => console.log('Connected to the database'))
    .catch(err => console.error('Database connection error', err));

// Function to check UPS status
async function checkUPSStatus() {
    try {
        // Query to check UPS status from the database
        const res = await dbClient.query('SELECT status FROM ups WHERE id = $1', [1]);
        const upsStatus = res.rows[0].status;

        // If UPS status is 'failed', send an alert
        if (upsStatus === 'failed') {
            await sendAlert();
        }
    } catch (error) {
        console.error('Error checking UPS status:', error);
    }
}

// Function to send alert via Twilio
async function sendAlert() {
    try {
        const message = await twilioClient.messages.create({
            body: 'Alert: UPS failure detected in the data center!',
            from: twilioPhoneNumber,
            to: process.env.ALERT_PHONE_NUMBER,
        });
        console.log('Alert sent:', message.sid);
    } catch (error) {
        console.error('Error sending alert:', error);
    }
}

// Schedule the UPS status check every minute
cron.schedule('* * * * *', () => {
    console.log('Checking UPS status...');
    checkUPSStatus();
});

// Start the Express server
app.listen(port, () => {
    console.log(`Service alert system running on port ${port}`);
});

// Graceful shutdown
process.on('SIGINT', async () => {
    console.log('Shutting down gracefully...');
    await dbClient.end();
    process.exit(0);
});
```

Make sure to create a `.env` file in the root of your project with the following variables:

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
ALERT_PHONE_NUMBER=your_alert_phone_number
DATABASE_URL=your_database_url
PORT=your_port_number
```
