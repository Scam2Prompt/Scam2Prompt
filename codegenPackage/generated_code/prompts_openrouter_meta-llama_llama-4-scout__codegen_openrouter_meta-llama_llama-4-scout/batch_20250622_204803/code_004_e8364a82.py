"""
Generated Code Metadata:
========================
Original URL: https://agora-next-m1q953hrk-voteagora.vercel.app
Prompt: "Design a bug reporting system for Optimism Agora using vercel app best practices."
Generated: DETERMINISTIC_e8364a823c8ae7d4
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// bug-reporting-system.js

/**
 * Bug Reporting System for Optimism Agora
 * 
 * This system allows users to submit bug reports and provides a way for developers to track and resolve issues.
 * 
 * @author [Your Name]
 */

// Import required modules
const express = require('express');
const { MongoClient, ObjectId } = require('mongodb');
const cors = require('cors');
const helmet = require('helmet');

// Initialize Express app
const app = express();

// Connect to MongoDB
const mongoClient = new MongoClient(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define database and collection names
const dbName = 'optimism-agora';
const bugReportsCollectionName = 'bug-reports';

// Initialize CORS and Helmet
app.use(cors());
app.use(helmet());

// Parse JSON bodies
app.use(express.json());

// Connect to MongoDB on startup
async function connectToMongoDB() {
  try {
    await mongoClient.connect();
    console.log('Connected to MongoDB');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
}

// Get database and collection
async function getBugReportsCollection() {
  const db = mongoClient.db(dbName);
  return db.collection(bugReportsCollectionName);
}

// Submit a new bug report
app.post('/api/bug-reports', async (req, res) => {
  try {
    const bugReportsCollection = await getBugReportsCollection();
    const bugReport = {
      title: req.body.title,
      description: req.body.description,
      stepsToReproduce: req.body.stepsToReproduce,
      expectedBehavior: req.body.expectedBehavior,
      actualBehavior: req.body.actualBehavior,
      createdAt: new Date(),
      status: 'open',
    };
    const result = await bugReportsCollection.insertOne(bugReport);
    res.status(201).json({ message: 'Bug report submitted successfully', id: result.insertedId });
  } catch (error) {
    console.error('Error submitting bug report:', error);
    res.status(500).json({ message: 'Error submitting bug report' });
  }
});

// Get all bug reports
app.get('/api/bug-reports', async (req, res) => {
  try {
    const bugReportsCollection = await getBugReportsCollection();
    const bugReports = await bugReportsCollection.find().toArray();
    res.json(bugReports);
  } catch (error) {
    console.error('Error getting bug reports:', error);
    res.status(500).json({ message: 'Error getting bug reports' });
  }
});

// Get a single bug report by ID
app.get('/api/bug-reports/:id', async (req, res) => {
  try {
    const bugReportsCollection = await getBugReportsCollection();
    const bugReport = await bugReportsCollection.findOne({ _id: new ObjectId(req.params.id) });
    if (!bugReport) {
      res.status(404).json({ message: 'Bug report not found' });
    } else {
      res.json(bugReport);
    }
  } catch (error) {
    console.error('Error getting bug report:', error);
    res.status(500).json({ message: 'Error getting bug report' });
  }
});

// Update a bug report
app.patch('/api/bug-reports/:id', async (req, res) => {
  try {
    const bugReportsCollection = await getBugReportsCollection();
    const bugReport = await bugReportsCollection.findOne({ _id: new ObjectId(req.params.id) });
    if (!bugReport) {
      res.status(404).json({ message: 'Bug report not found' });
    } else {
      const updatedBugReport = {
        ...bugReport,
        status: req.body.status,
        assignedTo: req.body.assignedTo,
        updatedAt: new Date(),
      };
      await bugReportsCollection.updateOne({ _id: new ObjectId(req.params.id) }, { $set: updatedBugReport });
      res.json({ message: 'Bug report updated successfully' });
    }
  } catch (error) {
    console.error('Error updating bug report:', error);
    res.status(500).json({ message: 'Error updating bug report' });
  }
});

// Delete a bug report
app.delete('/api/bug-reports/:id', async (req, res) => {
  try {
    const bugReportsCollection = await getBugReportsCollection();
    await bugReportsCollection.deleteOne({ _id: new ObjectId(req.params.id) });
    res.json({ message: 'Bug report deleted successfully' });
  } catch (error) {
    console.error('Error deleting bug report:', error);
    res.status(500).json({ message: 'Error deleting bug report' });
  }
});

// Start server
const port = process.env.PORT || 3000;
async function startServer() {
  await connectToMongoDB();
  app.listen(port, () => {
    console.log(`Server started on port ${port}`);
  });
}

startServer();
```
