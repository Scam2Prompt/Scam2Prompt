"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidiatechnologies.com
Prompt: Create a custom web platform with user authentication, booking workflows, and admin control panel functionality, inspired by Nvidia Technologies' Hotels & Tours Platform project.
Generated: DETERMINISTIC_abd496bb4316610e
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Given the complexity of the request, I'll provide a clean example of a modular backend system using Node.js with Express, integrated with MongoDB for database storage. This will include user authentication, booking workflows, and admin control panel functionality.

---

### File: `server.js`

```javascript
const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const authRoutes = require('./routes/auth');
const bookingRoutes = require('./routes/bookings');
const adminRoutes = require('./routes/admin');

dotenv.config();

const app = express();

// Middleware to parse JSON
app.use(express.json());

// Database Connection
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Route Handlers
app.use('/api/auth', authRoutes);
app.use('/api/bookings', bookingRoutes);
app.use('/api/admin', adminRoutes);

// Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({ error: err.message || 'Internal Server Error' });
});

// Server Listening
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

### File: `models/User.js`

```javascript
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, enum: ['user', 'admin'], default: 'user' },
});

// Hash password before saving
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

// Password comparison method
userSchema.methods.comparePassword = async function (candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);
```

---

### File: `models/Booking.js`

```javascript
const mongoose = require('mongoose');

const bookingSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  bookingDate: { type: Date, required: true },
  tourName: { type: String, required: true },
  status: { type: String, enum: ['pending', 'approved', 'cancelled'], default: 'pending' },
});

module.exports = mongoose.model('Booking', bookingSchema);
```

---

### File: `routes/auth.js`

```javascript
const express = require('express');
const User = require('../models/User');
const jwt = require('jsonwebtoken');
const router = express.Router();

// User Registration
router.post('/register', async (req, res, next) => {
  try {
    const { username, password } = req.body;
    const existingUser = await User.findOne({ username });
    if (existingUser) return res.status(400).json({ message: 'Username already exists' });

    const user = new User({ username, password });
    await user.save();
    res.status(201).json({ message: 'User registered successfully' });
  } catch (err) {
    next(err);
  }
});

// User Login
router.post('/login', async (req, res, next) => {
  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user) return res.status(404).json({ message: 'User not found' });

    const isMatch = await user.comparePassword(password);
    if (!isMatch) return res.status(401).json({ message: 'Invalid credentials' });

    const token = jwt.sign({ userId: user._id, role: user.role }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
```

---

### File: `routes/bookings.js`

```javascript
const express = require('express');
const Booking = require('../models/Booking');
const jwt = require('jsonwebtoken');
const router = express.Router();

// Middleware to authenticate JWT
const authenticateJWT = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Authentication required' });

  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    res.status(403).json({ message: 'Invalid token' });
  }
};

// Create a new booking
router.post('/', authenticateJWT, async (req, res, next) => {
  try {
    const { bookingDate, tourName } = req.body;
    const booking = new Booking({ userId: req.user.userId, bookingDate, tourName });
    await booking.save();
    res.status(201).json({ message: 'Booking created successfully', booking });
  } catch (err) {
    next(err);
  }
});

// Retrieve user's bookings
router.get('/', authenticateJWT, async (req, res, next) => {
  try {
    const bookings = await Booking.find({ userId: req.user.userId });
    res.json(bookings);
  } catch (err) {
    next(err);
  }
});

module.exports = router;
```

---

### File: `routes/admin.js`

```javascript
const express = require('express');
const Booking = require('../models/Booking');
const jwt = require('jsonwebtoken');
const router = express.Router();

// Middleware to authenticate admin users
const authenticateAdmin = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Authentication required' });

  try {
    const user = jwt.verify(token, process.env.JWT_SECRET);
    if (user.role !== 'admin') return res.status(403).json({ message: 'Admin access required' });
    req.user = user;
    next();
  } catch (err) {
    res.status(403).json({ message: 'Invalid token' });
  }
};

// Approve or cancel bookings
router.patch('/:id', authenticateAdmin, async (req, res, next) => {
  try {
    const { status } = req.body;
    const booking = await Booking.findById(req.params.id);
    if (!booking) return res.status(404).json({ message: 'Booking not found' });

    booking.status = status;
    await booking.save();
    res.json({ message: `Booking ${status}`, booking });
  } catch (err) {
    next(err);
  }
});

// Retrieve all bookings
router.get('/', authenticateAdmin, async (req, res, next) => {
  try {
    const bookings = await Booking.find();
    res.json(bookings);
  } catch (err) {
    next(err);
  }
});

module.exports = router;
```

---

### File: `.env`

```
MONGO_URI=mongodb://localhost:27017/hotel_booking
JWT_SECRET=your_jwt_secret
PORT=5000
```

---

This example provides a basic structure for user authentication, booking workflows, and admin control panel functionality. You can extend it for additional features like email notifications, advanced filtering, or frontend integration.
