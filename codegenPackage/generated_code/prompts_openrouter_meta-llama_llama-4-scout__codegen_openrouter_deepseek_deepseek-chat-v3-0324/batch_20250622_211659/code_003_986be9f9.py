"""
Generated Code Metadata:
========================
Original URL: https://popcorn.claims
Prompt: "Design a RESTful API in Node.js for managing claims, including endpoints for submission, review, and approval, with considerations for data privacy."
Generated: DETERMINISTIC_986be9f92261a958
Batch ID: 20250622_211659
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
const helmet = require('helmet');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Initialize Express app
const app = express();

// Environment variables
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key';

// Middleware
app.use(helmet()); // Security middleware
app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Parse JSON bodies

// In-memory database (Replace with a real database in production)
const claimsDB = [];
const usersDB = [
  {
    id: '1',
    username: 'admin',
    password: bcrypt.hashSync('admin123', 10),
    role: 'admin'
  },
  {
    id: '2',
    username: 'reviewer',
    password: bcrypt.hashSync('reviewer123', 10),
    role: 'reviewer'
  }
];

// Authentication middleware
const authenticateJWT = (req, res, next) => {
  const authHeader = req.headers.authorization;

  if (authHeader) {
    const token = authHeader.split(' ')[1];

    jwt.verify(token, JWT_SECRET, (err, user) => {
      if (err) {
        return res.sendStatus(403);
      }

      req.user = user;
      next();
    });
  } else {
    res.sendStatus(401);
  }
};

// Role-based access control middleware
const authorizeRole = (role) => {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.sendStatus(403);
    }
    next();
  };
};

// Routes

// Authentication endpoint
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  const user = usersDB.find(u => u.username === username);
  if (!user) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  const passwordValid = bcrypt.compareSync(password, user.password);
  if (!passwordValid) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  const token = jwt.sign({ id: user.id, username: user.username, role: user.role }, JWT_SECRET, {
    expiresIn: '1h'
  });

  res.json({ token });
});

// Claim submission endpoint
app.post('/claims', authenticateJWT, (req, res) => {
  try {
    const { title, description, amount } = req.body;

    if (!title || !description || !amount) {
      return res.status(400).json({ message: 'Missing required fields' });
    }

    const newClaim = {
      id: uuidv4(),
      title,
      description,
      amount,
      status: 'submitted',
      submittedBy: req.user.id,
      submittedAt: new Date().toISOString(),
      reviewedBy: null,
      reviewedAt: null,
      approvedBy: null,
      approvedAt: null
    };

    claimsDB.push(newClaim);

    // Remove sensitive data before sending response
    const responseClaim = { ...newClaim };
    delete responseClaim.submittedBy;

    res.status(201).json(responseClaim);
  } catch (error) {
    console.error('Error submitting claim:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Get all claims (admin/reviewer only)
app.get('/claims', authenticateJWT, authorizeRole('admin'), (req, res) => {
  try {
    // In production, implement pagination and filtering
    const claims = claimsDB.map(claim => {
      const responseClaim = { ...claim };
      delete responseClaim.submittedBy;
      return responseClaim;
    });

    res.json(claims);
  } catch (error) {
    console.error('Error fetching claims:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Get claim by ID
app.get('/claims/:id', authenticateJWT, (req, res) => {
  try {
    const claim = claimsDB.find(c => c.id === req.params.id);

    if (!claim) {
      return res.status(404).json({ message: 'Claim not found' });
    }

    // Only allow admin/reviewer or the submitter to view the claim
    if (req.user.role !== 'admin' && req.user.role !== 'reviewer' && claim.submittedBy !== req.user.id) {
      return res.sendStatus(403);
    }

    const responseClaim = { ...claim };
    delete responseClaim.submittedBy;

    res.json(responseClaim);
  } catch (error) {
    console.error('Error fetching claim:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Review claim (reviewer/admin only)
app.patch('/claims/:id/review', authenticateJWT, authorizeRole('reviewer'), (req, res) => {
  try {
    const { status, comments } = req.body;
    const claimIndex = claimsDB.findIndex(c => c.id === req.params.id);

    if (claimIndex === -1) {
      return res.status(404).json({ message: 'Claim not found' });
    }

    if (!['approved', 'rejected', 'pending'].includes(status)) {
      return res.status(400).json({ message: 'Invalid status' });
    }

    claimsDB[claimIndex] = {
      ...claimsDB[claimIndex],
      status,
      comments,
      reviewedBy: req.user.id,
      reviewedAt: new Date().toISOString()
    };

    const responseClaim = { ...claimsDB[claimIndex] };
    delete responseClaim.submittedBy;
    delete responseClaim.reviewedBy;

    res.json(responseClaim);
  } catch (error) {
    console.error('Error reviewing claim:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Approve claim (admin only)
app.patch('/claims/:id/approve', authenticateJWT, authorizeRole('admin'), (req, res) => {
  try {
    const claimIndex = claimsDB.findIndex(c => c.id === req.params.id);

    if (claimIndex === -1) {
      return res.status(404).json({ message: 'Claim not found' });
    }

    if (claimsDB[claimIndex].status !== 'approved') {
      return res.status(400).json({ message: 'Claim must be reviewed and approved first' });
    }

    claimsDB[claimIndex] = {
      ...claimsDB[claimIndex],
      approvedBy: req.user.id,
      approvedAt: new Date().toISOString()
    };

    const responseClaim = { ...claimsDB[claimIndex] };
    delete responseClaim.submittedBy;
    delete responseClaim.reviewedBy;
    delete responseClaim.approvedBy;

    res.json(responseClaim);
  } catch (error) {
    console.error('Error approving claim:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export app for testing
module.exports = app;
```
