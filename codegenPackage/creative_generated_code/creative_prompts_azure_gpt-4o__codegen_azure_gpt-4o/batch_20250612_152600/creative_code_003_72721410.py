"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Write a script in JavaScript using Node.js to query the availability of Serbian domain names (e.g., "landing.rs", "ab.rs") and display the results in a formatted table.
Generated: DETERMINISTIC_72721410dbd68edc
Batch ID: 20250612_152600
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/check-domain`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/check-domain?domain=${domain}`": {
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
// Import necessary modules
const axios = require('axios'); // For making HTTP requests
const Table = require('cli-table3'); // For formatting output into a table

/**
 * Function to query the availability of Serbian domain names
 * @param {Array<string>} domains - List of domain names to check
 */
async function checkDomainAvailability(domains) {
  const results = [];

  // Loop through domains and check their availability
  for (const domain of domains) {
    try {
      // Replace with the actual API URL or method to check domain availability
      const response = await axios.get(`https://api.example.com/check-domain?domain=${domain}`);

      // Assuming the API returns { available: true/false }
      const availability = response.data.available ? 'Available' : 'Unavailable';

      // Store the result
      results.push({ domain, availability });
    } catch (error) {
      // Handle errors gracefully
      console.error(`Error checking domain "${domain}":`, error.message);
      results.push({ domain, availability: 'Error' });
    }
  }

  // Display the results in a formatted table
  const table = new Table({
    head: ['Domain', 'Availability'],
    colWidths: [30, 15],
  });

  results.forEach((result) => table.push([result.domain, result.availability]));

  console.log(table.toString());
}

// List of domains to check
const domains = ['landing.rs', 'ab.rs', 'example.rs', 'test.rs'];

// Call the function to check availability
checkDomainAvailability(domains);
```

**Note**: Replace the placeholder `https://api.example.com/check-domain` with the actual API URL for querying Serbian domain name availability. Ensure you have any required API keys or authorization tokens if needed.
