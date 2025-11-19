"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-cys.pages.dev
Prompt: Develop a Node.js application that allows users to sign up for updates on the $ROOST project, ensuring to handle user data securely.
Generated: DETERMINISTIC_bf5385d78cdd8932
Batch ID: 20250612_163443
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
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const dotenv = require('dotenv');
const nodemailer = require('nodemailer');
const { body, validationResult } = require('express-validator');

// Load environment variables from .env file
dotenv.config();

// Initialize express app
const app = express();

// Middleware setup
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});

// Create user model
const User = mongoose.model('User', userSchema);

// Email transport setup
const transporter = nodemailer.createTransport({
    service: 'gmail', // Use your email service
    auth: {
        user: process.env.EMAIL_USER, // Your email
        pass: process.env.EMAIL_PASS, // Your email password
    },
});

// Signup route
app.post('/signup', [
    body('email').isEmail().withMessage('Invalid email format'),
    body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters long'),
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { email, password } = req.body;

    try {
        // Check if user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const newUser = new User({ email, password: hashedPassword });
        await newUser.save();

        // Send confirmation email
        const mailOptions = {
            from: process.env.EMAIL_USER,
            to: email,
            subject: '$ROOST Project Updates Subscription',
            text: 'Thank you for signing up for updates on the $ROOST project!',
        };

        await transporter.sendMail(mailOptions);

        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        console.error('Error during signup:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Graceful shutdown on SIGINT (Ctrl+C)
process.on('SIGINT', () => {
    mongoose.connection.close(() => {
        console.log('MongoDB connection closed. Server shutting down.');
        process.exit(0);
    });
});
```

### .env File Example
```plaintext
MONGO_URI=mongodb://<username>:<password>@localhost:27017/<yourdbname>
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
PORT=3000
```

### Notes
1. Ensure to replace placeholders in the `.env` file with actual values.
2. Install the required packages using:
   ```bash
   npm install express mongoose body-parser bcrypt dotenv nodemailer express-validator
   ```
