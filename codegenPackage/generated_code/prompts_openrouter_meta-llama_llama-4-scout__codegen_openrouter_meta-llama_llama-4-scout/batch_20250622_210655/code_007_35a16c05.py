"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: "Create a RESTful API to manage course purchases, including endpoints for course listing, purchase, and download, using Node.js and Express.js."
Generated: DETERMINISTIC_35a16c05ab395f30
Batch ID: 20250622_210655
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
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/course-purchases', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for courses
const courseSchema = new mongoose.Schema({
    title: String,
    price: Number,
    purchased: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

// Define schema for users
const userSchema = new mongoose.Schema({
    email: String,
    password: String,
    purchasedCourses: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Course' }]
});

// Compile schemas into models
const Course = mongoose.model('Course', courseSchema);
const User = mongoose.model('User', userSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Generate JWT token
const generateToken = (user) => {
    return jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
}

// Verify JWT token
const verifyToken = (req, res, next) => {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send('Access denied. No token provided.');

    try {
        const decoded = jwt.verify(token, 'secretkey');
        req.user = decoded;
        next();
    } catch (ex) {
        res.status(400).send('Invalid token.');
    }
}

// Get all courses
app.get('/api/courses', async (req, res) => {
    try {
        const courses = await Course.find().populate('purchased', '_id email');
        res.send(courses);
    } catch (ex) {
        res.status(500).send('Internal Server Error');
    }
});

// Purchase a course
app.post('/api/courses/:id/purchase', verifyToken, async (req, res) => {
    try {
        const course = await Course.findById(req.params.id);
        if (!course) return res.status(404).send('Course not found');

        const user = await User.findById(req.user.userId);
        if (user.purchasedCourses.includes(course._id)) return res.status(400).send('Course already purchased');

        course.purchased.push(user._id);
        user.purchasedCourses.push(course._id);

        await course.save();
        await user.save();

        res.send('Course purchased successfully');
    } catch (ex) {
        res.status(500).send('Internal Server Error');
    }
});

// Download a purchased course
app.get('/api/courses/:id/download', verifyToken, async (req, res) => {
    try {
        const course = await Course.findById(req.params.id).populate('purchased', '_id email');
        if (!course) return res.status(404).send('Course not found');

        const user = await User.findById(req.user.userId);
        if (!user.purchasedCourses.includes(course._id)) return res.status(403).send('Access denied');

        // Simulate course download
        res.send(`Downloading ${course.title}...`);
    } catch (ex) {
        res.status(500).send('Internal Server Error');
    }
});

// Register a new user
app.post('/api/users', async (req, res) => {
    try {
        const user = new User({
            email: req.body.email,
            password: await bcrypt.hash(req.body.password, 10)
        });

        await user.save();
        const token = generateToken(user);
        res.send({ token });
    } catch (ex) {
        res.status(500).send('Internal Server Error');
    }
});

// Login an existing user
app.post('/api/login', async (req, res) => {
    try {
        const user = await User.findOne({ email: req.body.email });
        if (!user) return res.status(400).send('Invalid email or password');

        const isValid = await bcrypt.compare(req.body.password, user.password);
        if (!isValid) return res.status(400).send('Invalid email or password');

        const token = generateToken(user);
        res.send({ token });
    } catch (ex) {
        res.status(500).send('Internal Server Error');
    }
});

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}...`));
```
