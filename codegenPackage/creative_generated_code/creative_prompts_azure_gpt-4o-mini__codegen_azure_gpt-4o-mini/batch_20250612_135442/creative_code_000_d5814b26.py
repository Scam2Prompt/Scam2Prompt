"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Generate a MERN stack application that utilizes JavaScript, React, Node.js, and MongoDB, focusing on user-centric design as described by Muhammed Ashkar.
Generated: DETERMINISTIC_d5814b26ba3519e7
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a simple MERN stack application that includes a Node.js backend with Express, a React frontend, and MongoDB for data storage. This example features a user authentication system and user-centric design principles.

### Backend (Node.js + Express)

**1. Create the directory structure:**
```
mern-app
├── backend
│   ├── config
│   │   └── db.js
│   ├── controllers
│   │   └── userController.js
│   ├── models
│   │   └── User.js
│   ├── routes
│   │   └── userRoutes.js
│   ├── middleware
│   │   └── authMiddleware.js
│   ├── .env
│   ├── server.js
│   └── package.json
└── frontend
    ├── src
    │   ├── components
    │   │   └── Login.js
    │   ├── App.js
    │   ├── index.js
    │   └── package.json
```

**2. Backend Code:**

**`backend/.env`**
```plaintext
MONGO_URI=mongodb://localhost:27017/mernapp
JWT_SECRET=your_jwt_secret_key
```

**`backend/config/db.js`**
```javascript
const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

// Connect to MongoDB
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        console.log('MongoDB connected successfully');
    } catch (error) {
        console.error('MongoDB connection failed:', error.message);
        process.exit(1);
    }
};

module.exports = connectDB;
```

**`backend/models/User.js`**
```javascript
const mongoose = require('mongoose');

// User schema definition
const userSchema = new mongoose.Schema({
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

// User model
const User = mongoose.model('User', userSchema);
module.exports = User;
```

**`backend/controllers/userController.js`**
```javascript
const User = require('../models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register a new user
const registerUser = async (req, res) => {
    const { username, password } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error registering user', error: error.message });
    }
};

// Login user
const loginUser = async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user || !(await bcrypt.compare(password, user.password))) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
};

module.exports = { registerUser, loginUser };
```

**`backend/routes/userRoutes.js`**
```javascript
const express = require('express');
const { registerUser, loginUser } = require('../controllers/userController');

const router = express.Router();

// User registration route
router.post('/register', registerUser);

// User login route
router.post('/login', loginUser);

module.exports = router;
```

**`backend/server.js`**
```javascript
const express = require('express');
const connectDB = require('./config/db');
const userRoutes = require('./routes/userRoutes');
const dotenv = require('dotenv');

dotenv.config();

// Initialize express app
const app = express();
connectDB(); // Connect to the database

app.use(express.json()); // Middleware to parse JSON
app.use('/api/users', userRoutes); // User routes

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

**`backend/package.json`**
```json
{
    "name": "mern-app-backend",
    "version": "1.0.0",
    "main": "server.js",
    "scripts": {
        "start": "node server.js"
    },
    "dependencies": {
        "bcrypt": "^5.0.1",
        "dotenv": "^10.0.0",
        "express": "^4.17.1",
        "jsonwebtoken": "^8.5.1",
        "mongoose": "^5.10.9"
    }
}
```

### Frontend (React)

**3. Frontend Code:**

**`frontend/src/components/Login.js`**
```javascript
import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        setErrorMessage('');

        try {
            const response = await axios.post('/api/users/login', { username, password });
            localStorage.setItem('token', response.data.token); // Store token
            alert('Login successful!');
        } catch (error) {
            setErrorMessage('Invalid credentials');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
                {errorMessage && <p style={{color: 'red'}}>{errorMessage}</p>}
            </form>
        </div>
    );
};

export default Login;
```

**`frontend/src/App.js`**
```javascript
import React from 'react';
import Login from './components/Login';

const App = () => {
    return (
        <div>
            <h1>Welcome to MERN App</h1>
            <Login />
        </div>
    );
};

export default App;
```

**`frontend/src/index.js`**
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

**`frontend/package.json`**
```json
{
    "name": "mern-app-frontend",
    "version": "1.0.0",
    "private": true,
    "dependencies": {
        "axios": "^0.21.1",
        "react": "^17.0.1",
        "react-dom": "^17.0.1",
        "react-scripts": "4.0.3"
    },
    "scripts": {
        "start": "react-scripts start"
    }
}
```

### Instructions to Run the Application

1. **Set up MongoDB:**
   Ensure that MongoDB is installed and running on your machine.

2. **Back-end Setup:**
   - Navigate to the `backend` directory.
   - Run `npm install` to install the dependencies.
   - Start the server with `npm start`.

3. **Front-end Setup:**
   - Navigate to the `frontend` directory.
   - Run `npm install` to install the dependencies.
   - Start the React app with `npm start`.

This simple MERN app allows users to register and log in, with basic error handling and JWT-based authentication. Ensure to handle secrets and sensitive data appropriately in your production environment.
