"""
Generated Code Metadata:
========================
Original URL: https://formulir.site
Prompt: "Develop a Node.js backend for managing user accounts and attendance records with face recognition login."
Generated: DETERMINISTIC_d54c958af3808e17
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const multer = require('multer');
const path = require('path');
const faceapi = require('face-api.js');
const { Canvas, Image } = require('canvas');
const fs = require('fs');
const cors = require('cors');

// Initialize Express app
const app = express();
app.use(express.json());
app.use(cors());

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// Models
const UserSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  faceDescriptor: { type: Array },
  role: { type: String, enum: ['user', 'admin'], default: 'user' },
  createdAt: { type: Date, default: Date.now }
});

const AttendanceSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  checkIn: { type: Date, default: Date.now },
  checkOut: { type: Date },
  status: { type: String, enum: ['present', 'absent', 'late'], default: 'present' }
});

const User = mongoose.model('User', UserSchema);
const Attendance = mongoose.model('Attendance', AttendanceSchema);

// Configure face-api.js
faceapi.env.monkeyPatch({ Canvas, Image });

async function loadModels() {
  await faceapi.nets.faceRecognitionNet.loadFromDisk('./models');
  await faceapi.nets.faceLandmark68Net.loadFromDisk('./models');
  await faceapi.nets.ssdMobilenetv1.loadFromDisk('./models');
  console.log('Face recognition models loaded');
}

loadModels().catch(err => console.error('Error loading models:', err));

// Multer configuration for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage });

// Utility functions
async function generateFaceDescriptor(imagePath) {
  const img = await Canvas.loadImage(imagePath);
  const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor();
  
  if (!detections) {
    throw new Error('No face detected in the image');
  }
  
  return Array.from(detections.descriptor);
}

async function verifyFace(imagePath, storedDescriptor) {
  const img = await Canvas.loadImage(imagePath);
  const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor();
  
  if (!detections) {
    throw new Error('No face detected in the image');
  }
  
  const distance = faceapi.euclideanDistance(storedDescriptor, detections.descriptor);
  return distance < 0.6; // Threshold for face recognition
}

// Authentication middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}

// Routes
// User registration
app.post('/register', upload.single('faceImage'), async (req, res) => {
  try {
    const { username, password, role } = req.body;
    
    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password are required' });
    }
    
    if (!req.file) {
      return res.status(400).json({ error: 'Face image is required' });
    }
    
    const existingUser = await User.findOne({ username });
    if (existingUser) {
      return res.status(400).json({ error: 'Username already exists' });
    }
    
    const hashedPassword = await bcrypt.hash(password, 10);
    const faceDescriptor = await generateFaceDescriptor(req.file.path);
    
    const user = new User({
      username,
      password: hashedPassword,
      faceDescriptor,
      role: role || 'user'
    });
    
    await user.save();
    
    // Clean up uploaded file
    fs.unlinkSync(req.file.path);
    
    res.status(201).json({ message: 'User registered successfully' });
  } catch (err) {
    console.error('Registration error:', err);
    if (req.file) fs.unlinkSync(req.file.path);
    res.status(500).json({ error: 'Registration failed', details: err.message });
  }
});

// Login with credentials
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    
    const user = await User.findOne({ username });
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    const token = jwt.sign(
      { userId: user._id, username: user.username, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );
    
    res.json({ token });
  } catch (err) {
    console.error('Login error:', err);
    res.status(500).json({ error: 'Login failed' });
  }
});

// Face recognition login
app.post('/face-login', upload.single('faceImage'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'Face image is required' });
    }
    
    const users = await User.find({});
    if (users.length === 0) {
      return res.status(404).json({ error: 'No users registered' });
    }
    
    let matchedUser = null;
    
    for (const user of users) {
      if (user.faceDescriptor) {
        const isMatch = await verifyFace(req.file.path, user.faceDescriptor);
        if (isMatch) {
          matchedUser = user;
          break;
        }
      }
    }
    
    if (!matchedUser) {
      return res.status(401).json({ error: 'Face not recognized' });
    }
    
    const token = jwt.sign(
      { userId: matchedUser._id, username: matchedUser.username, role: matchedUser.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );
    
    // Clean up uploaded file
    fs.unlinkSync(req.file.path);
    
    res.json({ token });
  } catch (err) {
    console.error('Face login error:', err);
    if (req.file) fs.unlinkSync(req.file.path);
    res.status(500).json({ error: 'Face login failed', details: err.message });
  }
});

// Check in
app.post('/check-in', authenticateToken, async (req, res) => {
  try {
    const attendance = new Attendance({
      userId: req.user.userId,
      status: 'present'
    });
    
    await attendance.save();
    res.status(201).json({ message: 'Checked in successfully' });
  } catch (err) {
    console.error('Check-in error:', err);
    res.status(500).json({ error: 'Check-in failed' });
  }
});

// Check out
app.post('/check-out', authenticateToken, async (req, res) => {
  try {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    const attendance = await Attendance.findOne({
      userId: req.user.userId,
      checkIn: { $gte: today },
      checkOut: { $exists: false }
    });
    
    if (!attendance) {
      return res.status(400).json({ error: 'No check-in record found for today' });
    }
    
    attendance.checkOut = new Date();
    await attendance.save();
    
    res.json({ message: 'Checked out successfully' });
  } catch (err) {
    console.error('Check-out error:', err);
    res.status(500).json({ error: 'Check-out failed' });
  }
});

// Get attendance records
app.get('/attendance', authenticateToken, async (req, res) => {
  try {
    const records = await Attendance.find({ userId: req.user.userId })
      .sort({ checkIn: -1 })
      .limit(30);
    
    res.json(records);
  } catch (err) {
    console.error('Attendance records error:', err);
    res.status
