"""
Generated Code Metadata:
========================
Original URL: https://baboons.vercel.app
Prompt: Design a simple backend API using Node.js that can support the Golden Baboons Mining Club application's functionality.
Generated: DETERMINISTIC_d19c7e316bc3835a
Batch ID: 20250622_211009
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
const port = 3000;
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((error) => console.error('Error connecting to MongoDB:', error));

// Define schema for user model
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
});

// Define schema for transaction model
const transactionSchema = new mongoose.Schema({
  userId: String,
  transactionDate: Date,
  amount: Number,
});

// Create models
const User = mongoose.model('User', userSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new user
/**
 * @api {post} /users Create a new user
 * @apiBody {String} username Username of the user
 * @apiBody {String} email Email of the user
 * @apiBody {String} password Password of the user
 * @apiSuccess {Object} user Created user object
 */
app.post('/users', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const user = new User({ username, email, password });
    await user.save();
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ message: 'Error creating user', error });
  }
});

// API endpoint to get all users
/**
 * @api {get} /users Get all users
 * @apiSuccess {Array} users Array of user objects
 */
app.get('/users', async (req, res) => {
  try {
    const users = await User.find().exec();
    res.json(users);
  } catch (error) {
    res.status(500).json({ message: 'Error getting users', error });
  }
});

// API endpoint to create a new transaction
/**
 * @api {post} /transactions Create a new transaction
 * @apiBody {String} userId ID of the user making the transaction
 * @apiBody {Date} transactionDate Date of the transaction
 * @apiBody {Number} amount Amount of the transaction
 * @apiSuccess {Object} transaction Created transaction object
 */
app.post('/transactions', async (req, res) => {
  try {
    const { userId, transactionDate, amount } = req.body;
    const transaction = new Transaction({ userId, transactionDate, amount });
    await transaction.save();
    res.status(201).json(transaction);
  } catch (error) {
    res.status(400).json({ message: 'Error creating transaction', error });
  }
});

// API endpoint to get all transactions for a user
/**
 * @api {get} /transactions/:userId Get all transactions for a user
 * @apiParam {String} userId ID of the user
 * @apiSuccess {Array} transactions Array of transaction objects
 */
app.get('/transactions/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const transactions = await Transaction.find({ userId }).exec();
    res.json(transactions);
  } catch (error) {
    res.status(500).json({ message: 'Error getting transactions', error });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal Server Error' });
});
```
