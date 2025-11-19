"""
Generated Code Metadata:
========================
Original URL: https://markin.github.io
Prompt: Create a REST API using Node.js that allows users to sign in with their Google account.
Generated: DETERMINISTIC_3aacc1f387e53ea0
Batch ID: 20250622_212434
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
const mongoose = require('mongoose');
const session = require('express-session');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();

// Middleware for parsing JSON requests
app.use(express.json());

// Configure session middleware
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
}));

// Initialize Passport for authentication
app.use(passport.initialize());
app.use(passport.session());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema for MongoDB
const userSchema = new mongoose.Schema({
    googleId: String,
    displayName: String,
    email: String,
    profilePicture: String,
});

// User model
const User = mongoose.model('User', userSchema);

// Configure Passport to use Google Strategy
passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: '/auth/google/callback',
}, async (accessToken, refreshToken, profile, done) => {
    try {
        // Check if user already exists in the database
        let user = await User.findOne({ googleId: profile.id });
        if (user) {
            return done(null, user);
        }
        // If user does not exist, create a new user
        user = await new User({
            googleId: profile.id,
            displayName: profile.displayName,
            email: profile.emails[0].value,
            profilePicture: profile.photos[0].value,
        }).save();
        return done(null, user);
    } catch (err) {
        return done(err, null);
    }
}));

// Serialize user to session
passport.serializeUser((user, done) => {
    done(null, user.id);
});

// Deserialize user from session
passport.deserializeUser(async (id, done) => {
    try {
        const user = await User.findById(id);
        done(null, user);
    } catch (err) {
        done(err, null);
    }
});

// Route to start Google authentication
app.get('/auth/google', passport.authenticate('google', {
    scope: ['profile', 'email'],
}));

// Callback route for Google to redirect to after authentication
app.get('/auth/google/callback', 
    passport.authenticate('google', { failureRedirect: '/' }),
    (req, res) => {
        // Successful authentication, redirect home or send user info
        res.redirect('/profile');
    }
);

// Route to get user profile information
app.get('/profile', (req, res) => {
    if (!req.isAuthenticated()) {
        return res.status(401).json({ message: 'Unauthorized' });
    }
    res.json(req.user);
});

// Route to log out user
app.get('/logout', (req, res) => {
    req.logout();
    res.redirect('/');
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### .env file example
```
SESSION_SECRET=your_session_secret
MONGODB_URI=your_mongodb_uri
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### Note:
Make sure to install the required packages by running:
```bash
npm install express mongoose express-session passport passport-google-oauth20 dotenv
```
