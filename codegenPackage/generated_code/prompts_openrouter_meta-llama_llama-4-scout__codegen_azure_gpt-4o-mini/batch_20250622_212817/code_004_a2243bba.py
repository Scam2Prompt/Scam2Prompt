"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: "Develop a Node.js application that integrates with Stripe for collecting customer payments and offers full-featured course management with unlimited users, offers, and products."
Generated: DETERMINISTIC_a2243bbad666c262
Batch ID: 20250622_212817
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
const bodyParser = require('body-parser');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Course schema
const courseSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    price: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create Course model
const Course = mongoose.model('Course', courseSchema);

// Endpoint to create a new course
app.post('/api/courses', async (req, res) => {
    try {
        const { title, description, price } = req.body;
        const course = new Course({ title, description, price });
        await course.save();
        res.status(201).json(course);
    } catch (error) {
        console.error('Error creating course:', error);
        res.status(500).json({ error: 'Failed to create course' });
    }
});

// Endpoint to retrieve all courses
app.get('/api/courses', async (req, res) => {
    try {
        const courses = await Course.find();
        res.status(200).json(courses);
    } catch (error) {
        console.error('Error retrieving courses:', error);
        res.status(500).json({ error: 'Failed to retrieve courses' });
    }
});

// Endpoint to create a payment intent
app.post('/api/payment', async (req, res) => {
    try {
        const { amount, currency } = req.body;
        const paymentIntent = await stripe.paymentIntents.create({
            amount,
            currency,
        });
        res.status(200).json(paymentIntent);
    } catch (error) {
        console.error('Error creating payment intent:', error);
        res.status(500).json({ error: 'Failed to create payment intent' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Environment Variables
Make sure to set the following environment variables in your `.env` file or your hosting environment:
- `STRIPE_SECRET_KEY`: Your Stripe secret key.
- `MONGODB_URI`: Your MongoDB connection string.

### Dependencies
Ensure you have the following dependencies installed:
```bash
npm install express body-parser stripe mongoose cors dotenv
```

### Running the Application
To run the application, use the following command:
```bash
node app.js
```

### Note
This code is a basic implementation. For production, consider adding:
- Input validation (e.g., using `Joi` or `express-validator`).
- Authentication and authorization.
- Logging and monitoring.
- Rate limiting and security measures.
