"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Develop a Node.js application to manage and display a list of partners, similar to the "Nos partenaires" section on the Mêtis website.
Generated: DETERMINISTIC_54407e2e30248cbb
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Node.js application for managing and displaying a list of partners:

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');
const { v4: uuidv4 } = require('uuid');
const path = require('path');
const multer = require('multer');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Partner model
const partnerSchema = new mongoose.Schema({
  _id: { type: String, default: uuidv4 },
  name: { type: String, required: true },
  description: { type: String, required: true },
  website: { type: String, required: true },
  logo: { type: String, required: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const Partner = mongoose.model('Partner', partnerSchema);

// Multer configuration for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname);
    cb(null, `${uuidv4()}${ext}`);
  }
});

const upload = multer({ 
  storage: storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype.startsWith('image/')) {
      cb(null, true);
    } else {
      cb(new Error('Only image files are allowed!'), false);
    }
  },
  limits: {
    fileSize: 5 * 1024 * 1024 // 5MB
  }
});

// API Routes

/**
 * GET /api/partners
 * Get all partners
 */
app.get('/api/partners', async (req, res) => {
  try {
    const partners = await Partner.find().sort({ createdAt: -1 });
    res.json(partners);
  } catch (err) {
    console.error('Error fetching partners:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * POST /api/partners
 * Create a new partner
 */
app.post('/api/partners', upload.single('logo'), async (req, res) => {
  try {
    const { name, description, website } = req.body;
    
    if (!name || !description || !website || !req.file) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const newPartner = new Partner({
      name,
      description,
      website,
      logo: req.file.path
    });

    await newPartner.save();
    res.status(201).json(newPartner);
  } catch (err) {
    console.error('Error creating partner:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * PUT /api/partners/:id
 * Update a partner
 */
app.put('/api/partners/:id', upload.single('logo'), async (req, res) => {
  try {
    const { id } = req.params;
    const { name, description, website } = req.body;
    
    const updateData = { 
      name, 
      description, 
      website,
      updatedAt: Date.now()
    };

    if (req.file) {
      updateData.logo = req.file.path;
    }

    const updatedPartner = await Partner.findByIdAndUpdate(id, updateData, { new: true });
    
    if (!updatedPartner) {
      return res.status(404).json({ error: 'Partner not found' });
    }

    res.json(updatedPartner);
  } catch (err) {
    console.error('Error updating partner:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

/**
 * DELETE /api/partners/:id
 * Delete a partner
 */
app.delete('/api/partners/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const deletedPartner = await Partner.findByIdAndDelete(id);
    
    if (!deletedPartner) {
      return res.status(404).json({ error: 'Partner not found' });
    }

    res.json({ message: 'Partner deleted successfully' });
  } catch (err) {
    console.error('Error deleting partner:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  
  if (err instanceof multer.MulterError) {
    return res.status(400).json({ error: 'File upload error: ' + err.message });
  } else if (err) {
    return res.status(500).json({ error: 'Internal server error' });
  }
  
  next();
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```

You'll also need a `.env` file:

```env
MONGODB_URI=mongodb://localhost:27017/partners_db
```

And a `package.json` file:

```json
{
  "name": "partners-api",
  "version": "1.0.0",
  "description": "API for managing partners",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.0.3",
    "express": "^4.18.2",
    "mongoose": "^7.0.0",
    "multer": "^1.4.5-lts.1",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "jest": "^29.5.0",
    "nodemon": "^2.0.20",
    "supertest": "^6.3.3"
  }
}
```
