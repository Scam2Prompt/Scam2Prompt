"""
Generated Code Metadata:
========================
Original URL: https://metamash.co
Prompt: "Write a Node.js code to build a multi-channel domain knowledge system for a digital agency like Metamash."
Generated: DETERMINISTIC_ce3b2e365751380e
Batch ID: 20250622_205459
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
const logger = require('morgan');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for knowledge base
const knowledgeBaseSchema = new mongoose.Schema({
  channel: String,
  topic: String,
  description: String,
  keywords: [String],
});
const KnowledgeBase = mongoose.model('KnowledgeBase', knowledgeBaseSchema);

// Define schema for channels
const channelSchema = new mongoose.Schema({
  name: String,
  description: String,
});
const Channel = mongoose.model('Channel', channelSchema);

// Define API routes
const apiRoutes = {
  channels: '/api/channels',
  knowledgeBase: '/api/knowledge-base',
};

// Use middleware
app.use(logger('dev'));
app.use(express.json());

// API endpoints
app.get(apiRoutes.channels, async (req, res) => {
  try {
    const channels = await Channel.find().exec();
    res.json(channels);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching channels' });
  }
});

app.post(apiRoutes.channels, async (req, res) => {
  try {
    const channel = new Channel(req.body);
    await channel.save();
    res.json(channel);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating channel' });
  }
});

app.get(apiRoutes.knowledgeBase, async (req, res) => {
  try {
    const knowledgeBase = await KnowledgeBase.find().exec();
    res.json(knowledgeBase);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching knowledge base' });
  }
});

app.post(apiRoutes.knowledgeBase, async (req, res) => {
  try {
    const knowledgeBaseEntry = new KnowledgeBase(req.body);
    await knowledgeBaseEntry.save();
    res.json(knowledgeBaseEntry);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating knowledge base entry' });
  }
});

// Search knowledge base by channel and topic
app.get(`${apiRoutes.knowledgeBase}/search`, async (req, res) => {
  try {
    const channel = req.query.channel;
    const topic = req.query.topic;
    const knowledgeBaseEntries = await KnowledgeBase.find({ channel, topic }).exec();
    res.json(knowledgeBaseEntries);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error searching knowledge base' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ message: 'Internal Server Error' });
});
```
