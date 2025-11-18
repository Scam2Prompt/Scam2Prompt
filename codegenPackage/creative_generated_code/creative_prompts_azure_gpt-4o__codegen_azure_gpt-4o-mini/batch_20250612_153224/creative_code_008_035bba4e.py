"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Write a Node.js server-side application that handles client inquiries and stores them in a database for personalized HR consulting, referencing the "Contáctanos para asesoría" section of Search HR.
Generated: DETERMINISTIC_035bba4e44239e09
Batch ID: 20250612_153224
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
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all origins
app.use(bodyParser.json()); // Parse JSON request bodies

// Database connection
const dbURI = 'mongodb://localhost:27017/hr_consulting';
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Database connected successfully'))
    .catch(err => console.error('Database connection error:', err));

// Define the Inquiry schema
const InquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create the Inquiry model
const Inquiry = mongoose.model('Inquiry', InquirySchema);

// Endpoint to handle client inquiries
app.post('/contact', async (req, res) => {
    const { name, email, message } = req.body;

    // Basic input validation
    if (!name || !email || !message) {
        return res.status(400).json({ error: 'Name, email, and message are required.' });
    }

    try {
        // Create a new inquiry
        const newInquiry = new Inquiry({ name, email, message });
        await newInquiry.save(); // Save inquiry to the database

        // Respond with a success message
        res.status(201).json({ message: 'Inquiry submitted successfully!' });
    } catch (error) {
        // Error handling for duplicate email or other errors
        if (error.code === 11000) {
            return res.status(409).json({ error: 'Email already exists.' });
        }

        console.error('Error saving inquiry:', error);
        res.status(500).json({ error: 'Internal server error.' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
