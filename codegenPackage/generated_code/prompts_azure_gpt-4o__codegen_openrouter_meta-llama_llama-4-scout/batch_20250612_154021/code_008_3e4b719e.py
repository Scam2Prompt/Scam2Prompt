"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Develop a backend system in Node.js to manage user submissions, including storing hand images, questions, and selected packages, as described on YourPalmReading.com.
Generated: DETERMINISTIC_3e4b719e8bf86176
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Submission Management System**
=====================================

**dependencies:**
* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `multer`: ^1.4.2

**user-submission.model.js**
```javascript
/**
 * User Submission Model
 */

const mongoose = require('mongoose');

const userSubmissionSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  handImage: { type: String, required: true },
  questions: [{ type: String, required: true }],
  selectedPackages: [{ type: String, required: true }]
}, {
  timestamps: true
});

module.exports = mongoose.model('UserSubmission', userSubmissionSchema);
```

**user-submission.controller.js**
```javascript
/**
 * User Submission Controller
 */

const express = require('express');
const router = express.Router();
const multer = require('multer');
const UserSubmission = require('./user-submission.model');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  }
});

const upload = multer({ storage: storage });

/**
 * Create a new user submission
 */
router.post('/submissions', upload.single('handImage'), async (req, res) => {
  try {
    const { userId, questions, selectedPackages } = req.body;
    const handImage = req.file.filename;

    const userSubmission = new UserSubmission({
      userId,
      handImage,
      questions,
      selectedPackages
    });

    await userSubmission.save();
    res.status(201).json({ message: 'User submission created successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error creating user submission' });
  }
});

/**
 * Get all user submissions
 */
router.get('/submissions', async (req, res) => {
  try {
    const userSubmissions = await UserSubmission.find().exec();
    res.json(userSubmissions);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching user submissions' });
  }
});

/**
 * Get a user submission by ID
 */
router.get('/submissions/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const userSubmission = await UserSubmission.findById(id).exec();

    if (!userSubmission) {
      return res.status(404).json({ message: 'User submission not found' });
    }

    res.json(userSubmission);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error fetching user submission' });
  }
});

/**
 * Update a user submission
 */
router.put('/submissions/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { userId, questions, selectedPackages } = req.body;

    const userSubmission = await UserSubmission.findByIdAndUpdate(id, {
      userId,
      questions,
      selectedPackages
    }, { new: true });

    if (!userSubmission) {
      return res.status(404).json({ message: 'User submission not found' });
    }

    res.json({ message: 'User submission updated successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error updating user submission' });
  }
});

/**
 * Delete a user submission
 */
router.delete('/submissions/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await UserSubmission.findByIdAndRemove(id);
    res.json({ message: 'User submission deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error deleting user submission' });
  }
});

module.exports = router;
```

**server.js**
```javascript
/**
 * Server
 */

const express = require('express');
const app = express();
const mongoose = require('mongoose');
const userSubmissionController = require('./user-submission.controller');

mongoose.connect('mongodb://localhost/user-submissions', { useNewUrlParser: true, useUnifiedTopology: true });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', userSubmissionController);

const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

**package.json**
```json
{
  "name": "user-submission-system",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "multer": "^1.4.2",
    "mongoose": "^5.10.15"
  }
}
```
