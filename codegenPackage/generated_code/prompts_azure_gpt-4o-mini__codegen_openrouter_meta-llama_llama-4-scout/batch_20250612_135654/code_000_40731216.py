"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Generate code for a web application that implements a self-development program similar to the METATIME concept, focusing on body and consciousness integration.
Generated: DETERMINISTIC_407312168737d4a0
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**METATIME Web Application**
==========================

**dependencies:**

*   `express`: ^4.17.1
*   `mongodb`: ^3.6.4
*   `mongoose`: ^5.9.18

**models/User.js**
```javascript
// Import mongoose library
const mongoose = require('mongoose');

// Define user schema
const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    body: {
        energy: {
            type: Number,
            default: 50
        },
        health: {
            type: Number,
            default: 50
        }
    },
    consciousness: {
        focus: {
            type: Number,
            default: 50
        },
        awareness: {
            type: Number,
            default: 50
        }
    },
    exercises: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Exercise'
        }
    ]
});

// Export User model
module.exports = mongoose.model('User', userSchema);
```

**models/Exercise.js**
```javascript
// Import mongoose library
const mongoose = require('mongoose');

// Define exercise schema
const exerciseSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    type: {
        type: String,
        required: true,
        enum: ['body', 'consciousness']
    },
    description: {
        type: String,
        required: true
    },
    targetValue: {
        type: Number,
        required: true
    },
    currentValue: {
        type: Number,
        default: 0
    }
});

// Export Exercise model
module.exports = mongoose.model('Exercise', exerciseSchema);
```

**routes/user.js**
```javascript
// Import express library
const express = require('express');

// Import User model
const User = require('../models/User');

// Create router
const router = express.Router();

// Get all users
router.get('/', async (req, res) => {
    try {
        const users = await User.find().populate('exercises');
        res.json(users);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get user by ID
router.get('/:id', async (req, res) => {
    try {
        const user = await User.findById(req.params.id).populate('exercises');
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.json(user);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Create new user
router.post('/', async (req, res) => {
    try {
        const user = new User(req.body);
        await user.save();
        res.status(201).json(user);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Update user
router.put('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.json(user);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Delete user
router.delete('/:id', async (req, res) => {
    try {
        await User.findByIdAndRemove(req.params.id);
        res.json({ message: 'User deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Add exercise to user
router.post('/:id/exercises', async (req, res) => {
    try {
        const user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        const exercise = await Exercise.findById(req.body.exerciseId);
        if (!exercise) {
            return res.status(404).json({ message: 'Exercise not found' });
        }
        user.exercises.push(exercise._id);
        await user.save();
        res.json(user);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Export router
module.exports = router;
```

**routes/exercise.js**
```javascript
// Import express library
const express = require('express');

// Import Exercise model
const Exercise = require('../models/Exercise');

// Create router
const router = express.Router();

// Get all exercises
router.get('/', async (req, res) => {
    try {
        const exercises = await Exercise.find();
        res.json(exercises);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Get exercise by ID
router.get('/:id', async (req, res) => {
    try {
        const exercise = await Exercise.findById(req.params.id);
        if (!exercise) {
            return res.status(404).json({ message: 'Exercise not found' });
        }
        res.json(exercise);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Create new exercise
router.post('/', async (req, res) => {
    try {
        const exercise = new Exercise(req.body);
        await exercise.save();
        res.status(201).json(exercise);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Update exercise
router.put('/:id', async (req, res) => {
    try {
        const exercise = await Exercise.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!exercise) {
            return res.status(404).json({ message: 'Exercise not found' });
        }
        res.json(exercise);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Delete exercise
router.delete('/:id', async (req, res) => {
    try {
        await Exercise.findByIdAndRemove(req.params.id);
        res.json({ message: 'Exercise deleted successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Export router
module.exports = router;
```

**app.js**
```javascript
// Import express library
const express = require('express');

// Import mongoose library
const mongoose = require('mongoose');

// Import user router
const userRouter = require('./routes/user');

// Import exercise router
const exerciseRouter = require('./routes/exercise');

// Create express app
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/metatime', { useNewUrlParser: true, useUnifiedTopology: true });

// Define middleware
app.use(express.json());

// Use routers
app.use('/users', userRouter);
app.use('/exercises', exerciseRouter);

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
