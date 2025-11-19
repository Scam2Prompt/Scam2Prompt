"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Create a RESTful API using Node.js to manage and display a collection of photographs, similar to those featured on charosnavarro.com.
Generated: DETERMINISTIC_86b7fbf3d4e5db22
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**photography-api.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const multer = require('multer');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define photograph schema
const photographSchema = new mongoose.Schema({
  title: String,
  description: String,
  imageUrl: String,
  createdAt: { type: Date, default: Date.now },
});

// Create photograph model
const Photograph = mongoose.model('Photograph', photographSchema);

// Set up middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set up Multer for image uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});

const upload = multer({ storage });

// Get all photographs
app.get('/photographs', async (req, res) => {
  try {
    const photographs = await Photograph.find().sort({ createdAt: -1 });
    res.json(photographs);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching photographs' });
  }
});

// Get a single photograph by ID
app.get('/photographs/:id', async (req, res) => {
  try {
    const photograph = await Photograph.findById(req.params.id);
    if (!photograph) {
      res.status(404).json({ message: 'Photograph not found' });
    } else {
      res.json(photograph);
    }
  } catch (error) {
    res.status(500).json({ message: 'Error fetching photograph' });
  }
});

// Create a new photograph
app.post('/photographs', upload.single('image'), async (req, res) => {
  try {
    const photograph = new Photograph({
      title: req.body.title,
      description: req.body.description,
      imageUrl: `/uploads/${req.file.filename}`,
    });
    await photograph.save();
    res.json(photograph);
  } catch (error) {
    res.status(500).json({ message: 'Error creating photograph' });
  }
});

// Update a photograph
app.put('/photographs/:id', async (req, res) => {
  try {
    const photograph = await Photograph.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    if (!photograph) {
      res.status(404).json({ message: 'Photograph not found' });
    } else {
      res.json(photograph);
    }
  } catch (error) {
    res.status(500).json({ message: 'Error updating photograph' });
  }
});

// Delete a photograph
app.delete('/photographs/:id', async (req, res) => {
  try {
    await Photograph.findByIdAndRemove(req.params.id);
    res.json({ message: 'Photograph deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Error deleting photograph' });
  }
});

// Serve uploaded images
app.use('/uploads', express.static('uploads'));

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**.env**
```makefile
DB_URL=mongodb://localhost:27017/photography-api
PORT=3000
```

**package.json**
```json
{
  "name": "photography-api",
  "version": "1.0.0",
  "scripts": {
    "start": "node photography-api.js"
  },
  "dependencies": {
    "dotenv": "^10.0.0",
    "express": "^4.17.1",
    "mongoose": "^6.2.10",
    "multer": "^1.4.2"
  }
}
```
