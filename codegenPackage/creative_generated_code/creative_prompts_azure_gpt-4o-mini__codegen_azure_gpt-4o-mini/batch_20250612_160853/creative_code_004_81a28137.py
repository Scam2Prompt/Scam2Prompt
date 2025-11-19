"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Construct a RESTful API endpoint in Node.js that allows users to access success stories from the SKI Foundation's initiatives in empowering local entrepreneurs.
Generated: DETERMINISTIC_81a28137151636fe
Batch ID: 20250612_160853
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
const express = require('express');
const mongoose = require('mongoose');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// MongoDB connection URI
const mongoUri = 'mongodb://localhost:27017/ski_foundation';

// Connect to MongoDB
mongoose.connect(mongoUri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for success stories
const successStorySchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    entrepreneur: { type: String, required: true },
    date: { type: Date, default: Date.now }
});

// Create a model for success stories
const SuccessStory = mongoose.model('SuccessStory', successStorySchema);

// API endpoint to get all success stories
app.get('/api/success-stories', async (req, res) => {
    try {
        const stories = await SuccessStory.find();
        res.status(200).json(stories);
    } catch (error) {
        console.error('Error fetching success stories:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// API endpoint to create a new success story
app.post('/api/success-stories', async (req, res) => {
    const { title, description, entrepreneur } = req.body;

    // Basic validation
    if (!title || !description || !entrepreneur) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    try {
        const newStory = new SuccessStory({ title, description, entrepreneur });
        await newStory.save();
        res.status(201).json(newStory);
    } catch (error) {
        console.error('Error creating success story:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
