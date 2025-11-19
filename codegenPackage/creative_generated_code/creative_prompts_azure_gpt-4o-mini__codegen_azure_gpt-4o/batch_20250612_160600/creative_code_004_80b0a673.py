"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: What are the steps to set up a lead generation form using Typeform's templates? Include code examples for customization.
Generated: DETERMINISTIC_80b0a673e550c4f8
Batch ID: 20250612_160600
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.typeform.com/workspaces/${WORKSPACE_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms/${formId}`;": {
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
 * Typeform Lead Generation Integration Example
 * 
 * This example demonstrates how to set up a lead generation form
 * using Typeform's templates and customize it using the Typeform API.
 * 
 * Requirements:
 * - Node.js environment
 * - A Typeform account with API access
 * - Install Axios via npm for HTTP requests: `npm install axios`
 */

const axios = require("axios");

// Replace with your Typeform API token
const TYPEFORM_API_TOKEN = "your_typeform_api_token_here";

// Template ID for Lead Generation form (replace with the actual template ID from Typeform)
const TEMPLATE_ID = "template_id_here";

// Your Typeform workspace ID (use the Typeform API to find your workspace details)
const WORKSPACE_ID = "workspace_id_here";

/**
 * Create a Lead Generation form using a Typeform template.
 */
async function createLeadGenForm() {
  const url = "https://api.typeform.com/forms";

  const headers = {
    Authorization: `Bearer ${TYPEFORM_API_TOKEN}`,
    "Content-Type": "application/json",
  };

  const formData = {
    title: "Custom Lead Generation Form", // Customize the form title
    workspace: { href: `https://api.typeform.com/workspaces/${WORKSPACE_ID}` },
    fields: [
      {
        type: "short_text",
        title: "What is your name?",
        required: true,
      },
      {
        type: "email",
        title: "What is your email address?",
        required: true,
      },
      {
        type: "dropdown",
        title: "What service are you interested in?",
        choices: [{ label: "Option 1" }, { label: "Option 2" }, { label: "Option 3" }],
      },
    ],
    settings: {
      is_public: true, // Make the form public
      is_trial: false, // If you're using a trial account, set this to true
      language: "en", // Set the default language
    },
  };

  try {
    // Make the API request to create the form
    const response = await axios.post(url, formData, { headers });
    console.log("Form created successfully:", response.data);
  } catch (error) {
    console.error("Error creating the form:", error.response?.data || error.message);
  }
}

/**
 * Update a form's settings or fields using its form ID.
 * @param {string} formId The ID of the form to update.
 */
async function updateFormSettings(formId) {
  const url = `https://api.typeform.com/forms/${formId}`;

  const headers = {
    Authorization: `Bearer ${TYPEFORM_API_TOKEN}`,
    "Content-Type": "application/json",
  };

  const updateData = {
    title: "Updated Lead Generation Form Title", // Update title
    settings: {
      is_public: true, // Ensure the form is public
      show_progress_bar: true, // Enable progress bar
      show_typeform_branding: false, // Disable Typeform branding
    },
  };

  try {
    // Make the API request to update the form
    const response = await axios.put(url, updateData, { headers });
    console.log("Form updated successfully:", response.data);
  } catch (error) {
    console.error("Error updating the form:", error.response?.data || error.message);
  }
}

// Example usage:
// Step 1: Create a lead generation form
createLeadGenForm();

// Step 2: Update an existing form (replace `formId` with the actual ID)
// updateFormSettings("form_id_here");
```

This sample code demonstrates how to set up and customize a lead generation form using the Typeform API. Replace placeholder values (e.g., `your_typeform_api_token_here`) with actual values from your Typeform account. Install Axios (`npm install axios`) before running the code.
