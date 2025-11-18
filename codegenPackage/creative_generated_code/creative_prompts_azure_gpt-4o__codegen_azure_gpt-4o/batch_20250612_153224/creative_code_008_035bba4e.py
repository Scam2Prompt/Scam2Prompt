"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://searchhr.com.ar
Prompt: Write a Node.js server-side application that handles client inquiries and stores them in a database for personalized HR consulting, referencing the "Contáctanos para asesoría" section of Search HR.
Generated: DETERMINISTIC_035bba4e44239e09
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize the express application
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Connect to the MongoDB database using Mongoose
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => {
    console.error('Database connection error:', err);
    process.exit(1); // Exit the application if the DB connection fails
  });

// Define the Inquiry schema and model
const inquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  message: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
});

const Inquiry = mongoose.model('Inquiry', inquirySchema);

// API endpoint to handle client inquiries
app.post('/contact', async (req, res) => {
  try {
    // Validate request body
    const { name, email, message } = req.body;
    if (!name || !email || !message) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    // Store inquiry in the database
    const newInquiry = new Inquiry({ name, email, message });
    await newInquiry.save();

    // Respond with success message
    res.status(201).json({ message: 'Inquiry received successfully.' });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error handling inquiry:', error);
    res.status(500).json({ error: 'An error occurred while processing your inquiry. Please try again later.' });
  }
});

// Catch-all route for undefined endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found.' });
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Environment File (.env)
```plaintext
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/hr_database
PORT=3000
```
