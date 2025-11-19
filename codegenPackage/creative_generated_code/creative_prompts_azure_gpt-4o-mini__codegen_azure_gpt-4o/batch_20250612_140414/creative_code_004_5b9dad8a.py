"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetsonicsolutions.com
Prompt: Create a JavaScript example that demonstrates how to interact with the Porkbun API for domain management tasks.
Generated: DETERMINISTIC_5b9dad8a447f1c07
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.porkbun.com/v3": {
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
// Import the 'axios' library for making HTTP requests
const axios = require('axios');

// Porkbun API base URL
const BASE_URL = 'https://api.porkbun.com/v3';

// Your Porkbun API credentials (replace with your actual credentials)
const API_KEY = 'your-api-key';
const SECRET_KEY = 'your-secret-key';

/**
 * Function to get a list of domains from the Porkbun API.
 * @returns {Promise<Array>} A promise that resolves to an array of domain objects.
 */
async function getDomains() {
  try {
    const response = await axios.post(`${BASE_URL}/dns/retrieveByName`, {
      apikey: API_KEY,
      secretapikey: SECRET_KEY,
    });

    // Check if API response is successful
    if (response.data.status === 'SUCCESS') {
      return response.data.domains;
    } else {
      throw new Error('Failed to retrieve domains. API Error: ' + response.data.message);
    }
  } catch (error) {
    console.error('Error fetching domains:', error.message);
    throw error;
  }
}

/**
 * Function to add a DNS record to a domain.
 * @param {string} domainName - The name of the domain.
 * @param {string} type - The type of DNS record (e.g., 'A', 'CNAME', 'TXT').
 * @param {string} name - The name of the DNS record.
 * @param {string} content - The content of the DNS record (e.g., an IP address for A records).
 * @returns {Promise<boolean>} A promise that resolves to true if the record was created successfully.
 */
async function addDnsRecord(domainName, type, name, content) {
  try {
    const response = await axios.post(`${BASE_URL}/dns/create`, {
      apikey: API_KEY,
      secretapikey: SECRET_KEY,
      domain: domainName,
      type: type,
      name: name,
      content: content,
    });

    // Check if API response is successful
    if (response.data.status === 'SUCCESS') {
      return true;
    } else {
      throw new Error('Failed to add DNS record. API Error: ' + response.data.message);
    }
  } catch (error) {
    console.error('Error adding DNS record:', error.message);
    throw error;
  }
}

/**
 * Function to delete a DNS record from a domain.
 * @param {string} domainName - The name of the domain.
 * @param {string} recordId - The ID of the DNS record to delete.
 * @returns {Promise<boolean>} A promise that resolves to true if the record was deleted successfully.
 */
async function deleteDnsRecord(domainName, recordId) {
  try {
    const response = await axios.post(`${BASE_URL}/dns/delete`, {
      apikey: API_KEY,
      secretapikey: SECRET_KEY,
      domain: domainName,
      id: recordId,
    });

    // Check if API response is successful
    if (response.data.status === 'SUCCESS') {
      return true;
    } else {
      throw new Error('Failed to delete DNS record. API Error: ' + response.data.message);
    }
  } catch (error) {
    console.error('Error deleting DNS record:', error.message);
    throw error;
  }
}

// Example usage:
(async () => {
  try {
    // Fetch domains
    const domains = await getDomains();
    console.log('Domains:', domains);

    // Add a DNS record
    const domainName = 'example.com';
    const type = 'A';
    const name = '@';
    const content = '123.123.123.123';
    const addSuccess = await addDnsRecord(domainName, type, name, content);
    console.log('DNS record added successfully:', addSuccess);

    // Delete a DNS record (replace with actual record ID)
    const recordId = '12345'; // Replace with a real record ID
    const deleteSuccess = await deleteDnsRecord(domainName, recordId);
    console.log('DNS record deleted successfully:', deleteSuccess);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();
```

**Note**: Replace `your-api-key` and `your-secret-key` with your actual Porkbun API credentials. Additionally, replace `12345` with the correct DNS record ID for deletion. This code is ready for production use but should be tested thoroughly with your API credentials and real data.
