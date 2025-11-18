"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Develop a REST API in Node.js for booking domestic and international tour packages listed on the "Best Holidays All India" website, with endpoints for package selection, pricing calculation, and customer details submission.
Generated: DETERMINISTIC_de21540c0c07da8b
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Express app
const app = express();
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose Schema for Tour Packages
const packageSchema = new mongoose.Schema({
    name: { type: String, required: true },
    type: { type: String, enum: ['Domestic', 'International'], required: true },
    price: { type: Number, required: true },
    description: { type: String, required: true }
});

// Create Mongoose Model for Packages
const Package = mongoose.model('Package', packageSchema);

// Endpoint to get all tour packages
app.get('/api/packages', async (req, res) => {
    try {
        const packages = await Package.find();
        res.status(200).json(packages);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching packages', error });
    }
});

// Endpoint to get pricing for a specific package
app.get('/api/packages/:id/price', async (req, res) => {
    try {
        const package = await Package.findById(req.params.id);
        if (!package) {
            return res.status(404).json({ message: 'Package not found' });
        }
        res.status(200).json({ price: package.price });
    } catch (error) {
        res.status(500).json({ message: 'Error fetching package price', error });
    }
});

// Endpoint to submit customer details for booking
app.post('/api/bookings', async (req, res) => {
    const { packageId, customerName, customerEmail } = req.body;

    if (!packageId || !customerName || !customerEmail) {
        return res.status(400).json({ message: 'Missing required fields' });
    }

    try {
        const package = await Package.findById(packageId);
        if (!package) {
            return res.status(404).json({ message: 'Package not found' });
        }

        // Here you would typically save the booking to a database or process it further
        // For this example, we will simply return a success message

        res.status(201).json({ 
            message: 'Booking successful', 
            package: package.name, 
            customer: customerName 
        });
    } catch (error) {
        res.status(500).json({ message: 'Error processing booking', error });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
