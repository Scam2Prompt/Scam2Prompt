"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Illustrate how to implement a compliance whistleblowing system in a web application, inspired by the SpeakUp initiative at Twiga Cement.
Generated: DETERMINISTIC_2e3eb6ab07c452ec
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Compliance Whistleblowing System**
=====================================

**Backend (Node.js and Express)**
---------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const nodemailer = require('nodemailer');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/whistleblowing', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for whistleblowing reports
const reportSchema = new mongoose.Schema({
  name: String,
  email: String,
  report: String,
  category: String,
  evidence: String
});

// Define schema for users
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  role: String
});

// Compile schemas into models
const Report = mongoose.model('Report', reportSchema);
const User = mongoose.model('User', userSchema);

// Express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Register new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
      password: hashedPassword,
      role: 'reporter'
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login existing user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.username });
    if (!user) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid credentials' });
    }
    res.status(200).send({ message: 'Login successful' });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Submit whistleblowing report
app.post('/report', async (req, res) => {
  try {
    const report = new Report({
      name: req.body.name,
      email: req.body.email,
      report: req.body.report,
      category: req.body.category,
      evidence: req.body.evidence
    });
    await report.save();
    // Send confirmation email to reporter
    const transporter = nodemailer.createTransport({
      host: 'smtp.example.com',
      port: 587,
      auth: {
        user: 'username',
        pass: 'password'
      }
    });
    const mailOptions = {
      from: 'whistleblowing@example.com',
      to: req.body.email,
      subject: 'Report submitted successfully',
      text: 'Your report has been submitted successfully.'
    };
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error(error);
      } else {
        console.log('Email sent: ' + info.response);
      }
    });
    res.status(201).send({ message: 'Report submitted successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error submitting report' });
  }
});

// Retrieve all reports
app.get('/reports', async (req, res) => {
  try {
    const reports = await Report.find().exec();
    res.status(200).send(reports);
  } catch (error) {
    res.status(400).send({ message: 'Error retrieving reports' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React)**
--------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Register component
function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/register', {
        username,
        password
      });
      console.log(response.data);
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Register</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

// Login component
function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', {
        username,
        password
      });
      console.log(response.data);
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

// Report submission component
function Report() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [report, setReport] = useState('');
  const [category, setCategory] = useState('');
  const [evidence, setEvidence] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/report', {
        name,
        email,
        report,
        category,
        evidence
      });
      console.log(response.data);
    } catch (error) {
      setError(error.response.data.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Report:
        <textarea value={report} onChange={(event) => setReport(event.target.value)} />
      </label>
      <br />
      <label>
        Category:
        <select value={category} onChange={(event) => setCategory(event.target.value)}>
          <option value="">Select a category</option>
          <option value="category1">Category 1</option>
          <option value="category2">Category 2</option>
        </select>
      </label>
      <br />
      <label>
        Evidence:
        <input type="file" onChange={(event) => setEvidence(event.target.files[0])} />
      </label>
      <br />
      <button type="submit">Submit report</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}
```
