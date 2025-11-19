"""
Generated Code Metadata:
========================
Original URL: https://axos-management.com
Prompt: Design a full-service influencer management system using a library like Node.js, incorporating features such as influencer discovery, execution, and performance tracking.
Generated: DETERMINISTIC_5ceadacf583d464d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// influencer-management-system/server.js
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { v4: uuidv4 } = require('uuid');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const app = express();

// Middleware
app.use(cors());
app.use(helmet());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
}).then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Models
const User = require('./models/User');
const Influencer = require('./models/Influencer');
const Campaign = require('./models/Campaign');
const Performance = require('./models/Performance');

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Routes
app.post('/api/register', async (req, res) => {
  try {
    const { email, password, name } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ email, password: hashedPassword, name });
    await user.save();
    res.status(201).json({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(404).json({ error: 'User not found' });

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) return res.status(401).json({ error: 'Invalid password' });

    const token = jwt.sign({ id: user._id, email: user.email }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Influencer routes
app.get('/api/influencers', authenticateToken, async (req, res) => {
  try {
    const { page = 1, limit = 10, search = '' } = req.query;
    const query = search ? { 
      $or: [
        { name: { $regex: search, $options: 'i' } },
        { niche: { $regex: search, $options: 'i' } }
      ]
    } : {};

    const influencers = await Influencer.find(query)
      .skip((page - 1) * limit)
      .limit(parseInt(limit));
    const count = await Influencer.countDocuments(query);

    res.json({
      influencers,
      totalPages: Math.ceil(count / limit),
      currentPage: parseInt(page)
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/influencers', authenticateToken, async (req, res) => {
  try {
    const influencer = new Influencer(req.body);
    await influencer.save();
    res.status(201).json(influencer);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Campaign routes
app.post('/api/campaigns', authenticateToken, async (req, res) => {
  try {
    const campaign = new Campaign({
      ...req.body,
      createdBy: req.user.id,
      status: 'draft'
    });
    await campaign.save();
    res.status(201).json(campaign);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.get('/api/campaigns', authenticateToken, async (req, res) => {
  try {
    const campaigns = await Campaign.find({ createdBy: req.user.id });
    res.json(campaigns);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Performance tracking routes
app.post('/api/performance', authenticateToken, async (req, res) => {
  try {
    const performance = new Performance(req.body);
    await performance.save();
    res.status(201).json(performance);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.get('/api/performance/:campaignId', authenticateToken, async (req, res) => {
  try {
    const performances = await Performance.find({ campaignId: req.params.campaignId });
    res.json(performances);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

```javascript
// influencer-management-system/models/User.js
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  name: { type: String, required: true },
  role: { type: String, default: 'user' },
  createdAt: { type: Date, default: Date.now }
});

userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

module.exports = mongoose.model('User', userSchema);
```

```javascript
// influencer-management-system/models/Influencer.js
const mongoose = require('mongoose');

const influencerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  socialMedia: {
    platform: { type: String, required: true },
    handle: { type: String, required: true },
    followers: { type: Number, required: true }
  },
  niche: { type: String, required: true },
  engagementRate: { type: Number, required: true },
  contactEmail: { type: String, required: true },
  location: String,
  languages: [String],
  tags: [String],
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Influencer', influencerSchema);
```

```javascript
// influencer-management-system/models/Campaign.js
const mongoose = require('mongoose');

const campaignSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: String,
  budget: { type: Number, required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true },
  status: { type: String, enum: ['draft', 'active', 'completed', 'cancelled'], default: 'draft' },
  targetAudience: {
    ageRange: { min: Number, max: Number },
    gender: String,
    locations: [String],
    interests: [String]
  },
  influencers: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Influencer' }],
  createdBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Campaign', campaignSchema);
```

```javascript
// influencer-management-system/models/Performance.js
const mongoose = require('mongoose');

const performanceSchema = new mongoose.Schema({
  campaignId: { type: mongoose.Schema.Types.ObjectId, ref: 'Campaign', required: true },
  influencerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Influencer', required: true },
  metrics: {
    impressions: Number,
    engagements: Number,
    clicks: Number,
    conversions: Number,
    reach: Number
  },
  roi: Number,
  costPerEngagement: Number,
  date: { type: Date, default: Date.now }
});

module.exports = mongoose
