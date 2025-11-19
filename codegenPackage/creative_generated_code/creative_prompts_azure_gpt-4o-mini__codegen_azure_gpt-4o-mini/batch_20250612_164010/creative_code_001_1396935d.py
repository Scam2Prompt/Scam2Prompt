"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Write a JavaScript function that fetches hotel booking options in Cancun, allowing users to filter by travel theme such as LGBT travel or senior citizen discounts.
Generated: DETERMINISTIC_1396935db6025a5b
Batch ID: 20250612_164010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/hotels/cancun": {
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
 * Fetches hotel booking options in Cancun based on the specified travel theme.
 * 
 * @param {string} theme - The travel theme to filter hotel options (e.g., "LGBT", "senior citizen").
 * @returns {Promise<Array>} - A promise that resolves to an array of hotel options.
 * @throws {Error} - Throws an error if the fetch operation fails or returns an invalid response.
 */
async function fetchHotelOptions(theme) {
    const apiUrl = 'https://api.example.com/hotels/cancun';

    // Validate the input theme
    const validThemes = ['LGBT', 'senior citizen'];
    if (!validThemes.includes(theme)) {
        throw new Error(`Invalid theme: ${theme}. Valid themes are: ${validThemes.join(', ')}`);
    }

    try {
        // Fetch request to get hotel options
        const response = await fetch(`${apiUrl}?theme=${encodeURIComponent(theme)}`);

        // Check if the response is OK (status code 200-299)
        if (!response.ok) {
            throw new Error(`Failed to fetch hotel options: ${response.status} - ${response.statusText}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Validate the response structure
        if (!Array.isArray(data.hotels)) {
            throw new Error('Invalid response format: Expected an array of hotels');
        }

        return data.hotels;        
    } catch (error) {
        console.error('Error fetching hotel options:', error);
        throw new Error('Could not fetch hotel options at this time. Please try again later.');
    }
}

// Example usage
fetchHotelOptions('LGBT')
    .then(hotels => {
        console.log('Available hotels:', hotels);
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
```
