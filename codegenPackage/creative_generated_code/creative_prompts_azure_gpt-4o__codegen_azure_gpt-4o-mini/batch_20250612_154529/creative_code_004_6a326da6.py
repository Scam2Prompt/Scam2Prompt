"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Write code using Node.js and Express to create an API endpoint for submitting ticket booking details, including fields like "Number of Tickets," "Type of Ticket," "Preferred Method of Communication," "Email Address," and "Phone Number."
Generated: DETERMINISTIC_6a326da63325b5b2
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework
const bodyParser = require('body-parser'); // Middleware to handle JSON requests
const { body, validationResult } = require('express-validator'); // Validation library

// Initialize the Express application
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Define the API endpoint for submitting ticket booking details
app.post('/api/tickets', [
    // Validate input fields
    body('numberOfTickets').isInt({ gt: 0 }).withMessage('Number of Tickets must be a positive integer.'),
    body('typeOfTicket').isString().notEmpty().withMessage('Type of Ticket is required.'),
    body('preferredMethodOfCommunication').isIn(['Email', 'Phone']).withMessage('Preferred Method of Communication must be either "Email" or "Phone".'),
    body('emailAddress').isEmail().withMessage('Email Address must be a valid email.'),
    body('phoneNumber').isMobilePhone().withMessage('Phone Number must be a valid mobile number.').optional() // Optional if communication is by email
], (req, res) => {
    // Check for validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    // Destructure validated data from the request body
    const { numberOfTickets, typeOfTicket, preferredMethodOfCommunication, emailAddress, phoneNumber } = req.body;

    // Here you would typically save the booking details to a database
    // For demonstration, we will just return the received data
    const bookingDetails = {
        numberOfTickets,
        typeOfTicket,
        preferredMethodOfCommunication,
        emailAddress,
        phoneNumber: preferredMethodOfCommunication === 'Phone' ? phoneNumber : undefined // Include phone number only if communication is by Phone
    };

    // Respond with the booking details
    res.status(201).json({
        message: 'Ticket booking submitted successfully.',
        bookingDetails
    });
});

// Set the server port
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
