"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Recommend a library or tool to manage domain details programmatically, ensuring compatibility with JavaScript-based applications.
Generated: DETERMINISTIC_d509452d62bb7391
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A JavaScript example to manage domain details programmatically
 * using the `whois-json` library. This library allows fetching domain information
 * and parsing it into JSON format for easy manipulation.
 *
 * Prerequisites:
 * - Install the library using: npm install whois-json
 * - Ensure Node.js environment is correctly set up
 */

// Import the required library
const whois = require('whois-json');

/**
 * Fetch domain details programmatically.
 * @param {string} domain - The domain name to fetch details for.
 * @returns {Promise<object>} - A promise that resolves to the domain details in JSON format.
 */
async function fetchDomainDetails(domain) {
  try {
    // Validate the domain input
    if (!domain || typeof domain !== 'string') {
      throw new Error('Invalid domain name. Please provide a valid string.');
    }

    // Fetch domain data using the whois-json library
    const domainDetails = await whois(domain);

    // Return the parsed domain details
    return domainDetails;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching domain details:', error.message);
    throw error;
  }
}

// Example usage of the fetchDomainDetails function
(async () => {
  try {
    const domain = 'example.com'; // Replace with your desired domain
    const details = await fetchDomainDetails(domain);
    console.log('Domain Details:', details); // Output the domain details
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();
```
