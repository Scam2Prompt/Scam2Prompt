"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Develop a Node.js application that integrates Immediate GPT's registration process with a backend database to store user information securely.
Generated: DETERMINISTIC_7aa1eb209e5b132d
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
require('dotenv').config();

// Create an instance of Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Connect to MongoDB database
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define user schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

// User model
const User = mongoose.model('User', userSchema);

// Endpoint to register a new user
app.post('/register', async (req, res) => {
    const { username, email, password } = req.body;

    try {
        // Check if all fields are present
        if (!username || !email || !password) {
            return res.status(400).json({ message: 'All fields are required.' });
        }

        // Check if user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(409).json({ message: 'User already exists.' });
        }

        // Hash the password before saving
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create a new user
        const newUser = new User({
            username,
            email,
            password: hashedPassword,
        });

        // Save the new user to the database
        await newUser.save();

        // Respond with success message
        return res.status(201).json({ message: 'User registered successfully.' });
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Internal server error.' });
    }
});

// Endpoint to login a user
app.post('/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        // Check if all fields are present
        if (!email || !password) {
            return res.status(400).json({ message: 'All fields are required.' });
        }

        // Find user by email
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(401).json({ message: 'Invalid credentials.' });
        }

        // Compare provided password with hashed password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ message: 'Invalid credentials.' });
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });

        // Respond with success message and token
        return res.status(200).json({ message: 'Login successful.', token });
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```plaintext
// .env file content (example)
// MONGODB_URI=mongodb://localhost:27017/your_database_name
// JWT_SECRET=your_jwt_secret_key
```
