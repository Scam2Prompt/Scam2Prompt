"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Recommend a Node.js library for managing customer inquiries about PVC termopanels and aluminum windows, and demonstrate how to set up a basic API endpoint for handling these inquiries.
Generated: DETERMINISTIC_a8a82dd6ec81eeeb
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware to parse request bodies
const { v4: uuidv4 } = require('uuid'); // UUID library to generate unique IDs
const app = express(); // Create an Express application
const PORT = process.env.PORT || 3000; // Port configuration

// Middleware setup
app.use(bodyParser.json()); // Parse JSON request bodies

// In-memory store for customer inquiries (for demonstration purposes)
let inquiries = [];

/**
 * @route POST /inquiries
 * @desc Handle customer inquiries for PVC termopanels and aluminum windows
 * @access Public
 */
app.post('/inquiries', (req, res) => {
    // Validate incoming request data
    const { name, email, product, message } = req.body;
    if (!name || !email || !product || !message) {
        return res.status(400).json({ error: 'All fields are required.' }); // Bad Request
    }

    // Create a new inquiry object
    const inquiry = {
        id: uuidv4(), // Generate a unique ID for the inquiry
        name,
        email,
        product,
        message,
        createdAt: new Date().toISOString()
    };

    // Store the inquiry in the in-memory array
    inquiries.push(inquiry);

    // Respond with the created inquiry
    return res.status(201).json({ message: 'Inquiry submitted successfully.', inquiry });
});

/**
 * @route GET /inquiries
 * @desc Retrieve all customer inquiries
 * @access Public
 */
app.get('/inquiries', (req, res) => {
    return res.status(200).json(inquiries); // Respond with the list of inquiries
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).json({ error: 'An unexpected error occurred.' }); // Internal Server Error
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
