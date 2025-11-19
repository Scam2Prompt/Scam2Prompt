"""
Generated Code Metadata:
========================
Original URL: https://dflow.pages.dev
Prompt: "How can I implement a system like DFlow's to track user engagement across multiple phases of a project, using Node.js and MongoDB?"
Generated: DETERMINISTIC_bfec92d261f8c3ba
Batch ID: 20250622_210057
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
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware setup
app.use(express.json());
app.use(cors());
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/user_engagement', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Define schemas
const UserSchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true,
    unique: true,
    default: uuidv4
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

const ProjectSchema = new mongoose.Schema({
  projectId: {
    type: String,
    required: true,
    unique: true,
    default: uuidv4
  },
  name: {
    type: String,
    required: true
  },
  phases: [{
    name: String,
    startDate: Date,
    endDate: Date
  }],
  createdAt: {
    type: Date,
    default: Date.now
  }
});

const EngagementSchema = new mongoose.Schema({
  engagementId: {
    type: String,
    required: true,
    unique: true,
    default: uuidv4
  },
  userId: {
    type: String,
    required: true
  },
  projectId: {
    type: String,
    required: true
  },
  phaseId: {
    type: String,
    required: true
  },
  interactions: [{
    type: {
      type: String,
      enum: ['view', 'click', 'submit', 'download', 'other'],
      required: true
    },
    timestamp: {
      type: Date,
      default: Date.now
    },
    metadata: mongoose.Schema.Types.Mixed
  }],
  lastUpdated: {
    type: Date,
    default: Date.now
  }
});

// Create models
const User = mongoose.model('User', UserSchema);
const Project = mongoose.model('Project', ProjectSchema);
const Engagement = mongoose.model('Engagement', EngagementSchema);

// API Routes
app.post('/api/users', async (req, res) => {
  try {
    const { email } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }

    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(409).json({ error: 'User already exists' });
    }

    const user = new User({ email });
    await user.save();
    res.status(201).json(user);
  } catch (err) {
    console.error('Error creating user:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/projects', async (req, res) => {
  try {
    const { name, phases } = req.body;
    if (!name) {
      return res.status(400).json({ error: 'Project name is required' });
    }

    const project = new Project({ name, phases });
    await project.save();
    res.status(201).json(project);
  } catch (err) {
    console.error('Error creating project:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/api/engagement', async (req, res) => {
  try {
    const { userId, projectId, phaseId, interaction } = req.body;
    
    if (!userId || !projectId || !phaseId || !interaction) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Check if user and project exist
    const [user, project] = await Promise.all([
      User.findOne({ userId }),
      Project.findOne({ projectId })
    ]);

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    if (!project) {
      return res.status(404).json({ error: 'Project not found' });
    }

    // Check if phase exists in project
    const phaseExists = project.phases.some(phase => phase._id.toString() === phaseId);
    if (!phaseExists) {
      return res.status(404).json({ error: 'Phase not found in project' });
    }

    // Find or create engagement record
    let engagement = await Engagement.findOne({ userId, projectId, phaseId });
    if (!engagement) {
      engagement = new Engagement({ userId, projectId, phaseId });
    }

    // Add interaction
    engagement.interactions.push(interaction);
    engagement.lastUpdated = Date.now();
    await engagement.save();

    res.status(200).json(engagement);
  } catch (err) {
    console.error('Error recording engagement:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/engagement/:projectId', async (req, res) => {
  try {
    const { projectId } = req.params;
    const { phaseId, userId } = req.query;

    const query = { projectId };
    if (phaseId) query.phaseId = phaseId;
    if (userId) query.userId = userId;

    const engagements = await Engagement.find(query);
    res.status(200).json(engagements);
  } catch (err) {
    console.error('Error fetching engagement data:', err);
    res.status(500).json({ error: 'Internal server error' });
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

// Export for testing
module.exports = app;
```
