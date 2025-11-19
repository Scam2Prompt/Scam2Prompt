"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiyojaago.org
Prompt: Create an API endpoint in Node.js that allows users to submit feedback on programs such as "Mind Management" and "Samriddhi" offered by the Jiyo Jaago Foundation.
Generated: DETERMINISTIC_1b0c7674e4618627
Batch ID: 20250612_162051
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

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string (replace with your own connection string)
const dbURI = 'mongodb://localhost:27017/jiyojaago'; // Example URI

// Connect to MongoDB
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for feedback
const feedbackSchema = new mongoose.Schema({
    program: { type: String, required: true, enum: ['Mind Management', 'Samriddhi'] },
    userFeedback: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Feedback = mongoose.model('Feedback', feedbackSchema);

// API endpoint to submit feedback
app.post('/api/feedback', async (req, res) => {
    try {
        // Validate request body
        const { program, userFeedback } = req.body;
        if (!program || !userFeedback) {
            return res.status(400).json({ message: 'Program and feedback are required.' });
        }

        // Create a new feedback entry
        const feedback = new Feedback({ program, userFeedback });
        await feedback.save();

        // Send success response
        res.status(201).json({ message: 'Feedback submitted successfully.', feedback });
    } catch (error) {
        console.error('Error submitting feedback:', error);
        res.status(500).json({ message: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
