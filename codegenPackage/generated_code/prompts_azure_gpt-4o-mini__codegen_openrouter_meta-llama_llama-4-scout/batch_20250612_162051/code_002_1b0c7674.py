"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Create an API endpoint in Node.js that allows users to submit feedback on programs such as "Mind Management" and "Samriddhi" offered by the Jiyo Jaago Foundation.
Generated: DETERMINISTIC_1b0c7674e4618627
Batch ID: 20250612_162051
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
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define the feedback schema
const feedbackSchema = new mongoose.Schema({
  programName: {
    type: String,
    required: true,
    enum: ['Mind Management', 'Samriddhi'],
  },
  feedback: {
    type: String,
    required: true,
  },
  rating: {
    type: Number,
    required: true,
    min: 1,
    max: 5,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

// Create a model for the feedback schema
const Feedback = mongoose.model('Feedback', feedbackSchema);

// Create an Express app
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to submit feedback
app.post('/api/feedback', async (req, res) => {
  try {
    const { programName, feedback, rating } = req.body;

    // Validate input data
    if (!programName || !feedback || !rating) {
      return res.status(400).json({
        error: 'Please provide all required fields: programName, feedback, and rating',
      });
    }

    // Create a new feedback document
    const newFeedback = new Feedback({ programName, feedback, rating });

    // Save the feedback document to MongoDB
    await newFeedback.save();

    // Return a success response
    res.status(201).json({
      message: 'Feedback submitted successfully',
      feedback: newFeedback,
    });
  } catch (err) {
    // Return an error response
    res.status(500).json({
      error: 'Error submitting feedback',
      details: err.message,
    });
  }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal Server Error',
    details: err.message,
  });
});
```
