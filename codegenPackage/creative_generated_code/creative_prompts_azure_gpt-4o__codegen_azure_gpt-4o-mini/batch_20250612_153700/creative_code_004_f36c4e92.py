"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Suggest tools or frameworks for developing a JavaScript-based presale app with secure payment integration and user authentication features.
Generated: DETERMINISTIC_f36c4e92d9db4450
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Framework for building web applications
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const session = require('express-session'); // Middleware for handling sessions
const passport = require('passport'); // Middleware for authentication
const LocalStrategy = require('passport-local').Strategy; // Local strategy for username and password authentication
const bcrypt = require('bcrypt'); // Library for hashing passwords
const Stripe = require('stripe'); // Library for Stripe payment integration

// Initialize application
const app = express();
const PORT = process.env.PORT || 3000;
const stripe = Stripe('YOUR_STRIPE_SECRET_KEY'); // Use your actual Stripe secret key

// Middleware configuration
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({ secret: 'your_secret_key', resave: false, saveUninitialized: true }));
app.use(passport.initialize());
app.use(passport.session());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/presaleApp', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// User schema definition
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

// User model
const User = mongoose.model('User', userSchema);

// Passport local strategy for user authentication
passport.use(new LocalStrategy(
    async (username, password, done) => {
        try {
            const user = await User.findOne({ username });
            if (!user) return done(null, false, { message: 'Incorrect username.' });
            const isMatch = await bcrypt.compare(password, user.password);
            if (!isMatch) return done(null, false, { message: 'Incorrect password.' });
            return done(null, user);
        } catch (err) {
            return done(err);
        }
    }
));

// Serialize user instance to session
passport.serializeUser((user, done) => done(null, user.id));

// Deserialize user instance from session
passport.deserializeUser(async (id, done) => {
    try {
        const user = await User.findById(id);
        done(null, user);
    } catch (err) {
        done(err);
    }
});

// User registration route
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });
        await newUser.save();
        res.status(201).send('User registered successfully');
    } catch (error) {
        console.error('Registration error:', error);
        res.status(500).send('Error registering user');
    }
});

// User login route
app.post('/login', passport.authenticate('local'), (req, res) => {
    res.status(200).send('Logged in successfully');
});

// Payment route
app.post('/create-payment-intent', async (req, res) => {
    const { amount } = req.body; // Amount should be in cents
    try {
        const paymentIntent = await stripe.paymentIntents.create({
            amount,
            currency: 'usd',
        });
        res.status(200).send({ clientSecret: paymentIntent.client_secret });
    } catch (error) {
        console.error('Payment error:', error);
        res.status(500).send('Error creating payment intent');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
