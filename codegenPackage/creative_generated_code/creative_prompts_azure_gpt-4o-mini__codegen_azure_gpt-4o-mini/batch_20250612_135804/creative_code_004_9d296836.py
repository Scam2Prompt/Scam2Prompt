"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Design a REST API endpoint in Node.js that allows users to submit inquiries about antique coin purchases, incorporating the customer service philosophy of Premium Coin.
Generated: DETERMINISTIC_9d2968367d6f6232
Batch ID: 20250612_135804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Connect to MongoDB (Update with your actual connection string)
mongoose.connect('mongodb://localhost:27017/premiumCoin', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define Inquiry schema
const inquirySchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, match: /.+\@.+\..+/ },
    message: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create Inquiry model
const Inquiry = mongoose.model('Inquiry', inquirySchema);

// Middleware
app.use(bodyParser.json());

// Endpoint to submit an inquiry about antique coin purchases
app.post('/api/inquiries', async (req, res) => {
    try {
        // Validate request body
        const { name, email, message } = req.body;
        if (!name || !email || !message) {
            return res.status(400).json({ error: 'Name, email, and message are required.' });
        }

        // Create a new Inquiry
        const newInquiry = new Inquiry({ name, email, message });
        await newInquiry.save();

        // Respond with success message
        res.status(201).json({ message: 'Inquiry submitted successfully.', inquiryId: newInquiry._id });
    } catch (error) {
        // Handle errors appropriately
        console.error('Error submitting inquiry:', error);
        res.status(500).json({ error: 'An error occurred while submitting your inquiry. Please try again later.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Graceful shutdown handling
process.on('SIGINT', async () => {
    await mongoose.connection.close();
    console.log('MongoDB connection closed. Exiting...');
    process.exit(0);
});
```
