"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Develop a backend system in Node.js to manage user submissions, including storing hand images, questions, and selected packages, as described on YourPalmReading.com.
Generated: DETERMINISTIC_3e4b719e8bf86176
Batch ID: 20250612_154021
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
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const multer = require('multer');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());
app.use('/uploads', express.static('uploads'));

// MongoDB connection setup
mongoose.connect('mongodb://localhost:27017/palmReadingDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define a schema for user submissions
const submissionSchema = new mongoose.Schema({
    handImage: {
        type: String,
        required: true,
    },
    question: {
        type: String,
        required: true,
    },
    selectedPackage: {
        type: String,
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create a model for user submissions
const Submission = mongoose.model('Submission', submissionSchema);

// Configure multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, `${Date.now()}-${file.originalname}`);
    },
});

const upload = multer({ storage });

// Endpoint to handle user submissions
app.post('/submit', upload.single('handImage'), async (req, res) => {
    try {
        const { question, selectedPackage } = req.body;

        // Create a new submission instance
        const newSubmission = new Submission({
            handImage: req.file.path,
            question,
            selectedPackage,
        });

        // Save the submission to the database
        await newSubmission.save();
        res.status(201).json({ message: 'Submission successful', submission: newSubmission });
    } catch (error) {
        console.error('Error processing submission:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Endpoint to retrieve all submissions
app.get('/submissions', async (req, res) => {
    try {
        const submissions = await Submission.find();
        res.status(200).json(submissions);
    } catch (error) {
        console.error('Error retrieving submissions:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
