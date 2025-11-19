"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nissta.org
Prompt: Create a REST API endpoint in Node.js that allows users to submit inquiries related to sugar industry challenges, reflecting the objectives of NISSTA to address sector issues.
Generated: DETERMINISTIC_80557ea7ac716373
Batch ID: 20250612_135343
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
const mongoose = require('mongoose');

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/nissta'; // Change as necessary

// Connect to MongoDB
mongoose.connect(mongoURI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Inquiry schema
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create Inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Define REST API endpoint to submit inquiries
app.post('/api/inquiries', async (req, res) => {
    try {
        // Validate request body
        const { name, email, message } = req.body;
        if (!name || !email || !message) {
            return res.status(400).json({ error: 'Name, email, and message are required.' });
        }

        // Create a new Inquiry document
        const inquiry = new Inquiry({ name, email, message });

        // Save the inquiry to the database
        await inquiry.save();

        // Respond with the created inquiry
        res.status(201).json(inquiry);
    } catch (error) {
        console.error('Error while submitting inquiry:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Define a port and start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing purposes (if needed)
module.exports = app;
```
