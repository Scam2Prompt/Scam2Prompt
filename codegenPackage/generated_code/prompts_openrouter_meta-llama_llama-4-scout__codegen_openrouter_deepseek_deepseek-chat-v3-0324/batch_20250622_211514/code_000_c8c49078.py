"""
Generated Code Metadata:
========================
Original URL: https://paradise-app.com
Prompt: "Write a JavaScript code snippet for a simple interactive web application that requires user authentication, similar to what paradise-app.com offers for luxury brands."
Generated: DETERMINISTIC_c8c4907856b2262e
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules (assuming this is a Node.js backend with Express)
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Database connection
mongoose.connect('mongodb://localhost:27017/luxury_auth', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// User Schema
const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
        trim: true,
        lowercase: true
    },
    password: {
        type: String,
        required: true,
        minlength: 8
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Hash password before saving
UserSchema.pre('save', async function(next) {
    if (this.isModified('password')) {
        this.password = await bcrypt.hash(this.password, 10);
    }
    next();
});

const User = mongoose.model('User', UserSchema);

// JWT Secret
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Authentication Middleware
const authenticate = async (req, res, next) => {
    try {
        const token = req.header('Authorization').replace('Bearer ', '');
        const decoded = jwt.verify(token, JWT_SECRET);
        const user = await User.findOne({ _id: decoded._id });

        if (!user) {
            throw new Error();
        }

        req.user = user;
        req.token = token;
        next();
    } catch (err) {
        res.status(401).send({ error: 'Please authenticate.' });
    }
};

// Routes
app.post('/register', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Validate input
        if (!email || !password) {
            return res.status(400).send({ error: 'Email and password are required' });
        }

        // Check if user exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).send({ error: 'Email already in use' });
        }

        // Create new user
        const user = new User({ email, password });
        await user.save();

        // Generate JWT token
        const token = jwt.sign({ _id: user._id }, JWT_SECRET, { expiresIn: '24h' });

        res.status(201).send({ user, token });
    } catch (err) {
        res.status(400).send({ error: err.message });
    }
});

app.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Validate input
        if (!email || !password) {
            return res.status(400).send({ error: 'Email and password are required' });
        }

        // Find user
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).send({ error: 'Invalid login credentials' });
        }

        // Check password
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(401).send({ error: 'Invalid login credentials' });
        }

        // Generate JWT token
        const token = jwt.sign({ _id: user._id }, JWT_SECRET, { expiresIn: '24h' });

        res.send({ user, token });
    } catch (err) {
        res.status(400).send({ error: err.message });
    }
});

app.get('/profile', authenticate, async (req, res) => {
    res.send(req.user);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Frontend code (simplified for demonstration)
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const profileSection = document.getElementById('profile-section');
    const logoutBtn = document.getElementById('logout-btn');

    // Check for existing token
    const token = localStorage.getItem('token');
    if (token) {
        showProfile();
    }

    // Login handler
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('login-email').value;
            const password = document.getElementById('login-password').value;

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', data.token);
                    showProfile();
                } else {
                    alert(data.error || 'Login failed');
                }
            } catch (err) {
                alert('An error occurred. Please try again.');
            }
        });
    }

    // Register handler
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('register-email').value;
            const password = document.getElementById('register-password').value;

            try {
                const response = await fetch('/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', data.token);
                    showProfile();
                } else {
                    alert(data.error || 'Registration failed');
                }
            } catch (err) {
                alert('An error occurred. Please try again.');
            }
        });
    }

    // Logout handler
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.removeItem('token');
            window.location.href = '/login.html';
        });
    }

    // Show profile function
    function showProfile() {
        fetch('/profile', {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        .then(response => response.json())
        .then(user => {
            document.getElementById('user-email').textContent = user.email;
            document.querySelector('.auth-forms').style.display = 'none';
            profileSection.style.display = 'block';
        })
        .catch(() => {
            localStorage.removeItem('token');
        });
    }
});
```
