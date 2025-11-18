"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Recommend libraries or APIs for building a web application that requires JavaScript to function properly, similar to the requirements indicated on the Step App domain page.
Generated: DETERMINISTIC_fdf506f2d71f3d5f
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const cors = require('cors'); // Middleware for enabling CORS
const morgan = require('morgan'); // HTTP request logger middleware

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies
app.use(morgan('dev')); // Log HTTP requests in development mode

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/myapp', { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => {
    console.error('MongoDB connection error:', err);
    process.exit(1); // Exit application if MongoDB connection fails
});

// Define a simple schema for a User
const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
});

// Create a model based on the schema
const User = mongoose.model('User', userSchema);

// API endpoint to create a new user
app.post('/api/users', async (req, res) => {
    try {
        const newUser = new User(req.body);
        const savedUser = await newUser.save();
        res.status(201).json(savedUser); // Respond with the created user
    } catch (error) {
        console.error('Error creating user:', error);
        res.status(400).json({ error: 'Unable to create user' }); // Error handling
    }
});

// API endpoint to get all users
app.get('/api/users', async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users); // Respond with the list of users
    } catch (error) {
        console.error('Error fetching users:', error);
        res.status(500).json({ error: 'Unable to fetch users' }); // Error handling
    }
});

// Set the application to listen on a specific port
const PORT = process.env.PORT || 3000; // Default to port 3000 if not specified
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log server start
});

// Export the app for testing or further development
module.exports = app;
```
