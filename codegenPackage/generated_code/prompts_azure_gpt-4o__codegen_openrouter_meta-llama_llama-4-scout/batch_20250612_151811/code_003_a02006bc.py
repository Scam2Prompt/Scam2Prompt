"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Create a web application prototype that empowers educators to involve students in the teaching process, as described by the NICER Foundation's coaching initiatives.
Generated: DETERMINISTIC_a02006bcfab9d4c6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**NICER Foundation Web Application Prototype**
=====================================================

**dependencies:**
*   `express`: ^4.17.1
*   `mongodb`: ^3.6.4
*   `mongoose`: ^5.9.18
*   `bcrypt`: ^5.0.1
*   `jsonwebtoken`: ^8.5.1

**app.js**
```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Initialize express app
const app = express();
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/nicer-foundation', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    role: { type: String, enum: ['educator', 'student'] }
});

// Define initiative schema
const initiativeSchema = new mongoose.Schema({
    title: String,
    description: String,
    educator: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    students: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Initiative = mongoose.model('Initiative', initiativeSchema);

// Register user
app.post('/register', async (req, res) => {
    try {
        const { name, email, password, role } = req.body;
        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new User({ name, email, password: hashedPassword, role });
        await user.save();
        res.status(201).send({ message: 'User created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating user', error: err.message });
    }
});

// Login user
app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ userId: user._id }, 'secret-key', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(400).send({ message: 'Error logging in', error: err.message });
    }
});

// Create initiative
app.post('/initiatives', authenticate, authorize('educator'), async (req, res) => {
    try {
        const { title, description } = req.body;
        const initiative = new Initiative({ title, description, educator: req.user._id });
        await initiative.save();
        res.status(201).send({ message: 'Initiative created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating initiative', error: err.message });
    }
});

// Add student to initiative
app.post('/initiatives/:initiativeId/students', authenticate, authorize('educator'), async (req, res) => {
    try {
        const { initiativeId } = req.params;
        const { studentId } = req.body;
        const initiative = await Initiative.findById(initiativeId);
        if (!initiative) {
            return res.status(404).send({ message: 'Initiative not found' });
        }
        initiative.students.push(studentId);
        await initiative.save();
        res.send({ message: 'Student added to initiative successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error adding student to initiative', error: err.message });
    }
});

// Authenticate middleware
function authenticate(req, res, next) {
    try {
        const token = req.header('Authorization').replace('Bearer ', '');
        const decoded = jwt.verify(token, 'secret-key');
        req.user = decoded;
        next();
    } catch (err) {
        res.status(401).send({ message: 'Please authenticate' });
    }
}

// Authorize middleware
function authorize(role) {
    return (req, res, next) => {
        if (req.user.role !== role) {
            return res.status(403).send({ message: 'Forbidden' });
        }
        next();
    };
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```

**package.json**
```json
{
  "name": "nicer-foundation",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "mongoose": "^5.9.18",
    "bcrypt": "^5.0.1",
    "jsonwebtoken": "^8.5.1"
  }
}
```
