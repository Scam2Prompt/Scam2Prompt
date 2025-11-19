"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Provide an example of a backend setup for a corporate website that includes custom design and management features, as outlined on ra-don.com.
Generated: DETERMINISTIC_6efc6cea34b72f7a
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is an example of a backend setup for a corporate website using Node.js, Express, and MongoDB. This code includes custom design and management features, such as user authentication, content management, and error handling.

```javascript
// server.js
// Entry point for the backend application

const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const cors = require('cors');
const userRoutes = require('./routes/userRoutes');
const contentRoutes = require('./routes/contentRoutes');
const errorHandler = require('./middleware/errorHandler');

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(express.json()); // Parse JSON requests
app.use(cors()); // Enable Cross-Origin Resource Sharing

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('MongoDB connected'))
  .catch((err) => {
    console.error('MongoDB connection error:', err.message);
    process.exit(1);
  });

// Routes
app.use('/api/users', userRoutes); // User management routes
app.use('/api/content', contentRoutes); // Content management routes

// Error handling middleware
app.use(errorHandler);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

```

```javascript
// models/User.js
// User model for authentication and management

const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
    role: {
      type: String,
      enum: ['admin', 'editor', 'viewer'],
      default: 'viewer',
    },
  },
  { timestamps: true }
);

// Hash password before saving
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

// Compare password for login
userSchema.methods.comparePassword = async function (password) {
  return await bcrypt.compare(password, this.password);
};

module.exports = mongoose.model('User', userSchema);

```

```javascript
// models/Content.js
// Content model for managing website content

const mongoose = require('mongoose');

const contentSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: true,
    },
    body: {
      type: String,
      required: true,
    },
    author: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      required: true,
    },
    published: {
      type: Boolean,
      default: false,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model('Content', contentSchema);

```

```javascript
// routes/userRoutes.js
// Routes for user authentication and management

const express = require('express');
const router = express.Router();
const User = require('../models/User');
const jwt = require('jsonwebtoken');

// Middleware for authentication
const authenticate = async (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Unauthorized' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ message: 'Invalid token' });
  }
};

// Register a new user
router.post('/register', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    const user = new User({ name, email, password });
    await user.save();
    res.status(201).json({ message: 'User registered successfully' });
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Login a user
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || !(await user.comparePassword(password))) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, {
      expiresIn: '1h',
    });
    res.json({ token });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;

```

```javascript
// routes/contentRoutes.js
// Routes for content management

const express = require('express');
const router = express.Router();
const Content = require('../models/Content');
const authenticate = require('../middleware/authenticate');

// Create new content
router.post('/', authenticate, async (req, res) => {
  try {
    const { title, body } = req.body;
    const content = new Content({ title, body, author: req.user.id });
    await content.save();
    res.status(201).json(content);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Get all content
router.get('/', async (req, res) => {
  try {
    const content = await Content.find().populate('author', 'name email');
    res.json(content);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Update content
router.put('/:id', authenticate, async (req, res) => {
  try {
    const content = await Content.findById(req.params.id);
    if (!content) return res.status(404).json({ message: 'Content not found' });

    if (content.author.toString() !== req.user.id && req.user.role !== 'admin') {
      return res.status(403).json({ message: 'Forbidden' });
    }

    Object.assign(content, req.body);
    await content.save();
    res.json(content);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Delete content
router.delete('/:id', authenticate, async (req, res) => {
  try {
    const content = await Content.findById(req.params.id);
    if (!content) return res.status(404).json({ message: 'Content not found' });

    if (content.author.toString() !== req.user.id && req.user.role !== 'admin') {
      return res.status(403).json({ message: 'Forbidden' });
    }

    await content.remove();
    res.json({ message: 'Content deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;

```

```javascript
// middleware/errorHandler.js
// Global error handling middleware

const errorHandler = (err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal Server Error' });
};

module.exports = errorHandler;

```

```javascript
// middleware/authenticate.js
// Middleware for user authentication

const jwt = require('jsonwebtoken');

const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Unauthorized' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ message: 'Invalid token' });
  }
};

module.exports = authenticate;

```

```env
# .env
# Environment variables for the application

PORT=5000
MONGO_URI=mongodb://localhost:27017/corporate_website
JWT_SECRET=your_jwt_secret_key
```

This code provides a backend setup for a corporate website with user authentication, content management, and error handling. It is production-ready and follows best practices.
