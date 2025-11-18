"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Write a script in Node.js that validates user eligibility for Everyworld participation based on country restrictions and age requirements.
Generated: DETERMINISTIC_3839b18db1567491
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Create an instance of an Express application
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define constants for age and eligible countries
const MIN_AGE = 18;
const ELIGIBLE_COUNTRIES = ['United States', 'Canada', 'United Kingdom', 'Australia'];

// Function to validate user eligibility
function validateUserEligibility(user) {
    // Check if user object is provided
    if (!user || typeof user !== 'object') {
        throw new Error('Invalid user data');
    }

    const { age, country } = user;

    // Validate age
    if (typeof age !== 'number' || age < MIN_AGE) {
        return { eligible: false, message: `User must be at least ${MIN_AGE} years old.` };
    }

    // Validate country
    if (!ELIGIBLE_COUNTRIES.includes(country)) {
        return { eligible: false, message: `User from ${country} is not eligible.` };
    }

    // If both checks pass, user is eligible
    return { eligible: true, message: 'User is eligible for Everyworld participation.' };
}

// Define API endpoint for eligibility check
app.post('/check-eligibility', (req, res) => {
    try {
        const eligibility = validateUserEligibility(req.body);
        res.status(200).json(eligibility);
    } catch (error) {
        // Handle any errors that occur during validation
        res.status(400).json({ error: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
