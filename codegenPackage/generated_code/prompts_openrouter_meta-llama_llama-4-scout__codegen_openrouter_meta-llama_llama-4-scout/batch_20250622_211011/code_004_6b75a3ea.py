"""
Generated Code Metadata:
========================
Original URL: https://claytest.vercel.app
Prompt: Design a basic JavaScript API for user interaction with a challenge app, incorporating features from claytest.vercel.app.
Generated: DETERMINISTIC_6b75a3eaa06674f5
Batch ID: 20250622_211011
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
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/challenge-app', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

// Define challenge schema
const challengeSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    completed: { type: Boolean, default: false },
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Challenge = mongoose.model('Challenge', challengeSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/api/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;
        if (!username || !email || !password) {
            return res.status(400).json({ error: 'Please provide all required fields' });
        }

        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ error: 'Email already in use' });
        }

        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ username, email, password: hashedPassword });
        await user.save();
        res.json({ message: 'User created successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error creating user' });
    }
});

// Login a user
app.post('/api/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        if (!email || !password) {
            return res.status(400).json({ error: 'Please provide all required fields' });
        }

        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).json({ error: 'Invalid email or password' });
        }

        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ error: 'Invalid email or password' });
        }

        const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error logging in' });
    }
});

// Get all challenges
app.get('/api/challenges', authenticateToken, async (req, res) => {
    try {
        const challenges = await Challenge.find();
        res.json(challenges);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error fetching challenges' });
    }
});

// Create a new challenge
app.post('/api/challenges', authenticateToken, async (req, res) => {
    try {
        const { title, description } = req.body;
        if (!title || !description) {
            return res.status(400).json({ error: 'Please provide all required fields' });
        }

        const challenge = new Challenge({ title, description });
        await challenge.save();
        res.json({ message: 'Challenge created successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error creating challenge' });
    }
});

// Update a challenge
app.patch('/api/challenges/:id', authenticateToken, async (req, res) => {
    try {
        const { id } = req.params;
        const { title, description, completed } = req.body;

        const challenge = await Challenge.findById(id);
        if (!challenge) {
            return res.status(404).json({ error: 'Challenge not found' });
        }

        if (title) challenge.title = title;
        if (description) challenge.description = description;
        if (completed !== undefined) challenge.completed = completed;

        await challenge.save();
        res.json({ message: 'Challenge updated successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error updating challenge' });
    }
});

// Delete a challenge
app.delete('/api/challenges/:id', authenticateToken, async (req, res) => {
    try {
        const { id } = req.params;
        await Challenge.findByIdAndDelete(id);
        res.json({ message: 'Challenge deleted successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error deleting challenge' });
    }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).json({ error: 'Access denied' });

    try {
        const verified = jwt.verify(token, 'secretkey');
        req.user = verified;
        next();
    } catch (err) {
        console.error(err);
        res.status(400).json({ error: 'Invalid token' });
    }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
