"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Develop an API endpoint in Node.js for managing pet service appointments, including validation for service types like "banho e tosa" as mentioned on the Petland website.
Generated: DETERMINISTIC_010eec3becb4a9fe
Batch ID: 20250612_164043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');

// Create an Express application
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON request body

// Define valid service types as per Petland offerings
const validServiceTypes = ['banho e tosa', 'veterinary consultation', 'grooming', 'training'];

// Endpoint to handle appointment creation
app.post('/api/appointments', (req, res) => {
  try {
    // Extract data from the request body
    const { petName, ownerName, serviceType, appointmentDate } = req.body;

    // Validate required fields
    if (!petName || !ownerName || !serviceType || !appointmentDate) {
      return res.status(400).json({
        error: 'Missing required fields. Please provide petName, ownerName, serviceType, and appointmentDate.',
      });
    }

    // Validate service type
    if (!validServiceTypes.includes(serviceType)) {
      return res.status(400).json({
        error: `Invalid service type. Accepted values are: ${validServiceTypes.join(', ')}`,
      });
    }

    // Validate appointment date
    const parsedDate = new Date(appointmentDate);
    if (isNaN(parsedDate.getTime())) {
      return res.status(400).json({
        error: 'Invalid appointment date. Please provide a valid date in ISO 8601 format.',
      });
    }

    // Simulate saving the appointment (this would typically involve a database)
    const newAppointment = {
      id: Date.now(), // Generate a unique ID (simple approach, not suitable for large-scale apps)
      petName,
      ownerName,
      serviceType,
      appointmentDate: parsedDate.toISOString(),
    };

    // Respond with the created appointment
    res.status(201).json({
      message: 'Appointment created successfully!',
      appointment: newAppointment,
    });
  } catch (err) {
    // Catch unexpected errors and respond with an internal server error
    console.error('Error creating appointment:', err); // Log error for debugging purposes
    res.status(500).json({
      error: 'Internal server error. Please try again later.',
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use environment variable or default to port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
