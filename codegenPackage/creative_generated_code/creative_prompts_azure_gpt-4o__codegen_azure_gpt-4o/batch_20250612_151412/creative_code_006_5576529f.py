"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revcke.cash
Prompt: Develop a script using Node.js to automate the process of switching domain nameservers to Hostinger's nameservers.
Generated: DETERMINISTIC_5576529f9308381b
Batch ID: 20250612_151412
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.domainprovider.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.domainprovider.com/v1`": {
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
// File: changeNameservers.js

// Import required modules
const axios = require('axios'); // For making API requests
const dotenv = require('dotenv'); // For securely managing environment variables

// Load environment variables from a .env file
dotenv.config();

// Configuration for the script
const config = {
  apiBaseUrl: 'https://api.domainprovider.com/v1', // Replace with your domain registrar's API base URL
  hostingerNameservers: [
    'ns1.dns-parking.com',
    'ns2.dns-parking.com',
  ],
  domainName: process.env.DOMAIN_NAME, // Domain name to modify, e.g., 'example.com'
  apiKey: process.env.API_KEY, // API key for authenticating requests
};

// Helper function to log errors and exit
function handleError(error) {
  console.error('An error occurred:', error.message || error);
  process.exit(1); // Exit the script with a failure code
}

// Function to change nameservers
async function changeNameservers(domainName, newNameservers) {
  try {
    console.log(`Starting nameserver update for domain: ${domainName}`);

    // Construct the API request payload
    const payload = {
      nameservers: newNameservers,
    };

    // Make an API request to update nameservers
    const response = await axios.put(
      `${config.apiBaseUrl}/domains/${domainName}/nameservers`,
      payload,
      {
        headers: {
          Authorization: `Bearer ${config.apiKey}`,
          'Content-Type': 'application/json',
        },
      }
    );

    // Check if the request was successful
    if (response.status === 200) {
      console.log(`Successfully updated nameservers for ${domainName}.`);
    } else {
      throw new Error(
        `Unexpected response status: ${response.status} - ${response.data}`
      );
    }
  } catch (error) {
    // Handle any errors that occur during the API request
    handleError(error);
  }
}

// Main function to initiate nameserver update
async function main() {
  // Validate required environment variables
  if (!config.domainName || !config.apiKey) {
    console.error(
      'Missing required configuration. Ensure DOMAIN_NAME and API_KEY are defined in your .env file.'
    );
    process.exit(1);
  }

  // Change nameservers for the specified domain
  await changeNameservers(config.domainName, config.hostingerNameservers);
}

// Run the script
main();
```

---

**Instructions:**
1. Save this script to a file named `changeNameservers.js`.
2. Create a `.env` file in the same directory with the following variables:
   ```
   DOMAIN_NAME=your-domain.com
   API_KEY=your-api-key
   ```
3. Run the script using `node changeNameservers.js`.

**Important:** Replace `https://api.domainprovider.com/v1` with the actual API base URL provided by your domain registrar. Ensure the registrar's API supports nameserver updates, and consult their API documentation for proper endpoints and payload formats.
