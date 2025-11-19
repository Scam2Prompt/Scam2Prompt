"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Create a RESTful API using Node.js to manage gift card purchases and inventory for an e-commerce platform similar to https://irgift.info, supporting various gaming platforms.
Generated: DETERMINISTIC_7126946dad4d8f61
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**gift-card-api.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/gift-card-api', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for gift cards
const giftCardSchema = new mongoose.Schema({
  platform: { type: String, required: true },
  cardType: { type: String, required: true },
  cardValue: { type: Number, required: true },
  quantity: { type: Number, required: true },
  purchased: { type: Boolean, default: false }
});

// Define schema for users
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

// Compile schemas into models
const GiftCard = mongoose.model('GiftCard', giftCardSchema);
const User = mongoose.model('User', userSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({ username: req.body.username, password: hashedPassword });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user', error });
  }
});

// Login a user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.username });
    if (!user) return res.status(401).send({ message: 'Invalid username or password' });
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) return res.status(401).send({ message: 'Invalid username or password' });
    const token = jwt.sign({ userId: user._id }, 'secret-key', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in', error });
  }
});

// Authenticate middleware
const authenticate = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    const decoded = jwt.verify(token, 'secret-key');
    req.user = await User.findById(decoded.userId);
    next();
  } catch (error) {
    res.status(401).send({ message: 'Please authenticate' });
  }
};

// Get all gift cards
app.get('/gift-cards', authenticate, async (req, res) => {
  try {
    const giftCards = await GiftCard.find().populate('platform');
    res.send(giftCards);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching gift cards', error });
  }
});

// Get a single gift card
app.get('/gift-cards/:id', authenticate, async (req, res) => {
  try {
    const giftCard = await GiftCard.findById(req.params.id).populate('platform');
    if (!giftCard) return res.status(404).send({ message: 'Gift card not found' });
    res.send(giftCard);
  } catch (error) {
    res.status(500).send({ message: 'Error fetching gift card', error });
  }
});

// Create a new gift card
app.post('/gift-cards', authenticate, async (req, res) => {
  try {
    const giftCard = new GiftCard(req.body);
    await giftCard.save();
    res.status(201).send(giftCard);
  } catch (error) {
    res.status(400).send({ message: 'Error creating gift card', error });
  }
});

// Update a gift card
app.patch('/gift-cards/:id', authenticate, async (req, res) => {
  try {
    const giftCard = await GiftCard.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!giftCard) return res.status(404).send({ message: 'Gift card not found' });
    res.send(giftCard);
  } catch (error) {
    res.status(500).send({ message: 'Error updating gift card', error });
  }
});

// Delete a gift card
app.delete('/gift-cards/:id', authenticate, async (req, res) => {
  try {
    await GiftCard.findByIdAndRemove(req.params.id);
    res.send({ message: 'Gift card deleted successfully' });
  } catch (error) {
    res.status(500).send({ message: 'Error deleting gift card', error });
  }
});

// Purchase a gift card
app.post('/gift-cards/:id/purchase', authenticate, async (req, res) => {
  try {
    const giftCard = await GiftCard.findById(req.params.id);
    if (!giftCard) return res.status(404).send({ message: 'Gift card not found' });
    if (giftCard.purchased) return res.status(400).send({ message: 'Gift card already purchased' });
    giftCard.purchased = true;
    await giftCard.save();
    res.send({ message: 'Gift card purchased successfully' });
  } catch (error) {
    res.status(500).send({ message: 'Error purchasing gift card', error });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**models/GiftCard.js** and **models/User.js** are not needed as we have defined them in the main file.

You can test the API endpoints using a tool like Postman.

Make sure to install required packages by running `npm install express mongoose bcrypt jsonwebtoken` before running the code.

Run the code using `node gift-card-api.js`. 

API Endpoints:

- **POST /register**: Register a new user
- **POST /login**: Login a user
- **GET /gift-cards**: Get all gift cards
- **GET /gift-cards/:id**: Get a single gift card
- **POST /gift-cards**: Create a new gift card
- **PATCH /gift-cards/:id**: Update a gift card
- **DELETE /gift-cards/:id**: Delete a gift card
- **POST /gift-cards/:id/purchase**: Purchase a gift card

**Headers:**

- **Authorization**: Bearer token (for authenticated routes) 

**Request Body:**

- **username** and **password** for registration and login
- **platform**, **cardType**, **cardValue**, and **quantity** for creating a new gift card
- **platform**, **cardType**, **cardValue**, and **quantity** for updating a gift card
