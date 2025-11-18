"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Provide an example of how to use Typeform's API to embed a video quiz into a website and collect user responses.
Generated: DETERMINISTIC_13cae6109da31298
Batch ID: 20250612_151912
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://form.typeform.com/${formId}`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://form.typeform.com/your_form_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.typeform.com/forms/${formId}/responses`;": {
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
const axios = require('axios'); // Axios for making HTTP requests

// Typeform API credentials (replace with your actual API key)
const TYPEFORM_API_KEY = 'your_typeform_api_key';

// Typeform form ID (replace with your actual form ID)
const TYPEFORM_FORM_ID = 'your_form_id';

// Function to create a Typeform embed URL
function generateTypeformEmbedUrl(formId) {
  // Base embed URL for Typeform
  const BASE_EMBED_URL = `https://form.typeform.com/${formId}`;

  // Return the full embed URL
  return BASE_EMBED_URL;
}

// Function to fetch responses from the Typeform API
async function fetchTypeformResponses(formId) {
  try {
    // Typeform API endpoint for retrieving responses
    const url = `https://api.typeform.com/forms/${formId}/responses`;

    // Make GET request to Typeform API
    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${TYPEFORM_API_KEY}`, // Provide API key for authentication
      },
    });

    // Return the retrieved responses
    return response.data.items;
  } catch (error) {
    // Handle errors (e.g., network issues, invalid form ID/API key)
    console.error('Error fetching Typeform responses:', error.message);
    throw new Error('Failed to fetch responses from Typeform API.');
  }
}

// Example usage of the above functions
(async () => {
  try {
    // Generate Typeform embed URL
    const embedUrl = generateTypeformEmbedUrl(TYPEFORM_FORM_ID);

    // Log embed URL
    console.log('Embed this URL into your website:', embedUrl);

    // Fetch user responses
    const responses = await fetchTypeformResponses(TYPEFORM_FORM_ID);

    // Log user responses
    console.log('Collected User Responses:', responses);
  } catch (error) {
    // Handle any errors during the process
    console.error('An error occurred:', error.message);
  }
})();
```

**Instructions for embedding the Typeform form into a website:**
1. Copy the generated `embedUrl` from the console output.
2. Use the URL to embed the form into your HTML page using an `<iframe>` tag:
```html
<iframe 
  src="https://form.typeform.com/your_form_id" 
  width="100%" 
  height="500px" 
  frameborder="0">
</iframe>
```
