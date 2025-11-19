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

**athlete-certifications-api.js**
```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const { validate } = require('joi');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/athlete-certifications', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for Athlete model
const athleteSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  certifications: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Certification' }]
});

// Define schema for Team model
const teamSchema = new mongoose.Schema({
  name: { type: String, required: true },
  athletes: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Athlete' }],
  records: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Record' }]
});

// Define schema for Certification model
const certificationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  athlete: { type: mongoose.Schema.Types.ObjectId, ref: 'Athlete' },
  issuedAt: { type: Date, required: true }
});

// Define schema for Record model
const recordSchema = new mongoose.Schema({
  name: { type: String, required: true },
  value: { type: String, required: true },
  team: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
  achievedAt: { type: Date, required: true }
});

// Create models
const Athlete = mongoose.model('Athlete', athleteSchema);
const Team = mongoose.model('Team', teamSchema);
const Certification = mongoose.model('Certification', certificationSchema);
const Record = mongoose.model('Record', recordSchema);

// Define Joi validation schemas
const athleteValidation = Joi.object({
  name: Joi.string().required(),
  email: Joi.string().email().required()
});

const teamValidation = Joi.object({
  name: Joi.string().required()
});

const certificationValidation = Joi.object({
  name: Joi.string().required(),
  description: Joi.string(),
  athleteId: Joi.string().required(),
  issuedAt: Joi.date().required()
});

const recordValidation = Joi.object({
  name: Joi.string().required(),
  value: Joi.string().required(),
  teamId: Joi.string().required(),
  achievedAt: Joi.date().required()
});

// Middleware to parse JSON bodies
app.use(express.json());

// Athlete routes
app.post('/athletes', async (req, res) => {
  try {
    const { error } = validate(req.body, athleteValidation);
    if (error) return res.status(400).send({ message: error.details[0].message });

    const athlete = new Athlete(req.body);
    await athlete.save();
    res.send(athlete);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/athletes', async (req, res) => {
  try {
    const athletes = await Athlete.find().populate('certifications');
    res.send(athletes);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/athletes/:id', async (req, res) => {
  try {
    const athlete = await Athlete.findById(req.params.id).populate('certifications');
    if (!athlete) return res.status(404).send({ message: 'Athlete not found' });
    res.send(athlete);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Team routes
app.post('/teams', async (req, res) => {
  try {
    const { error } = validate(req.body, teamValidation);
    if (error) return res.status(400).send({ message: error.details[0].message });

    const team = new Team(req.body);
    await team.save();
    res.send(team);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/teams', async (req, res) => {
  try {
    const teams = await Team.find().populate('athletes').populate('records');
    res.send(teams);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/teams/:id', async (req, res) => {
  try {
    const team = await Team.findById(req.params.id).populate('athletes').populate('records');
    if (!team) return res.status(404).send({ message: 'Team not found' });
    res.send(team);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Certification routes
app.post('/certifications', async (req, res) => {
  try {
    const { error } = validate(req.body, certificationValidation);
    if (error) return res.status(400).send({ message: error.details[0].message });

    const certification = new Certification(req.body);
    await certification.save();
    res.send(certification);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/certifications', async (req, res) => {
  try {
    const certifications = await Certification.find().populate('athlete');
    res.send(certifications);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Record routes
app.post('/records', async (req, res) => {
  try {
    const { error } = validate(req.body, recordValidation);
    if (error) return res.status(400).send({ message: error.details[0].message });

    const record = new Record(req.body);
    await record.save();
    res.send(record);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

app.get('/records', async (req, res) => {
  try {
    const records = await Record.find().populate('team');
    res.send(records);
  } catch (err) {
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**models/index.js**
```javascript
// Export models
module.exports = {
  Athlete: require('./athlete.model'),
  Team: require('./team.model'),
  Certification: require('./certification.model'),
  Record: require('./record.model')
};
```

**models/athlete.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define Athlete model
const athleteSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  certifications: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Certification' }]
});

// Export Athlete model
module.exports = mongoose.model('Athlete', athleteSchema);
```

**models/team.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define Team model
const teamSchema = new mongoose.Schema({
  name: { type: String, required: true },
  athletes: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Athlete' }],
  records: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Record' }]
});

// Export Team model
module.exports = mongoose.model('Team', teamSchema);
```

**models/certification.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define Certification model
const certificationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  description: { type: String },
  athlete: { type: mongoose.Schema.Types.ObjectId, ref: 'Athlete' },
  issuedAt: { type: Date, required: true }
});

// Export Certification model
module.exports = mongoose.model('Certification', certificationSchema);
```

**models/record.model.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define Record model
const recordSchema = new mongoose.Schema({
  name: { type: String, required: true },
  value: { type: String, required: true },
  team: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
  achievedAt: { type: Date, required: true }
});

// Export Record model
module.exports = mongoose.model('Record', recordSchema);
```
