"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gottrumpmemes.net
Prompt: Write a JavaScript function that fetches and displays detailed information about Las Vegas neighborhoods from an API, including community features and housing prices.
Generated: DETERMINISTIC_2f87b6a7bef90baf
Batch ID: 20250612_155751
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/neighborhoods/lasvegas": {
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
 * Function to fetch and display detailed information about Las Vegas neighborhoods
 * including community features and housing prices.
 */
async function getLasVegasNeighborhoods() {
    // API endpoint for fetching Las Vegas neighborhoods data
    const apiUrl = 'https://api.example.com/neighborhoods/lasvegas';

    try {
        // Fetch data from the API
        const response = await fetch(apiUrl);

        // Check if the response status is OK (status code 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
        }

        // Parse the response JSON
        const data = await response.json();

        // Validate the data structure
        if (!Array.isArray(data) || data.length === 0) {
            throw new Error('Invalid or empty data received from API');
        }

        // Display neighborhood details in a user-friendly format
        console.log('Las Vegas Neighborhoods Information:');
        data.forEach((neighborhood, index) => {
            // Ensure the expected data exists for each neighborhood
            const { name, communityFeatures, housingPrices } = neighborhood;
            if (!name || !communityFeatures || !housingPrices) {
                console.warn(`Incomplete data for neighborhood at index ${index}`);
                return;
            }

            // Log neighborhood details
            console.log(`\nName: ${name}`);
            console.log(`Community Features: ${communityFeatures.join(', ')}`);
            console.log(`Housing Prices: $${housingPrices.low} - $${housingPrices.high}`);
        });
    } catch (error) {
        // Log errors for debugging purposes
        console.error('An error occurred while fetching Las Vegas neighborhoods:', error.message);
    }
}

// Execute the function
getLasVegasNeighborhoods();
```
