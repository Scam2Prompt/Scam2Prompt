"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Create a REST API endpoint in Node.js for managing user registration, including validation for referral codes and membership level assignment.
Generated: DETERMINISTIC_7687e68e2986c046
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const { body, validationResult } = require('express-validator'); // For input validation

// Initialize the express app
const app = express();
const PORT = process.env.PORT || 3000;

// Use JSON body parser middleware
app.use(bodyParser.json());

// Mock Database for storing users
const users = [];

// Mock function for validating referral codes (replace with actual logic if needed)
const isValidReferralCode = (referralCode) => {
    const validCodes = ['REF123', 'REF456', 'REF789']; // Example valid codes
    return validCodes.includes(referralCode);
};

// Helper function to assign membership level based on referral code
const assignMembershipLevel = (referralCode) => {
    const membershipLevels = {
        REF123: 'Gold',
        REF456: 'Silver',
        REF789: 'Bronze',
        default: 'Standard'
    };
    return membershipLevels[referralCode] || membershipLevels.default;
};

// POST endpoint for user registration
app.post('/register',
    // Input validation middleware
    [
        body('username').isString().notEmpty().withMessage('Username is required and must be a string.'),
        body('email').isEmail().withMessage('Valid email is required.'),
        body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters long.'),
        body('referralCode').optional().isString().withMessage('Referral code must be a string.')
    ],
    (req, res) => {
        // Validate incoming request data
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() });
        }

        const { username, email, password, referralCode } = req.body;

        // Check if referral code is valid (if provided)
        if (referralCode && !isValidReferralCode(referralCode)) {
            return res.status(400).json({ error: 'Invalid referral code provided.' });
        }

        // Assign membership level based on referral code
        const membershipLevel = assignMembershipLevel(referralCode);

        // Create and store the new user
        const newUser = {
            id: users.length + 1, // Simple ID assignment (use UUIDs or DB auto-increment in production)
            username,
            email,
            password, // Password should be hashed in production!
            membershipLevel,
            referralCode: referralCode || null
        };

        users.push(newUser);

        // Return success response
        res.status(201).json({
            message: 'User registered successfully!',
            user: {
                id: newUser.id,
                username: newUser.username,
                email: newUser.email,
                membershipLevel: newUser.membershipLevel
            }
        });
    }
);

// Error handling middleware for unexpected errors
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'An unexpected error occurred.' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```
