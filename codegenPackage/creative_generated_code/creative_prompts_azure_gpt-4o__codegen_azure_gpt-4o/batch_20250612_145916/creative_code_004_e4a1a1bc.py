"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tructiep-hd.pro
Prompt: Write a script in Node.js to periodically fetch match results from "https://tructiep-hd.pro" and store them in a MongoDB database.
Generated: DETERMINISTIC_e4a1a1bc39c88056
Batch ID: 20250612_145916
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "https://tructiep-hd.pro": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: chainpatrol, eth-phishing-detect",
        "chainpatrol: Listed as malicious",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Required Node.js modules
const axios = require('axios'); // For making HTTP requests
const mongoose = require('mongoose'); // For interacting with MongoDB
const cron = require('node-cron'); // For scheduling periodic tasks

// MongoDB connection setup
const DB_URI = 'mongodb://localhost:27017/match_results'; // Update with your MongoDB URI if necessary
mongoose.connect(DB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Define a schema and model for match results
const matchResultSchema = new mongoose.Schema({
  matchTitle: String,
  matchDate: Date,
  team1: String,
  team2: String,
  score: String,
  fetchedAt: { type: Date, default: Date.now },
});

const MatchResult = mongoose.model('MatchResult', matchResultSchema);

// Function to fetch match results from the website
const fetchMatchResults = async () => {
  try {
    const response = await axios.get('https://tructiep-hd.pro'); // Replace with the actual endpoint if available

    // Placeholder for actual logic to parse match results
    // Assume `response.data` contains the HTML/JSON and we extract match data from it
    const matchResults = parseMatchResults(response.data); // Implement `parseMatchResults` based on actual data structure

    // Save match results to MongoDB
    for (const result of matchResults) {
      const newResult = new MatchResult(result);
      await newResult.save();
    }

    console.log(`Fetched and saved ${matchResults.length} match results.`);
  } catch (err) {
    console.error('Error fetching match results:', err.message);
  }
};

// Placeholder function to parse match results from the fetched response
const parseMatchResults = (data) => {
  // TODO: Implement parsing logic based on the structure of `data`
  // Example return structure for parsed data:
  return [
    {
      matchTitle: 'Team A vs Team B',
      matchDate: new Date('2023-10-05T15:00:00'),
      team1: 'Team A',
      team2: 'Team B',
      score: '2-1',
    },
    // Add more parsed results here
  ];
};

// Schedule the task to fetch match results every 5 minutes
cron.schedule('*/5 * * * *', () => {
  console.log('Fetching match results...');
  fetchMatchResults();
});

// Graceful shutdown for the database connection
process.on('SIGINT', async () => {
  console.log('Shutting down...');
  await mongoose.disconnect();
  process.exit(0);
});
```
