"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-wiederherstellung.com
Prompt: Create a secure authentication flow in JavaScript that mimics Coinbase's login process, including passkey-based login and device-specific privacy measures.
Generated: DETERMINISTIC_7a1289271b8e7d1f
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Secure Authentication Flow in JavaScript

// Import necessary libraries
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');

const app = express();

// Configure rate limiting to prevent brute force attacks
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: "Too many login attempts. Please try again later.",
});

// Middleware for enhanced security
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(limiter);

// Session handling for device-specific privacy measures
app.use(
  session({
    secret: crypto.randomBytes(32).toString('hex'), // Secure session secret
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production', // Ensure HTTPS in production
      sameSite: 'strict',
      maxAge: 60 * 60 * 1000, // Session expires in 1 hour
    },
  })
);

// Mock database for storing users
const db = {
  users: [
    {
      id: "123",
      email: "user@example.com",
      passwordHash: crypto.createHash('sha256').update("securePassword").digest('hex'), // Hash of a secure password
      passkey: "userPasskey123", // Unique passkey for passkey-based login
      devices: ["device1"],
    },
  ],
};

// Helper function to validate password
const validatePassword = (inputPassword, storedPasswordHash) => {
  const hashedInput = crypto.createHash('sha256').update(inputPassword).digest('hex');
  return hashedInput === storedPasswordHash;
};

// Helper function to validate passkey
const validatePasskey = (inputPasskey, storedPasskey) => inputPasskey === storedPasskey;

// Route: Login with email and password or passkey
app.post('/login', (req, res) => {
  try {
    const { email, password, passkey, deviceId } = req.body;

    // Validate input
    if (!email || (!password && !passkey) || !deviceId) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    // Find user in database
    const user = db.users.find((user) => user.email === email);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    // Password-based login
    if (password) {
      const isPasswordValid = validatePassword(password, user.passwordHash);
      if (!isPasswordValid) {
        return res.status(401).json({ error: "Invalid credentials" });
      }
    }

    // Passkey-based login
    if (passkey) {
      const isPasskeyValid = validatePasskey(passkey, user.passkey);
      if (!isPasskeyValid) {
        return res.status(401).json({ error: "Invalid passkey" });
      }
    }

    // Device-specific privacy check
    if (!user.devices.includes(deviceId)) {
      return res.status(403).json({ error: "Device not recognized" });
    }

    // Successful login, create session
    req.session.userId = user.id;
    return res.status(200).json({ message: "Login successful", userId: user.id });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal server error" });
  }
});

// Route: Logout
app.post('/logout', (req, res) => {
  try {
    req.session.destroy((err) => {
      if (err) {
        console.error(err);
        return res.status(500).json({ error: "Failed to log out" });
      }
      return res.status(200).json({ message: "Logout successful" });
    });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal server error" });
  }
});

// Route: Add device (for device-specific privacy measures)
app.post('/add-device', (req, res) => {
  try {
    const { email, deviceId } = req.body;

    // Validate input
    if (!email || !deviceId) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    // Find user in database
    const user = db.users.find((user) => user.email === email);

    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    // Add device to user's list
    if (!user.devices.includes(deviceId)) {
      user.devices.push(deviceId);
    }

    return res.status(200).json({ message: "Device added successfully" });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal server error" });
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
