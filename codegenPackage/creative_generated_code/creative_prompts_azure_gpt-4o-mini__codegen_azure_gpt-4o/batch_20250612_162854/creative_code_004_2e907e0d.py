"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calib3r.io
Prompt: Write a function in JavaScript that pings a website and logs the status, inspired by the shutdown notice of Calib3r.
Generated: DETERMINISTIC_2e907e0d752229bc
Batch ID: 20250612_162854
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.nonexistentwebsite123.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com": {
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
 * Function to ping a website and log its status.
 * @param {string} url - The URL of the website to ping.
 */
async function pingWebsite(url) {
    try {
        // Validate the input URL.
        if (typeof url !== 'string' || !url.startsWith('http')) {
            throw new Error('Invalid URL. Please provide a valid URL starting with http or https.');
        }

        // Perform a fetch request to check the website status.
        const response = await fetch(url, { method: 'HEAD' }); // Using HEAD to minimize bandwidth usage.

        if (response.ok) {
            console.log(`Website ${url} is up. Status: ${response.status} ${response.statusText}`);
        } else {
            console.log(`Website ${url} is down or unreachable. Status: ${response.status} ${response.statusText}`);
        }
    } catch (error) {
        // Handle network errors or any other exceptions.
        console.error(`An error occurred while pinging ${url}:`, error.message);
    }
}

// Example usage:
pingWebsite('https://www.example.com');
pingWebsite('https://www.nonexistentwebsite123.com');
```
