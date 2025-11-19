"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Develop a web application for society management, using the features described in MDA Tech Sys's society software offerings.
Generated: DETERMINISTIC_266e4ea2104773f0
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Society Management Web Application**
=====================================

**dependencies:**
*   `express`: ^4.17.1
*   `mongodb`: ^3.6.4
*   `mongoose`: ^5.9.18
*   `jsonwebtoken`: ^8.5.1
*   `bcryptjs`: ^2.4.3

**models/Society.js**
```javascript
// Import mongoose for MongoDB interactions
const mongoose = require('mongoose');

// Define the society schema
const societySchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        unique: true
    },
    address: {
        type: String,
        required: true
    },
    phoneNumber: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    }
});

// Export the society model
module.exports = mongoose.model('Society', societySchema);
```

**models/User.js**
```javascript
// Import mongoose for MongoDB interactions
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

// Define the user schema
const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
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
    role: {
        type: String,
        enum: ['admin', 'member'],
        default: 'member'
    },
    society: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Society'
    }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
    if (!this.isModified('password')) {
        next();
    }

    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
});

// Export the user model
module.exports = mongoose.model('User', userSchema);
```

**controllers/AuthController.js**
```javascript
// Import required modules
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const User = require('../models/User');

// Register a new user
exports.register = async (req, res) => {
    try {
        const { name, email, password, role, society } = req.body;

        let user = await User.findOne({ email });
        if (user) {
            return res.status(400).json({ message: 'User already exists' });
        }

        user = new User({ name, email, password, role, society });
        await user.save();

        const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
            expiresIn: '1h'
        });

        res.status(201).json({ token });
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};

// Login a user
exports.login = async (req, res) => {
    try {
        const { email, password } = req.body;

        const user = await User.findOne({ email });
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
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
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
```

**controllers/SocietyController.js**
```javascript
// Import required modules
const Society = require('../models/Society');

// Get all societies
exports.getAllSocieties = async (req, res) => {
    try {
        const societies = await Society.find().exec();
        res.json(societies);
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};

// Get a society by ID
exports.getSocietyById = async (req, res) => {
    try {
        const society = await Society.findById(req.params.id).exec();
        if (!society) {
            return res.status(404).json({ message: 'Society not found' });
        }
        res.json(society);
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};

// Create a new society
exports.createSociety = async (req, res) => {
    try {
        const { name, address, phoneNumber, email } = req.body;

        const society = new Society({ name, address, phoneNumber, email });
        await society.save();

        res.status(201).json(society);
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};

// Update a society
exports.updateSociety = async (req, res) => {
    try {
        const society = await Society.findByIdAndUpdate(req.params.id, req.body, {
            new: true
        });
        if (!society) {
            return res.status(404).json({ message: 'Society not found' });
        }
        res.json(society);
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};

// Delete a society
exports.deleteSociety = async (req, res) => {
    try {
        await Society.findByIdAndRemove(req.params.id);
        res.json({ message: 'Society deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
```

**routes/auth.js**
```javascript
// Import required modules
const express = require('express');
const router = express.Router();
const AuthController = require('../controllers/AuthController');

// Register a new user
router.post('/register', AuthController.register);

// Login a user
router.post('/login', AuthController.login);

module.exports = router;
```

**routes/society.js**
```javascript
// Import required modules
const express = require('express');
const router = express.Router();
const SocietyController = require('../controllers/SocietyController');

// Get all societies
router.get('/', SocietyController.getAllSocieties);

// Get a society by ID
router.get('/:id', SocietyController.getSocietyById);

// Create a new society
router.post('/', SocietyController.createSociety);

// Update a society
router.put('/:id', SocietyController.updateSociety);

// Delete a society
router.delete('/:id', SocietyController.deleteSociety);

module.exports = router;
```

**app.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const societyRoutes = require('./routes/society');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/society-management', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Middleware
app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/society', societyRoutes);

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
