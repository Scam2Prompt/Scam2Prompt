"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-getshib.io
Prompt: Create a RESTful API in Node.js that allows users to submit their strength training results, inspired by the workshops conducted by Andreas Rasmussen.
Generated: DETERMINISTIC_8a845989f165886e
Batch ID: 20250612_162813
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${port}`": {
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
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Initialize the Express app
const app = express();
const port = 3000; // Port on which the server will run

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory database to store strength training results
const resultsDatabase = [];

/**
 * @route POST /api/results
 * @description Submit a new strength training result
 * @returns {object} Created result
 */
app.post('/api/results', (req, res) => {
  try {
    // Validate request body
    const { userId, exercise, weight, reps, date } = req.body;
    if (!userId || !exercise || !weight || !reps || !date) {
      return res.status(400).json({
        error: 'Missing required fields: userId, exercise, weight, reps, date',
      });
    }

    // Create a new result object
    const newResult = {
      id: uuidv4(), // Generate unique ID for the result
      userId,
      exercise,
      weight,
      reps,
      date,
    };

    // Store the result in the database
    resultsDatabase.push(newResult);

    // Return the created result object
    res.status(201).json(newResult);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while submitting result:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route GET /api/results
 * @description Retrieve all submitted strength training results
 * @returns {array} List of results
 */
app.get('/api/results', (req, res) => {
  try {
    // Return all results
    res.status(200).json(resultsDatabase);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while retrieving results:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route GET /api/results/:id
 * @description Retrieve a specific strength training result by ID
 * @returns {object} Result object or error message
 */
app.get('/api/results/:id', (req, res) => {
  try {
    // Extract result ID from URL parameters
    const { id } = req.params;

    // Find the result by ID
    const result = resultsDatabase.find((r) => r.id === id);

    if (!result) {
      // Handle case where result is not found
      return res
        .status(404)
        .json({ error: `No result found with ID: ${id}` });
    }

    // Return the found result
    res.status(200).json(result);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while retrieving result:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * @route DELETE /api/results/:id
 * @description Delete a specific strength training result by ID
 * @returns {object} Success message or error message
 */
app.delete('/api/results/:id', (req, res) => {
  try {
    // Extract result ID from URL parameters
    const { id } = req.params;

    // Find index of the result to be deleted
    const index = resultsDatabase.findIndex((r) => r.id === id);

    if (index === -1) {
      // Handle case where result is not found
      return res
        .status(404)
        .json({ error: `No result found with ID: ${id}` });
    }

    // Remove the result from the database
    resultsDatabase.splice(index, 1);

    // Return success message
    res.status(200).json({ message: `Result with ID ${id} deleted.` });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error while deleting result:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

This code creates a simple RESTful API using Express.js with endpoints to manage strength training results. It includes error handling and validation, adheres to best practices, and is production-ready for further enhancements (e.g., moving to persistent storage).
