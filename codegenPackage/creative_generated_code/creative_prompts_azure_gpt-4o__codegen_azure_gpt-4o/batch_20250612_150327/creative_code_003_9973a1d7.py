"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Create a JavaScript function using the Typeform API to generate an NPS (Net Promoter Score) survey and automatically send results to Google Sheets for analysis.
Generated: DETERMINISTIC_9973a1d7a85ea318
Batch ID: 20250612_150327
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://sheets.googleapis.com/v4/spreadsheets/${GOOGLE_SHEETS_SPREADSHEET_ID}/values/${GOOGLE_SHEETS_RANGE}:append?valueInputOption=USER_ENTERED`;": {
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
/**
 * Typeform API and Google Sheets Integration for NPS Survey
 * This script generates an NPS survey using Typeform API and sends the responses
 * to a Google Sheets document for further analysis.
 */

// Import necessary libraries for HTTP requests
const axios = require('axios');

/**
 * Configuration
 * Replace the placeholders with actual API keys and IDs.
 */
const TYPEFORM_API_KEY = 'your_typeform_api_key'; // Your Typeform API key
const GOOGLE_SHEETS_API_KEY = 'your_google_sheets_api_key'; // Your Google Sheets API key
const GOOGLE_SHEETS_SPREADSHEET_ID = 'your_google_spreadsheet_id'; // ID of your Google Sheets document
const GOOGLE_SHEETS_RANGE = 'Sheet1!A1'; // Range where data will be inserted in Google Sheets

/**
 * Function to create an NPS survey using Typeform API
 * @returns {Promise<string>} The URL of the created survey
 */
async function createNPSSurvey() {
  try {
    // Typeform API endpoint for creating a form
    const url = 'https://api.typeform.com/forms';

    // NPS survey template
    const data = {
      title: 'NPS Survey',
      fields: [
        {
          type: 'opinion_scale',
          title: 'How likely are you to recommend our product or service to a friend or colleague?',
          labels: ['Not at all likely', '', '', '', '', '', '', '', '', 'Extremely likely'],
          required: true,
        },
        {
          type: 'long_text',
          title: 'What is the primary reason for your score?',
          required: false,
        },
      ],
    };

    // Send POST request to Typeform API
    const response = await axios.post(url, data, {
      headers: {
        Authorization: `Bearer ${TYPEFORM_API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    // Return the URL of the created survey
    return response.data._links.display;
  } catch (error) {
    console.error('Error creating NPS survey:', error.message);
    throw new Error('Failed to create NPS survey.');
  }
}

/**
 * Function to send survey results to Google Sheets
 * @param {Array<Object>} responses - Array of survey responses
 * @returns {Promise<void>}
 */
async function sendResultsToGoogleSheets(responses) {
  try {
    // Google Sheets API endpoint for appending data
    const url = `https://sheets.googleapis.com/v4/spreadsheets/${GOOGLE_SHEETS_SPREADSHEET_ID}/values/${GOOGLE_SHEETS_RANGE}:append?valueInputOption=USER_ENTERED`;

    // Prepare the data for insertion
    const values = responses.map(response => [
      response.score,
      response.reason || 'N/A',
    ]);

    const data = {
      values,
    };

    // Send POST request to Google Sheets API
    await axios.post(url, data, {
      headers: {
        Authorization: `Bearer ${GOOGLE_SHEETS_API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    console.log('Results successfully sent to Google Sheets.');
  } catch (error) {
    console.error('Error sending results to Google Sheets:', error.message);
    throw new Error('Failed to send results to Google Sheets.');
  }
}

/**
 * Example usage: Create survey and process responses
 */
(async () => {
  try {
    // Step 1: Create NPS survey
    const surveyUrl = await createNPSSurvey();
    console.log('NPS Survey created successfully:', surveyUrl);

    // Step 2: Simulate receiving responses (replace with actual response handling)
    const exampleResponses = [
      { score: 9, reason: 'Great customer service.' },
      { score: 6, reason: 'Product is good, but support is slow.' },
      { score: 2, reason: 'Very dissatisfied with the experience.' },
    ];

    // Step 3: Send simulated responses to Google Sheets
    await sendResultsToGoogleSheets(exampleResponses);
  } catch (error) {
    console.error('Error in survey process:', error.message);
  }
})();
```

**Note:** Ensure you have the necessary API keys and permissions configured to access Typeform and Google Sheets for this code to work.
