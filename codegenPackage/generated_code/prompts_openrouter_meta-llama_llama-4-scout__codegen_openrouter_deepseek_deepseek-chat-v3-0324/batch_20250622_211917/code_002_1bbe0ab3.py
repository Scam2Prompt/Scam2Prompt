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
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Database of football teams with their achievements
const footballTeams = [
    {
        id: 1,
        name: 'Juventus',
        country: 'Italy',
        achievements: [
            '36 Serie A titles',
            '14 Coppa Italia titles',
            '2 UEFA Champions League titles',
            '3 UEFA Cups'
        ]
    },
    {
        id: 2,
        name: 'Real Madrid',
        country: 'Spain',
        achievements: [
            '35 La Liga titles',
            '20 Copa del Rey titles',
            '14 UEFA Champions League titles'
        ]
    },
    {
        id: 3,
        name: 'Bayern Munich',
        country: 'Germany',
        achievements: [
            '32 Bundesliga titles',
            '20 DFB-Pokal titles',
            '6 UEFA Champions League titles'
        ]
    }
];

// GET all football teams
app.get('/api/teams', (req, res) => {
    try {
        res.status(200).json(footballTeams);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET a specific football team by ID
app.get('/api/teams/:id', (req, res) => {
    try {
        const teamId = parseInt(req.params.id);
        const team = footballTeams.find(t => t.id === teamId);

        if (!team) {
            return res.status(404).json({ error: 'Team not found' });
        }

        res.status(200).json(team);
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

// 404 handler for undefined routes
app.use((req, res) => {
    res.status(404).json({ error: 'Resource not found' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
