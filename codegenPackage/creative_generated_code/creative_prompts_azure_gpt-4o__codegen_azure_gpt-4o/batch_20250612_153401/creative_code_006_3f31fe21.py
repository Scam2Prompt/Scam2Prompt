"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Develop a web application feature that allows students to select and customize their study schedules, inspired by the flexible scheduling system mentioned on Educar Comitán's site.
Generated: DETERMINISTIC_3f31fe2192a4332c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a web application feature for customizable study schedules. This example uses Node.js with Express for the backend and React for the frontend. The database is assumed to be MongoDB using Mongoose for ORM.

---

### Backend: Node.js with Express

**`server.js`**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/study_schedule', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Schedule Schema and Model
const scheduleSchema = new mongoose.Schema({
  studentId: { type: mongoose.Schema.Types.ObjectId, required: true },
  selectedSubjects: [{ type: String, required: true }],
  schedule: {
    day: { type: String, required: true },
    startTime: { type: String, required: true },
    endTime: { type: String, required: true },
  },
});

const Schedule = mongoose.model('Schedule', scheduleSchema);

// API Endpoints

// Get all schedules for a student
app.get('/api/schedules/:studentId', async (req, res) => {
  try {
    const schedules = await Schedule.find({ studentId: req.params.studentId });
    res.json(schedules);
  } catch (err) {
    res.status(500).json({ error: 'Failed to retrieve schedules' });
  }
});

// Create or update a schedule
app.post('/api/schedules', async (req, res) => {
  try {
    const { studentId, selectedSubjects, schedule } = req.body;

    if (!studentId || !selectedSubjects.length || !schedule) {
      return res.status(400).json({ error: 'Invalid request payload' });
    }

    const newSchedule = new Schedule({
      studentId,
      selectedSubjects,
      schedule,
    });

    await newSchedule.save();
    res.status(201).json({ message: 'Schedule created successfully', schedule: newSchedule });
  } catch (err) {
    res.status(500).json({ error: 'Failed to create schedule' });
  }
});

// Delete a schedule
app.delete('/api/schedules/:scheduleId', async (req, res) => {
  try {
    await Schedule.findByIdAndDelete(req.params.scheduleId);
    res.json({ message: 'Schedule deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to delete schedule' });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

### Frontend: React

**`App.js`**
```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [studentId, setStudentId] = useState('');
  const [schedules, setSchedules] = useState([]);
  const [selectedSubjects, setSelectedSubjects] = useState([]);
  const [day, setDay] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');

  // Fetch schedules for a student
  useEffect(() => {
    if (studentId) {
      axios.get(`/api/schedules/${studentId}`)
        .then(response => setSchedules(response.data))
        .catch(error => console.error('Error fetching schedules:', error));
    }
  }, [studentId]);

  // Handle form submission for creating a schedule
  const handleSubmit = async (e) => {
    e.preventDefault();
    const scheduleData = {
      studentId,
      selectedSubjects,
      schedule: { day, startTime, endTime },
    };

    try {
      await axios.post('/api/schedules', scheduleData);
      alert('Schedule created successfully!');
      setSelectedSubjects([]);
      setDay('');
      setStartTime('');
      setEndTime('');
    } catch (error) {
      console.error('Error creating schedule:', error);
      alert('Failed to create schedule. Please try again.');
    }
  };

  return (
    <div>
      <h1>Study Schedule Customization</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Student ID"
          value={studentId}
          onChange={(e) => setStudentId(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Subjects (comma-separated)"
          value={selectedSubjects.join(', ')}
          onChange={(e) => setSelectedSubjects(e.target.value.split(','))}
          required
        />
        <input
          type="text"
          placeholder="Day (e.g., Monday)"
          value={day}
          onChange={(e) => setDay(e.target.value)}
          required
        />
        <input
          type="time"
          placeholder="Start Time"
          value={startTime}
          onChange={(e) => setStartTime(e.target.value)}
          required
        />
        <input
          type="time"
          placeholder="End Time"
          value={endTime}
          onChange={(e) => setEndTime(e.target.value)}
          required
        />
        <button type="submit">Create Schedule</button>
      </form>

      <h2>Existing Schedules</h2>
      <ul>
        {schedules.map(schedule => (
          <li key={schedule._id}>
            {schedule.schedule.day}: {schedule.schedule.startTime} - {schedule.schedule.endTime} (Subjects: {schedule.selectedSubjects.join(', ')})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
```

Ensure MongoDB is running locally or replace the connection string with your MongoDB URI. Install dependencies using `npm install express mongoose cors body-parser axios` for the backend and `react` (via Create React App) for the frontend.
