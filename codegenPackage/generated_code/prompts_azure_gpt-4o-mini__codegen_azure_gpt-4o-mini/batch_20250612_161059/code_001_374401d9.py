"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Write a REST API in Node.js that allows users to donate to educational programs for underprivileged children, similar to the initiatives by Indological India.
Generated: DETERMINISTIC_374401d9ce6eb0c8
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/education-donations'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a Mongoose schema for donations
const donationSchema = new mongoose.Schema({
    donorName: { type: String, required: true },
    amount: { type: Number, required: true, min: 1 },
    message: { type: String, required: false },
    createdAt: { type: Date, default: Date.now }
});

// Create a Mongoose model for donations
const Donation = mongoose.model('Donation', donationSchema);

// Route to create a new donation
app.post('/donate', async (req, res) => {
    try {
        const { donorName, amount, message } = req.body;

        // Validate request body
        if (!donorName || !amount) {
            return res.status(400).json({ error: 'Donor name and amount are required.' });
        }

        // Create a new donation
        const donation = new Donation({ donorName, amount, message });
        await donation.save();

        // Respond with the created donation
        res.status(201).json(donation);
    } catch (error) {
        console.error('Error creating donation:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Route to get all donations
app.get('/donations', async (req, res) => {
    try {
        const donations = await Donation.find();
        res.status(200).json(donations);
    } catch (error) {
        console.error('Error fetching donations:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Instructions to Run the Code
1. Ensure you have Node.js and MongoDB installed on your machine.
2. Create a new directory for your project and navigate into it.
3. Run `npm init -y` to create a `package.json` file.
4. Install the required packages by running:
   ```bash
   npm install express mongoose body-parser cors
   ```
5. Save the provided code in a file named `app.js`.
6. Start your MongoDB server.
7. Run the application with:
   ```bash
   node app.js
   ```
8. You can test the API using tools like Postman or curl.
