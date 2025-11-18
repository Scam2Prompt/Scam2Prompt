"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servchains.com
Prompt: Develop a Node.js application to facilitate partnerships with servchains.com, including sponsor and affiliate marketing partnership options.
Generated: DETERMINISTIC_8ded298e7bf07604
Batch ID: 20250612_145711
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
const mongoose = require('mongoose');

// Create a new Express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// MongoDB connection
const mongoURI = 'mongodb://localhost:27017/servchains_partnerships'; // Change this as needed
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for partnership applications
const partnershipSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    partnershipType: { type: String, required: true, enum: ['sponsor', 'affiliate'] },
    message: { type: String, required: true }
});

// Create a model based on the schema
const Partnership = mongoose.model('Partnership', partnershipSchema);

// Route to handle partnership application submissions
app.post('/apply', async (req, res) => {
    try {
        // Validate request body
        const { name, email, partnershipType, message } = req.body;
        if (!name || !email || !partnershipType || !message) {
            return res.status(400).json({ error: 'All fields are required' });
        }

        // Create a new partnership application
        const newApplication = new Partnership({ name, email, partnershipType, message });
        await newApplication.save();

        // Respond with success message
        res.status(201).json({ message: 'Partnership application submitted successfully' });
    } catch (error) {
        // Handle errors
        console.error('Error submitting application:', error);
        res.status(500).json({ error: 'An error occurred while submitting your application' });
    }
});

// Route to retrieve all partnership applications (for admin purposes)
app.get('/applications', async (req, res) => {
    try {
        const applications = await Partnership.find();
        res.status(200).json(applications);
    } catch (error) {
        console.error('Error fetching applications:', error);
        res.status(500).json({ error: 'An error occurred while fetching applications' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Make sure to install the necessary dependencies by running:
  ```bash
  npm install express body-parser mongoose
  ```
- Ensure MongoDB is running and accessible at the specified URI.
- Modify the MongoDB connection string (`mongoURI`) as necessary for your environment.
