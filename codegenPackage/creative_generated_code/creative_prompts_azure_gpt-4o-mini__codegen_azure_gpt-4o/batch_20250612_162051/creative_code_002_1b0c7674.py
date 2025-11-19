"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiyojaago.org
Prompt: Create an API endpoint in Node.js that allows users to submit feedback on programs such as "Mind Management" and "Samriddhi" offered by the Jiyo Jaago Foundation.
Generated: DETERMINISTIC_1b0c7674e4618627
Batch ID: 20250612_162051
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

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require("express");
const bodyParser = require("body-parser");
const { v4: uuidv4 } = require("uuid");

// Initialize Express app
const app = express();
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// In-Memory database (for demonstration purposes)
const feedbackData = [];

// API endpoint to submit feedback
/**
 * @route POST /api/feedback
 * @description Submit feedback for a program
 * @param {string} name - Name of the user submitting feedback
 * @param {string} email - Email of the user
 * @param {string} program - Name of the program ("Mind Management" or "Samriddhi")
 * @param {string} feedback - Text feedback from the user
 * @returns {object} Response object with success status and submitted data
 */
app.post("/api/feedback", (req, res) => {
  try {
    // Extract data from the request body
    const { name, email, program, feedback } = req.body;

    // Validate input data
    if (!name || !email || !program || !feedback) {
      return res.status(400).json({
        error: "All fields (name, email, program, feedback) are required.",
      });
    }

    // Check if the program is valid
    const validPrograms = ["Mind Management", "Samriddhi"];
    if (!validPrograms.includes(program)) {
      return res.status(400).json({
        error: `Invalid program. Accepted values are: ${validPrograms.join(", ")}`,
      });
    }

    // Construct feedback object
    const feedbackEntry = {
      id: uuidv4(), // Generate a unique ID for feedback
      name,
      email,
      program,
      feedback,
      date: new Date().toISOString(),
    };

    // Save feedback in the in-memory database
    feedbackData.push(feedbackEntry);

    // Respond with success and submitted data
    return res.status(201).json({
      message: "Feedback submitted successfully.",
      data: feedbackEntry,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error("Error submitting feedback:", error);
    return res.status(500).json({
      error: "An unexpected error occurred while processing your request.",
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```
