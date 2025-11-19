"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: How would you implement a car rental system with over 25 years of service experience, including quality vehicle fleet management and trusted customer base, using Node.js and Express.js?
Generated: DETERMINISTIC_7517e1b1bcf13b8f
Batch ID: 20250622_210650
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
mongoose.connect('mongodb://localhost/car-rental', { useNewUrlParser: true, useUnifiedTopology: true });

// Define vehicle schema
const vehicleSchema = new mongoose.Schema({
  vehicleId: String,
  type: String,
  model: String,
  year: Number,
  available: Boolean
});

// Define user schema
const userSchema = new mongoose.Schema({
  userId: String,
  name: String,
  email: String,
  password: String
});

// Define rental schema
const rentalSchema = new mongoose.Schema({
  rentalId: String,
  userId: String,
  vehicleId: String,
  rentalDate: Date,
  returnDate: Date
});

// Create models
const Vehicle = mongoose.model('Vehicle', vehicleSchema);
const User = mongoose.model('User', userSchema);
const Rental = mongoose.model('Rental', rentalSchema);

// Express middleware
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      userId: req.body.userId,
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login a user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user.userId }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Add a new vehicle
app.post('/vehicles', async (req, res) => {
  try {
    const vehicle = new Vehicle({
      vehicleId: req.body.vehicleId,
      type: req.body.type,
      model: req.body.model,
      year: req.body.year,
      available: true
    });
    await vehicle.save();
    res.status(201).send({ message: 'Vehicle added successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error adding vehicle' });
  }
});

// Get all vehicles
app.get('/vehicles', async (req, res) => {
  try {
    const vehicles = await Vehicle.find();
    res.send(vehicles);
  } catch (error) {
    res.status(400).send({ message: 'Error getting vehicles' });
  }
});

// Rent a vehicle
app.post('/rentals', authenticateToken, async (req, res) => {
  try {
    const vehicle = await Vehicle.findOne({ vehicleId: req.body.vehicleId });
    if (!vehicle || !vehicle.available) {
      return res.status(400).send({ message: 'Vehicle not available' });
    }
    const rental = new Rental({
      rentalId: req.body.rentalId,
      userId: req.user.userId,
      vehicleId: req.body.vehicleId,
      rentalDate: new Date(),
      returnDate: null
    });
    vehicle.available = false;
    await vehicle.save();
    await rental.save();
    res.status(201).send({ message: 'Vehicle rented successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error renting vehicle' });
  }
});

// Return a vehicle
app.put('/rentals/:rentalId', authenticateToken, async (req, res) => {
  try {
    const rental = await Rental.findOne({ rentalId: req.params.rentalId });
    if (!rental || rental.userId !== req.user.userId) {
      return res.status(401).send({ message: 'Unauthorized' });
    }
    const vehicle = await Vehicle.findOne({ vehicleId: rental.vehicleId });
    vehicle.available = true;
    await vehicle.save();
    rental.returnDate = new Date();
    await rental.save();
    res.send({ message: 'Vehicle returned successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error returning vehicle' });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ message: 'Access denied' });
  try {
    const decoded = jwt.verify(token, 'secretkey');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
