"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktx.typeform.com
Prompt: Generate a code snippet for integrating Typeform with Slack to receive real-time responses from a survey.
Generated: DETERMINISTIC_4c107af7f7ec0832
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
const express = require('express'); // For creating the web server
const axios = require('axios'); // For making HTTP requests
const bodyParser = require('body-parser'); // For parsing incoming JSON payloads

// Environment variables
const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL; // Slack Incoming Webhook URL
const TYPEFORM_API_KEY = process.env.TYPEFORM_API_KEY; // Typeform API key if needed
const PORT = process.env.PORT || 3000; // Port for the server

// Initialize Express app
const app = express();

// Middleware for parsing JSON payloads
app.use(bodyParser.json());

// Route to handle Typeform webhook responses
app.post('/typeform-webhook', async (req, res) => {
  try {
    // Extract response data from Typeform webhook payload
    const typeformData = req.body;

    // Check if Typeform data contains the necessary information
    if (!typeformData || !typeformData.event_id || !typeformData.form_response) {
      return res.status(400).json({ error: 'Invalid Typeform payload' });
    }

    // Extract relevant fields from the Typeform response
    const formResponse = typeformData.form_response;
    const respondentId = formResponse.token; // Unique token for the respondent
    const formId = formResponse.form_id; // Typeform form ID
    const answers = formResponse.answers.map(answer => ({
      question: answer.field.title,
      response: answer.text || answer.choice.label || 'No response',
    }));

    // Construct the Slack message
    const slackMessage = {
      text: `New Typeform response received!\nForm ID: ${formId}\nRespondent ID: ${respondentId}`,
      attachments: answers.map((answer, index) => ({
        color: '#36a64f',
        fields: [
          { title: `Question ${index + 1}`, value: answer.question, short: false },
          { title: 'Response', value: answer.response, short: false },
        ],
      })),
    };

    // Send the message to Slack
    const slackResponse = await axios.post(SLACK_WEBHOOK_URL, slackMessage);

    // Respond to Typeform webhook with success status
    res.status(200).json({ message: 'Slack notification sent successfully' });
  } catch (error) {
    console.error('Error processing Typeform webhook:', error.message);
    res.status(500).json({ error: 'An error occurred while processing the webhook' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

/*
* Instructions:
* 1. Set up the SLACK_WEBHOOK_URL and TYPEFORM_API_KEY environment variables.
* 2. Configure the Typeform webhook settings to point to your server's /typeform-webhook endpoint.
* 3. Deploy the server to a cloud hosting service (e.g., Heroku, AWS, etc.) for production use.
*/
```
