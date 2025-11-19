"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Generate a RESTful API in Node.js for managing documents and publications related to the activities of Khao Luang Subdistrict Administrative Organization, including endpoints for uploading, retrieving, and searching documents.
Generated: DETERMINISTIC_2ad4f14376fd8f52
Batch ID: 20250622_211706
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
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/khao_luang_docs', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
    console.log('Connected to MongoDB');
});

// Document model
const DocumentSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        trim: true
    },
    category: {
        type: String,
        required: true,
        trim: true
    },
    filePath: {
        type: String,
        required: true
    },
    uploadDate: {
        type: Date,
        default: Date.now
    },
    tags: [{
        type: String,
        trim: true
    }]
});

const Document = mongoose.model('Document', DocumentSchema);

// File upload configuration
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const uploadDir = 'uploads/';
        if (!fs.existsSync(uploadDir)) {
            fs.mkdirSync(uploadDir, { recursive: true });
        }
        cb(null, uploadDir);
    },
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
    }
});

const upload = multer({ 
    storage: storage,
    fileFilter: (req, file, cb) => {
        const filetypes = /pdf|doc|docx|xls|xlsx|ppt|pptx|txt/;
        const extname = filetypes.test(path.extname(file.originalname).toLowerCase());
        const mimetype = filetypes.test(file.mimetype);

        if (extname && mimetype) {
            return cb(null, true);
        } else {
            cb(new Error('Only document files are allowed!'));
        }
    }
}).single('document');

// API Routes

/**
 * @route POST /api/documents
 * @desc Upload a new document
 * @access Public
 */
app.post('/api/documents', (req, res) => {
    upload(req, res, async (err) => {
        if (err) {
            return res.status(400).json({ error: err.message });
        }

        if (!req.file) {
            return res.status(400).json({ error: 'No file uploaded' });
        }

        try {
            const { title, description, category, tags } = req.body;
            
            const document = new Document({
                title,
                description,
                category,
                filePath: req.file.path,
                tags: tags ? tags.split(',').map(tag => tag.trim()) : []
            });

            await document.save();
            res.status(201).json(document);
        } catch (error) {
            // Clean up uploaded file if document creation fails
            if (req.file && fs.existsSync(req.file.path)) {
                fs.unlinkSync(req.file.path);
            }
            res.status(500).json({ error: 'Failed to save document' });
        }
    });
});

/**
 * @route GET /api/documents
 * @desc Get all documents with optional search and filtering
 * @access Public
 */
app.get('/api/documents', async (req, res) => {
    try {
        const { search, category, tag } = req.query;
        const query = {};

        if (search) {
            query.$or = [
                { title: { $regex: search, $options: 'i' } },
                { description: { $regex: search, $options: 'i' } }
            ];
        }

        if (category) {
            query.category = category;
        }

        if (tag) {
            query.tags = tag;
        }

        const documents = await Document.find(query).sort({ uploadDate: -1 });
        res.json(documents);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch documents' });
    }
});

/**
 * @route GET /api/documents/:id
 * @desc Get a single document by ID
 * @access Public
 */
app.get('/api/documents/:id', async (req, res) => {
    try {
        const document = await Document.findById(req.params.id);
        if (!document) {
            return res.status(404).json({ error: 'Document not found' });
        }
        res.json(document);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch document' });
    }
});

/**
 * @route GET /api/documents/:id/download
 * @desc Download a document file
 * @access Public
 */
app.get('/api/documents/:id/download', async (req, res) => {
    try {
        const document = await Document.findById(req.params.id);
        if (!document) {
            return res.status(404).json({ error: 'Document not found' });
        }

        if (!fs.existsSync(document.filePath)) {
            return res.status(404).json({ error: 'File not found' });
        }

        res.download(document.filePath, path.basename(document.filePath));
    } catch (error) {
        res.status(500).json({ error: 'Failed to download document' });
    }
});

/**
 * @route DELETE /api/documents/:id
 * @desc Delete a document
 * @access Public
 */
app.delete('/api/documents/:id', async (req, res) => {
    try {
        const document = await Document.findByIdAndDelete(req.params.id);
        if (!document) {
            return res.status(404).json({ error: 'Document not found' });
        }

        // Delete the associated file
        if (fs.existsSync(document.filePath)) {
            fs.unlinkSync(document.filePath);
        }

        res.json({ message: 'Document deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete document' });
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
```
