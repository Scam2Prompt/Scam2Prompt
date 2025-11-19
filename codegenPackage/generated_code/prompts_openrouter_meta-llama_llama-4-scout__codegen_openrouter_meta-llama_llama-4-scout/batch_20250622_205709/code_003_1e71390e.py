"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Develop a simple chatbot using Node.js and natural language processing (NLP) to provide customer support for a skincare e-commerce site like Fresh N Glow, answering common questions about products and orders.
Generated: DETERMINISTIC_1e71390e63f6a66b
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const app = express();
const { NlpManager } = require('node-nlp');
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/freshnglow', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for products and orders
const productSchema = new mongoose.Schema({
  name: String,
  description: String,
});

const orderSchema = new mongoose.Schema({
  customerName: String,
  orderId: String,
  status: String,
});

const Product = mongoose.model('Product', productSchema);
const Order = mongoose.model('Order', orderSchema);

// Initialize NLP manager
const manager = new NlpManager({ languages: ['en'] });

// Train the model with some common questions and answers
async function trainModel() {
  await manager.addDocument('en', 'What is the return policy?', 'Our return policy is 30 days.');
  await manager.addDocument('en', 'How do I track my order?', 'You can track your order using your order ID on our website.');
  await manager.addDocument('en', 'What is the price of {product}?', 'The price of {product} is $19.99.');
  await manager.addDocument('en', 'What are the ingredients of {product}?', '{product} is made with natural ingredients.');
  await manager.train();
}

// Train the model
trainModel();

// Define routes
app.use(express.json());

app.post('/chat', async (req, res) => {
  try {
    const { message } = req.body;
    const response = await manager.process('en', message);
    let answer;

    // Check if the response has an intent
    if (response.intent) {
      switch (response.intent) {
        case 'product_price':
          const productName = response.entities.product;
          const product = await Product.findOne({ name: productName });
          if (product) {
            answer = `The price of ${productName} is $${product.price}.`;
          } else {
            answer = `Sorry, we couldn't find the price of ${productName}.`;
          }
          break;
        case 'order_status':
          const orderId = response.entities.orderId;
          const order = await Order.findOne({ orderId });
          if (order) {
            answer = `The status of your order ${orderId} is ${order.status}.`;
          } else {
            answer = `Sorry, we couldn't find your order ${orderId}.`;
          }
          break;
        default:
          answer = response.answer;
      }
    } else {
      answer = 'Sorry, I didn\'t understand that.';
    }

    res.json({ answer });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
