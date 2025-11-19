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
const cron = require('node-cron');
const nodemailer = require('nodemailer');

// Initialize Express app
const app = express();
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/realestate', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for User model
const userSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    location: { type: String, required: true },
    priceRange: { type: String, required: true },
    subscribed: { type: Boolean, default: true }
});

// Define schema for Listing model
const listingSchema = new mongoose.Schema({
    title: { type: String, required: true },
    location: { type: String, required: true },
    price: { type: Number, required: true },
    publishedDate: { type: Date, default: Date.now }
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Listing = mongoose.model('Listing', listingSchema);

// Create a transporter for sending emails
const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // or 'STARTTLS'
    auth: {
        user: 'your-email@gmail.com',
        pass: 'your-password'
    }
});

// API endpoint to subscribe user
app.post('/subscribe', async (req, res) => {
    try {
        const { email, location, priceRange } = req.body;
        const existingUser = await User.findOne({ email });
        if (existingUser) {
            return res.status(400).send({ message: 'User already subscribed' });
        }
        const user = new User({ email, location, priceRange });
        await user.save();
        res.send({ message: 'Subscribed successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error subscribing user' });
    }
});

// API endpoint to unsubscribe user
app.post('/unsubscribe', async (req, res) => {
    try {
        const { email } = req.body;
        await User.findOneAndUpdate({ email }, { subscribed: false });
        res.send({ message: 'Unsubscribed successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error unsubscribing user' });
    }
});

// Function to send daily updates to subscribed users
const sendDailyUpdates = async () => {
    try {
        const users = await User.find({ subscribed: true });
        const listings = await Listing.find({ publishedDate: { $gte: new Date(Date.now() - 24 * 60 * 60 * 1000) } });

        users.forEach(async (user) => {
            const filteredListings = listings.filter((listing) => {
                return listing.location.includes(user.location) &&
                    listing.price >= user.priceRange.split('-')[0] &&
                    listing.price <= user.priceRange.split('-')[1];
            });

            if (filteredListings.length > 0) {
                const mailOptions = {
                    from: 'your-email@gmail.com',
                    to: user.email,
                    subject: 'Daily Real Estate Updates',
                    text: 'New listings found:\n' + filteredListings.map((listing) => `${listing.title} - ${listing.location} - ${listing.price}`).join('\n')
                };

                transporter.sendMail(mailOptions, (error, info) => {
                    if (error) {
                        console.error('Error sending email:', error);
                    } else {
                        console.log('Email sent:', info.response);
                    }
                });
            }
        });
    } catch (err) {
        console.error('Error sending daily updates:', err);
    }
};

// Schedule daily updates using cron job
cron.schedule('0 0 * * *', () => {
    sendDailyUpdates();
});

// API endpoint to add new listing
app.post('/listings', async (req, res) => {
    try {
        const { title, location, price } = req.body;
        const listing = new Listing({ title, location, price });
        await listing.save();
        res.send({ message: 'Listing added successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Error adding listing' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
