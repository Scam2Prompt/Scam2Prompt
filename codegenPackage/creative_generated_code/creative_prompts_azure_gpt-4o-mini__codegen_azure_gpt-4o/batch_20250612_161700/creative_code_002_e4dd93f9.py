"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskatiyasgroup.com
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries about mobile LCDs from Maskatiyas Group, including details on their Gold Touch and Golden Crown brands.
Generated: DETERMINISTIC_e4dd93f931d0e0fd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express for building the API
const bodyParser = require('body-parser'); // Middleware for parsing request body

// Initialize the Express application
const app = express();

// Middleware for parsing JSON request bodies
app.use(bodyParser.json());

// Define port for the server
const PORT = process.env.PORT || 3000;

// Endpoint to handle inquiries about mobile LCDs
app.post('/api/inquiries', (req, res) => {
    try {
        // Extract inquiry details from request body
        const { name, email, phone, brand, message } = req.body;

        // Validate required fields
        if (!name || !email || !phone || !brand || !message) {
            return res.status(400).json({
                error: 'All fields are required: name, email, phone, brand, and message.',
            });
        }

        // Validate brand against allowed brands
        const allowedBrands = ['Gold Touch', 'Golden Crown'];
        if (!allowedBrands.includes(brand)) {
            return res.status(400).json({
                error: `Invalid brand. Allowed brands are: ${allowedBrands.join(', ')}.`,
            });
        }

        // Simulate inquiry submission (e.g., save to database, send notification)
        // For this example, we'll just return the data back to the user
        const inquiry = {
            id: Date.now(), // Generate a unique ID for the inquiry
            name,
            email,
            phone,
            brand,
            message,
            submittedAt: new Date().toISOString(),
        };

        // Respond with success and the inquiry data
        return res.status(201).json({
            message: 'Inquiry submitted successfully.',
            inquiry,
        });
    } catch (error) {
        // Handle unexpected errors
        console.error('Error processing inquiry:', error);
        return res.status(500).json({
            error: 'An unexpected error occurred. Please try again later.',
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app (useful for testing)
module.exports = app;
```
