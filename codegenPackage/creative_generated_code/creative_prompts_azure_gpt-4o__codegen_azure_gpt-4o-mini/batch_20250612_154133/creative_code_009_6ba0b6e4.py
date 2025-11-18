"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guolvbao.com
Prompt: Write a JavaScript function to filter and display football match data, including live scores and statistical analysis, similar to the "赛事数据和分析" feature described on the webpage.
Generated: DETERMINISTIC_6ba0b6e4f04292d9
Batch ID: 20250612_154133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.football-data.org/v2/matches": {
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
 * Fetches and filters football match data, including live scores and statistical analysis.
 * 
 * @async
 * @function fetchAndDisplayMatchData
 * @param {string} apiUrl - The API endpoint to fetch match data from.
 * @param {string} league - The league to filter matches by.
 * @returns {void}
 */
async function fetchAndDisplayMatchData(apiUrl, league) {
    try {
        // Fetch the match data from the API
        const response = await fetch(apiUrl);
        
        // Check if the response is valid
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON data
        const data = await response.json();

        // Filter the matches for the specified league
        const filteredMatches = data.matches.filter(match => match.league === league);

        // Display the filtered matches
        displayMatches(filteredMatches);
    } catch (error) {
        console.error('Error fetching match data:', error);
    }
}

/**
 * Displays the filtered match data.
 *
 * @function displayMatches
 * @param {Array} matches - The array of filtered match data to display.
 * @returns {void}
 */
function displayMatches(matches) {
    // Check if there are any matches to display
    if (matches.length === 0) {
        console.log('No matches found for the specified league.');
        return;
    }

    // Iterate over each match and display relevant information
    matches.forEach(match => {
        console.log(`Match: ${match.homeTeam} vs ${match.awayTeam}`);
        console.log(`Score: ${match.liveScore}`);
        console.log(`Date: ${new Date(match.date).toLocaleString()}`);
        console.log(`Stats:`, match.statistics);
        console.log('-----------------------------------');
    });
}

// Example usage:
// fetchAndDisplayMatchData('https://api.football-data.org/v2/matches', 'Premier League');
```
