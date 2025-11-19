"""
Generated Code Metadata:
========================
Original URL: https://rworld.pro
Prompt: Design a simple backend API using Node.js to support a ride-sharing application like RideBNB.
Generated: DETERMINISTIC_e53f6d90252c5278
Batch ID: 20250622_211453
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
mongoose.connect('mongodb://localhost/ridebnb', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for users
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String,
    role: { type: String, enum: ['driver', 'rider'] }
});

// Define schema for rides
const rideSchema = new mongoose.Schema({
    pickup: String,
    dropoff: String,
    driver: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    rider: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    status: { type: String, enum: ['requested', 'accepted', 'started', 'ended'] }
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Ride = mongoose.model('Ride', rideSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/users', async (req, res) => {
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

// Login a user
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
        const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
        res.send({ token });
    } catch (err) {
        res.status(400).send({ message: 'Error logging in', error: err.message });
    }
});

// Request a ride
app.post('/rides', authenticateToken, async (req, res) => {
    try {
        const { pickup, dropoff } = req.body;
        const ride = new Ride({ pickup, dropoff, status: 'requested', rider: req.user.userId });
        await ride.save();
        res.status(201).send({ message: 'Ride requested successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error requesting ride', error: err.message });
    }
});

// Accept a ride
app.patch('/rides/:rideId/accept', authenticateToken, async (req, res) => {
    try {
        const rideId = req.params.rideId;
        const ride = await Ride.findById(rideId);
        if (!ride) {
            return res.status(404).send({ message: 'Ride not found' });
        }
        if (ride.status !== 'requested') {
            return res.status(400).send({ message: 'Ride is not in requested state' });
        }
        ride.driver = req.user.userId;
        ride.status = 'accepted';
        await ride.save();
        res.send({ message: 'Ride accepted successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error accepting ride', error: err.message });
    }
});

// Start a ride
app.patch('/rides/:rideId/start', authenticateToken, async (req, res) => {
    try {
        const rideId = req.params.rideId;
        const ride = await Ride.findById(rideId);
        if (!ride) {
            return res.status(404).send({ message: 'Ride not found' });
        }
        if (ride.status !== 'accepted') {
            return res.status(400).send({ message: 'Ride is not in accepted state' });
        }
        ride.status = 'started';
        await ride.save();
        res.send({ message: 'Ride started successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error starting ride', error: err.message });
    }
});

// End a ride
app.patch('/rides/:rideId/end', authenticateToken, async (req, res) => {
    try {
        const rideId = req.params.rideId;
        const ride = await Ride.findById(rideId);
        if (!ride) {
            return res.status(404).send({ message: 'Ride not found' });
        }
        if (ride.status !== 'started') {
            return res.status(400).send({ message: 'Ride is not in started state' });
        }
        ride.status = 'ended';
        await ride.save();
        res.send({ message: 'Ride ended successfully' });
    } catch (err) {
        res.status(400).send({ message: 'Error ending ride', error: err.message });
    }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send({ message: 'Access denied. No token provided.' });
    try {
        const decoded = jwt.verify(token, 'secretkey');
        req.user = decoded;
        next();
    } catch (err) {
        res.status(400).send({ message: 'Invalid token', error: err.message });
    }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
