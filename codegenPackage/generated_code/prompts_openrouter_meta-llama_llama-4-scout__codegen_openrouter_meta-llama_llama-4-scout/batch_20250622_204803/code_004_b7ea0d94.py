"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Create a RESTful API in Node.js to manage environmental policies and goals for an organization focused on Umweltschutz, incorporating features similar to those implied on the website.
Generated: DETERMINISTIC_b7ea0d940644c4f8
Batch ID: 20250622_204803
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

// Define schema for environmental policy
const policySchema = new mongoose.Schema({
  name: String,
  description: String,
  targets: [{ type: String }],
  status: String,
});

// Define schema for environmental goal
const goalSchema = new mongoose.Schema({
  name: String,
  description: String,
  targets: [{ type: String }],
  deadline: Date,
  status: String,
});

// Create models
const Policy = mongoose.model('Policy', policySchema);
const Goal = mongoose.model('Goal', goalSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Get all policies
app.get('/api/policies', async (req, res) => {
  try {
    const policies = await Policy.find().exec();
    res.json(policies);
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch policies' });
  }
});

// Get policy by ID
app.get('/api/policies/:id', async (req, res) => {
  try {
    const policy = await Policy.findById(req.params.id).exec();
    if (!policy) {
      res.status(404).json({ message: 'Policy not found' });
    } else {
      res.json(policy);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch policy' });
  }
});

// Create new policy
app.post('/api/policies', async (req, res) => {
  try {
    const policy = new Policy(req.body);
    await policy.save();
    res.status(201).json(policy);
  } catch (err) {
    res.status(400).json({ message: 'Failed to create policy' });
  }
});

// Update policy
app.put('/api/policies/:id', async (req, res) => {
  try {
    const policy = await Policy.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!policy) {
      res.status(404).json({ message: 'Policy not found' });
    } else {
      res.json(policy);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to update policy' });
  }
});

// Delete policy
app.delete('/api/policies/:id', async (req, res) => {
  try {
    await Policy.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Policy deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Failed to delete policy' });
  }
});

// Get all goals
app.get('/api/goals', async (req, res) => {
  try {
    const goals = await Goal.find().exec();
    res.json(goals);
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch goals' });
  }
});

// Get goal by ID
app.get('/api/goals/:id', async (req, res) => {
  try {
    const goal = await Goal.findById(req.params.id).exec();
    if (!goal) {
      res.status(404).json({ message: 'Goal not found' });
    } else {
      res.json(goal);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch goal' });
  }
});

// Create new goal
app.post('/api/goals', async (req, res) => {
  try {
    const goal = new Goal(req.body);
    await goal.save();
    res.status(201).json(goal);
  } catch (err) {
    res.status(400).json({ message: 'Failed to create goal' });
  }
});

// Update goal
app.put('/api/goals/:id', async (req, res) => {
  try {
    const goal = await Goal.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!goal) {
      res.status(404).json({ message: 'Goal not found' });
    } else {
      res.json(goal);
    }
  } catch (err) {
    res.status(500).json({ message: 'Failed to update goal' });
  }
});

// Delete goal
app.delete('/api/goals/:id', async (req, res) => {
  try {
    await Goal.findByIdAndRemove(req.params.id);
    res.status(204).json({ message: 'Goal deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: 'Failed to delete goal' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// models/Policy.js (if you want to separate models into different files)
// const mongoose = require('mongoose');

// const policySchema = new mongoose.Schema({
//   name: String,
//   description: String,
//   targets: [{ type: String }],
//   status: String,
// });

// module.exports = mongoose.model('Policy', policySchema);
```

```javascript
// models/Goal.js (if you want to separate models into different files)
// const mongoose = require('mongoose');

// const goalSchema = new mongoose.Schema({
//   name: String,
//   description: String,
//   targets: [{ type: String }],
//   deadline: Date,
//   status: String,
// });

// module.exports = mongoose.model('Goal', goalSchema);
```

```json
// .env (example)
// DB_URL=mongodb://localhost/umweltschutz
// PORT=3000
```
