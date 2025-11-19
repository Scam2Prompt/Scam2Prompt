"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Create a REST API endpoint in Node.js that allows users to retrieve information about fitness classes offered at Batıkent Tofaş Spor Klübü, including timings and trainers.
Generated: DETERMINISTIC_814ea917af3c192e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample data for fitness classes
const fitnessClasses = [
  {
    id: 1,
    name: "Yoga",
    description: "Beginner-friendly yoga class focusing on flexibility and relaxation",
    schedule: [
      { day: "Monday", time: "09:00 - 10:00", trainer: "Aylin Demir" },
      { day: "Wednesday", time: "09:00 - 10:00", trainer: "Aylin Demir" },
      { day: "Friday", time: "09:00 - 10:00", trainer: "Aylin Demir" }
    ]
  },
  {
    id: 2,
    name: "Pilates",
    description: "Core strengthening and posture improvement",
    schedule: [
      { day: "Tuesday", time: "18:00 - 19:00", trainer: "Mehmet Yılmaz" },
      { day: "Thursday", time: "18:00 - 19:00", trainer: "Mehmet Yılmaz" }
    ]
  },
  {
    id: 3,
    name: "Zumba",
    description: "High-energy dance workout with Latin rhythms",
    schedule: [
      { day: "Monday", time: "19:00 - 20:00", trainer: "Ebru Şahin" },
      { day: "Wednesday", time: "19:00 - 20:00", trainer: "Ebru Şahin" },
      { day: "Saturday", time: "11:00 - 12:00", trainer: "Ebru Şahin" }
    ]
  },
  {
    id: 4,
    name: "CrossFit",
    description: "High-intensity functional training",
    schedule: [
      { day: "Tuesday", time: "07:00 - 08:00", trainer: "Can Aydın" },
      { day: "Thursday", time: "07:00 - 08:00", trainer: "Can Aydın" },
      { day: "Saturday", time: "10:00 - 11:00", trainer: "Can Aydın" }
    ]
  }
];

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Service is running' });
});

// GET all fitness classes
app.get('/api/classes', (req, res) => {
  try {
    res.status(200).json(fitnessClasses);
  } catch (error) {
    console.error('Error fetching classes:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET specific class by ID
app.get('/api/classes/:id', (req, res) => {
  try {
    const classId = parseInt(req.params.id);
    const fitnessClass = fitnessClasses.find(c => c.id === classId);

    if (!fitnessClass) {
      return res.status(404).json({ error: 'Class not found' });
    }

    res.status(200).json(fitnessClass);
  } catch (error) {
    console.error('Error fetching class:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// GET classes by day
app.get('/api/classes/day/:day', (req, res) => {
  try {
    const day = req.params.day.charAt(0).toUpperCase() + req.params.day.slice(1).toLowerCase();
    const validDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    
    if (!validDays.includes(day)) {
      return res.status(400).json({ error: 'Invalid day parameter' });
    }

    const classesOnDay = fitnessClasses.map(classItem => {
      const schedule = classItem.schedule.filter(s => s.day === day);
      if (schedule.length > 0) {
        return {
          id: classItem.id,
          name: classItem.name,
          description: classItem.description,
          schedule: schedule
        };
      }
      return null;
    }).filter(Boolean);

    res.status(200).json(classesOnDay);
  } catch (error) {
    console.error('Error fetching classes by day:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
