"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Develop a backend system in Node.js to manage user submissions, including storing hand images, questions, and selected packages, as described on YourPalmReading.com.
Generated: DETERMINISTIC_3e4b719e8bf86176
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// server.js

// Load required modules
const express = require('express');       // Web framework for Node.js
const multer = require('multer');         // Middleware to handle file uploads
const path = require('path');             // Module to handle file paths
const bodyParser = require('body-parser');// Middleware to parse incoming request bodies
const fs = require('fs');                 // File system module
const mongoose = require('mongoose');     // MongoDB object modeling tool

// Initialize the Express app
const app = express();

// Configure bodyParser to handle JSON data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Setup database connection using Mongoose
mongoose.connect('mongodb://localhost:27017/yourPalmReading', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Connected to MongoDB');
}).catch((err) => {
  console.error('Database connection error:', err);
});

// Define Mongoose schema for UserSubmission
const userSubmissionSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  questions: { type: String, required: true },
  selectedPackage: { type: String, required: true },
  handImagePath: { type: String, required: true },
}, { timestamps: true });

// Create Mongoose model for UserSubmission
const UserSubmission = mongoose.model('UserSubmission', userSubmissionSchema);

// Configure Multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadPath = path.join(__dirname, 'uploads');
    if (!fs.existsSync(uploadPath)) {
      fs.mkdirSync(uploadPath, { recursive: true });
    }
    cb(null, uploadPath);
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  },
});
const upload = multer({ storage });

// Route to handle user submissions
app.post('/submit', upload.single('handImage'), async (req, res) => {
  try {
    // Ensure the required fields are present
    const { name, email, questions, selectedPackage } = req.body;
    if (!name || !email || !questions || !selectedPackage || !req.file) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    // Create a new UserSubmission instance
    const submission = new UserSubmission({
      name,
      email,
      questions,
      selectedPackage,
      handImagePath: req.file.path,
    });

    // Save the submission to the database
    await submission.save();

    // Respond with success status
    res.status(201).json({ message: 'Submission successful.', submission });
  } catch (err) {
    console.error('Error saving submission:', err);
    res.status(500).json({ error: 'An unexpected error occurred.' });
  }
});

// Route to retrieve all submissions (admin-only access)
app.get('/submissions', async (req, res) => {
  try {
    const submissions = await UserSubmission.find();
    res.status(200).json(submissions);
  } catch (err) {
    console.error('Error retrieving submissions:', err);
    res.status(500).json({ error: 'An unexpected error occurred.' });
  }
});

// Route to retrieve a specific submission by ID
app.get('/submissions/:id', async (req, res) => {
  try {
    const submission = await UserSubmission.findById(req.params.id);
    if (!submission) {
      return res.status(404).json({ error: 'Submission not found.' });
    }
    res.status(200).json(submission);
  } catch (err) {
    console.error('Error retrieving submission:', err);
    res.status(500).json({ error: 'An unexpected error occurred.' });
  }
});

// Route to delete a specific submission by ID
app.delete('/submissions/:id', async (req, res) => {
  try {
    const submission = await UserSubmission.findByIdAndDelete(req.params.id);
    if (!submission) {
      return res.status(404).json({ error: 'Submission not found.' });
    }
    res.status(200).json({ message: 'Submission deleted successfully.' });
  } catch (err) {
    console.error('Error deleting submission:', err);
    res.status(500).json({ error: 'An unexpected error occurred.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
