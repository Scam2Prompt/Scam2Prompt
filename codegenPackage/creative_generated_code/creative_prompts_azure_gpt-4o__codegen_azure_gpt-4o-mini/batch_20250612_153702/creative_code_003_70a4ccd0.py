"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-check.vercel.app
Prompt: Write a Node.js server-side script for a web application that could be part of Flare Global Soft's IT services offerings. Include basic API endpoints for user authentication.
Generated: DETERMINISTIC_70a4ccd0d1a043d4
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bcrypt = require('bcrypt'); // Password hashing library
const jwt = require('jsonwebtoken'); // JWT library for authentication
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
require('dotenv').config(); // Load environment variables from .env file

// Initialize express app
const app = express();

// Middleware
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

// User model
const User = mongoose.model('User', userSchema);

// API endpoint for user registration
app.post('/api/register', async (req, res) => {
    const { username, password } = req.body;

    // Validate input
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required' });
    }

    try {
        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);
        // Create new user
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        // Handle errors
        res.status(500).json({ message: 'Error registering user', error: error.message });
    }
});

// API endpoint for user login
app.post('/api/login', async (req, res) => {
    const { username, password } = req.body;

    // Validate input
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required' });
    }

    try {
        // Find user by username
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(401).json({ message: 'Invalid username or password' });
        }

        // Compare passwords
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(401).json({ message: 'Invalid username or password' });
        }

        // Generate JWT
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.status(200).json({ message: 'Login successful', token });
    } catch (error) {
        // Handle errors
        res.status(500).json({ message: 'Error logging in', error: error.message });
    }
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### Instructions to run the code:
1. Ensure you have Node.js installed on your machine.
2. Create a new directory for your project and navigate into it.
3. Run `npm init -y` to create a `package.json` file.
4. Install the required dependencies:
   ```bash
   npm install express mongoose bcrypt jsonwebtoken body-parser dotenv
   ```
5. Create a `.env` file in your project root with the following variables:
   ```
   MONGO_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret
   ```
6. Save the script in a file (e.g., `server.js`).
7. Run the server using:
   ```bash
   node server.js
   ```
8. You can interact with the API using Postman or any HTTP client.
