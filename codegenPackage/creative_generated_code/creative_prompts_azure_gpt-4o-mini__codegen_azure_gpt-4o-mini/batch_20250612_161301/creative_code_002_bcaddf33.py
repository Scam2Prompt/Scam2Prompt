"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a REST API endpoint in Node.js that allows users to submit applications for courses at the Kigali Institute, emphasizing the scholarship and financial aid options.
Generated: DETERMINISTIC_bcaddf33df01dca0
Batch ID: 20250612_161301
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
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection string (replace with your own)
const mongoURI = 'mongodb://localhost:27017/kigali_institute';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define schema for course applications
const applicationSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    course: { type: String, required: true },
    scholarship: { type: Boolean, default: false },
    financialAid: { type: Boolean, default: false },
    dateSubmitted: { type: Date, default: Date.now }
});

// Create model from schema
const Application = mongoose.model('Application', applicationSchema);

// Define the endpoint to submit applications
app.post('/api/apply', async (req, res) => {
    const { name, email, course, scholarship, financialAid } = req.body;

    // Validate incoming data
    if (!name || !email || !course) {
        return res.status(400).json({ error: 'Name, email, and course are required.' });
    }

    try {
        // Create a new application
        const newApplication = new Application({ name, email, course, scholarship, financialAid });

        // Save application to the database
        await newApplication.save();

        // Respond with success message
        res.status(201).json({ message: 'Application submitted successfully!', application: newApplication });

    } catch (error) {
        // Handle potential errors
        console.error('Error submitting application:', error);
        res.status(500).json({ error: 'An error occurred while submitting the application.' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
