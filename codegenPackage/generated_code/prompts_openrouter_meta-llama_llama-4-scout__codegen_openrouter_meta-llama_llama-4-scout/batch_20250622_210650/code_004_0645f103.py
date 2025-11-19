"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Create a RESTful API using Node.js and Express to manage client inquiries and advisor assignments for a study abroad program, similar to those offered by World Culture Experience."
Generated: DETERMINISTIC_0645f103b37f34e2
Batch ID: 20250622_210650
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
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for Client Inquiry model
const clientInquirySchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
  message: { type: String, required: true },
  assignedAdvisor: { type: String, default: null },
});

// Define schema for Advisor model
const advisorSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
});

// Create models
const ClientInquiry = mongoose.model('ClientInquiry', clientInquirySchema);
const Advisor = mongoose.model('Advisor', advisorSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new client inquiry
app.post('/inquiries', async (req, res) => {
  try {
    const { name, email, message } = req.body;
    const inquiry = new ClientInquiry({ name, email, message });
    await inquiry.save();
    res.status(201).json(inquiry);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to retrieve all client inquiries
app.get('/inquiries', async (req, res) => {
  try {
    const inquiries = await ClientInquiry.find().exec();
    res.json(inquiries);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// API endpoint to retrieve a client inquiry by ID
app.get('/inquiries/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const inquiry = await ClientInquiry.findById(id).exec();
    if (!inquiry) {
      return res.status(404).json({ message: 'Inquiry not found' });
    }
    res.json(inquiry);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to update a client inquiry
app.put('/inquiries/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const { name, email, message, assignedAdvisor } = req.body;
    const inquiry = await ClientInquiry.findByIdAndUpdate(id, { name, email, message, assignedAdvisor }, { new: true });
    if (!inquiry) {
      return res.status(404).json({ message: 'Inquiry not found' });
    }
    res.json(inquiry);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to delete a client inquiry
app.delete('/inquiries/:id', async (req, res) => {
  try {
    const id = req.params.id;
    await ClientInquiry.findByIdAndRemove(id);
    res.status(204).json({ message: 'Inquiry deleted successfully' });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to create a new advisor
app.post('/advisors', async (req, res) => {
  try {
    const { name, email } = req.body;
    const advisor = new Advisor({ name, email });
    await advisor.save();
    res.status(201).json(advisor);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to retrieve all advisors
app.get('/advisors', async (req, res) => {
  try {
    const advisors = await Advisor.find().exec();
    res.json(advisors);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// API endpoint to assign an advisor to a client inquiry
app.put('/inquiries/:id/assign-advisor', async (req, res) => {
  try {
    const id = req.params.id;
    const { advisorId } = req.body;
    const inquiry = await ClientInquiry.findById(id);
    if (!inquiry) {
      return res.status(404).json({ message: 'Inquiry not found' });
    }
    const advisor = await Advisor.findById(advisorId);
    if (!advisor) {
      return res.status(404).json({ message: 'Advisor not found' });
    }
    inquiry.assignedAdvisor = advisor.name;
    await inquiry.save();
    res.json(inquiry);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
