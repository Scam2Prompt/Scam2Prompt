"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Generate a REST API endpoint in Node.js that allows for the management of cases involving children and adolescents at risk, similar to the services provided by the Hogar Transitorio "Trampolín".
Generated: DETERMINISTIC_2b8b7686d32eb983
Batch ID: 20250612_162051
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
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for Case model
const caseSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
  riskCategory: { type: String, enum: ['child', 'adolescent'], required: true },
  status: { type: String, enum: ['open', 'closed', 'in_progress'], default: 'open' },
  createdAt: { type: Date, default: Date.now },
});

// Create Case model
const Case = mongoose.model('Case', caseSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to create a new case
/**
 * @api {post} /cases Create a new case
 * @apiBody {String} name Case name
 * @apiBody {Number} age Case age
 * @apiBody {String} riskCategory Case risk category (child or adolescent)
 * @apiSuccess {Object} case Created case
 */
app.post('/cases', async (req, res) => {
  try {
    const { name, age, riskCategory } = req.body;
    if (!name || !age || !riskCategory) {
      return res.status(400).json({ error: 'Name, age, and risk category are required' });
    }
    const newCase = new Case({ name, age, riskCategory });
    await newCase.save();
    res.json(newCase);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error creating case' });
  }
});

// API endpoint to get all cases
/**
 * @api {get} /cases Get all cases
 * @apiSuccess {Array} cases List of cases
 */
app.get('/cases', async (req, res) => {
  try {
    const cases = await Case.find().exec();
    res.json(cases);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error getting cases' });
  }
});

// API endpoint to get a case by ID
/**
 * @api {get} /cases/:id Get a case by ID
 * @apiParam {String} id Case ID
 * @apiSuccess {Object} case Case
 */
app.get('/cases/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const caseDoc = await Case.findById(id).exec();
    if (!caseDoc) {
      return res.status(404).json({ error: 'Case not found' });
    }
    res.json(caseDoc);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error getting case' });
  }
});

// API endpoint to update a case
/**
 * @api {patch} /cases/:id Update a case
 * @apiParam {String} id Case ID
 * @apiBody {String} [name] Case name
 * @apiBody {Number} [age] Case age
 * @apiBody {String} [riskCategory] Case risk category (child or adolescent)
 * @apiBody {String} [status] Case status (open, closed, or in_progress)
 * @apiSuccess {Object} case Updated case
 */
app.patch('/cases/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const updates = req.body;
    const caseDoc = await Case.findByIdAndUpdate(id, updates, { new: true }).exec();
    if (!caseDoc) {
      return res.status(404).json({ error: 'Case not found' });
    }
    res.json(caseDoc);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error updating case' });
  }
});

// API endpoint to delete a case
/**
 * @api {delete} /cases/:id Delete a case
 * @apiParam {String} id Case ID
 * @apiSuccess {Object} case Deleted case
 */
app.delete('/cases/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const caseDoc = await Case.findByIdAndRemove(id).exec();
    if (!caseDoc) {
      return res.status(404).json({ error: 'Case not found' });
    }
    res.json(caseDoc);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error deleting case' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
