"""
Generated Code Metadata:
========================
Original URL: https://buylibracoins.com
Prompt: Develop a code snippet in Node.js to create a RESTful API for managing e-wallet transactions, specifically for online slot games with multiple payment options.
Generated: DETERMINISTIC_273e58221622a7e6
Batch ID: 20250622_204907
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
const stripe = require('stripe')('sk_test_51L5C9kJk4L7L5L5L5L5L5L5L5');
const paypal = require('paypal-rest-sdk');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/ewallet', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for users
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  balance: { type: Number, default: 0 }
});

// Define schema for transactions
const transactionSchema = new mongoose.Schema({
  userId: String,
  amount: Number,
  paymentMethod: String,
  status: String
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
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
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Get user balance
app.get('/balance', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);
    res.send({ balance: user.balance });
  } catch (error) {
    res.status(400).send({ message: 'Error getting balance' });
  }
});

// Make a deposit
app.post('/deposit', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);
    user.balance += req.body.amount;
    await user.save();
    const transaction = new Transaction({
      userId: req.user.userId,
      amount: req.body.amount,
      paymentMethod: req.body.paymentMethod,
      status: 'success'
    });
    await transaction.save();
    res.send({ message: 'Deposit successful' });
  } catch (error) {
    res.status(400).send({ message: 'Error making deposit' });
  }
});

// Make a withdrawal
app.post('/withdraw', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);
    if (user.balance < req.body.amount) {
      return res.status(400).send({ message: 'Insufficient balance' });
    }
    user.balance -= req.body.amount;
    await user.save();
    const transaction = new Transaction({
      userId: req.user.userId,
      amount: req.body.amount,
      paymentMethod: req.body.paymentMethod,
      status: 'success'
    });
    await transaction.save();
    res.send({ message: 'Withdrawal successful' });
  } catch (error) {
    res.status(400).send({ message: 'Error making withdrawal' });
  }
});

// Pay with Stripe
app.post('/pay-stripe', authenticateToken, async (req, res) => {
  try {
    const charge = await stripe.charges.create({
      amount: req.body.amount,
      currency: 'usd',
      source: req.body.source
    });
    const transaction = new Transaction({
      userId: req.user.userId,
      amount: req.body.amount,
      paymentMethod: 'stripe',
      status: 'success'
    });
    await transaction.save();
    res.send({ message: 'Payment successful' });
  } catch (error) {
    res.status(400).send({ message: 'Error making payment' });
  }
});

// Pay with PayPal
app.post('/pay-paypal', authenticateToken, async (req, res) => {
  try {
    paypal.configure({
      'mode': 'sandbox', // live or sandbox
      'client_id': 'YOUR_CLIENT_ID',
      'client_secret': 'YOUR_CLIENT_SECRET'
    });
    const payment = {
      'intent': 'sale',
      'payer': {
        'payment_method': 'paypal'
      },
      'redirect_urls': {
        'return_url': '/success',
        'cancel_url': '/cancel'
      },
      'transactions': [{
        'amount': {
          'currency': 'USD',
          'total': req.body.amount
        },
        'description': 'Payment for online slot games'
      }]
    };
    paypal.payment.create(payment, function (error, payment) {
      if (error) {
        return res.status(400).send({ message: 'Error making payment' });
      }
      res.redirect(payment.approval_url);
    });
  } catch (error) {
    res.status(400).send({ message: 'Error making payment' });
  }
});

// Middleware to authenticate token
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ message: 'Access denied' });
  try {
    const verified = jwt.verify(token, 'secretkey');
    req.user = verified;
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
