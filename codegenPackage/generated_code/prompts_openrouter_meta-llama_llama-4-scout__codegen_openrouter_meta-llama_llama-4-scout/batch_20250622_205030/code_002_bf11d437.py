"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Generate a RESTful API endpoint in Node.js to manage comic book orders, including endpoints for retrieving comic book information, processing payments, and sending order confirmations, inspired by the "Top G" comic book series.
Generated: DETERMINISTIC_bf11d437bf7c8e82
Batch ID: 20250622_205030
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
const stripe = require('stripe')('sk_test_key'); // Replace with your Stripe secret key
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/topgcomics', { useNewUrlParser: true, useUnifiedTopology: true });

// Define comic book schema
const comicBookSchema = new mongoose.Schema({
  title: String,
  issue: Number,
  price: Number,
  description: String
});

// Define order schema
const orderSchema = new mongoose.Schema({
  comicBookId: { type: mongoose.Schema.Types.ObjectId, ref: 'ComicBook' },
  customerName: String,
  customerEmail: String,
  paymentStatus: String
});

// Create models
const ComicBook = mongoose.model('ComicBook', comicBookSchema);
const Order = mongoose.model('Order', orderSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to retrieve comic book information
/**
 * @route GET /comics/:id
 * @description Retrieve comic book information
 * @param {string} id - Comic book ID
 * @returns {object} Comic book information
 */
app.get('/comics/:id', async (req, res) => {
  try {
    const comicBook = await ComicBook.findById(req.params.id);
    if (!comicBook) {
      return res.status(404).json({ message: 'Comic book not found' });
    }
    res.json(comicBook);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Endpoint to create a new order
/**
 * @route POST /orders
 * @description Create a new order
 * @param {object} req.body - Order information
 * @returns {object} Order information
 */
app.post('/orders', async (req, res) => {
  try {
    const { comicBookId, customerName, customerEmail } = req.body;
    const comicBook = await ComicBook.findById(comicBookId);
    if (!comicBook) {
      return res.status(404).json({ message: 'Comic book not found' });
    }
    const order = new Order({ comicBookId, customerName, customerEmail, paymentStatus: 'pending' });
    await order.save();
    res.json(order);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Endpoint to process payment for an order
/**
 * @route POST /orders/:id/payment
 * @description Process payment for an order
 * @param {string} id - Order ID
 * @param {object} req.body - Payment information
 * @returns {object} Payment result
 */
app.post('/orders/:id/payment', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }
    const comicBook = await ComicBook.findById(order.comicBookId);
    if (!comicBook) {
      return res.status(404).json({ message: 'Comic book not found' });
    }
    const paymentMethod = req.body.paymentMethod;
    const paymentIntent = await stripe.paymentIntents.create({
      amount: comicBook.price * 100,
      currency: 'usd',
      payment_method_types: [paymentMethod]
    });
    res.json({ clientSecret: paymentIntent.client_secret });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Endpoint to confirm payment and send order confirmation
/**
 * @route POST /orders/:id/confirm
 * @description Confirm payment and send order confirmation
 * @param {string} id - Order ID
 * @returns {object} Confirmation result
 */
app.post('/orders/:id/confirm', async (req, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }
    const comicBook = await ComicBook.findById(order.comicBookId);
    if (!comicBook) {
      return res.status(404).json({ message: 'Comic book not found' });
    }
    // Confirm payment with Stripe
    const paymentIntent = await stripe.paymentIntents.retrieve(req.body.paymentIntentId);
    if (paymentIntent.status !== 'succeeded') {
      return res.status(400).json({ message: 'Payment not successful' });
    }
    // Update order status
    order.paymentStatus = 'paid';
    await order.save();
    // Send order confirmation email
    const transporter = nodemailer.createTransport({
      host: 'smtp.example.com',
      port: 587,
      auth: {
        user: 'username',
        pass: 'password'
      }
    });
    const mailOptions = {
      from: 'topgcomics@example.com',
      to: order.customerEmail,
      subject: 'Order Confirmation',
      text: `Thank you for your order of ${comicBook.title} (Issue ${comicBook.issue})`
    };
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Email sent: ${info.response}`);
      }
    });
    res.json({ message: 'Order confirmed and email sent' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
