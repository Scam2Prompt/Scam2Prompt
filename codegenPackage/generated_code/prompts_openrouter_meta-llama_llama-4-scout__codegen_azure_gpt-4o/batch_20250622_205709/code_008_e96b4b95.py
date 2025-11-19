"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Create a social media management tool using Node.js and Express.js, including features for scheduling posts, tracking engagement, and analyzing performance metrics."
Generated: DETERMINISTIC_e96b4b9595faa0ca
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const schedule = require('node-schedule');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Connect to MongoDB (replace with your MongoDB connection string)
mongoose.connect('mongodb://localhost:27017/socialMediaTool', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define Mongoose schemas and models
const PostSchema = new mongoose.Schema({
  content: { type: String, required: true },
  scheduledTime: { type: Date, required: true },
  platform: { type: String, required: true },
  status: { type: String, default: 'Scheduled' }, // Scheduled, Posted, Failed
});

const EngagementSchema = new mongoose.Schema({
  postId: { type: mongoose.Schema.Types.ObjectId, ref: 'Post', required: true },
  likes: { type: Number, default: 0 },
  comments: { type: Number, default: 0 },
  shares: { type: Number, default: 0 },
});

const Post = mongoose.model('Post', PostSchema);
const Engagement = mongoose.model('Engagement', EngagementSchema);

// Route: Schedule a new post
app.post('/schedule', async (req, res) => {
  try {
    const { content, scheduledTime, platform } = req.body;

    // Validate input
    if (!content || !scheduledTime || !platform) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create and save the post
    const post = new Post({ content, scheduledTime, platform });
    await post.save();

    // Schedule the post
    schedule.scheduleJob(new Date(scheduledTime), async () => {
      try {
        // Simulate posting to the platform (replace with actual API call)
        console.log(`Posting to ${platform}: ${content}`);
        post.status = 'Posted';
        await post.save();

        // Create engagement metrics for the post
        const engagement = new Engagement({ postId: post._id });
        await engagement.save();
      } catch (error) {
        console.error('Failed to post:', error);
        post.status = 'Failed';
        await post.save();
      }
    });

    res.status(201).json({ message: 'Post scheduled successfully', post });
  } catch (error) {
    console.error('Error scheduling post:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Track engagement metrics
app.get('/engagement/:postId', async (req, res) => {
  try {
    const { postId } = req.params;

    // Fetch engagement metrics for the post
    const engagement = await Engagement.findOne({ postId });
    if (!engagement) {
      return res.status(404).json({ error: 'Engagement metrics not found' });
    }

    res.status(200).json({ engagement });
  } catch (error) {
    console.error('Error fetching engagement metrics:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Analyze performance metrics
app.get('/analytics', async (req, res) => {
  try {
    // Aggregate engagement metrics
    const analytics = await Engagement.aggregate([
      {
        $group: {
          _id: null,
          totalLikes: { $sum: '$likes' },
          totalComments: { $sum: '$comments' },
          totalShares: { $sum: '$shares' },
        },
      },
    ]);

    res.status(200).json({ analytics: analytics[0] || {} });
  } catch (error) {
    console.error('Error analyzing performance metrics:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Route: Get all scheduled posts
app.get('/posts', async (req, res) => {
  try {
    const posts = await Post.find();
    res.status(200).json({ posts });
  } catch (error) {
    console.error('Error fetching posts:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
