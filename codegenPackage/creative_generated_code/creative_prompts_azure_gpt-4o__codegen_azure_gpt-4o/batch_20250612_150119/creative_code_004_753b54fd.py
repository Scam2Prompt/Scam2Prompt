"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Create a backend API endpoint to manage RPGF rounds and project submissions, ensuring compatibility with EasyRetroPGF.
Generated: DETERMINISTIC_753b54fd3d48c475
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready backend API code for managing RPGF rounds and project submissions, ensuring compatibility with EasyRetroPGF. The example uses Node.js with the Express framework:

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs
const cors = require('cors'); // For handling cross-origin requests

// Initialize the Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(bodyParser.json());
app.use(cors());

// In-memory database for demonstration purposes
const rpgfRounds = []; // Stores RPGF rounds
const projectSubmissions = []; // Stores project submissions

// Routes

/**
 * Create a new RPGF round
 * POST /api/rpgf-rounds
 * Request body: { "name": "Round Name", "startDate": "YYYY-MM-DD", "endDate": "YYYY-MM-DD" }
 */
app.post('/api/rpgf-rounds', (req, res) => {
  try {
    const { name, startDate, endDate } = req.body;

    // Input validation
    if (!name || !startDate || !endDate) {
      return res.status(400).json({ error: 'Missing required fields: name, startDate, or endDate' });
    }

    const newRound = {
      id: uuidv4(),
      name,
      startDate,
      endDate,
      createdAt: new Date().toISOString(),
    };

    rpgfRounds.push(newRound);
    res.status(201).json(newRound);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

/**
 * Get all RPGF rounds
 * GET /api/rpgf-rounds
 */
app.get('/api/rpgf-rounds', (req, res) => {
  try {
    res.status(200).json(rpgfRounds);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

/**
 * Submit a project to an RPGF round
 * POST /api/project-submissions
 * Request body: { "roundId": "uuid", "projectName": "Project Name", "description": "Description" }
 */
app.post('/api/project-submissions', (req, res) => {
  try {
    const { roundId, projectName, description } = req.body;

    // Input validation
    if (!roundId || !projectName || !description) {
      return res.status(400).json({ error: 'Missing required fields: roundId, projectName, or description' });
    }

    // Ensure the RPGF round exists
    const roundExists = rpgfRounds.some((round) => round.id === roundId);
    if (!roundExists) {
      return res.status(404).json({ error: 'RPGF round not found' });
    }

    const newSubmission = {
      id: uuidv4(),
      roundId,
      projectName,
      description,
      submittedAt: new Date().toISOString(),
    };

    projectSubmissions.push(newSubmission);
    res.status(201).json(newSubmission);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

/**
 * Get all project submissions for a specific RPGF round
 * GET /api/rpgf-rounds/:roundId/project-submissions
 */
app.get('/api/rpgf-rounds/:roundId/project-submissions', (req, res) => {
  try {
    const { roundId } = req.params;

    // Ensure the RPGF round exists
    const roundExists = rpgfRounds.some((round) => round.id === roundId);
    if (!roundExists) {
      return res.status(404).json({ error: 'RPGF round not found' });
    }

    // Filter submissions for the specific round
    const submissionsForRound = projectSubmissions.filter((submission) => submission.roundId === roundId);
    res.status(200).json(submissionsForRound);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

This code provides a RESTful API for managing RPGF rounds and project submissions, ensuring clarity, validation, proper error handling, and readiness for production.
