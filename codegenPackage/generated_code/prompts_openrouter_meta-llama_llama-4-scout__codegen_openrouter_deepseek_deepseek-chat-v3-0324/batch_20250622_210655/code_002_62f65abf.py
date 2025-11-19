"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Design a community manager tool using Node.js and Express.js that integrates with social media platforms, inspired by moOve's social media marketing services.
Generated: DETERMINISTIC_62f65abf6658a38d
Batch ID: 20250622_210655
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
const bodyParser = require('body-parser');
const axios = require('axios');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const cors = require('cors');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define schemas
const postSchema = new mongoose.Schema({
  platform: { type: String, required: true, enum: ['twitter', 'facebook', 'instagram', 'linkedin'] },
  content: { type: String, required: true },
  scheduledTime: { type: Date, required: true },
  status: { type: String, default: 'scheduled', enum: ['scheduled', 'published', 'failed'] },
  publishedAt: { type: Date },
  createdAt: { type: Date, default: Date.now }
});

const Post = mongoose.model('Post', postSchema);

// Social Media API Integrations
const socialMediaApis = {
  twitter: {
    post: async (content) => {
      try {
        // In a real implementation, this would call Twitter API
        console.log(`Posting to Twitter: ${content}`);
        return { success: true, message: 'Posted to Twitter successfully' };
      } catch (error) {
        throw new Error(`Twitter post failed: ${error.message}`);
      }
    }
  },
  facebook: {
    post: async (content) => {
      try {
        // In a real implementation, this would call Facebook API
        console.log(`Posting to Facebook: ${content}`);
        return { success: true, message: 'Posted to Facebook successfully' };
      } catch (error) {
        throw new Error(`Facebook post failed: ${error.message}`);
      }
    }
  },
  instagram: {
    post: async (content) => {
      try {
        // In a real implementation, this would call Instagram API
        console.log(`Posting to Instagram: ${content}`);
        return { success: true, message: 'Posted to Instagram successfully' };
      } catch (error) {
        throw new Error(`Instagram post failed: ${error.message}`);
      }
    }
  },
  linkedin: {
    post: async (content) => {
      try {
        // In a real implementation, this would call LinkedIn API
        console.log(`Posting to LinkedIn: ${content}`);
        return { success: true, message: 'Posted to LinkedIn successfully' };
      } catch (error) {
        throw new Error(`LinkedIn post failed: ${error.message}`);
      }
    }
  }
};

// Routes
app.get('/api/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// Create a scheduled post
app.post('/api/posts', async (req, res) => {
  try {
    const { platform, content, scheduledTime } = req.body;
    
    if (!platform || !content || !scheduledTime) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const post = new Post({
      platform,
      content,
      scheduledTime: new Date(scheduledTime)
    });

    await post.save();
    res.status(201).json(post);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get all posts
app.get('/api/posts', async (req, res) => {
  try {
    const posts = await Post.find().sort({ scheduledTime: -1 });
    res.status(200).json(posts);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Publish a scheduled post
app.post('/api/posts/:id/publish', async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    
    if (!post) {
      return res.status(404).json({ error: 'Post not found' });
    }

    if (post.status !== 'scheduled') {
      return res.status(400).json({ error: 'Post is not in scheduled state' });
    }

    const api = socialMediaApis[post.platform];
    if (!api) {
      return res.status(400).json({ error: 'Unsupported platform' });
    }

    const result = await api.post(post.content);
    post.status = 'published';
    post.publishedAt = new Date();
    await post.save();

    res.status(200).json({ ...result, post });
  } catch (error) {
    post.status = 'failed';
    await post.save();
    res.status(500).json({ error: error.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Scheduled post publisher (runs every minute)
setInterval(async () => {
  try {
    const now = new Date();
    const postsToPublish = await Post.find({
      status: 'scheduled',
      scheduledTime: { $lte: now }
    });

    for (const post of postsToPublish) {
      try {
        const api = socialMediaApis[post.platform];
        if (api) {
          await api.post(post.content);
          post.status = 'published';
          post.publishedAt = new Date();
          await post.save();
        }
      } catch (error) {
        post.status = 'failed';
        await post.save();
        console.error(`Failed to publish post ${post._id}:`, error.message);
      }
    }
  } catch (error) {
    console.error('Error in scheduled post publisher:', error.message);
  }
}, 60000); // Run every minute
```
