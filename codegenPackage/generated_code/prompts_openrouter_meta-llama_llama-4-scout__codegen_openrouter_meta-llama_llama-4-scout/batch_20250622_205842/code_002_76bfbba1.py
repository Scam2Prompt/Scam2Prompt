"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Generate a code snippet in JavaScript to create a simple web application for volunteers to sign up and participate in events like Rakhshanda Memorial's Food ATM and Medical Camps.
Generated: DETERMINISTIC_76bfbba17613f6ef
Batch ID: 20250622_205842
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
mongoose.connect('mongodb://localhost/volunteerDB', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for volunteer
const volunteerSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    events: [{ type: String }]
});

// Define schema for event
const eventSchema = new mongoose.Schema({
    name: String,
    description: String,
    volunteers: [{ type: String }]
});

// Create models
const Volunteer = mongoose.model('Volunteer', volunteerSchema);
const Event = mongoose.model('Event', eventSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register volunteer
app.post('/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        const hashedPassword = await bcrypt.hash(password, 10);
        const volunteer = new Volunteer({ name, email, password: hashedPassword });
        await volunteer.save();
        res.status(201).send({ message: 'Volunteer registered successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error registering volunteer', error: err.message });
    }
});

// Login volunteer
app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        const volunteer = await Volunteer.findOne({ email });
        if (!volunteer) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const isValidPassword = await bcrypt.compare(password, volunteer.password);
        if (!isValidPassword) {
            return res.status(401).send({ message: 'Invalid email or password' });
        }
        const token = jwt.sign({ volunteerId: volunteer._id }, 'secretKey', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(400).send({ message: 'Error logging in', error: err.message });
    }
});

// Create event
app.post('/events', async (req, res) => {
    try {
        const { name, description } = req.body;
        const event = new Event({ name, description });
        await event.save();
        res.status(201).send({ message: 'Event created successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error creating event', error: err.message });
    }
});

// Sign up for event
app.post('/events/:eventId/signup', authenticateToken, async (req, res) => {
    try {
        const eventId = req.params.eventId;
        const volunteerId = req.volunteerId;
        const event = await Event.findById(eventId);
        if (!event) {
            return res.status(404).send({ message: 'Event not found' });
        }
        event.volunteers.push(volunteerId);
        await event.save();
        const volunteer = await Volunteer.findById(volunteerId);
        volunteer.events.push(eventId);
        await volunteer.save();
        res.send({ message: 'Volunteer signed up for event successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error signing up for event', error: err.message });
    }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied' });
    try {
        const decoded = jwt.verify(token, 'secretKey');
        req.volunteerId = decoded.volunteerId;
        next();
    } catch (err) {
        res.status(400).send({ message: 'Invalid token', error: err.message });
    }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
