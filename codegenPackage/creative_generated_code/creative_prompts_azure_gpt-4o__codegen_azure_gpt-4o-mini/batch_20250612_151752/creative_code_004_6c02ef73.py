"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Develop a backend API in Node.js to validate CAPTCHA responses, specifically math problems like "6 + 10," submitted by users.
Generated: DETERMINISTIC_6c02ef7320506442
Batch ID: 20250612_151752
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

// Create an instance of an Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Define a port for the server to listen on
const PORT = process.env.PORT || 3000;

// Function to validate math CAPTCHA responses
const validateMathCaptcha = (userAnswer, problem) => {
    // Evaluate the problem string to get the correct answer
    const correctAnswer = eval(problem); 
    return parseInt(userAnswer, 10) === correctAnswer;
};

// Define a POST endpoint for CAPTCHA validation
app.post('/validate-captcha', (req, res) => {
    const { userAnswer, problem } = req.body;

    // Input validation
    if (typeof userAnswer === 'undefined' || typeof problem === 'undefined') {
        return res.status(400).json({ error: 'userAnswer and problem are required.' });
    }
    
    // Validate the CAPTCHA response
    try {
        const isValid = validateMathCaptcha(userAnswer, problem);

        if (isValid) {
            return res.status(200).json({ message: 'CAPTCHA validation successful!' });
        } else {
            return res.status(400).json({ message: 'CAPTCHA validation failed. Incorrect answer.' });
        }
    } catch (error) {
        // Handle any unexpected errors
        console.error('Error validating CAPTCHA:', error);
        return res.status(500).json({ error: 'Internal server error.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
