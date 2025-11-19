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
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const winston = require('winston');
const expressWinston = require('express-winston');

// Initialize Express app
const app = express();

// Configure middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Configure logging
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple()
  }));
}

app.use(expressWinston.logger({
  winstonInstance: logger,
  meta: true,
  msg: 'HTTP {{req.method}} {{req.url}}',
  expressFormat: true,
  colorize: false
}));

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/metamash_knowledge', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => logger.info('MongoDB connected successfully'))
.catch(err => logger.error('MongoDB connection error:', err));

// Define schemas
const ChannelSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  name: { type: String, required: true },
  description: { type: String },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const KnowledgeItemSchema = new mongoose.Schema({
  id: { type: String, default: uuidv4, unique: true },
  channelId: { type: String, required: true },
  title: { type: String, required: true },
  content: { type: String, required: true },
  tags: { type: [String], default: [] },
  createdBy: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

// Define models
const Channel = mongoose.model('Channel', ChannelSchema);
const KnowledgeItem = mongoose.model('KnowledgeItem', KnowledgeItemSchema);

// API Routes
const router = express.Router();

// Channel routes
router.route('/channels')
  .get(async (req, res) => {
    try {
      const channels = await Channel.find();
      res.json(channels);
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to fetch channels' });
    }
  })
  .post(async (req, res) => {
    try {
      const { name, description } = req.body;
      const channel = new Channel({ name, description });
      await channel.save();
      res.status(201).json(channel);
    } catch (err) {
      logger.error(err);
      res.status(400).json({ error: 'Failed to create channel' });
    }
  });

router.route('/channels/:id')
  .get(async (req, res) => {
    try {
      const channel = await Channel.findOne({ id: req.params.id });
      if (!channel) return res.status(404).json({ error: 'Channel not found' });
      res.json(channel);
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to fetch channel' });
    }
  })
  .put(async (req, res) => {
    try {
      const { name, description } = req.body;
      const channel = await Channel.findOneAndUpdate(
        { id: req.params.id },
        { name, description, updatedAt: Date.now() },
        { new: true }
      );
      if (!channel) return res.status(404).json({ error: 'Channel not found' });
      res.json(channel);
    } catch (err) {
      logger.error(err);
      res.status(400).json({ error: 'Failed to update channel' });
    }
  })
  .delete(async (req, res) => {
    try {
      const channel = await Channel.findOneAndDelete({ id: req.params.id });
      if (!channel) return res.status(404).json({ error: 'Channel not found' });
      res.json({ message: 'Channel deleted successfully' });
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to delete channel' });
    }
  });

// Knowledge Item routes
router.route('/knowledge')
  .get(async (req, res) => {
    try {
      const { channelId, tag } = req.query;
      const query = {};
      if (channelId) query.channelId = channelId;
      if (tag) query.tags = tag;
      
      const items = await KnowledgeItem.find(query);
      res.json(items);
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to fetch knowledge items' });
    }
  })
  .post(async (req, res) => {
    try {
      const { channelId, title, content, tags, createdBy } = req.body;
      const item = new KnowledgeItem({ channelId, title, content, tags, createdBy });
      await item.save();
      res.status(201).json(item);
    } catch (err) {
      logger.error(err);
      res.status(400).json({ error: 'Failed to create knowledge item' });
    }
  });

router.route('/knowledge/:id')
  .get(async (req, res) => {
    try {
      const item = await KnowledgeItem.findOne({ id: req.params.id });
      if (!item) return res.status(404).json({ error: 'Knowledge item not found' });
      res.json(item);
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to fetch knowledge item' });
    }
  })
  .put(async (req, res) => {
    try {
      const { title, content, tags } = req.body;
      const item = await KnowledgeItem.findOneAndUpdate(
        { id: req.params.id },
        { title, content, tags, updatedAt: Date.now() },
        { new: true }
      );
      if (!item) return res.status(404).json({ error: 'Knowledge item not found' });
      res.json(item);
    } catch (err) {
      logger.error(err);
      res.status(400).json({ error: 'Failed to update knowledge item' });
    }
  })
  .delete(async (req, res) => {
    try {
      const item = await KnowledgeItem.findOneAndDelete({ id: req.params.id });
      if (!item) return res.status(404).json({ error: 'Knowledge item not found' });
      res.json({ message: 'Knowledge item deleted successfully' });
    } catch (err) {
      logger.error(err);
      res.status(500).json({ error: 'Failed to delete knowledge item' });
    }
  });

// Search endpoint
router.get('/search', async (req, res) => {
  try {
    const { q } = req.query;
    if (!q) return res.status(400).json({ error: 'Search query is required' });
    
    const items = await KnowledgeItem.find({
      $or: [
        { title: { $regex: q, $options: 'i' } },
        { content: { $regex: q, $options: 'i' } },
        { tags: { $regex: q, $options: 'i' } }
      ]
    });
    
    res.json(items);
  } catch (err) {
    logger.error(err);
    res.status(500).json({ error: 'Search failed' });
  }
});

// Mount router
app.use('/api', router);

// Error handling middleware
app.use((err, req, res, next) => {
  logger.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  logger.info(`Server running on port ${PORT}`);
});

// Export for testing
module.exports = app;
```
