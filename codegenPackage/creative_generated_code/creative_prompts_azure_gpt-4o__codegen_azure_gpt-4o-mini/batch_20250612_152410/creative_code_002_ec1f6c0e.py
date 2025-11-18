"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Develop a JavaScript function that integrates with the Meme Kombat API to fetch the current percentage of $MK tokens staked and display it dynamically on a webpage.
Generated: DETERMINISTIC_ec1f6c0eee554a6a
Batch ID: 20250612_152410
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.memekombat.com/staked-percentage": {
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
// Function to fetch the current percentage of $MK tokens staked from the Meme Kombat API
async function fetchStakedPercentage() {
    const apiUrl = 'https://api.memekombat.com/staked-percentage'; // The API endpoint to fetch data
    const percentageElement = document.getElementById('staked-percentage'); // HTML element to display the percentage

    try {
        // Fetch data from the API
        const response = await fetch(apiUrl);

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Check if the expected data is available
        if (data && typeof data.percentage === 'number') {
            // Update the inner HTML of the element to display the staked percentage
            percentageElement.innerText = `Current $MK Tokens Staked: ${data.percentage.toFixed(2)}%`;
        } else {
            throw new Error('Invalid data format received from the API.');
        }
    } catch (error) {
        console.error('Error fetching staked percentage:', error);
        // Display an error message in the HTML element
        percentageElement.innerText = 'Error fetching data. Please try again later.';
    }
}

// Call the function to fetch and display the staked percentage on page load
document.addEventListener('DOMContentLoaded', () => {
    fetchStakedPercentage();
});
```

```html
<!-- HTML snippet to include in the webpage -->
<div id="staked-percentage">Loading staked percentage...</div>
```

In this script, an API call is made to the specified endpoint to get the staking percentage, which is then displayed in the HTML element with the ID `staked-percentage`. Error handling is included to manage potential fetch errors and invalid data formats.
