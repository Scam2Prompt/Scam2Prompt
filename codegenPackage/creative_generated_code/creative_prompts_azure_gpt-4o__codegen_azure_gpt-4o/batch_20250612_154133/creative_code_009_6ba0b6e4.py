"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guolvbao.com
Prompt: Write a JavaScript function to filter and display football match data, including live scores and statistical analysis, similar to the "赛事数据和分析" feature described on the webpage.
Generated: DETERMINISTIC_6ba0b6e4f04292d9
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to filter and display football match data with live scores and statistics.
 * @param {Array<Object>} matches - Array of football match objects.
 * @param {Object} filterCriteria - Object specifying filter criteria (e.g., team name, league, etc.).
 * @returns {Array<Object>} - Array of filtered match objects with live scores and statistical analysis.
 */
function getFilteredMatchData(matches, filterCriteria) {
  // Validate input
  if (!Array.isArray(matches)) {
    throw new Error("Invalid input: 'matches' must be an array.");
  }
  if (typeof filterCriteria !== "object" || filterCriteria === null) {
    throw new Error("Invalid input: 'filterCriteria' must be a non-null object.");
  }

  /**
   * Helper function to check if a match satisfies the filter criteria.
   * @param {Object} match - The match object to check.
   * @returns {boolean} - Whether the match satisfies the criteria.
   */
  const satisfiesCriteria = (match) => {
    return Object.keys(filterCriteria).every((key) => match[key] === filterCriteria[key]);
  };

  // Filter matches based on criteria
  const filteredMatches = matches.filter(satisfiesCriteria);

  // Add statistical analysis and format data for display
  const enrichedMatches = filteredMatches.map((match) => {
    // Simulated statistical analysis (replace with real calculations as needed)
    const statistics = {
      possession: `${Math.floor(Math.random() * 50) + 50}%`, // Example: random possession %
      shotsOnTarget: Math.floor(Math.random() * 10), // Example: random shots on target
      fouls: Math.floor(Math.random() * 5), // Example: random fouls
    };

    return {
      ...match,
      liveScore: `${match.homeTeamScore} - ${match.awayTeamScore}`, // Format live score
      statistics, // Include generated statistics
    };
  });

  // Return enriched match data
  return enrichedMatches;
}

// Example usage:
try {
  const matches = [
    {
      id: 1,
      homeTeam: "Team A",
      awayTeam: "Team B",
      league: "Premier League",
      homeTeamScore: 2,
      awayTeamScore: 1,
    },
    {
      id: 2,
      homeTeam: "Team C",
      awayTeam: "Team D",
      league: "La Liga",
      homeTeamScore: 0,
      awayTeamScore: 3,
    },
  ];

  const filterCriteria = { league: "Premier League" }; // Example filter: only "Premier League" matches
  const result = getFilteredMatchData(matches, filterCriteria);

  console.log("Filtered and Enriched Match Data:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
