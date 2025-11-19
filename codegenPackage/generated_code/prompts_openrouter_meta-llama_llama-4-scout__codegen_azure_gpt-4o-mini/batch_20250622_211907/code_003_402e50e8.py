"""
Generated Code Metadata:
========================
Original URL: https://mottamask-lloggjin.godaddysites.com
Prompt: "Design a subscription-based service using Node.js and Express that sends daily updates on new real estate listings to users, incorporating filtering options for location and price."
Generated: DETERMINISTIC_402e50e8ededf297
Batch ID: 20250622_211907
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
const nodemailer = require('nodemailer');
const cron = require('node-cron');
const bodyParser = require('body-parser');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/real-estate', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('MongoDB connected');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Define User schema
const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    location: { type: String, required: true },
    priceRange: { type: [Number], required: true }, // [minPrice, maxPrice]
});

// Define Listing schema
const listingSchema = new mongoose.Schema({
    title: { type: String, required: true },
    location: { type: String, required: true },
    price: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create models
const User = mongoose.model('User', userSchema);
const Listing = mongoose.model('Listing', listingSchema);

// Endpoint to register users
app.post('/register', async (req, res) => {
    const { email, location, priceRange } = req.body;
    try {
        const user = new User({ email, location, priceRange });
        await user.save();
        res.status(201).send('User registered successfully');
    } catch (error) {
        res.status(400).send('Error registering user: ' + error.message);
    }
});

// Function to send email updates
const sendEmailUpdates = async (user, listings) => {
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com', // Replace with your email
            pass: 'your-email-password', // Replace with your email password
        },
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: user.email,
        subject: 'Daily Real Estate Listings Update',
        text: `New listings for you:\n\n${listings.map(listing => `${listing.title} - ${listing.location} - $${listing.price}`).join('\n')}`,
    };

    await transporter.sendMail(mailOptions);
};

// Cron job to send daily updates
cron.schedule('0 9 * * *', async () => {
    const users = await User.find();
    for (const user of users) {
        const listings = await Listing.find({
            location: user.location,
            price: { $gte: user.priceRange[0], $lte: user.priceRange[1] },
        });

        if (listings.length > 0) {
            await sendEmailUpdates(user, listings);
        }
    }
});

// Endpoint to add new listings
app.post('/listings', async (req, res) => {
    const { title, location, price } = req.body;
    try {
        const listing = new Listing({ title, location, price });
        await listing.save();
        res.status(201).send('Listing added successfully');
    } catch (error) {
        res.status(400).send('Error adding listing: ' + error.message);
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note:** 
- Replace `'your-email@gmail.com'` and `'your-email-password'` with your actual email credentials for the email service.
- Ensure to handle sensitive information securely in a production environment (e.g., using environment variables).
