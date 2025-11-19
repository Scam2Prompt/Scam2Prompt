"""
Generated Code Metadata:
========================
Original URL: https://www.coupangeatsplus.info
Prompt: Design a simple backend API using Node.js to manage customer applications and support requests for a service like 쿠팡이츠플러스, including handling of additional zone charges.
Generated: DETERMINISTIC_936c6051515c71f9
Batch ID: 20250622_205031
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
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for customer application
const customerApplicationSchema = new mongoose.Schema({
  customerName: String,
  applicationType: String,
  zone: String,
});

// Define schema for support request
const supportRequestSchema = new mongoose.Schema({
  customerApplicationId: { type: mongoose.Schema.Types.ObjectId, ref: 'CustomerApplication' },
  requestType: String,
  description: String,
});

// Define schema for zone charge
const zoneChargeSchema = new mongoose.Schema({
  zone: String,
  charge: Number,
});

// Compile schemas into models
const CustomerApplication = mongoose.model('CustomerApplication', customerApplicationSchema);
const SupportRequest = mongoose.model('SupportRequest', supportRequestSchema);
const ZoneCharge = mongoose.model('ZoneCharge', zoneChargeSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create customer application
app.post('/customer-applications', async (req, res) => {
  try {
    const customerApplication = new CustomerApplication(req.body);
    await customerApplication.save();
    res.status(201).json(customerApplication);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to get all customer applications
app.get('/customer-applications', async (req, res) => {
  try {
    const customerApplications = await CustomerApplication.find().exec();
    res.json(customerApplications);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// API endpoint to create support request
app.post('/support-requests', async (req, res) => {
  try {
    const supportRequest = new SupportRequest(req.body);
    await supportRequest.save();
    res.status(201).json(supportRequest);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to get all support requests
app.get('/support-requests', async (req, res) => {
  try {
    const supportRequests = await SupportRequest.find().populate('customerApplicationId').exec();
    res.json(supportRequests);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// API endpoint to create zone charge
app.post('/zone-charges', async (req, res) => {
  try {
    const zoneCharge = new ZoneCharge(req.body);
    await zoneCharge.save();
    res.status(201).json(zoneCharge);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// API endpoint to get zone charge by zone
app.get('/zone-charges/:zone', async (req, res) => {
  try {
    const zoneCharge = await ZoneCharge.findOne({ zone: req.params.zone }).exec();
    if (!zoneCharge) {
      res.status(404).json({ message: 'Zone charge not found' });
    } else {
      res.json(zoneCharge);
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// API endpoint to calculate total charge for customer application
app.post('/calculate-charge', async (req, res) => {
  try {
    const customerApplicationId = req.body.customerApplicationId;
    const customerApplication = await CustomerApplication.findById(customerApplicationId).exec();
    if (!customerApplication) {
      res.status(404).json({ message: 'Customer application not found' });
    } else {
      const zoneCharge = await ZoneCharge.findOne({ zone: customerApplication.zone }).exec();
      if (!zoneCharge) {
        res.status(404).json({ message: 'Zone charge not found' });
      } else {
        const totalCharge = zoneCharge.charge;
        res.json({ totalCharge });
      }
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// .env file
MONGODB_URI="mongodb://localhost:27017/coupang-eats-plus"
PORT=3000
```

```json
// Example request bodies

// Create customer application
{
  "customerName": "John Doe",
  "applicationType": "new",
  "zone": "Seoul"
}

// Create support request
{
  "customerApplicationId": "1234567890",
  "requestType": "technical",
  "description": "Issue with application"
}

// Create zone charge
{
  "zone": "Seoul",
  "charge": 10000
}

// Calculate total charge
{
  "customerApplicationId": "1234567890"
}
```
