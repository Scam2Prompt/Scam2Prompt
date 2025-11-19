"""
Generated Code Metadata:
========================
Original URL: https://member.bmtours.id
Prompt: Create a RESTful API using Node.js to handle user registration, login, and password reset for a tour management system.
Generated: DETERMINISTIC_aaff336fa110950f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Authentication API**
==========================

**dependencies:**
* `express`: ^4.17.1
* `mongodb`: ^3.6.3
* `bcrypt`: ^5.0.1
* `jsonwebtoken`: ^8.5.1

**user.model.js**
```javascript
// Import required modules
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

// Define user schema
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (this.isNew || this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

// Define user model
const User = mongoose.model('User', userSchema);

module.exports = User;
```

**auth.controller.js**
```javascript
// Import required modules
const express = require('express');
const router = express.Router();
const User = require('./user.model');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register user
router.post('/register', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: 'Email already exists' });
    }
    const user = new User({ name, email, password });
    await user.save();
    res.json({ message: 'User created successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Login user
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Reset password
router.patch('/reset-password', async (req, res) => {
  try {
    const { email, oldPassword, newPassword } = req.body;
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(oldPassword, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid old password' });
    }
    user.password = newPassword;
    await user.save();
    res.json({ message: 'Password updated successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
```

**app.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const authRouter = require('./auth.controller');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/tour-management', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.error('Error connecting to MongoDB:', error));

// Middleware
app.use(express.json());

// Routes
app.use('/api/auth', authRouter);

// Error handling
app.use((req, res) => {
  res.status(404).json({ message: 'Not Found' });
});

app.use((error, req, res) => {
  console.error(error);
  res.status(500).json({ message: 'Internal Server Error' });
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**.env**
```makefile
SECRET_KEY=your_secret_key_here
```

**package.json**
```json
{
  "name": "tour-management-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "bcrypt": "^5.0.1",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "mongodb": "^3.6.3",
    "mongoose": "^5.12.3"
  }
}
```
