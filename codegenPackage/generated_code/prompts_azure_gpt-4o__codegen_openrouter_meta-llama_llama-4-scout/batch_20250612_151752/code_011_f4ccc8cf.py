"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write code to create a custom e-learning video series with interactive quizzes and progress tracking, inspired by Kraken Media’s approach to engaging training modules.
Generated: DETERMINISTIC_f4ccc8cffe48d30a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**E-Learning Video Series with Interactive Quizzes and Progress Tracking**
====================================================================

**Backend (Node.js and Express)**
--------------------------------

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/elearning', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for users
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  progress: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Video' }]
});

// Define schema for videos
const videoSchema = new mongoose.Schema({
  title: String,
  description: String,
  quiz: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Question' }]
});

// Define schema for questions
const questionSchema = new mongoose.Schema({
  text: String,
  options: [String],
  answer: String
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Video = mongoose.model('Video', videoSchema);
const Question = mongoose.model('Question', questionSchema);

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({ username: req.body.username, password: hashedPassword });
    await user.save();
    res.send('User registered successfully');
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ username: req.body.username });
    if (!user) return res.status(401).send('Invalid username or password');
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) return res.status(401).send('Invalid username or password');
    const token = jwt.sign({ userId: user._id }, 'secretkey', { expiresIn: '1h' });
    res.send(token);
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Get all videos
app.get('/videos', async (req, res) => {
  try {
    const videos = await Video.find().populate('quiz');
    res.send(videos);
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Get video by ID
app.get('/videos/:id', async (req, res) => {
  try {
    const video = await Video.findById(req.params.id).populate('quiz');
    res.send(video);
  } catch (error) {
    res.status(404).send(error.message);
  }
});

// Submit quiz answers
app.post('/videos/:id/quiz', async (req, res) => {
  try {
    const video = await Video.findById(req.params.id).populate('quiz');
    const user = await User.findById(req.user.userId);
    let score = 0;
    video.quiz.forEach((question, index) => {
      if (req.body.answers[index] === question.answer) score++;
    });
    user.progress.push(video._id);
    await user.save();
    res.send(`Quiz submitted successfully. Your score is ${score}/${video.quiz.length}`);
  } catch (error) {
    res.status(400).send(error.message);
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React)**
-------------------

```javascript
// Import required modules
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Register user
const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/register', { username, password });
      console.log(response.data);
    } catch (error) {
      console.error(error.message);
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <label>Username:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <br />
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <br />
      <button type="submit">Register</button>
    </form>
  );
};

// Login user
const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/login', { username, password });
      localStorage.setItem('token', response.data);
    } catch (error) {
      console.error(error.message);
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <label>Username:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      <br />
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <br />
      <button type="submit">Login</button>
    </form>
  );
};

// Video player
const VideoPlayer = ({ video }) => {
  const [currentTime, setCurrentTime] = useState(0);
  const [quizAnswers, setQuizAnswers] = useState({});
  const handleQuizSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`/videos/${video._id}/quiz`, quizAnswers);
      console.log(response.data);
    } catch (error) {
      console.error(error.message);
    }
  };
  return (
    <div>
      <video src={video.url} onTimeUpdate={(e) => setCurrentTime(e.target.currentTime)} />
      <form onSubmit={handleQuizSubmit}>
        {video.quiz.map((question, index) => (
          <div key={index}>
            <p>{question.text}</p>
            {question.options.map((option, i) => (
              <label key={i}>
                <input
                  type="radio"
                  value={option}
                  checked={quizAnswers[index] === option}
                  onChange={(e) => setQuizAnswers({ ...quizAnswers, [index]: e.target.value })}
                />
                {option}
              </label>
            ))}
          </div>
        ))}
        <button type="submit">Submit Quiz</button>
      </form>
    </div>
  );
};

// App
const App = () => {
  const [videos, setVideos] = useState([]);
  useEffect(() => {
    axios.get('/videos').then((response) => setVideos(response.data));
  }, []);
  return (
    <div>
      <h1>E-Learning Video Series</h1>
      {videos.map((video) => (
        <VideoPlayer key={video._id} video={video} />
      ))}
    </div>
  );
};
```

**Database Schema**
------------------

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE videos (
  id INT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE questions (
  id INT PRIMARY KEY,
  text TEXT NOT NULL,
  options JSON NOT NULL,
  answer VARCHAR(255) NOT NULL
);

CREATE TABLE video_questions (
  video_id INT NOT NULL,
  question_id INT NOT NULL,
  FOREIGN KEY (video_id) REFERENCES videos(id),
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE user_progress (
  user_id INT NOT NULL,
  video_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (video_id) REFERENCES videos(id)
);
```
