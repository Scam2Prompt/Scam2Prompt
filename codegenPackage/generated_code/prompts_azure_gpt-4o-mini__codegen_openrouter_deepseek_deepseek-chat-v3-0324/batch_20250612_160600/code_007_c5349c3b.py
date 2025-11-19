"""
Generated Code Metadata:
========================
Original URL: https://originprotocol.typeform.com
Prompt: How can I utilize Typeform templates for lead generation? Provide a detailed example of a lead gen form setup.
Generated: DETERMINISTIC_c5349c3b985702c5
Batch ID: 20250612_160600
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com/webhooks/typeform": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/themes/6ZJ4L9": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

// Typeform API configuration
const TYPEFORM_API_KEY = 'your_typeform_api_key';
const TYPEFORM_API_BASE_URL = 'https://api.typeform.com';

// Create Typeform client
const typeformClient = axios.create({
  baseURL: TYPEFORM_API_BASE_URL,
  headers: {
    'Authorization': `Bearer ${TYPEFORM_API_KEY}`,
    'Content-Type': 'application/json'
  }
});

/**
 * Lead generation form template structure
 */
const leadGenFormTemplate = {
  title: 'Lead Generation Form',
  fields: [
    {
      title: 'What is your name?',
      type: 'short_text',
      validations: { required: true }
    },
    {
      title: 'What is your email address?',
      type: 'email',
      validations: { required: true }
    },
    {
      title: 'What is your phone number?',
      type: 'phone_number',
      validations: { required: false }
    },
    {
      title: 'What is your company name?',
      type: 'short_text',
      validations: { required: false }
    },
    {
      title: 'How can we help you?',
      type: 'multiple_choice',
      properties: {
        choices: [
          { label: 'Product demo' },
          { label: 'Pricing information' },
          { label: 'Technical support' },
          { label: 'Other' }
        ]
      },
      validations: { required: true }
    },
    {
      title: 'Any additional comments?',
      type: 'long_text',
      validations: { required: false }
    }
  ],
  settings: {
    is_public: true,
    language: 'en',
    progress_bar: 'percentage',
    show_progress_bar: true,
    show_typeform_branding: false,
    meta: {
      allow_indexing: false
    }
  },
  theme: {
    href: 'https://api.typeform.com/themes/6ZJ4L9'
  }
};

/**
 * Creates a new Typeform using the lead generation template
 * @returns {Promise<Object>} Created form data
 */
async function createLeadGenForm() {
  try {
    const response = await typeformClient.post('/forms', leadGenFormTemplate);
    return response.data;
  } catch (error) {
    console.error('Error creating Typeform:', error.response?.data || error.message);
    throw new Error('Failed to create lead generation form');
  }
}

/**
 * Handles form submission webhook
 * @param {Object} submissionData - Form submission data
 */
async function handleFormSubmission(submissionData) {
  try {
    // Process the lead data (e.g., save to CRM, send email, etc.)
    console.log('New lead captured:', {
      name: submissionData.answers.find(a => a.field.title === 'What is your name?')?.text,
      email: submissionData.answers.find(a => a.field.title === 'What is your email address?')?.email,
      phone: submissionData.answers.find(a => a.field.title === 'What is your phone number?')?.phone_number,
      company: submissionData.answers.find(a => a.field.title === 'What is your company name?')?.text,
      interest: submissionData.answers.find(a => a.field.title === 'How can we help you?')?.choice.label,
      comments: submissionData.answers.find(a => a.field.title === 'Any additional comments?')?.text
    });

    // Example: Send data to CRM
    // await sendToCRM(submissionData);
  } catch (error) {
    console.error('Error processing form submission:', error);
    throw new Error('Failed to process form submission');
  }
}

/**
 * Sets up a webhook for form submissions
 * @param {string} formId - Typeform form ID
 * @param {string} webhookUrl - Your webhook endpoint URL
 */
async function setupFormWebhook(formId, webhookUrl) {
  try {
    const webhookId = uuidv4();
    const response = await typeformClient.put(
      `/forms/${formId}/webhooks/${webhookId}`,
      {
        url: webhookUrl,
        enabled: true,
        secret: 'your_webhook_secret' // For verifying webhook requests
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error setting up webhook:', error.response?.data || error.message);
    throw new Error('Failed to setup form webhook');
  }
}

// Example usage
(async () => {
  try {
    // Create the form
    const form = await createLeadGenForm();
    console.log('Form created:', form._links.display);
    
    // Set up webhook (replace with your actual webhook URL)
    await setupFormWebhook(form.id, 'https://yourdomain.com/webhooks/typeform');
    console.log('Webhook setup complete');
  } catch (error) {
    console.error('Lead generation setup failed:', error.message);
  }
})();

// Example webhook handler (Express.js route)
/*
const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhooks/typeform', (req, res) => {
  try {
    // Verify webhook secret if needed
    if (req.headers['typeform-signature'] !== expectedSignature) {
      return res.status(403).send('Invalid signature');
    }
    
    // Process the form submission
    handleFormSubmission(req.body.form_response);
    res.status(200).send('OK');
  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).send('Error processing webhook');
  }
});

app.listen(3000, () => console.log('Webhook server running on port 3000'));
*/
```
