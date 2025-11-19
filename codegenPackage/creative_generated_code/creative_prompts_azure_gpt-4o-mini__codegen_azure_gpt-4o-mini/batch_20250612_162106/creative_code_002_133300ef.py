"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prominsac.com
Prompt: Write a function in JavaScript that displays item titles and subtitles from the Prominsac API response.
Generated: DETERMINISTIC_133300ef897e2d1b
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetches data from the Prominsac API and displays item titles and subtitles.
 * 
 * @async
 * @function displayItemTitlesAndSubtitles
 * @param {string} apiUrl - The URL of the Prominsac API.
 * @returns {Promise<void>} - A promise that resolves when the items are displayed.
 */
async function displayItemTitlesAndSubtitles(apiUrl) {
    try {
        // Fetch data from the API
        const response = await fetch(apiUrl);
        
        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON from the response
        const data = await response.json();
        
        // Check if the expected property 'items' exists in the response
        if (!data.items || !Array.isArray(data.items)) {
            throw new Error("Invalid response structure: 'items' not found or not an array.");
        }

        // Iterate over each item and display its title and subtitle
        data.items.forEach(item => {
            const title = item.title || 'No title available';
            const subtitle = item.subtitle || 'No subtitle available';
            console.log(`Title: ${title}, Subtitle: ${subtitle}`);
        });
    } catch (error) {
        // Log any errors that occur during the fetch or processing
        console.error("Error fetching or displaying items:", error);
    }
}

// Example usage: Replace 'YOUR_API_URL' with the actual API URL
// displayItemTitlesAndSubtitles('YOUR_API_URL');
```
