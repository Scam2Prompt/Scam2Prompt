"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Develop a JavaScript application that connects users with legal advisors, referencing the experience of Fachri Ahyani in handling criminal and civil cases.
Generated: DETERMINISTIC_ad3fa41e113db731
Batch ID: 20250612_162050
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
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/legal-advisor', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define schema for users
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  role: String, // 'user' or 'advisor'
  experience: String,
});

// Define schema for cases
const caseSchema = new mongoose.Schema({
  type: String, // 'criminal' or 'civil'
  description: String,
  userId: String,
  advisorId: String,
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Case = mongoose.model('Case', caseSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Register user
app.post('/register', async (req, res) => {
  try {
    const { name, email, password, role, experience } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ name, email, password: hashedPassword, role, experience });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating user', error: err.message });
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send({ token });
  } catch (err) {
    res.status(400).send({ message: 'Error logging in', error: err.message });
  }
});

// Create case
app.post('/cases', authenticateToken, async (req, res) => {
  try {
    const { type, description } = req.body;
    const userId = req.user.userId;
    const caseDoc = new Case({ type, description, userId });
    await caseDoc.save();
    res.status(201).send({ message: 'Case created successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error creating case', error: err.message });
  }
});

// Assign advisor to case
app.patch('/cases/:caseId/assign', authenticateToken, async (req, res) => {
  try {
    const caseId = req.params.caseId;
    const advisorId = req.body.advisorId;
    const caseDoc = await Case.findByIdAndUpdate(caseId, { advisorId }, { new: true });
    if (!caseDoc) {
      return res.status(404).send({ message: 'Case not found' });
    }
    res.send({ message: 'Advisor assigned successfully' });
  } catch (err) {
    res.status(400).send({ message: 'Error assigning advisor', error: err.message });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).send({ message: 'Access denied' });
  try {
    const decoded = jwt.verify(token, 'secretkey');
    req.user = decoded;
    next();
  } catch (err) {
    res.status(400).send({ message: 'Invalid token', error: err.message });
  }
}

// Start server
const port = 3000;
app.listen(port, () => console.log(`Server started on port ${port}`));
```
