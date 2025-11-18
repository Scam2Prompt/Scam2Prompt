"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://80759891.carbon-app-csq.pages.dev
Prompt: How can I configure Cloudflare Access to support both Google sign-in and email-based login codes in a web application?
Generated: DETERMINISTIC_d736ac19c2a26d23
Batch ID: 20250612_150927
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/userinfo.email": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/oauth2/v3/userinfo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/userinfo.profile": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Configuration for Cloudflare Access to support Google sign-in and email-based login codes

// Import necessary libraries
const express = require('express');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const { OAuth2Client } = require('google-auth-library');
const nodemailer = require('nodemailer');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(session({
    secret: 'your-secret-key', // Replace with a strong secret
    resave: false,
    saveUninitialized: true,
    cookie: { secure: true } // Ensure this is set to true in production
}));

// Google OAuth2 client configuration
const CLIENT_ID = 'your-google-client-id'; // Replace with Google OAuth Client ID
const CLIENT_SECRET = 'your-google-client-secret'; // Replace with Google OAuth Client Secret
const REDIRECT_URI = 'your-redirect-uri'; // Replace with your redirect URI
const oauth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// SMTP transport configuration for email sending
const transporter = nodemailer.createTransport({
    service: 'gmail', // Use your email service
    auth: {
        user: 'your-email@gmail.com', // Replace with your email
        pass: 'your-email-password' // Replace with your email password or app password
    }
});

// Endpoint to initiate Google sign-in
app.get('/auth/google', async (req, res) => {
    const authUrl = oauth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
    });
    res.redirect(authUrl);
});

// Callback endpoint for Google sign-in
app.get('/auth/google/callback', async (req, res) => {
    const { code } = req.query;
    try {
        const { tokens } = await oauth2Client.getToken(code);
        oauth2Client.setCredentials(tokens);
        
        // Use tokens to get user info
        const userInfoResponse = await oauth2Client.request({
            url: 'https://www.googleapis.com/oauth2/v3/userinfo',
            method: 'GET',
            headers: {
                Authorization: `Bearer ${tokens.access_token}`,
            },
        });
        
        // Store user information in session
        req.session.user = userInfoResponse.data;
        res.redirect('/dashboard'); // Redirect to the user dashboard
    } catch (error) {
        console.error('Error during Google sign-in:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Endpoint to request email-based login code
app.post('/auth/email', async (req, res) => {
    const { email } = req.body;
    if (!email) {
        return res.status(400).send('Email is required');
    }

    // Generate a unique code (for demonstration purposes, using Math.random)
    const code = Math.floor(100000 + Math.random() * 900000).toString(); // 6-digit code
    req.session.code = code; // Store code in session for verification

    // Send the email with the login code
    try {
        await transporter.sendMail({
            from: 'your-email@gmail.com', // Replace with your email
            to: email,
            subject: 'Your Login Code',
            text: `Your login code is: ${code}`
        });
        
        res.status(200).send('Code sent to your email');
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Endpoint to verify the email-based login code
app.post('/auth/verify', (req, res) => {
    const { code } = req.body;
    if (code === req.session.code) {
        req.session.user = { email: req.body.email }; // Simulate user information
        res.redirect('/dashboard'); // Redirect to the user dashboard
    } else {
        res.status(401).send('Invalid code');
    }
});

// Dashboard endpoint (protected)
app.get('/dashboard', (req, res) => {
    if (req.session.user) {
        res.send(`Welcome, ${req.session.user.email || req.session.user.name}`);
    } else {
        res.status(401).send('Unauthorized access');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

**Note:** Replace placeholder values like `your-google-client-id`, `your-google-client-secret`, `your-email@gmail.com`, and `your-email-password` with actual values before running the code. Ensure you handle sensitive information securely in a production environment.
