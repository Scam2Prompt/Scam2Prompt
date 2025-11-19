"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Develop a REST API that enables fans to upload and share short video "Grooves" promoting their favorite artist's songs, while earning tokenized rewards ($GROOVE).
Generated: DETERMINISTIC_73995249f5d7c1a8
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Groove API**
===============

**dependencies**
---------------

* `express`: ^4.17.1
* `multer`: ^1.4.2
* `mongodb`: ^3.6.4
* `jsonwebtoken`: ^8.5.1
* `bcryptjs`: ^2.4.3

**groove.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define Groove model
const grooveSchema = new mongoose.Schema({
  video: {
    type: Buffer,
    required: true
  },
  artist: {
    type: String,
    required: true
  },
  song: {
    type: String,
    required: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  rewards: {
    type: Number,
    default: 0
  },
  likes: {
    type: Number,
    default: 0
  },
  comments: {
    type: Number,
    default: 0
  }
});

// Export Groove model
module.exports = mongoose.model('Groove', grooveSchema);
```

**user.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

// Define User model
const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true
  },
  wallet: {
    type: Number,
    default: 0
  }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();

  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
});

// Export User model
module.exports = mongoose.model('User', userSchema);
```

**auth.controller.js**
```javascript
// Import User model, jsonwebtoken, and bcryptjs
const User = require('./user.model');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Register user
exports.register = async (req, res) => {
  try {
    const { username, email, password } = req.body;

    const existingUser = await User.findOne({ email });
    if (existingUser) return res.status(400).json({ message: 'Email already exists' });

    const user = new User({ username, email, password });
    await user.save();

    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h'
    });

    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

// Login user
exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email });
    if (!user) return res.status(401).json({ message: 'Invalid credentials' });

    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) return res.status(401).json({ message: 'Invalid credentials' });

    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h'
    });

    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};
```

**groove.controller.js**
```javascript
// Import Groove model, User model, and multer
const Groove = require('./groove.model');
const User = require('./user.model');
const multer = require('multer');

// Initialize multer
const upload = multer({ dest: './uploads/' });

// Create groove
exports.createGroove = upload.single('video'), async (req, res) => {
  try {
    const { artist, song } = req.body;
    const userId = req.user._id;

    const groove = new Groove({
      video: req.file.buffer,
      artist,
      song,
      user: userId
    });

    await groove.save();

    // Add rewards to user's wallet
    const user = await User.findById(userId);
    user.wallet += 10; // $GROOVE token
    await user.save();

    res.json({ message: 'Groove created successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

// Get all grooves
exports.getGrooves = async (req, res) => {
  try {
    const grooves = await Groove.find().populate('user', '_id username');
    res.json(grooves);
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

// Like groove
exports.likeGroove = async (req, res) => {
  try {
    const grooveId = req.params.id;

    const groove = await Groove.findById(grooveId);
    if (!groove) return res.status(404).json({ message: 'Groove not found' });

    groove.likes++;
    await groove.save();

    res.json({ message: 'Groove liked successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};
```

**app.js**
```javascript
// Import express, mongoose, and routes
const express = require('express');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const grooveRoutes = require('./routes/groove');

// Initialize express
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost/groove-api', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/grooves', grooveRoutes);

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**routes/auth.js**
```javascript
// Import express and auth controller
const express = require('express');
const router = express.Router();
const authController = require('../controllers/auth.controller');

// Register user
router.post('/register', authController.register);

// Login user
router.post('/login', authController.login);

module.exports = router;
```

**routes/groove.js**
```javascript
// Import express, groove controller, and authenticate middleware
const express = require('express');
const router = express.Router();
const grooveController = require('../controllers/groove.controller');
const authenticate = require('../middleware/authenticate');

// Create groove
router.post('/create', authenticate, grooveController.createGroove);

// Get all grooves
router.get('/', grooveController.getGrooves);

// Like groove
router.patch('/:id/like', authenticate, grooveController.likeGroove);

module.exports = router;
```

**middleware/authenticate.js**
```javascript
// Import jsonwebtoken
const jwt = require('jsonwebtoken');

// Authenticate middleware
exports.authenticate = async (req, res, next) => {
  try {
    const token = req.header('Authorization').replace('Bearer ', '');
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ message: 'Please authenticate' });
  }
};
```
