"""
Generated Code Metadata:
========================
Original URL: https://getrise.pro
Prompt: Suggest tools and frameworks for developing a JavaScript-based application similar to RainBNB, emphasizing scalability and performance.
Generated: DETERMINISTIC_46012e9d25e14661
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Suggested tools and frameworks for developing a JavaScript-based application similar to RainBNB.
 * 
 * @author [Your Name]
 */

// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');
const cors = require('cors');

// Initialize Express app
const app = express();

// Configure Express app
app.use(express.json());
app.use(helmet());
app.use(cors());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/rainbnb', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String
});

// Define listing schema
const listingSchema = new mongoose.Schema({
  title: String,
  description: String,
  price: Number,
  owner: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Listing = mongoose.model('Listing', listingSchema);

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating user', error: err });
  }
});

// Login user
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
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, {
      expiresIn: '1h'
    });
    res.send({ token });
  } catch (err) {
    res.status(400).send({ message: 'Error logging in', error: err });
  }
});

// Create listing
app.post('/listings', authenticate, async (req, res) => {
  try {
    const listing = new Listing({
      title: req.body.title,
      description: req.body.description,
      price: req.body.price,
      owner: req.user._id
    });
    await listing.save();
    res.status(201).send({ message: 'Listing created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating listing', error: err });
  }
});

// Authenticate middleware
function authenticate(req, res, next) {
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).send({ message: 'Access denied' });
  }
  try {
    const decoded = jwt.verify(token, process.env.SECRET_KEY);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(400).send({ message: 'Invalid token', error: err });
  }
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
