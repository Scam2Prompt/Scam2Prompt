"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Create an API endpoint in Node.js that allows users to submit their feedback on educational programs, inspired by the community engagement initiatives mentioned by UMM FM.
Generated: DETERMINISTIC_300139f3180423aa
Batch ID: 20250612_162050
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Create an instance of the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// MongoDB connection URL
const mongoURI = 'mongodb://localhost:27017/feedbackDB';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for feedback
const feedbackSchema = new mongoose.Schema({
    name: { type: String, required: true },
    program: { type: String, required: true },
    feedback: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for feedback
const Feedback = mongoose.model('Feedback', feedbackSchema);

// API endpoint to submit feedback
app.post('/api/feedback', async (req, res) => {
    try {
        // Destructure the feedback data from the request body
        const { name, program, feedback } = req.body;

        // Validate the incoming data
        if (!name || !program || !feedback) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new feedback entry
        const newFeedback = new Feedback({ name, program, feedback });

        // Save the feedback to the database
        await newFeedback.save();

        // Respond with a success message
        res.status(201).json({ message: 'Feedback submitted successfully!' });
    } catch (error) {
        console.error('Error submitting feedback:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
