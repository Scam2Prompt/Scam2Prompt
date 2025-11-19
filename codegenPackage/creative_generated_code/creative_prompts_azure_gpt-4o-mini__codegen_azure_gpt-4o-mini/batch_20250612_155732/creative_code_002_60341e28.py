"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seandahealthcare.co.za
Prompt: Create a REST API endpoint in Node.js that allows healthcare professionals to submit their applications to Seanda Healthcare.
Generated: DETERMINISTIC_60341e289e0ccd41
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { body, validationResult } = require('express-validator');

// Initialize the Express application
const app = express();

// Middleware to parse incoming JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'YOUR_MONGODB_CONNECTION_STRING';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define the application schema
const applicationSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    qualifications: { type: String, required: true },
    experience: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Application = mongoose.model('Application', applicationSchema);

// POST endpoint to submit applications
app.post('/api/apply', [
    // Validation rules
    body('name').notEmpty().withMessage('Name is required'),
    body('email').isEmail().withMessage('Valid email is required'),
    body('qualifications').notEmpty().withMessage('Qualifications are required'),
    body('experience').notEmpty().withMessage('Experience is required')
], async (req, res) => {
    // Validate request body
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    // Create a new application instance
    const application = new Application(req.body);

    try {
        // Save the application to the database
        const savedApplication = await application.save();
        return res.status(201).json({ message: 'Application submitted successfully', application: savedApplication });
    } catch (error) {
        console.error('Error saving application:', error);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
**Note**: Replace `YOUR_MONGODB_CONNECTION_STRING` with your actual MongoDB connection string.
