"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advancecryptoacademy.online
Prompt: Recommend a secure multi-tier architecture for a cryptocurrency investment platform like Advance Crypto Academy, emphasizing features such as SAFU (Secure Assets Fund for Users) and Comodo SSL encryption.
Generated: DETERMINISTIC_aa71a66a3c983d75
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example of a secure multi-tier architecture for a cryptocurrency investment platform. The code below demonstrates server-side development using Node.js (backend tier), secure database interactions (data tier), and a sample API endpoint that can be used for client-side applications (frontend tier).

```javascript
// Import necessary modules
const express = require('express');
const helmet = require('helmet');  // For securing HTTP headers
const rateLimit = require('express-rate-limit'); // Basic rate-limiting middleware to prevent brute force attacks
const dotenv = require('dotenv'); // For secure configuration management
const mongoose = require('mongoose'); // MongoDB ORM for secure database interaction
const crypto = require('crypto'); // For encryption and hashing
const { body, validationResult } = require('express-validator'); // Input validation

// Load environment variables from .env file
dotenv.config();

const app = express();
app.use(express.json()); // Middleware to parse JSON requests
app.use(helmet()); // Secure HTTP headers

// Rate-limiting middleware to prevent abuse
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // Limit each IP to 100 requests per windowMs
    message: 'Too many requests from this IP, please try again after 15 minutes.'
});
app.use(limiter);

// Database connection (MongoDB connection string in .env)
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Successfully connected to the database');
}).catch((err) => {
    console.error('Database connection failed:', err.message);
    process.exit(1);
});

// Define a secure Mongoose schema for users
const userSchema = new mongoose.Schema({
    username: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    passwordHash: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Pre-save hook to log user activity (e.g., SAFU fund access, if any)
userSchema.pre('save', async function (next) {
    // Hashing password before saving using SHA-256
    if (this.isModified('passwordHash')) {
        this.passwordHash = crypto.createHash('sha256').update(this.passwordHash).digest('hex');
    }
    next();
});

// Create a user model
const User = mongoose.model('User', userSchema);

// API endpoint to register a user
app.post('/api/register', [
    // Input validation
    body('username').isString().isLength({ min: 3 }).withMessage('Username must be at least 3 characters long.'),
    body('email').isEmail().withMessage('Invalid email address.'),
    body('password').isLength({ min: 8 }).withMessage('Password must be at least 8 characters long.'),
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        // Return input validation errors
        return res.status(400).json({ errors: errors.array() });
    }

    const { username, email, password } = req.body;

    try {
        // Check if the user already exists
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).json({ error: 'A user with this email already exists.' });
        }

        // Create and save the new user
        const newUser = new User({
            username,
            email,
            passwordHash: password // Password is hashed in the pre-save hook
        });

        await newUser.save();
        return res.status(201).json({ message: 'User registered successfully.' });

    } catch (error) {
        console.error('Error registering user:', error.message);
        return res.status(500).json({ error: 'Internal Server Error. Please try again later.' });
    }
});

// Placeholder for Comodo SSL Certificate usage
// In production, deploy this service on HTTPS infrastructure configured with Comodo SSL/TLS certificates

// Error handling for undefined routes
app.use((req, res) => {
    res.status(404).json({ error: 'Route not found.' });
});

// Global error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err.message);
    res.status(500).json({ error: 'Internal server error.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running securely on port ${PORT}`);
});
```

### Notes:
1. **Comodo SSL**: In production, deploy this on HTTPS infrastructure with Comodo SSL/TLS certificates. This is handled at the server or load balancer level, not directly in the code.
2. **SAFU (Secure Assets Fund for Users)**: This generally involves allocating a reserve fund for emergencies or security breaches. Implementing it would involve tracking transactions and maintaining a separate audited wallet.
3. **Environment Variables**: Sensitive data (e.g., database passwords, crypto keys) must be stored in `.env` files or secure secrets management systems in production.
