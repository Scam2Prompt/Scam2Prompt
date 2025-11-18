"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axilofsecrets.com
Prompt: Create a JavaScript widget to show live updates of football matches sourced from the "极速体育APP下载" website, including team scores and match status.
Generated: DETERMINISTIC_216fb17bb90f20fc
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/live-matches": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/api/live-matches`": {
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
// FootballMatchWidget.js

class FootballMatchWidget {
    constructor(apiUrl, refreshInterval = 30000) {
        this.apiUrl = apiUrl; // URL to fetch live match updates
        this.refreshInterval = refreshInterval; // Time in milliseconds to refresh data
        this.matchesContainer = document.getElementById('matches'); // Element to display matches
        this.fetchMatches(); // Initial fetch of matches
        this.startAutoRefresh(); // Start the refresh cycle
    }

    // Fetch live match data from the API
    async fetchMatches() {
        try {
            const response = await fetch(this.apiUrl);
            if (!response.ok) {
                throw new Error(`Error fetching matches: ${response.statusText}`);
            }
            const data = await response.json();
            this.updateMatches(data); // Update the match display with the new data
        } catch (error) {
            console.error("Failed to fetch live matches:", error);
            this.matchesContainer.innerHTML = "<p>Error loading matches. Please try again later.</p>";
        }
    }

    // Update the displayed matches with the new data
    updateMatches(matches) {
        this.matchesContainer.innerHTML = ""; // Clear existing matches
        matches.forEach(match => {
            const matchElement = this.createMatchElement(match);
            this.matchesContainer.appendChild(matchElement); // Append new match element
        });
    }

    // Create an HTML element for a single match
    createMatchElement(match) {
        const matchDiv = document.createElement('div');
        matchDiv.classList.add('match');

        // Create elements to display team names and scores
        const teamNames = document.createElement('h3');
        teamNames.textContent = `${match.homeTeam} vs ${match.awayTeam}`;

        const score = document.createElement('p');
        score.textContent = `Score: ${match.homeScore} - ${match.awayScore}`;

        const status = document.createElement('p');
        status.textContent = `Status: ${match.status}`;

        // Append elements to matchDiv
        matchDiv.appendChild(teamNames);
        matchDiv.appendChild(score);
        matchDiv.appendChild(status);

        return matchDiv; // Return the constructed match element
    }

    // Start an interval to refresh the match data
    startAutoRefresh() {
        setInterval(() => {
            this.fetchMatches(); // Fetch updated matches at the specified interval
        }, this.refreshInterval);
    }
}

// Example usage of the FootballMatchWidget
const apiUrl = 'https://example.com/api/live-matches'; // Replace with the actual API URL
const footballWidget = new FootballMatchWidget(apiUrl);

// HTML structure should have an element with the id 'matches' where the widget will display the data
// <div id="matches"></div>
```

**Note:** Replace `https://example.com/api/live-matches` with the actual API endpoint from the "极速体育APP下载" website that provides live match data.
