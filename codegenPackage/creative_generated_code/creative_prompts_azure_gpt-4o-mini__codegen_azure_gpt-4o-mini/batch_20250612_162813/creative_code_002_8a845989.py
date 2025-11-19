"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-getshib.io
Prompt: Create a RESTful API in Node.js that allows users to submit their strength training results, inspired by the workshops conducted by Andreas Rasmussen.
Generated: DETERMINISTIC_8a845989f165886e
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Create an instance of Express
const app = express();

// Middleware for parsing requests
app.use(bodyParser.json());

// MongoDB connection string (update with your own credentials)
const mongoURI = 'mongodb://localhost:27017/strengthTrainingResults';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected successfully'))
  .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for strength training results
const resultSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  exercise: { type: String, required: true },
  weight: { type: Number, required: true },
  repetitions: { type: Number, required: true },
  date: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Result = mongoose.model('Result', resultSchema);

// Endpoint to submit strength training results
app.post('/results', async (req, res) => {
  try {
    const { userId, exercise, weight, repetitions } = req.body;

    // Validate required fields
    if (!userId || !exercise || !weight || !repetitions) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    // Create a new result document
    const newResult = new Result({ userId, exercise, weight, repetitions });

    // Save the result to the database
    await newResult.save();

    // Respond with success message
    res.status(201).json({ message: 'Result submitted successfully', result: newResult });
  } catch (error) {
    // Handle errors and send response
    console.error('Error submitting result:', error);
    res.status(500).json({ error: 'An error occurred while submitting the result' });
  }
});

// Endpoint to get all results for a user
app.get('/results/:userId', async (req, res) => {
  try {
    const { userId } = req.params;

    // Fetch results from the database
    const results = await Result.find({ userId });

    // Respond with the results
    res.status(200).json(results);
  } catch (error) {
    // Handle errors and send response
    console.error('Error fetching results:', error);
    res.status(500).json({ error: 'An error occurred while fetching the results' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
