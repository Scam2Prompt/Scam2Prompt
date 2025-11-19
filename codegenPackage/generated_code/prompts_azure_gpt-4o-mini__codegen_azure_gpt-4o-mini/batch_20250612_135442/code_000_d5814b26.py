"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Generate a MERN stack application that utilizes JavaScript, React, Node.js, and MongoDB, focusing on user-centric design as described by Muhammed Ashkar.
Generated: DETERMINISTIC_d5814b26ba3519e7
Batch ID: 20250612_135442
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/api/auth/login": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/api/auth/register": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a simple MERN stack application that includes a basic user registration and login system. This example focuses on user-centric design principles.

### Backend (Node.js + Express + MongoDB)

**1. Create a new directory for your project and navigate into it:**
```bash
mkdir mern-user-auth
cd mern-user-auth
```

**2. Initialize a new Node.js project:**
```bash
npm init -y
```

**3. Install required packages:**
```bash
npm install express mongoose bcryptjs jsonwebtoken dotenv cors
```

**4. Create the following directory structure:**
```
mern-user-auth/
├── backend/
│   ├── config/
│   │   └── db.js
│   ├── models/
│   │   └── User.js
│   ├── routes/
│   │   └── auth.js
│   ├── .env
│   ├── server.js
└── frontend/
```

**5. Create the database connection file: `backend/config/db.js`:**
```javascript
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        console.log('MongoDB connected');
    } catch (error) {
        console.error('MongoDB connection failed:', error.message);
        process.exit(1); // Exit process with failure
    }
};

module.exports = connectDB;
```

**6. Create the User model: `backend/models/User.js`:**
```javascript
const mongoose = require('mongoose');

// User schema definition
const UserSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
    },
    password: {
        type: String,
        required: true,
    },
});

// Export the User model
module.exports = mongoose.model('User', UserSchema);
```

**7. Create authentication routes: `backend/routes/auth.js`:**
```javascript
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

const router = express.Router();

// Register a new user
router.post('/register', async (req, res) => {
    const { username, password } = req.body;

    try {
        // Check if user already exists
        let user = await User.findOne({ username });
        if (user) {
            return res.status(400).json({ msg: 'User already exists' });
        }

        // Create a new user
        user = new User({ username, password: await bcrypt.hash(password, 10) });
        await user.save();

        res.status(201).json({ msg: 'User registered successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ msg: 'Server error' });
    }
});

// Login user
router.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ msg: 'Invalid credentials' });
        }

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ msg: 'Invalid credentials' });
        }

        // Create and return JWT
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        console.error(error);
        res.status(500).json({ msg: 'Server error' });
    }
});

module.exports = router;
```

**8. Create the main server file: `backend/server.js`:**
```javascript
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db');
const authRoutes = require('./routes/auth');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to the database
connectDB();

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); // Parse JSON bodies

// Routes
app.use('/api/auth', authRoutes);

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

**9. Create a `.env` file in the `backend` directory:**
```
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
```

### Frontend (React)

**1. Navigate to the frontend directory and create a new React app:**
```bash
cd frontend
npx create-react-app .
```

**2. Install Axios for making HTTP requests:**
```bash
npm install axios
```

**3. Create a simple user interface: `frontend/src/App.js`:**
```javascript
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    // Handle user registration
    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('http://localhost:5000/api/auth/register', { username, password });
            setMessage(res.data.msg);
        } catch (error) {
            setMessage(error.response.data.msg);
        }
    };

    // Handle user login
    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('http://localhost:5000/api/auth/login', { username, password });
            setMessage('Login successful! Token: ' + res.data.token);
        } catch (error) {
            setMessage(error.response.data.msg);
        }
    };

    return (
        <div>
            <h1>User Authentication</h1>
            <form onSubmit={handleRegister}>
                <h2>Register</h2>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                <button type="submit">Register</button>
            </form>
            <form onSubmit={handleLogin}>
                <h2>Login</h2>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                <button type="submit">Login</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default App;
```

**4. Start the backend server:**
```bash
cd backend
node server.js
```

**5. Start the frontend React app:**
```bash
cd frontend
npm start
```

### Note:
- Replace `your_mongodb_connection_string` and `your_jwt_secret` in the `.env` file with your actual MongoDB connection string and a secret key for JWT.
- This is a basic implementation. For production, consider adding more features like input validation, user feedback, and enhanced security measures.
