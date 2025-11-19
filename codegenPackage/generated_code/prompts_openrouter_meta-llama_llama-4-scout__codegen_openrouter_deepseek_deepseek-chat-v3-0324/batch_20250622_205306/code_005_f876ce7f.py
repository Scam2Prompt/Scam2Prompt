"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Develop a customer support ticketing system using a library like React.js and Node.js, inspired by Maruf Online BD's 24/7 support features, and provide a basic implementation.
Generated: DETERMINISTIC_f876ce7febfde56e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Frontend: React.js components for the ticketing system

// TicketList.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TicketForm from './TicketForm';

const TicketList = () => {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const response = await axios.get('/api/tickets');
        setTickets(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTickets();
  }, []);

  const handleStatusChange = async (id, status) => {
    try {
      await axios.put(`/api/tickets/${id}`, { status });
      setTickets(tickets.map(ticket => 
        ticket._id === id ? { ...ticket, status } : ticket
      ));
    } catch (err) {
      setError(err.message);
    }
  };

  if (loading) return <div>Loading tickets...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="ticket-system">
      <h2>Customer Support Tickets</h2>
      <TicketForm setTickets={setTickets} />
      <div className="ticket-list">
        {tickets.map(ticket => (
          <div key={ticket._id} className={`ticket ${ticket.status}`}>
            <h3>{ticket.subject}</h3>
            <p>{ticket.description}</p>
            <div className="ticket-meta">
              <span>Status: {ticket.status}</span>
              <span>Created: {new Date(ticket.createdAt).toLocaleString()}</span>
            </div>
            <div className="ticket-actions">
              <select 
                value={ticket.status} 
                onChange={(e) => handleStatusChange(ticket._id, e.target.value)}
              >
                <option value="open">Open</option>
                <option value="in-progress">In Progress</option>
                <option value="resolved">Resolved</option>
              </select>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TicketList;

// TicketForm.jsx
import React, { useState } from 'react';
import axios from 'axios';

const TicketForm = ({ setTickets }) => {
  const [subject, setSubject] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    
    if (!subject || !description) {
      setError('Subject and description are required');
      return;
    }

    try {
      const response = await axios.post('/api/tickets', {
        subject,
        description,
        status: 'open'
      });
      setTickets(prev => [response.data, ...prev]);
      setSubject('');
      setDescription('');
      setSuccess(true);
      setTimeout(() => setSuccess(false), 3000);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="ticket-form">
      <h3>Create New Ticket</h3>
      {error && <div className="error">{error}</div>}
      {success && <div className="success">Ticket created successfully!</div>}
      <div className="form-group">
        <label>Subject:</label>
        <input
          type="text"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label>Description:</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <button type="submit">Submit Ticket</button>
    </form>
  );
};

export default TicketForm;
```

```javascript
// Backend: Node.js server with Express

// server.js
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const Ticket = require('./models/Ticket');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/support_tickets', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Routes
app.get('/api/tickets', async (req, res) => {
  try {
    const tickets = await Ticket.find().sort({ createdAt: -1 });
    res.json(tickets);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/tickets', async (req, res) => {
  try {
    const { subject, description, status } = req.body;
    const ticket = new Ticket({ subject, description, status });
    await ticket.save();
    res.status(201).json(ticket);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

app.put('/api/tickets/:id', async (req, res) => {
  try {
    const { status } = req.body;
    const ticket = await Ticket.findByIdAndUpdate(
      req.params.id,
      { status },
      { new: true }
    );
    if (!ticket) {
      return res.status(404).json({ error: 'Ticket not found' });
    }
    res.json(ticket);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```javascript
// models/Ticket.js
const mongoose = require('mongoose');

const ticketSchema = new mongoose.Schema({
  subject: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true,
    trim: true
  },
  status: {
    type: String,
    enum: ['open', 'in-progress', 'resolved'],
    default: 'open'
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

const Ticket = mongoose.model('Ticket', ticketSchema);

module.exports = Ticket;
```

```css
/* styles.css */
.ticket-system {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.ticket-form {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group textarea {
  min-height: 100px;
}

button {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #45a049;
}

.ticket-list {
  display: grid;
  gap: 15px;
}

.ticket {
  background: white;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.ticket h3 {
  margin-top: 0;
}

.ticket-meta {
  display: flex;
  justify-content: space-between;
  color: #666;
  font-size: 0.9em;
  margin: 10px 0;
}

.ticket-actions select {
  padding: 5px;
}

.error {
  color: #d32f2f;
  margin-bottom: 10px;
}

.success {
  color: #388e3c;
  margin-bottom: 10px;
}

.ticket.open {
  border-left: 4px solid #2196F3;
}

.ticket.in-progress {
  border-left: 4px solid #FFC107;
}

.ticket.resolved {
  border-left: 4px solid #4CAF50;
}
```
