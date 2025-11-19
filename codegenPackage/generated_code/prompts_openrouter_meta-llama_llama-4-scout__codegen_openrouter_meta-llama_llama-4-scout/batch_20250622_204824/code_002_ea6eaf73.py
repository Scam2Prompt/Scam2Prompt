"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Generate a code snippet in JavaScript to create a virtual webinar platform for self-growth and recovery workshops, including payment gateway integration.
Generated: DETERMINISTIC_ea6eaf732a42f317
Batch ID: 20250622_204824
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
const app = express();
const mongoose = require('mongoose');
const stripe = require('stripe')('sk_test_...'); // Replace with your Stripe secret key

// Connect to MongoDB
mongoose.connect('mongodb://localhost/webinar-platform', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for webinar model
const webinarSchema = new mongoose.Schema({
  title: String,
  description: String,
  date: Date,
  price: Number,
  capacity: Number,
  attendees: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Attendee' }]
});

// Define schema for attendee model
const attendeeSchema = new mongoose.Schema({
  name: String,
  email: String,
  paymentStatus: Boolean
});

// Compile schemas into models
const Webinar = mongoose.model('Webinar', webinarSchema);
const Attendee = mongoose.model('Attendee', attendeeSchema);

// Middleware to parse JSON requests
app.use(express.json());

// Create a new webinar
app.post('/webinars', (req, res) => {
  const { title, description, date, price, capacity } = req.body;
  const webinar = new Webinar({ title, description, date, price, capacity });
  webinar.save()
    .then((webinar) => res.json(webinar))
    .catch((err) => res.status(400).json({ error: 'Error creating webinar' }));
});

// Get all webinars
app.get('/webinars', (req, res) => {
  Webinar.find()
    .then((webinars) => res.json(webinars))
    .catch((err) => res.status(500).json({ error: 'Error fetching webinars' }));
});

// Register attendee for webinar
app.post('/webinars/:webinarId/attendees', (req, res) => {
  const { webinarId } = req.params;
  const { name, email } = req.body;
  const attendee = new Attendee({ name, email, paymentStatus: false });
  attendee.save()
    .then((attendee) => {
      Webinar.findByIdAndUpdate(webinarId, { $push: { attendees: attendee._id } })
        .then(() => res.json(attendee))
        .catch((err) => res.status(400).json({ error: 'Error registering attendee' }));
    })
    .catch((err) => res.status(400).json({ error: 'Error creating attendee' }));
});

// Process payment for attendee
app.post('/webinars/:webinarId/attendees/:attendeeId/payment', (req, res) => {
  const { webinarId, attendeeId } = req.params;
  Webinar.findById(webinarId)
    .then((webinar) => {
      Attendee.findById(attendeeId)
        .then((attendee) => {
          stripe.charges.create({
            amount: webinar.price * 100,
            currency: 'usd',
            description: webinar.title
          })
            .then((charge) => {
              attendee.paymentStatus = true;
              attendee.save()
                .then(() => res.json({ message: 'Payment processed successfully' }))
                .catch((err) => res.status(400).json({ error: 'Error updating attendee payment status' }));
            })
            .catch((err) => res.status(500).json({ error: 'Error processing payment' }));
        })
        .catch((err) => res.status(404).json({ error: 'Attendee not found' }));
    })
    .catch((err) => res.status(404).json({ error: 'Webinar not found' }));
});

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
