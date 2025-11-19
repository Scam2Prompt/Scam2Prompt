"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Create a RESTful API in Node.js to manage certifications and records for athletes and teams, similar to the Certidões FMA and Recordes Estaduais sections on the website.
Generated: DETERMINISTIC_bebb339cde72b3c6
Batch ID: 20250622_211748
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
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { validationResult } = require('express-validator');
const { body, param } = require('express-validator');

// Initialize Express app
const app = express();

// Apply security middleware
app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/athleteCertifications', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Mongoose Schemas
const athleteSchema = new mongoose.Schema({
  name: { type: String, required: true },
  birthDate: { type: Date, required: true },
  team: { type: String, required: true },
  sport: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const certificationSchema = new mongoose.Schema({
  athleteId: { type: mongoose.Schema.Types.ObjectId, ref: 'Athlete', required: true },
  certificationType: { type: String, required: true },
  certificationDate: { type: Date, required: true },
  expirationDate: { type: Date },
  status: { type: String, enum: ['active', 'expired', 'revoked'], default: 'active' },
  details: { type: String }
});

const recordSchema = new mongoose.Schema({
  athleteId: { type: mongoose.Schema.Types.ObjectId, ref: 'Athlete', required: true },
  recordType: { type: String, required: true },
  event: { type: String, required: true },
  result: { type: String, required: true },
  date: { type: Date, required: true },
  location: { type: String, required: true },
  isStateRecord: { type: Boolean, default: false }
});

// Mongoose Models
const Athlete = mongoose.model('Athlete', athleteSchema);
const Certification = mongoose.model('Certification', certificationSchema);
const Record = mongoose.model('Record', recordSchema);

// Validation middleware
const validateAthlete = [
  body('name').isString().notEmpty(),
  body('birthDate').isISO8601(),
  body('team').isString().notEmpty(),
  body('sport').isString().notEmpty()
];

const validateCertification = [
  body('athleteId').isMongoId(),
  body('certificationType').isString().notEmpty(),
  body('certificationDate').isISO8601(),
  body('expirationDate').optional().isISO8601(),
  body('details').optional().isString()
];

const validateRecord = [
  body('athleteId').isMongoId(),
  body('recordType').isString().notEmpty(),
  body('event').isString().notEmpty(),
  body('result').isString().notEmpty(),
  body('date').isISO8601(),
  body('location').isString().notEmpty(),
  body('isStateRecord').optional().isBoolean()
];

// Routes
app.get('/athletes', async (req, res) => {
  try {
    const athletes = await Athlete.find();
    res.json(athletes);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching athletes', error: err.message });
  }
});

app.post('/athletes', validateAthlete, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const athlete = new Athlete(req.body);
    await athlete.save();
    res.status(201).json(athlete);
  } catch (err) {
    res.status(500).json({ message: 'Error creating athlete', error: err.message });
  }
});

app.get('/athletes/:id', [
  param('id').isMongoId()
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const athlete = await Athlete.findById(req.params.id);
    if (!athlete) {
      return res.status(404).json({ message: 'Athlete not found' });
    }
    res.json(athlete);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching athlete', error: err.message });
  }
});

app.get('/athletes/:id/certifications', [
  param('id').isMongoId()
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const certifications = await Certification.find({ athleteId: req.params.id });
    res.json(certifications);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching certifications', error: err.message });
  }
});

app.post('/certifications', validateCertification, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const certification = new Certification(req.body);
    await certification.save();
    res.status(201).json(certification);
  } catch (err) {
    res.status(500).json({ message: 'Error creating certification', error: err.message });
  }
});

app.get('/records', async (req, res) => {
  try {
    const records = await Record.find().populate('athleteId');
    res.json(records);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching records', error: err.message });
  }
});

app.post('/records', validateRecord, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  try {
    const record = new Record(req.body);
    await record.save();
    res.status(201).json(record);
  } catch (err) {
    res.status(500).json({ message: 'Error creating record', error: err.message });
  }
});

app.get('/records/state', async (req, res) => {
  try {
    const stateRecords = await Record.find({ isStateRecord: true }).populate('athleteId');
    res.json(stateRecords);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching state records', error: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Something went wrong!' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
