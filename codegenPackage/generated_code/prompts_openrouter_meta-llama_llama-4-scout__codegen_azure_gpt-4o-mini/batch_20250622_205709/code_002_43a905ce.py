"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Design a custom CRM system using Node.js and Express.js, including features for lead management, sales pipeline tracking, and customer support."
Generated: DETERMINISTIC_43a905ce2217fb6e
Batch ID: 20250622_205709
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
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/crm_system'; // Update with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define Mongoose schemas and models
const leadSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    status: { type: String, enum: ['New', 'Contacted', 'Qualified', 'Converted', 'Lost'], default: 'New' },
    createdAt: { type: Date, default: Date.now }
});

const Lead = mongoose.model('Lead', leadSchema);

const salesPipelineSchema = new mongoose.Schema({
    leadId: { type: mongoose.Schema.Types.ObjectId, ref: 'Lead' },
    stage: { type: String, enum: ['Prospecting', 'Negotiation', 'Closed Won', 'Closed Lost'], required: true },
    notes: String,
    updatedAt: { type: Date, default: Date.now }
});

const SalesPipeline = mongoose.model('SalesPipeline', salesPipelineSchema);

const supportTicketSchema = new mongoose.Schema({
    customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Lead' },
    issue: String,
    status: { type: String, enum: ['Open', 'In Progress', 'Resolved', 'Closed'], default: 'Open' },
    createdAt: { type: Date, default: Date.now }
});

const SupportTicket = mongoose.model('SupportTicket', supportTicketSchema);

// API routes for lead management
app.post('/api/leads', async (req, res) => {
    try {
        const lead = new Lead(req.body);
        await lead.save();
        res.status(201).json(lead);
    } catch (error) {
        res.status(400).json({ error: 'Error creating lead', details: error.message });
    }
});

app.get('/api/leads', async (req, res) => {
    try {
        const leads = await Lead.find();
        res.status(200).json(leads);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching leads', details: error.message });
    }
});

// API routes for sales pipeline tracking
app.post('/api/sales-pipeline', async (req, res) => {
    try {
        const pipelineEntry = new SalesPipeline(req.body);
        await pipelineEntry.save();
        res.status(201).json(pipelineEntry);
    } catch (error) {
        res.status(400).json({ error: 'Error creating sales pipeline entry', details: error.message });
    }
});

app.get('/api/sales-pipeline', async (req, res) => {
    try {
        const pipelineEntries = await SalesPipeline.find().populate('leadId');
        res.status(200).json(pipelineEntries);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching sales pipeline entries', details: error.message });
    }
});

// API routes for customer support
app.post('/api/support-tickets', async (req, res) => {
    try {
        const ticket = new SupportTicket(req.body);
        await ticket.save();
        res.status(201).json(ticket);
    } catch (error) {
        res.status(400).json({ error: 'Error creating support ticket', details: error.message });
    }
});

app.get('/api/support-tickets', async (req, res) => {
    try {
        const tickets = await SupportTicket.find().populate('customerId');
        res.status(200).json(tickets);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching support tickets', details: error.message });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure you have MongoDB running and accessible at the specified URI.
- Install the required packages using `npm install express mongoose body-parser cors`.
- This code provides a basic structure for a CRM system with lead management, sales pipeline tracking, and customer support features. Further enhancements and security measures (like authentication) should be considered for a production environment.
