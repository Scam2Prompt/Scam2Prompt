"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: Develop a JavaScript-based app that retrieves and displays domain expiration dates using an external API.
Generated: DETERMINISTIC_a4eaecbdc2f3a465
Batch ID: 20250612_153728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/domain/${domain}/expiration`;": {
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
// Importing necessary libraries
const express = require('express');
const axios = require('axios');

// Initializing the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(express.json());

// Function to fetch domain expiration date from an external API
async function fetchDomainExpiration(domain) {
    const apiUrl = `https://api.example.com/domain/${domain}/expiration`; // Replace with a real API URL

    try {
        const response = await axios.get(apiUrl);
        if (response.status === 200) {
            return response.data.expiration_date; // Adjust according to the API response structure
        } else {
            throw new Error('Failed to retrieve data from API');
        }
    } catch (error) {
        console.error(`Error fetching expiration date for domain ${domain}:`, error.message);
        throw error; // Propagate the error for further handling
    }
}

// API endpoint to get domain expiration date
app.get('/api/domain/:domain/expiration', async (req, res) => {
    const domain = req.params.domain;

    // Validate domain format (simple regex for demonstration)
    const domainRegex = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$/;
    if (!domainRegex.test(domain)) {
        return res.status(400).json({ error: 'Invalid domain format' });
    }

    try {
        const expirationDate = await fetchDomainExpiration(domain);
        res.status(200).json({ domain, expirationDate });
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Starting the Express server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
