"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Develop a simple web application that allows users to track their earnings from multiple crypto faucets, inspired by the features of Moon5.
Generated: DETERMINISTIC_af045a5028761da4
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Crypto Faucet Tracker Web Application**
=====================================

**dependencies:**

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `mongoose`: ^5.10.15
* `body-parser`: ^1.19.0

**models/User.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define user schema
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  faucets: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Faucet' }]
});

// Export user model
module.exports = mongoose.model('User', userSchema);
```

**models/Faucet.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define faucet schema
const faucetSchema = new mongoose.Schema({
  name: { type: String, required: true },
  url: { type: String, required: true },
  earnings: [{ type: { date: Date, amount: Number } }]
});

// Export faucet model
module.exports = mongoose.model('Faucet', faucetSchema);
```

**app.js**
```javascript
// Import dependencies
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const User = require('./models/User');
const Faucet = require('./models/Faucet');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/crypto-faucet-tracker', { useNewUrlParser: true, useUnifiedTopology: true });

// Initialize express app
const app = express();

// Use body-parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Register user
app.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const user = new User({ username, email, password });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user || user.password !== password) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }
    res.send({ message: 'User logged in successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in user', error });
  }
});

// Add faucet
app.post('/faucets', async (req, res) => {
  try {
    const { name, url } = req.body;
    const faucet = new Faucet({ name, url });
    await faucet.save();
    res.status(201).send({ message: 'Faucet added successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error adding faucet', error });
  }
});

// Log earnings
app.post('/faucets/:faucetId/earnings', async (req, res) => {
  try {
    const { faucetId } = req.params;
    const { amount } = req.body;
    const faucet = await Faucet.findById(faucetId);
    if (!faucet) {
      return res.status(404).send({ message: 'Faucet not found' });
    }
    faucet.earnings.push({ date: new Date(), amount });
    await faucet.save();
    res.send({ message: 'Earnings logged successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error logging earnings', error });
  }
});

// Get user faucets
app.get('/users/:userId/faucets', async (req, res) => {
  try {
    const { userId } = req.params;
    const user = await User.findById(userId).populate('faucets');
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }
    res.send(user.faucets);
  } catch (error) {
    res.status(400).send({ message: 'Error getting user faucets', error });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**package.json**
```json
{
  "name": "crypto-faucet-tracker",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mongodb": "^3.6.4",
    "mongoose": "^5.10.15",
    "body-parser": "^1.19.0"
  }
}
```
