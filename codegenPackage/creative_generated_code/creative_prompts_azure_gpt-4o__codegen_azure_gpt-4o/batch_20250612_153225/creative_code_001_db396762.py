"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Generate a REST API in Node.js for a personal trainer service that includes endpoints for plan selection, physical evaluation (via video uploads), personalized workout delivery, and user support via WhatsApp.
Generated: DETERMINISTIC_db396762f1fad39d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Framework for building REST APIs
const multer = require('multer'); // Middleware for handling file uploads
const path = require('path'); // Utilities for working with file paths
const bodyParser = require('body-parser'); // Middleware for parsing JSON and urlencoded requests

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Multer configuration for video uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads'); // Save uploaded files to 'uploads' folder
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`); // Generate unique file names
  },
});
const upload = multer({
  storage: storage,
  fileFilter: (req, file, cb) => {
    // Accept only video files
    const fileTypes = /mp4|mov|avi|mkv/;
    const extname = fileTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = fileTypes.test(file.mimetype);
    if (extname && mimetype) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type. Only video files are allowed.'));
    }
  },
});

// Endpoints

// 1. Plan Selection
app.post('/api/plans/select', (req, res) => {
  const { userId, planId } = req.body;

  // Validate input
  if (!userId || !planId) {
    return res.status(400).json({ error: 'User ID and Plan ID are required.' });
  }

  // Simulate plan selection logic (e.g., save to database)
  // For demonstration purposes, we'll return a success response
  return res.status(200).json({
    message: 'Plan selected successfully.',
    userId,
    planId,
  });
});

// 2. Physical Evaluation (Video Upload)
app.post('/api/evaluation/upload', upload.single('video'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No video file uploaded.' });
  }

  // Simulate saving video evaluation details (e.g., save file info to database)
  return res.status(200).json({
    message: 'Video uploaded successfully.',
    filePath: req.file.path,
  });
});

// 3. Personalized Workout Delivery
app.get('/api/workout/personalized', (req, res) => {
  const { userId } = req.query;

  // Validate input
  if (!userId) {
    return res.status(400).json({ error: 'User ID is required.' });
  }

  // Simulate fetching personalized workout plan for the user
  // For demonstration purposes, we'll return a static response
  return res.status(200).json({
    userId,
    workoutPlan: {
      day1: 'Cardio and Stretching',
      day2: 'Strength Training',
      day3: 'Yoga',
    },
  });
});

// 4. User Support via WhatsApp
app.post('/api/support/whatsapp', (req, res) => {
  const { userId, message } = req.body;

  // Validate input
  if (!userId || !message) {
    return res.status(400).json({ error: 'User ID and message are required.' });
  }

  // Simulate sending a WhatsApp message
  // For demonstration purposes, we'll return a success response
  return res.status(200).json({
    message: 'Support message sent successfully via WhatsApp.',
    userId,
    sentMessage: message,
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500).json({ error: 'An internal server error occurred.' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
