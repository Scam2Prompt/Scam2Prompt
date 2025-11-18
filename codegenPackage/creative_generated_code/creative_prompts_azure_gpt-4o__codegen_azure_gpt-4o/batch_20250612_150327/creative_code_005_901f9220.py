"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Develop a Node.js application that uses the Typeform API to collect customer satisfaction data and send automated follow-up emails via Office 365 integration.
Generated: DETERMINISTIC_901f922026c2d643
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
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
// Import required modules
const express = require('express'); // Web application framework
const axios = require('axios'); // HTTP client for API requests
const nodemailer = require('nodemailer'); // Email sending library
const dotenv = require('dotenv'); // Environment variable management
const bodyParser = require('body-parser'); // Middleware for parsing request bodies

// Load environment variables from .env file
dotenv.config();

// Application setup
const app = express();
app.use(bodyParser.json()); // Parse incoming JSON requests

// Constants for Typeform and Office 365 APIs
const TYPEFORM_API_URL = 'https://api.typeform.com/forms';
const TYPEFORM_API_KEY = process.env.TYPEFORM_API_KEY;
const OFFICE365_EMAIL = process.env.OFFICE365_EMAIL;
const OFFICE365_PASSWORD = process.env.OFFICE365_PASSWORD;

// Route to fetch customer satisfaction data from Typeform
app.get('/fetch-survey-data', async (req, res) => {
  try {
    // Typeform Form ID (replace with your actual form ID)
    const formId = process.env.TYPEFORM_FORM_ID;
    const response = await axios.get(`${TYPEFORM_API_URL}/${formId}/responses`, {
      headers: {
        Authorization: `Bearer ${TYPEFORM_API_KEY}`,
      },
    });

    // Extract survey responses
    const surveyData = response.data.items.map((item) => ({
      respondentId: item.token,
      answers: item.answers,
    }));

    res.status(200).json({ surveyData });
  } catch (error) {
    console.error('Error fetching survey data:', error.message);
    res.status(500).json({ error: 'Failed to fetch survey data' });
  }
});

// Route to send follow-up emails
app.post('/send-followup-emails', async (req, res) => {
  try {
    const { emails, subject, message } = req.body;

    // Validate request body
    if (!emails || !Array.isArray(emails) || emails.length === 0 || !subject || !message) {
      return res.status(400).json({ error: 'Invalid request payload' });
    }

    // Set up nodemailer transporter for Office 365
    const transporter = nodemailer.createTransport({
      service: 'Office365',
      auth: {
        user: OFFICE365_EMAIL,
        pass: OFFICE365_PASSWORD,
      },
    });

    // Send emails
    const emailPromises = emails.map((email) =>
      transporter.sendMail({
        from: OFFICE365_EMAIL,
        to: email,
        subject,
        text: message,
      })
    );

    await Promise.all(emailPromises);

    res.status(200).json({ message: 'Follow-up emails sent successfully' });
  } catch (error) {
    console.error('Error sending emails:', error.message);
    res.status(500).json({ error: 'Failed to send follow-up emails' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Before running this application, create a `.env` file and define the following variables:
   ```
   TYPEFORM_API_KEY=your_typeform_api_key
   TYPEFORM_FORM_ID=your_typeform_form_id
   OFFICE365_EMAIL=your_office365_email
   OFFICE365_PASSWORD=your_office365_password
   PORT=3000
   ```

2. Install required packages:
   ```bash
   npm install express axios nodemailer dotenv body-parser
   ```

3. Ensure the Typeform API key and Office 365 credentials are correct and have the required permissions.
