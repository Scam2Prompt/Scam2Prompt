"""
Generated Code Metadata:
========================
Original URL: https://paymentsbot.site
Prompt: "Design a RESTful API for managing payments that can be integrated with an admin panel built on a JavaScript framework."
Generated: DETERMINISTIC_e6a330d19e16d93d
Batch ID: 20250622_211032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Payment API using Node.js and Express**
====================================================

**dependencies:**
* express: ^4.17.1
* mongoose: ^6.2.10
* bcrypt: ^5.0.1
* jsonwebtoken: ^8.5.1

**payment.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define payment schema
const paymentSchema = new mongoose.Schema({
  amount: {
    type: Number,
    required: true
  },
  paymentMethod: {
    type: String,
    enum: ['credit_card', 'paypal', 'bank_transfer'],
    required: true
  },
  paymentStatus: {
    type: String,
    enum: ['pending', 'success', 'failed'],
    default: 'pending'
  },
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  }
});

// Create payment model
const Payment = mongoose.model('Payment', paymentSchema);

module.exports = Payment;
```

**user.model.js**
```javascript
// Import mongoose and bcrypt
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

// Define user schema
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  email: {
    type: String,
    unique: true,
    required: true
  },
  password: {
    type: String,
    required: true
  }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (this.isNew || this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

// Create user model
const User = mongoose.model('User', userSchema);

module.exports = User;
```

**auth.controller.js**
```javascript
// Import jsonwebtoken, bcrypt, and User model
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('./user.model');

// Register user
async function register(req, res) {
  try {
    const { name, email, password } = req.body;
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: 'Email already exists' });
    }
    const user = new User({ name, email, password });
    await user.save();
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h'
    });
    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
}

// Login user
async function login(req, res) {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h'
    });
    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
}

module.exports = { register, login };
```

**payment.controller.js**
```javascript
// Import Payment model and authenticate middleware
const Payment = require('./payment.model');
const authenticate = require('./authenticate.middleware');

// Create payment
async function createPayment(req, res) {
  try {
    const { amount, paymentMethod } = req.body;
    const userId = req.user._id;
    const payment = new Payment({ amount, paymentMethod, userId });
    await payment.save();
    res.json(payment);
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
}

// Get all payments for a user
async function getPayments(req, res) {
  try {
    const userId = req.user._id;
    const payments = await Payment.find({ userId });
    res.json(payments);
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
}

// Update payment status
async function updatePaymentStatus(req, res) {
  try {
    const paymentId = req.params.paymentId;
    const { paymentStatus } = req.body;
    const payment = await Payment.findByIdAndUpdate(paymentId, { paymentStatus }, { new: true });
    if (!payment) {
      return res.status(404).json({ message: 'Payment not found' });
    }
    res.json(payment);
  } catch (error) {
    res.status(500).json({ message: 'Internal server error' });
  }
}

module.exports = { createPayment, getPayments, updatePaymentStatus };
```

**authenticate.middleware.js**
```javascript
// Import jsonwebtoken
const jwt = require('jsonwebtoken');

// Authenticate middleware
function authenticate(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).json({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).json({ message: 'Invalid token' });
  }
}

module.exports = authenticate;
```

**payment.route.js**
```javascript
// Import express, payment controller, and authenticate middleware
const express = require('express');
const { createPayment, getPayments, updatePaymentStatus } = require('./payment.controller');
const authenticate = require('./authenticate.middleware');

const router = express.Router();

// Create payment
router.post('/payments', authenticate, createPayment);

// Get all payments for a user
router.get('/payments', authenticate, getPayments);

// Update payment status
router.patch('/payments/:paymentId', authenticate, updatePaymentStatus);

module.exports = router;
```

**auth.route.js**
```javascript
// Import express and auth controller
const express = require('express');
const { register, login } = require('./auth.controller');

const router = express.Router();

// Register user
router.post('/register', register);

// Login user
router.post('/login', login);

module.exports = router;
```

**app.js**
```javascript
// Import express, mongoose, and routes
const express = require('express');
const mongoose = require('mongoose');
const paymentRoute = require('./payment.route');
const authRoute = require('./auth.route');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/payment-api', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.error('Error connecting to MongoDB:', error));

// Middleware
app.use(express.json());

// Routes
app.use('/api/auth', authRoute);
app.use('/api', paymentRoute);

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
