"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Write a code example in JavaScript for a mindfulness exercise app that incorporates DBT principles and techniques for stress reduction."
Generated: DETERMINISTIC_9da794230ee7a7df
Batch ID: 20250622_210650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Mindfulness Exercise App using DBT Principles
// This app provides users with stress reduction exercises based on Dialectical Behavior Therapy (DBT).

// Import necessary modules
const express = require('express'); // Web framework for building the app
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const fs = require('fs'); // File system module for reading exercise data

// Initialize the Express app
const app = express();
const PORT = 3000;

// Middleware setup
app.use(bodyParser.json());

// Load mindfulness exercises from a JSON file
let exercises = [];
try {
  const data = fs.readFileSync('./exercises.json', 'utf-8');
  exercises = JSON.parse(data);
} catch (error) {
  console.error('Error loading exercises:', error.message);
}

// Utility function to get a random exercise
const getRandomExercise = () => {
  if (exercises.length === 0) {
    throw new Error('No exercises available.');
  }
  const randomIndex = Math.floor(Math.random() * exercises.length);
  return exercises[randomIndex];
};

// Route: Get a random mindfulness exercise
app.get('/exercise', (req, res) => {
  try {
    const exercise = getRandomExercise();
    res.status(200).json({
      success: true,
      exercise,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message,
    });
  }
});

// Route: Add a new mindfulness exercise
app.post('/exercise', (req, res) => {
  const { name, description, technique } = req.body;

  // Validate input
  if (!name || !description || !technique) {
    return res.status(400).json({
      success: false,
      message: 'All fields (name, description, technique) are required.',
    });
  }

  // Add the new exercise
  const newExercise = { name, description, technique };
  exercises.push(newExercise);

  // Save the updated exercises to the file
  try {
    fs.writeFileSync('./exercises.json', JSON.stringify(exercises, null, 2));
    res.status(201).json({
      success: true,
      message: 'Exercise added successfully.',
      exercise: newExercise,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Error saving exercise: ' + error.message,
    });
  }
});

// Route: List all mindfulness exercises
app.get('/exercises', (req, res) => {
  res.status(200).json({
    success: true,
    exercises,
  });
});

// Error handling middleware for unexpected errors
app.use((err, req, res, next) => {
  console.error('Unexpected error:', err.message);
  res.status(500).json({
    success: false,
    message: 'An unexpected error occurred.',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Mindfulness Exercise App is running on http://localhost:${PORT}`);
});

/*
 * Example JSON file (exercises.json):
 * [
 *   {
 *     "name": "Deep Breathing",
 *     "description": "Focus on your breath. Inhale deeply for 4 seconds, hold for 4 seconds, and exhale for 4 seconds.",
 *     "technique": "Breathing Exercise"
 *   },
 *   {
 *     "name": "Body Scan",
 *     "description": "Pay attention to each part of your body, starting from your toes and moving upward.",
 *     "technique": "Mindfulness"
 *   }
 * ]
 */
```
