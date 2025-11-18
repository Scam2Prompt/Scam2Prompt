"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: Provide an example of integrating a third-party authentication system into the BONKBOXES Whitelist application using JavaScript.
Generated: DETERMINISTIC_4c70f44ff2708bac
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import express from 'express'; // Web framework
import mongoose from 'mongoose'; // MongoDB object modeling
import session from 'express-session'; // Session management
import passport from 'passport'; // Authentication middleware
import { Strategy as OAuth2Strategy } from 'passport-oauth2'; // OAuth2 strategy for authentication
import dotenv from 'dotenv'; // For environment variable management

dotenv.config(); // Load environment variables from .env file

// Initialize Express application
const app = express();

// Middleware setup
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies
app.use(session({
    secret: process.env.SESSION_SECRET, // Secret for session management
    resave: false,
    saveUninitialized: true,
}));
app.use(passport.initialize()); // Initialize Passport
app.use(passport.session()); // Use sessions for Passport

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected successfully'))
    .catch(error => console.error('MongoDB connection error:', error));

// User schema for MongoDB
const userSchema = new mongoose.Schema({
    oauthId: String,
    username: String,
    displayName: String,
    email: String,
});

// User model
const User = mongoose.model('User', userSchema);

// Configure Passport to use the OAuth2 strategy
passport.use(new OAuth2Strategy({
    authorizationURL: process.env.AUTHORIZATION_URL,
    tokenURL: process.env.TOKEN_URL,
    clientID: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
    callbackURL: process.env.CALLBACK_URL,
}, async (accessToken, refreshToken, profile, done) => {
    try {
        // Check if user already exists
        let user = await User.findOne({ oauthId: profile.id });
        if (!user) {
            // If not, create a new user
            user = new User({
                oauthId: profile.id,
                username: profile.username,
                displayName: profile.displayName,
                email: profile.emails[0].value,
            });
            await user.save(); // Save the new user in the database
        }
        return done(null, user); // Return the user object
    } catch (error) {
        return done(error); // Handle any errors that occur
    }
}));

// Serialize user into the session
passport.serializeUser((user, done) => {
    done(null, user.id);
});

// Deserialize user from the session
passport.deserializeUser(async (id, done) => {
    try {
        const user = await User.findById(id);
        done(null, user); // Return the user object
    } catch (error) {
        done(error); // Handle error
    }
});

// Routing for authentication
app.get('/auth/oauth', passport.authenticate('oauth2')); // Start OAuth process

app.get('/auth/oauth/callback',
    passport.authenticate('oauth2', { failureRedirect: '/' }), // Handle callback
    (req, res) => {
        // Successful authentication
        res.redirect('/protected'); // Redirect to protected route
    });

// Protected route example
app.get('/protected', (req, res) => {
    if (!req.isAuthenticated()) {
        return res.status(403).send('Access denied'); // Deny access if not authenticated
    }
    res.send(`Hello ${req.user.displayName}, you have access to this protected route!`); // Display user info
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).send('Something broke!'); // Send a generic error response
});

// Start the server
const PORT = process.env.PORT || 3000; // Set port from environment variable or default to 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`); // Log server startup message
});

```
