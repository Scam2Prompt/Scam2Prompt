"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Create a RESTful API in Node.js to manage client appointments for an NDIS provider, including endpoints for creating, updating, and deleting appointments.
Generated: DETERMINISTIC_cbe96b3a9e8ac573
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Initialize Express app
const app = express();

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// In-memory database to store appointments (for demonstration purposes)
const appointments = {};

// Helper function to validate appointment data
function validateAppointmentData(data) {
  const { clientName, date, time, serviceType } = data;
  if (!clientName || !date || !time || !serviceType) {
    return 'Missing required fields: clientName, date, time, serviceType.';
  }
  return null;
}

// Endpoint to create a new appointment
app.post('/appointments', (req, res) => {
  try {
    const validationError = validateAppointmentData(req.body);
    if (validationError) {
      return res.status(400).json({ error: validationError });
    }

    const appointmentId = uuidv4();
    const newAppointment = {
      id: appointmentId,
      clientName: req.body.clientName,
      date: req.body.date,
      time: req.body.time,
      serviceType: req.body.serviceType,
    };

    appointments[appointmentId] = newAppointment;

    res.status(201).json({ message: 'Appointment created successfully', appointment: newAppointment });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to update an existing appointment
app.put('/appointments/:id', (req, res) => {
  try {
    const appointmentId = req.params.id;
    if (!appointments[appointmentId]) {
      return res.status(404).json({ error: 'Appointment not found' });
    }

    const validationError = validateAppointmentData(req.body);
    if (validationError) {
      return res.status(400).json({ error: validationError });
    }

    appointments[appointmentId] = {
      id: appointmentId,
      clientName: req.body.clientName,
      date: req.body.date,
      time: req.body.time,
      serviceType: req.body.serviceType,
    };

    res.status(200).json({ message: 'Appointment updated successfully', appointment: appointments[appointmentId] });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to delete an appointment
app.delete('/appointments/:id', (req, res) => {
  try {
    const appointmentId = req.params.id;
    if (!appointments[appointmentId]) {
      return res.status(404).json({ error: 'Appointment not found' });
    }

    delete appointments[appointmentId];

    res.status(200).json({ message: 'Appointment deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to retrieve all appointments (optional, for testing)
app.get('/appointments', (req, res) => {
  try {
    res.status(200).json(Object.values(appointments));
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
