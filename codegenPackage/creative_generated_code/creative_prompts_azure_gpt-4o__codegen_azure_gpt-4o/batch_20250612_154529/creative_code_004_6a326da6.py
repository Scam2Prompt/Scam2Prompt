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
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express app
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define the ticket booking API endpoint
app.post('/api/book-ticket', (req, res) => {
  try {
    // Extract booking details from the request body
    const { numberOfTickets, typeOfTicket, preferredCommunication, email, phone } = req.body;

    // Basic validation for required fields
    if (
      !numberOfTickets ||
      !typeOfTicket ||
      !preferredCommunication ||
      (!email && !phone)
    ) {
      return res.status(400).json({
        error: 'Missing required fields. Please provide all necessary information.',
      });
    }

    // Validate ticket count (must be a positive integer)
    if (numberOfTickets <= 0 || !Number.isInteger(numberOfTickets)) {
      return res.status(400).json({
        error: 'Invalid value for "Number of Tickets". Must be a positive integer.',
      });
    }

    // Validate preferred communication method
    const validCommunicationMethods = ['email', 'phone', 'none'];
    if (!validCommunicationMethods.includes(preferredCommunication.toLowerCase())) {
      return res.status(400).json({
        error: 'Invalid "Preferred Method of Communication". Valid options are: email, phone, none.',
      });
    }

    // Validate email format if provided
    if (email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        return res.status(400).json({
          error: 'Invalid email address format.',
        });
      }
    }

    // Validate phone number format if provided
    if (phone) {
      const phoneRegex = /^[0-9]{10}$/; // Example validation for a 10-digit phone number
      if (!phoneRegex.test(phone)) {
        return res.status(400).json({
          error: 'Invalid phone number format. Must be a 10-digit number.',
        });
      }
    }

    // Process and save booking details (mock implementation)
    const bookingDetails = {
      numberOfTickets,
      typeOfTicket,
      preferredCommunication,
      email,
      phone,
      bookingTimestamp: new Date(),
    };

    // Respond with success message and submitted booking details
    return res.status(201).json({
      message: 'Ticket booking successful!',
      bookingDetails,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error processing ticket booking:', error);
    return res.status(500).json({
      error: 'An unexpected error occurred. Please try again later.',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
