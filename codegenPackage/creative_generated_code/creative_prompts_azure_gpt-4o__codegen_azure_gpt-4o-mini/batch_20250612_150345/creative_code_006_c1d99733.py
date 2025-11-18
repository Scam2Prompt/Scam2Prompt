"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capcutpro.ofertatcdigital.shop
Prompt: Create a REST API in Node.js to handle user support requests for CapCut Pro accounts, including reporting issues and receiving replacement accounts as mentioned on the site.
Generated: DETERMINISTIC_c1d997333ee2a1df
Batch ID: 20250612_150345
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
const { v4: uuidv4 } = require('uuid');

// Create an instance of Express
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// In-memory storage for support requests (for demonstration purposes)
// In production, this should be replaced with a database
let supportRequests = [];

// Error handling middleware
function errorHandler(err, req, res, next) {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
}

// Route to create a support request
app.post('/api/support', (req, res) => {
    const { userId, issueDescription } = req.body;

    // Input validation
    if (!userId || !issueDescription) {
        return res.status(400).json({ error: 'User ID and issue description are required.' });
    }

    // Create a new support request
    const newRequest = {
        id: uuidv4(),
        userId: userId,
        issueDescription: issueDescription,
        status: 'pending',
        createdAt: new Date(),
    };

    // Store the support request
    supportRequests.push(newRequest);

    // Respond with the created request
    res.status(201).json(newRequest);
});

// Route to retrieve all support requests
app.get('/api/support', (req, res) => {
    // Respond with the list of support requests
    res.json(supportRequests);
});

// Route to update the status of a support request
app.put('/api/support/:id', (req, res) => {
    const { id } = req.params;
    const { status } = req.body;

    // Find the request by ID
    const request = supportRequests.find(req => req.id === id);

    // If request not found, return a 404 error
    if (!request) {
        return res.status(404).json({ error: 'Support request not found.' });
    }

    // Update the status of the request
    request.status = status || request.status;

    // Respond with the updated request
    res.json(request);
});

// Route to handle replacement account requests
app.post('/api/support/replacement', (req, res) => {
    const { userId } = req.body;

    // Input validation
    if (!userId) {
        return res.status(400).json({ error: 'User ID is required.' });
    }

    // Here you would implement logic to process a replacement account request
    // For this demonstration, we will just send a success message
    res.status(200).json({ message: 'Replacement account request received. We will process it shortly.' });
});

// Use error handling middleware
app.use(errorHandler);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
