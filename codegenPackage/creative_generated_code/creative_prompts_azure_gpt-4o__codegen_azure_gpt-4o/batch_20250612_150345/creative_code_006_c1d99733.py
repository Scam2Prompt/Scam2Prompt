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
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the app
const app = express();
app.use(bodyParser.json());

// Mock data storage (In production, use a database like MongoDB or PostgreSQL)
const supportRequests = [];

// Helper function to generate unique IDs for requests
const generateId = () => '_' + Math.random().toString(36).substr(2, 9);

// Routes

/**
 * POST /api/support/report
 * Endpoint to report an issue with a CapCut Pro account
 * Request Body: { "email": "string", "issue": "string" }
 * Response: { "status": "success", "message": "Issue reported successfully", "requestId": "string" }
 */
app.post('/api/support/report', (req, res) => {
    try {
        const { email, issue } = req.body;

        // Validate input
        if (!email || !issue) {
            return res.status(400).json({ status: 'error', message: 'Email and issue are required.' });
        }

        // Create a new support request
        const requestId = generateId();
        const newRequest = {
            requestId,
            email,
            issue,
            status: 'reported', // Status: reported, in-progress, resolved
            createdAt: new Date()
        };

        // Save the request
        supportRequests.push(newRequest);

        // Respond with success
        res.status(201).json({
            status: 'success',
            message: 'Issue reported successfully',
            requestId
        });
    } catch (error) {
        // Handle unexpected errors gracefully
        res.status(500).json({ status: 'error', message: 'An unexpected error occurred.' });
    }
});

/**
 * POST /api/support/replacement
 * Endpoint to request a replacement CapCut Pro account
 * Request Body: { "email": "string", "reason": "string" }
 * Response: { "status": "success", "message": "Replacement request submitted", "requestId": "string" }
 */
app.post('/api/support/replacement', (req, res) => {
    try {
        const { email, reason } = req.body;

        // Validate input
        if (!email || !reason) {
            return res.status(400).json({ status: 'error', message: 'Email and reason are required.' });
        }

        // Create a replacement request
        const requestId = generateId();
        const newRequest = {
            requestId,
            email,
            reason,
            status: 'requested', // Status: requested, in-progress, completed
            createdAt: new Date()
        };

        // Save the request
        supportRequests.push(newRequest);

        // Respond with success
        res.status(201).json({
            status: 'success',
            message: 'Replacement request submitted',
            requestId
        });
    } catch (error) {
        // Handle unexpected errors gracefully
        res.status(500).json({ status: 'error', message: 'An unexpected error occurred.' });
    }
});

/**
 * GET /api/support/requests/:requestId
 * Endpoint to check the status of a support request
 * URL Parameter: requestId
 * Response: { "status": "success", "request": { "requestId": "string", ... } }
 */
app.get('/api/support/requests/:requestId', (req, res) => {
    try {
        const { requestId } = req.params;

        // Find the request by ID
        const request = supportRequests.find(r => r.requestId === requestId);

        if (!request) {
            return res.status(404).json({ status: 'error', message: 'Request not found.' });
        }

        // Respond with the request details
        res.status(200).json({
            status: 'success',
            request
        });
    } catch (error) {
        // Handle unexpected errors gracefully
        res.status(500).json({ status: 'error', message: 'An unexpected error occurred.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app (useful for testing or integration with other modules)
module.exports = app;
```
