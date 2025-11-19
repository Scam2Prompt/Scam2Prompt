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
const mongoose = require('mongoose');
const router = express.Router();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/umm-fm-feedback', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Could not connect to MongoDB', err));

// Define the feedback schema
const feedbackSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    program: { type: String, required: true },
    feedback: { type: String, required: true },
    rating: { type: Number, required: true, min: 1, max: 5 }
});

// Create a model from the schema
const Feedback = mongoose.model('Feedback', feedbackSchema);

// API endpoint to submit feedback
router.post('/feedback', async (req, res) => {
    try {
        // Validate request body
        if (!req.body.name || !req.body.email || !req.body.program || !req.body.feedback || !req.body.rating) {
            return res.status(400).json({ message: 'Please provide all required fields' });
        }

        // Create a new feedback document
        const feedback = new Feedback(req.body);

        // Save the feedback document to MongoDB
        await feedback.save();

        // Return a success response
        res.status(201).json({ message: 'Feedback submitted successfully' });
    } catch (err) {
        // Return an error response
        res.status(500).json({ message: 'Failed to submit feedback', error: err.message });
    }
});

// API endpoint to retrieve all feedback
router.get('/feedback', async (req, res) => {
    try {
        // Retrieve all feedback documents from MongoDB
        const feedback = await Feedback.find().exec();

        // Return a success response with feedback data
        res.status(200).json(feedback);
    } catch (err) {
        // Return an error response
        res.status(500).json({ message: 'Failed to retrieve feedback', error: err.message });
    }
});

// Create an Express app
const app = express();
app.use(express.json());

// Use the router
app.use('/api', router);

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
