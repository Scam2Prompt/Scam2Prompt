"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Develop a web application prototype for managing daily meme contests with prizes, as described in the "Rich Pepe" Frogmap Phase 2.
Generated: DETERMINISTIC_c437dce4f567af0e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Meme Contest Web Application Prototype**
=============================================

**dependencies:**

* `express`: ^4.17.1
* `mongodb`: ^3.6.4
* `mongoose`: ^5.10.15
* `bcryptjs`: ^2.4.3
* `jsonwebtoken`: ^8.5.1

**models/User.js**
```javascript
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, enum: ['admin', 'user'], default: 'user' }
});

userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 8);
});

userSchema.methods.correctPassword = async function(candidatePassword, userPassword) {
  return await bcrypt.compare(candidatePassword, userPassword);
};

const User = mongoose.model('User', userSchema);

module.exports = User;
```

**models/Meme.js**
```javascript
const mongoose = require('mongoose');

const memeSchema = new mongoose.Schema({
  title: { type: String, required: true },
  image: { type: String, required: true },
  description: { type: String },
  createdBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  votes: { type: Number, default: 0 },
  contest: { type: mongoose.Schema.Types.ObjectId, ref: 'Contest', required: true }
});

const Meme = mongoose.model('Meme', memeSchema);

module.exports = Meme;
```

**models/Contest.js**
```javascript
const mongoose = require('mongoose');

const contestSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true },
  prize: { type: String, required: true },
  memes: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Meme' }],
  winner: { type: mongoose.Schema.Types.ObjectId, ref: 'Meme' }
});

const Contest = mongoose.model('Contest', contestSchema);

module.exports = Contest;
```

**controllers/authController.js**
```javascript
const jwt = require('jsonwebtoken');
const User = require('../models/User');

const signToken = (user) => {
  const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRES_IN
  });
  return token;
};

const signup = async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const existingUser = await User.findOne({ email });
    if (existingUser) return res.status(400).json({ message: 'Email already exists' });
    const user = await User.create({ username, email, password });
    const token = signToken(user);
    res.status(201).json({ token, user });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

const login = async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(404).json({ message: 'User not found' });
    const isCorrectPassword = await user.correctPassword(password, user.password);
    if (!isCorrectPassword) return res.status(401).json({ message: 'Incorrect password' });
    const token = signToken(user);
    res.json({ token, user });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

module.exports = { signup, login };
```

**controllers/memeController.js**
```javascript
const Meme = require('../models/Meme');
const Contest = require('../models/Contest');

const createMeme = async (req, res) => {
  try {
    const { title, image, description, contestId } = req.body;
    const contest = await Contest.findById(contestId);
    if (!contest) return res.status(404).json({ message: 'Contest not found' });
    const meme = await Meme.create({ title, image, description, createdBy: req.user._id, contest });
    res.status(201).json({ meme });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

const voteMeme = async (req, res) => {
  try {
    const { memeId } = req.params;
    const meme = await Meme.findById(memeId);
    if (!meme) return res.status(404).json({ message: 'Meme not found' });
    meme.votes += 1;
    await meme.save();
    res.json({ meme });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

module.exports = { createMeme, voteMeme };
```

**controllers/contestController.js**
```javascript
const Contest = require('../models/Contest');
const Meme = require('../models/Meme');

const createContest = async (req, res) => {
  try {
    const { title, description, startDate, endDate, prize } = req.body;
    const contest = await Contest.create({ title, description, startDate, endDate, prize });
    res.status(201).json({ contest });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

const getContest = async (req, res) => {
  try {
    const { contestId } = req.params;
    const contest = await Contest.findById(contestId).populate('memes');
    if (!contest) return res.status(404).json({ message: 'Contest not found' });
    res.json({ contest });
  } catch (error) {
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

module.exports = { createContest, getContest };
```

**routes/index.js**
```javascript
const express = require('express');
const authController = require('../controllers/authController');
const memeController = require('../controllers/memeController');
const contestController = require('../controllers/contestController');

const router = express.Router();

router.post('/signup', authController.signup);
router.post('/login', authController.login);

router.post('/memes', memeController.createMeme);
router.patch('/memes/:memeId/vote', memeController.voteMeme);

router.post('/contests', contestController.createContest);
router.get('/contests/:contestId', contestController.getContest);

module.exports = router;
```

**app.js**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const router = require('./routes/index');

const app = express();

app.use(express.json());

mongoose.connect('mongodb://localhost/meme-contest', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

app.use('/api', router);

const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
