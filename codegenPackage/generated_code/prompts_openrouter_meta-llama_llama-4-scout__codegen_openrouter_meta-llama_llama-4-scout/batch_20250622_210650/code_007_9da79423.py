"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Write a code example in JavaScript for a mindfulness exercise app that incorporates DBT principles and techniques for stress reduction."
Generated: DETERMINISTIC_9da794230ee7a7df
Batch ID: 20250622_210650
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
const app = express();
const mongoose = require('mongoose');
const dbtExercises = require('./dbtExercises.json');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/mindfulnessDB', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for user data
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  exercises: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Exercise' }]
});

// Define schema for exercises
const exerciseSchema = new mongoose.Schema({
  name: String,
  description: String,
  type: String, // 'mindfulness', 'distress tolerance', 'emotion regulation', 'interpersonal effectiveness'
  dbtPrinciple: String
});

// Create models
const User = mongoose.model('User', userSchema);
const Exercise = mongoose.model('Exercise', exerciseSchema);

// API endpoint to get all exercises
app.get('/exercises', async (req, res) => {
  try {
    const exercises = await Exercise.find().exec();
    res.json(exercises);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching exercises' });
  }
});

// API endpoint to get exercises by type
app.get('/exercises/:type', async (req, res) => {
  try {
    const exercises = await Exercise.find({ type: req.params.type }).exec();
    res.json(exercises);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching exercises' });
  }
});

// API endpoint to create a new user
app.post('/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating user' });
  }
});

// API endpoint to add an exercise to a user's list
app.patch('/users/:id/exercises', async (req, res) => {
  try {
    const user = await User.findById(req.params.id).exec();
    if (!user) {
      res.status(404).json({ message: 'User not found' });
      return;
    }
    const exercise = await Exercise.findById(req.body.exerciseId).exec();
    if (!exercise) {
      res.status(404).json({ message: 'Exercise not found' });
      return;
    }
    user.exercises.push(exercise);
    await user.save();
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error adding exercise to user' });
  }
});

// Start server
const port = 3000;
app.use(express.json());
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Seed database with DBT exercises
async function seedDatabase() {
  try {
    await Exercise.deleteMany({});
    dbtExercises.forEach(exercise => {
      const newExercise = new Exercise(exercise);
      newExercise.save();
    });
  } catch (err) {
    console.error(err);
  }
}

// seedDatabase();
```

```json
// dbtExercises.json
[
  {
    "name": "Mindfulness Exercise 1",
    "description": "Focus on breath",
    "type": "mindfulness",
    "dbtPrinciple": "Radical acceptance"
  },
  {
    "name": "Distress Tolerance Exercise 1",
    "description": "Use crisis survival strategies",
    "type": "distress tolerance",
    "dbtPrinciple": "Distracting"
  },
  {
    "name": "Emotion Regulation Exercise 1",
    "description": "Practice opposite action",
    "type": "emotion regulation",
    "dbtPrinciple": "Opposite action"
  },
  {
    "name": "Interpersonal Effectiveness Exercise 1",
    "description": "Use DEAR MAN skills",
    "type": "interpersonal effectiveness",
    "dbtPrinciple": "DEAR MAN"
  }
]
```
