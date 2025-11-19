"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.com
Prompt: "Design a RESTful API in Node.js to manage Budi Bromo Tour's bookings, including Jeep rentals, hotel reservations, and catering services."
Generated: DETERMINISTIC_21d51d7f48f78123
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
mongoose.connect('mongodb://localhost/budi-bromo-tour', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for users
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: { type: String, enum: ['admin', 'customer'] }
});

// Define schema for jeep rentals
const jeepRentalSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  rentalDate: Date,
  returnDate: Date,
  jeepType: String
});

// Define schema for hotel reservations
const hotelReservationSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  checkInDate: Date,
  checkOutDate: Date,
  roomType: String
});

// Define schema for catering services
const cateringServiceSchema = new mongoose.Schema({
  customer: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  serviceDate: Date,
  menu: String
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const JeepRental = mongoose.model('JeepRental', jeepRentalSchema);
const HotelReservation = mongoose.model('HotelReservation', hotelReservationSchema);
const CateringService = mongoose.model('CateringService', cateringServiceSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/api/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword,
      role: 'customer'
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login a user
app.post('/api/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Create a new jeep rental
app.post('/api/jeep-rentals', authenticateToken, async (req, res) => {
  try {
    const jeepRental = new JeepRental({
      customer: req.user.userId,
      rentalDate: req.body.rentalDate,
      returnDate: req.body.returnDate,
      jeepType: req.body.jeepType
    });
    await jeepRental.save();
    res.status(201).send({ message: 'Jeep rental created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating jeep rental', error });
  }
});

// Create a new hotel reservation
app.post('/api/hotel-reservations', authenticateToken, async (req, res) => {
  try {
    const hotelReservation = new HotelReservation({
      customer: req.user.userId,
      checkInDate: req.body.checkInDate,
      checkOutDate: req.body.checkOutDate,
      roomType: req.body.roomType
    });
    await hotelReservation.save();
    res.status(201).send({ message: 'Hotel reservation created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating hotel reservation', error });
  }
});

// Create a new catering service
app.post('/api/catering-services', authenticateToken, async (req, res) => {
  try {
    const cateringService = new CateringService({
      customer: req.user.userId,
      serviceDate: req.body.serviceDate,
      menu: req.body.menu
    });
    await cateringService.save();
    res.status(201).send({ message: 'Catering service created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating catering service', error });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token == null) return res.status(401).send({ message: 'Access denied. No token provided.' });
  jwt.verify(token, 'secretkey', (err, user) => {
    if (err) return res.status(403).send({ message: 'Invalid token' });
    req.user = user;
    next();
  });
}

// Get all jeep rentals for a customer
app.get('/api/jeep-rentals', authenticateToken, async (req, res) => {
  try {
    const jeepRentals = await JeepRental.find({ customer: req.user.userId });
    res.send(jeepRentals);
  } catch (error) {
    res.status(400).send({ message: 'Error getting jeep rentals', error });
  }
});

// Get all hotel reservations for a customer
app.get('/api/hotel-reservations', authenticateToken, async (req, res) => {
  try {
    const hotelReservations = await HotelReservation.find({ customer: req.user.userId });
    res.send(hotelReservations);
  } catch (error) {
    res.status(400).send({ message: 'Error getting hotel reservations', error });
  }
});

// Get all catering services for a customer
app.get('/api/catering-services', authenticateToken, async (req, res) => {
  try {
    const cateringServices = await CateringService.find({ customer: req.user.userId });
    res.send(cateringServices);
  } catch (error) {
    res.status(400).send({ message: 'Error getting catering services', error });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
