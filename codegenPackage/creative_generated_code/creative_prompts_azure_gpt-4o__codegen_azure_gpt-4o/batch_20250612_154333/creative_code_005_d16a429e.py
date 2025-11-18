"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusiiiuatapi.azurewebsites.net
Prompt: Create a function in Node.js to interact with the Exodus III login API, including error handling for incorrect credentials.
Generated: DETERMINISTIC_d16a429eb2375515
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const axios = require('axios');

/**
 * Function to interact with the Exodus III login API.
 * @param {string} apiUrl - The URL of the Exodus III login API.
 * @param {string} username - The username for login.
 * @param {string} password - The password for login.
 * @returns {Promise<Object>} - A promise that resolves to the login response data or rejects with an error.
 */
async function loginToExodusIII(apiUrl, username, password) {
  try {
    // Validate input parameters
    if (!apiUrl || !username || !password) {
      throw new Error('Missing required parameters: apiUrl, username, or password.');
    }

    // Prepare the request payload
    const payload = {
      username,
      password
    };

    // Make the POST request to the login API
    const response = await axios.post(apiUrl, payload, {
      headers: {
        'Content-Type': 'application/json' // Ensure the request uses the correct content type
      }
    });

    // Check if the response status indicates a successful login
    if (response.status === 200 && response.data.success) {
      // Return the response data on successful login
      return response.data;
    } else {
      // Handle unsuccessful login attempts
      throw new Error(response.data.message || 'Login failed.');
    }
  } catch (error) {
    // Handle errors and provide meaningful messages
    if (error.response) {
      // API responded with a status code outside the 2xx range
      throw new Error(`API Error: ${error.response.data.message || 'Unknown error occurred.'}`);
    } else if (error.request) {
      // No response received from the API
      throw new Error('No response received from the API. Please check the API URL or your network connection.');
    } else {
      // Other errors (e.g., input validation, payload formatting)
      throw new Error(`Error: ${error.message}`);
    }
  }
}

// Export the function for use in other parts of the application
module.exports = loginToExodusIII;
```
