"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Create a Node.js application that takes advantage of iFastNet's unlimited bandwidth and disk space.
Generated: DETERMINISTIC_4cdfb9293102682b
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Node.js File Upload Service for iFastNet

```javascript
const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const morgan = require('morgan');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Initialize Express app
const app = express();

// Security middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));

// Rate limiting to prevent abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Configure storage for uploaded files
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const uploadDir = 'uploads/';
    
    // Create upload directory if it doesn't exist
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    // Generate unique filename with timestamp
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  }
});

// File filter to restrict file types if needed
const fileFilter = (req, file, cb) => {
  const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain'];
  if (allowedTypes.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new Error('Invalid file type'), false);
  }
};

// Initialize multer with configuration
const upload = multer({
  storage: storage,
  fileFilter: fileFilter,
  limits: {
    fileSize: 1024 * 1024 * 100 // 100MB file size limit
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// File upload endpoint
app.post('/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }
    
    res.status(201).json({
      message: 'File uploaded successfully',
      file: {
        originalName: req.file.originalname,
        fileName: req.file.filename,
        size: req.file.size,
        path: req.file.path
      }
    });
  } catch (error) {
    console.error('Upload error:', error);
    res.status(500).json({ error: 'Failed to upload file' });
  }
});

// File download endpoint
app.get('/download/:filename', (req, res) => {
  try {
    const filePath = path.join(__dirname, 'uploads', req.params.filename);
    
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'File not found' });
    }
    
    res.download(filePath);
  } catch (error) {
    console.error('Download error:', error);
    res.status(500).json({ error: 'Failed to download file' });
  }
});

// File list endpoint
app.get('/files', (req, res) => {
  try {
    const uploadDir = path.join(__dirname, 'uploads');
    
    if (!fs.existsSync(uploadDir)) {
      return res.status(200).json({ files: [] });
    }
    
    fs.readdir(uploadDir, (err, files) => {
      if (err) {
        throw err;
      }
      
      res.status(200).json({ files });
    });
  } catch (error) {
    console.error('File list error:', error);
    res.status(500).json({ error: 'Failed to retrieve file list' });
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
  console.log(`Upload directory: ${path.join(__dirname, 'uploads')}`);
});

// Handle process termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully');
  server.close(() => {
    console.log('Process terminated');
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully');
  server.close(() => {
    console.log('Process terminated');
  });
});
```

```json
// package.json
{
  "name": "ifastnet-file-service",
  "version": "1.0.0",
  "description": "File upload service for iFastNet",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "express-rate-limit": "^6.7.0",
    "helmet": "^7.0.0",
    "morgan": "^1.10.0",
    "multer": "^1.4.5-lts.1"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "nodemon": "^3.0.2",
    "supertest": "^6.3.3"
  }
}
```

```javascript
// tests/app.test.js
const request = require('supertest');
const app = require('../index');
const fs = require('fs');
const path = require('path');

describe('File Service API', () => {
  const testFilePath = path.join(__dirname, 'test-file.txt');
  
  beforeAll(() => {
    // Create a test file
    fs.writeFileSync(testFilePath, 'This is a test file');
  });
  
  afterAll(() => {
    // Clean up test file
    if (fs.existsSync(testFilePath)) {
      fs.unlinkSync(testFilePath);
    }
  });
  
  it('should return healthy status', async () => {
    const res = await request(app).get('/health');
    expect(res.statusCode).toEqual(200);
    expect(res.body.status).toEqual('healthy');
  });
  
  it('should upload a file', async () => {
    const res = await request(app)
      .post('/upload')
      .attach('file', testFilePath);
    
    expect(res.statusCode).toEqual(201);
    expect(res.body.message).toEqual('File uploaded successfully');
    expect(res.body.file).toBeDefined();
    
    // Clean up uploaded file
    if (res.body.file && res.body.file.path) {
      fs.unlinkSync(res.body.file.path);
    }
  });
  
  it('should return 400 for no file uploaded', async () => {
    const res = await request(app).post('/upload');
    expect(res.statusCode).toEqual(400);
    expect(res.body.error).toEqual('No file uploaded');
  });
  
  it('should list uploaded files', async () => {
    const res = await request(app).get('/files');
    expect(res.statusCode).toEqual(200);
    expect(res.body.files).toBeDefined();
  });
});
```
