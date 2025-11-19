"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Create a vidanjör service request system using React, Node.js, and Express, allowing customers to submit service requests and track their status in real-time.
Generated: DETERMINISTIC_6c6b22350d5e4069
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// server.js (Node.js + Express backend)
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Service Request Schema
const serviceRequestSchema = new mongoose.Schema({
  customerName: { type: String, required: true },
  email: { type: String, required: true },
  phone: { type: String, required: true },
  address: { type: String, required: true },
  serviceType: { type: String, required: true },
  description: { type: String, required: true },
  status: { type: String, default: 'Pending' },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const ServiceRequest = mongoose.model('ServiceRequest', serviceRequestSchema);

// API Routes
app.get('/api/requests', async (req, res) => {
  try {
    const requests = await ServiceRequest.find().sort({ createdAt: -1 });
    res.json(requests);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/requests', async (req, res) => {
  const request = new ServiceRequest({
    customerName: req.body.customerName,
    email: req.body.email,
    phone: req.body.phone,
    address: req.body.address,
    serviceType: req.body.serviceType,
    description: req.body.description
  });

  try {
    const newRequest = await request.save();
    res.status(201).json(newRequest);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.patch('/api/requests/:id', async (req, res) => {
  try {
    const updatedRequest = await ServiceRequest.findByIdAndUpdate(
      req.params.id,
      { status: req.body.status, updatedAt: Date.now() },
      { new: true }
    );
    res.json(updatedRequest);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```javascript
// client/src/App.js (React frontend)
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [requests, setRequests] = useState([]);
  const [formData, setFormData] = useState({
    customerName: '',
    email: '',
    phone: '',
    address: '',
    serviceType: '',
    description: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Fetch all service requests
  useEffect(() => {
    const fetchRequests = async () => {
      try {
        setLoading(true);
        const response = await axios.get('/api/requests');
        setRequests(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch service requests');
        setLoading(false);
      }
    };
    fetchRequests();
  }, []);

  // Handle form input changes
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const response = await axios.post('/api/requests', formData);
      setRequests([response.data, ...requests]);
      setFormData({
        customerName: '',
        email: '',
        phone: '',
        address: '',
        serviceType: '',
        description: ''
      });
      setLoading(false);
    } catch (err) {
      setError('Failed to submit service request');
      setLoading(false);
    }
  };

  // Update request status
  const updateStatus = async (id, status) => {
    try {
      const response = await axios.patch(`/api/requests/${id}`, { status });
      setRequests(requests.map(req => 
        req._id === id ? response.data : req
      ));
    } catch (err) {
      setError('Failed to update request status');
    }
  };

  return (
    <div className="container">
      <h1>Vidanjör Service Request System</h1>
      
      {/* Request Form */}
      <div className="form-container">
        <h2>Submit Service Request</h2>
        {error && <div className="error">{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Name:</label>
            <input 
              type="text" 
              name="customerName" 
              value={formData.customerName} 
              onChange={handleChange} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Email:</label>
            <input 
              type="email" 
              name="email" 
              value={formData.email} 
              onChange={handleChange} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Phone:</label>
            <input 
              type="tel" 
              name="phone" 
              value={formData.phone} 
              onChange={handleChange} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Address:</label>
            <input 
              type="text" 
              name="address" 
              value={formData.address} 
              onChange={handleChange} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Service Type:</label>
            <select 
              name="serviceType" 
              value={formData.serviceType} 
              onChange={handleChange} 
              required
            >
              <option value="">Select a service</option>
              <option value="Cleaning">Cleaning</option>
              <option value="Maintenance">Maintenance</option>
              <option value="Inspection">Inspection</option>
              <option value="Repair">Repair</option>
            </select>
          </div>
          <div className="form-group">
            <label>Description:</label>
            <textarea 
              name="description" 
              value={formData.description} 
              onChange={handleChange} 
              required 
            />
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Submitting...' : 'Submit Request'}
          </button>
        </form>
      </div>

      {/* Requests List */}
      <div className="requests-container">
        <h2>Service Requests</h2>
        {loading ? (
          <p>Loading requests...</p>
        ) : (
          <div className="requests-list">
            {requests.map(request => (
              <div key={request._id} className="request-card">
                <h3>{request.customerName}</h3>
                <p><strong>Service:</strong> {request.serviceType}</p>
                <p><strong>Description:</strong> {request.description}</p>
                <p><strong>Status:</strong> 
                  <select 
                    value={request.status} 
                    onChange={(e) => updateStatus(request._id, e.target.value)}
                  >
                    <option value="Pending">Pending</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                    <option value="Cancelled">Cancelled</option>
                  </select>
                </p>
                <p><strong>Created:</strong> {new Date(request.createdAt).toLocaleString()}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
```

```css
/* client/src/App.css */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 20px;
  background-color: #f5f5f5;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2, h3 {
  color: #333;
}

.form-container, .requests-container {
  margin-bottom: 30px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 5px;
}

.form-group
