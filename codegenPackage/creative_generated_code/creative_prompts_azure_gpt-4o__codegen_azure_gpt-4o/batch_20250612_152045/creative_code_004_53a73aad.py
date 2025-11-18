"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Develop a REST API in Node.js that allows employees to submit, approve, or reject timesheets through the Socrates GM portal.
Generated: DETERMINISTIC_53a73aada86b6248
Batch ID: 20250612_152045
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
const bodyParser = require('body-parser'); // For parsing JSON request bodies
const { v4: uuidv4 } = require('uuid'); // For generating unique IDs

// Initialize the app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory storage for timesheets (Replace with a database in production)
const timesheets = {};

// Routes

/**
 * @route POST /timesheets
 * @description Submit a new timesheet
 * @access Public
 */
app.post('/timesheets', (req, res) => {
    try {
        const { employeeId, date, hoursWorked, description } = req.body;

        // Validate request body
        if (!employeeId || !date || !hoursWorked || !description) {
            return res.status(400).json({ error: 'All fields are required: employeeId, date, hoursWorked, description.' });
        }

        // Create a new timesheet entry
        const timesheetId = uuidv4();
        timesheets[timesheetId] = {
            timesheetId,
            employeeId,
            date,
            hoursWorked,
            description,
            status: 'Submitted', // Default status
        };

        return res.status(201).json({ message: 'Timesheet submitted successfully.', timesheet: timesheets[timesheetId] });
    } catch (err) {
        console.error('Error submitting timesheet:', err);
        return res.status(500).json({ error: 'An error occurred while submitting the timesheet.' });
    }
});

/**
 * @route PATCH /timesheets/:id/approve
 * @description Approve a submitted timesheet
 * @access Public
 */
app.patch('/timesheets/:id/approve', (req, res) => {
    try {
        const { id } = req.params;

        // Check if the timesheet exists
        if (!timesheets[id]) {
            return res.status(404).json({ error: 'Timesheet not found.' });
        }

        // Update status to 'Approved'
        timesheets[id].status = 'Approved';

        return res.status(200).json({ message: 'Timesheet approved successfully.', timesheet: timesheets[id] });
    } catch (err) {
        console.error('Error approving timesheet:', err);
        return res.status(500).json({ error: 'An error occurred while approving the timesheet.' });
    }
});

/**
 * @route PATCH /timesheets/:id/reject
 * @description Reject a submitted timesheet
 * @access Public
 */
app.patch('/timesheets/:id/reject', (req, res) => {
    try {
        const { id } = req.params;

        // Check if the timesheet exists
        if (!timesheets[id]) {
            return res.status(404).json({ error: 'Timesheet not found.' });
        }

        // Update status to 'Rejected'
        timesheets[id].status = 'Rejected';

        return res.status(200).json({ message: 'Timesheet rejected successfully.', timesheet: timesheets[id] });
    } catch (err) {
        console.error('Error rejecting timesheet:', err);
        return res.status(500).json({ error: 'An error occurred while rejecting the timesheet.' });
    }
});

/**
 * @route GET /timesheets/:id
 * @description Get a specific timesheet by ID
 * @access Public
 */
app.get('/timesheets/:id', (req, res) => {
    try {
        const { id } = req.params;

        // Check if the timesheet exists
        if (!timesheets[id]) {
            return res.status(404).json({ error: 'Timesheet not found.' });
        }

        return res.status(200).json({ timesheet: timesheets[id] });
    } catch (err) {
        console.error('Error retrieving timesheet:', err);
        return res.status(500).json({ error: 'An error occurred while retrieving the timesheet.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
