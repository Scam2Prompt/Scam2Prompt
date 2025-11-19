"""
Generated Code Metadata:
========================
Original URL: https://anatomiaairdrop.typeform.com
Prompt: Develop an employee onboarding form using Typeform's form builder, integrating it with Slack for notification.
Generated: DETERMINISTIC_92f95b11dbf06d80
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming request bodies
app.use(bodyParser.json());

// Typeform webhook endpoint to receive form submissions
app.post('/webhook/typeform', async (req, res) => {
    try {
        // Validate the request body
        if (!req.body || !req.body.form_response) {
            return res.status(400).send('Invalid request body');
        }

        // Extract relevant data from the Typeform response
        const { form_response } = req.body;
        const employeeData = form_response.answers.map(answer => {
            return {
                id: answer.id,
                type: answer.type,
                text: answer.text || answer.email || answer.number
            };
        });

        // Prepare the message for Slack
        const slackMessage = {
            text: `New Employee Onboarding Submission:\n${JSON.stringify(employeeData, null, 2)}`,
        };

        // Send notification to Slack
        const slackWebhookUrl = process.env.SLACK_WEBHOOK_URL; // Ensure this is set in your environment variables
        await axios.post(slackWebhookUrl, slackMessage);

        // Respond to Typeform to acknowledge receipt
        res.status(200).send('Webhook received and processed');
    } catch (error) {
        console.error('Error processing Typeform webhook:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Environment Variables
Make sure to set the following environment variable before running the application:
- `SLACK_WEBHOOK_URL`: The incoming webhook URL for your Slack channel.

### Dependencies
To run this code, ensure you have the following dependencies installed:
```bash
npm install express body-parser axios
```

### Running the Application
You can start the application by running:
```bash
node app.js
```

### Note
This code assumes that you have set up a Typeform webhook to point to the `/webhook/typeform` endpoint of your application.
