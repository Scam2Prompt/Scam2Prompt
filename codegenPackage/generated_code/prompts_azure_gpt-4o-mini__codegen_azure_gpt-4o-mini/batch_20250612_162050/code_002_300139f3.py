"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Create an API endpoint in Node.js that allows users to submit their feedback on educational programs, inspired by the community engagement initiatives mentioned by UMM FM.
Generated: DETERMINISTIC_300139f3180423aa
Batch ID: 20250612_162050
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB (replace with your connection string)
mongoose.connect('mongodb://localhost:27017/feedbackDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define a schema for feedback
const feedbackSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    program: { type: String, required: true },
    comments: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a model for feedback
const Feedback = mongoose.model('Feedback', feedbackSchema);

// API endpoint to submit feedback
app.post('/api/feedback', async (req, res) => {
    try {
        // Validate request body
        const { name, email, program, comments } = req.body;
        if (!name || !email || !program || !comments) {
            return res.status(400).json({ error: 'All fields are required.' });
        }

        // Create a new feedback document
        const feedback = new Feedback({ name, email, program, comments });

        // Save feedback to the database
        await feedback.save();

        // Respond with success message
        res.status(201).json({ message: 'Feedback submitted successfully.' });
    } catch (error) {
        // Handle errors and respond with a 500 status code
        console.error('Error saving feedback:', error);
        res.status(500).json({ error: 'An error occurred while submitting feedback.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
