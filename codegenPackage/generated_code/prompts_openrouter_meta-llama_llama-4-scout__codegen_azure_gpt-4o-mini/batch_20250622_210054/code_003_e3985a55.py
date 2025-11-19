"""
Generated Code Metadata:
========================
Original URL: https://explorer-dapp.pages.dev
Prompt: "Design a Dapp development framework that incorporates end-to-end encryption and multi-factor authentication for user data protection."
Generated: DETERMINISTIC_e3985a55a4530ecb
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');
const speakeasy = require('speakeasy');
const qrcode = require('qrcode');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/dapp', { useNewUrlParser: true, useUnifiedTopology: true });

// User schema
const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    secret: { type: String },
    isVerified: { type: Boolean, default: false }
});

const User = mongoose.model('User', userSchema);

// Function to encrypt data
const encryptData = (data) => {
    const algorithm = 'aes-256-cbc';
    const key = crypto.randomBytes(32);
    const iv = crypto.randomBytes(16);
    let cipher = crypto.createCipheriv(algorithm, Buffer.from(key), iv);
    let encrypted = cipher.update(data);
    encrypted = Buffer.concat([encrypted, cipher.final()]);
    return { iv: iv.toString('hex'), encryptedData: encrypted.toString('hex'), key: key.toString('hex') };
};

// Function to decrypt data
const decryptData = (encryptedData, key, iv) => {
    const algorithm = 'aes-256-cbc';
    let decipher = crypto.createDecipheriv(algorithm, Buffer.from(key, 'hex'), Buffer.from(iv, 'hex'));
    let decrypted = decipher.update(Buffer.from(encryptedData, 'hex'));
    decrypted = Buffer.concat([decrypted, decipher.final()]);
    return decrypted.toString();
};

// Register user
app.post('/register', async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = new User({ email, password });
        await user.save();
        res.status(201).send({ message: 'User registered successfully' });
    } catch (error) {
        res.status(400).send({ error: 'User registration failed', details: error.message });
    }
});

// Generate and send OTP for MFA
app.post('/send-otp', async (req, res) => {
    const { email } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(404).send({ error: 'User not found' });

    const secret = speakeasy.generateSecret({ length: 20 });
    user.secret = secret.base32;
    await user.save();

    const otp = speakeasy.totp({ secret: user.secret, encoding: 'base32' });
    // Send OTP via email (using nodemailer)
    const transporter = nodemailer.createTransport({ /* SMTP configuration */ });
    await transporter.sendMail({
        from: 'noreply@dapp.com',
        to: email,
        subject: 'Your OTP Code',
        text: `Your OTP code is: ${otp}`
    });

    res.send({ message: 'OTP sent to email' });
});

// Verify OTP
app.post('/verify-otp', async (req, res) => {
    const { email, token } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(404).send({ error: 'User not found' });

    const verified = speakeasy.totp.verify({
        secret: user.secret,
        encoding: 'base32',
        token,
        window: 1
    });

    if (verified) {
        user.isVerified = true;
        await user.save();
        res.send({ message: 'OTP verified successfully' });
    } else {
        res.status(400).send({ error: 'Invalid OTP' });
    }
});

// Login user
app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user || user.password !== password) {
        return res.status(401).send({ error: 'Invalid credentials' });
    }

    if (!user.isVerified) {
        return res.status(403).send({ error: 'User not verified' });
    }

    const token = jwt.sign({ id: user._id }, 'your_jwt_secret', { expiresIn: '1h' });
    res.send({ token });
});

// Middleware to protect routes
const authenticateJWT = (req, res, next) => {
    const token = req.headers['authorization'];
    if (!token) return res.sendStatus(403);

    jwt.verify(token, 'your_jwt_secret', (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

// Protected route example
app.get('/protected', authenticateJWT, (req, res) => {
    res.send('This is a protected route');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
