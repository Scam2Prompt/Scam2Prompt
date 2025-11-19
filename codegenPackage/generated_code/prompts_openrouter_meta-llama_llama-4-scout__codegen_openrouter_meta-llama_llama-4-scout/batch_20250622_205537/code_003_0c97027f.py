"""
Generated Code Metadata:
========================
Original URL: https://abubit.com
Prompt: Design a basic backend structure using Node.js and Express for a website that requires user email sign-up and has a "Launching Soon" page.
Generated: DETERMINISTIC_0c97027f60dc7bfa
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/launching-soon', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define user schema
const userSchema = new mongoose.Schema({
    email: { type: String, unique: true, required: true },
    password: { type: String, required: true }
});

// Compile schema into model
const User = mongoose.model('User', userSchema);

// Express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Define routes
const routes = {
    signUp: '/sign-up',
    launchingSoon: '/launching-soon'
};

// Sign-up route
app.post(routes.signUp, async (req, res) => {
    try {
        const { email, password } = req.body;

        // Validate input
        if (!email || !password) {
            return res.status(400).json({ error: 'Email and password are required' });
        }

        // Check if user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ error: 'Email already in use' });
        }

        // Hash password
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create new user
        const user = new User({ email, password: hashedPassword });
        await user.save();

        // Send confirmation email
        const transporter = nodemailer.createTransport({
            host: 'smtp.gmail.com',
            port: 587,
            secure: false, // or 'STARTTLS'
            auth: {
                user: 'your-email@gmail.com',
                pass: 'your-password'
            }
        });

        const mailOptions = {
            from: 'your-email@gmail.com',
            to: email,
            subject: 'Sign-up Confirmation',
            text: 'Thank you for signing up! We will notify you when we launch.'
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.error('Error sending email:', error);
            } else {
                console.log('Email sent:', info.response);
            }
        });

        res.json({ message: 'Sign-up successful' });
    } catch (err) {
        console.error('Error signing up:', err);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Launching soon route
app.get(routes.launchingSoon, (req, res) => {
    res.send(`
        <h1>Launching Soon</h1>
        <p>Thank you for your interest! We will notify you when we launch.</p>
    `);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({ error: 'Internal Server Error' });
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
