"""
Generated Code Metadata:
========================
Original URL: https://info-dex.com
Prompt: Design a login system with a password recovery mechanism using a specific programming framework (e.g., React, Angular, Vue.js).
Generated: DETERMINISTIC_fd938ce8e96508ff
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// React Login System with Password Recovery
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginSystem = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isRecoveryMode, setIsRecoveryMode] = useState(false);
  const [recoveryEmail, setRecoveryEmail] = useState('');
  const [recoveryMessage, setRecoveryMessage] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/auth/login', { email, password });
      localStorage.setItem('token', response.data.token);
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    }
  };

  const handlePasswordRecovery = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/auth/recover', { email: recoveryEmail });
      setRecoveryMessage('Password recovery email sent. Please check your inbox.');
    } catch (err) {
      setRecoveryMessage(err.response?.data?.message || 'Recovery failed');
    }
  };

  return (
    <div className="login-container">
      {!isRecoveryMode ? (
        <form onSubmit={handleLogin}>
          <h2>Login</h2>
          {error && <div className="error-message">{error}</div>}
          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">Login</button>
          <button
            type="button"
            className="recovery-link"
            onClick={() => setIsRecoveryMode(true)}
          >
            Forgot Password?
          </button>
        </form>
      ) : (
        <form onSubmit={handlePasswordRecovery}>
          <h2>Password Recovery</h2>
          {recoveryMessage && <div className="info-message">{recoveryMessage}</div>}
          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              value={recoveryEmail}
              onChange={(e) => setRecoveryEmail(e.target.value)}
              required
            />
          </div>
          <button type="submit">Recover Password</button>
          <button
            type="button"
            className="back-link"
            onClick={() => setIsRecoveryMode(false)}
          >
            Back to Login
          </button>
        </form>
      )}
    </div>
  );
};

export default LoginSystem;
```

```javascript
// Backend API (Node.js/Express)
const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const User = require('../models/User');
const sendEmail = require('../utils/email');

// Login endpoint
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    // Validate input
    if (!email || !password) {
      return res.status(400).json({ message: 'Please provide email and password' });
    }

    // Check if user exists
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Validate password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Generate JWT token
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h'
    });

    res.json({ token });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Server error' });
  }
});

// Password recovery endpoint
router.post('/recover', async (req, res) => {
  try {
    const { email } = req.body;
    
    // Validate input
    if (!email) {
      return res.status(400).json({ message: 'Please provide email' });
    }

    // Check if user exists
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    // Generate reset token
    const resetToken = crypto.randomBytes(20).toString('hex');
    user.resetPasswordToken = crypto
      .createHash('sha256')
      .update(resetToken)
      .digest('hex');
    user.resetPasswordExpire = Date.now() + 3600000; // 1 hour
    await user.save();

    // Send email
    const resetUrl = `${req.protocol}://${req.get('host')}/reset-password/${resetToken}`;
    await sendEmail({
      email: user.email,
      subject: 'Password Reset Request',
      message: `You are receiving this email because you requested a password reset. Please make a PUT request to: \n\n ${resetUrl}`
    });

    res.json({ message: 'Email sent' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Server error' });
  }
});

module.exports = router;
```

```javascript
// Email utility
const nodemailer = require('nodemailer');

const sendEmail = async (options) => {
  // Create transporter
  const transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASSWORD
    }
  });

  // Define email options
  const mailOptions = {
    from: process.env.FROM_EMAIL,
    to: options.email,
    subject: options.subject,
    text: options.message
  };

  // Send email
  await transporter.sendMail(mailOptions);
};

module.exports = sendEmail;
```
