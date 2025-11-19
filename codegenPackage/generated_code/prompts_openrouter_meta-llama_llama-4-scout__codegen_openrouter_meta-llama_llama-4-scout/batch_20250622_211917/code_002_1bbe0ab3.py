"""
Generated Code Metadata:
========================
Original URL: https://casapiticilor.ro
Prompt: Generate a REST API endpoint in Node.js that returns a list of famous football teams, including Juventus, along with their achievements, and handles cases where a requested resource is not found.
Generated: DETERMINISTIC_1bbe0ab314467ff9
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Enable JSON parsing for incoming requests
app.use(express.json());

// Define a class for FootballTeam
class FootballTeam {
  constructor(name, achievements) {
    this.name = name;
    this.achievements = achievements;
  }
}

// In-memory data store for football teams
const footballTeams = [
  new FootballTeam('Juventus', ['Serie A', 'UEFA Champions League']),
  new FootballTeam('Barcelona', ['La Liga', 'UEFA Champions League']),
  new FootballTeam('Manchester United', ['Premier League', 'UEFA Champions League']),
];

// API endpoint to get all football teams
app.get('/api/teams', (req, res) => {
  try {
    // Return a JSON response with all football teams
    res.json(footballTeams);
  } catch (error) {
    // Handle any unexpected errors
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a football team by name
app.get('/api/teams/:name', (req, res) => {
  try {
    const teamName = req.params.name;
    const team = footballTeams.find((t) => t.name.toLowerCase() === teamName.toLowerCase());

    if (!team) {
      // Return a 404 response if the team is not found
      res.status(404).json({ message: `Team '${teamName}' not found` });
    } else {
      // Return a JSON response with the team details
      res.json(team);
    }
  } catch (error) {
    // Handle any unexpected errors
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
