"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Design a web application for users to create and share their own Géminito-style music games."
Generated: DETERMINISTIC_28a09032e2971ea4
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Gemini Game Creator Web Application**
=====================================

**Backend (Node.js and Express)**
--------------------------------

```javascript
// server.js
const express = require('express');
const app = express();
const port = 3000;
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/gemini-games', { useNewUrlParser: true, useUnifiedTopology: true });

// Define user schema
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String
});

// Define game schema
const gameSchema = new mongoose.Schema({
  title: String,
  description: String,
  creator: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  levels: [{ type: String }]
});

// Compile schemas into models
const User = mongoose.model('User', userSchema);
const Game = mongoose.model('Game', gameSchema);

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Register user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({
      username: req.body.username,
      email: req.body.email,
      password: hashedPassword
    });
    await user.save();
    res.status(201).send({ message: 'User created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating user' });
  }
});

// Login user
app.post('/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const isValidPassword = await bcrypt.compare(req.body.password, user.password);
    if (!isValidPassword) {
      return res.status(401).send({ message: 'Invalid email or password' });
    }
    const token = jwt.sign({ userId: user._id }, 'secret-key', { expiresIn: '1h' });
    res.send({ token });
  } catch (error) {
    res.status(400).send({ message: 'Error logging in' });
  }
});

// Create game
app.post('/games', authenticateToken, async (req, res) => {
  try {
    const game = new Game({
      title: req.body.title,
      description: req.body.description,
      creator: req.user._id,
      levels: req.body.levels
    });
    await game.save();
    res.status(201).send({ message: 'Game created successfully' });
  } catch (error) {
    res.status(400).send({ message: 'Error creating game' });
  }
});

// Get all games
app.get('/games', async (req, res) => {
  try {
    const games = await Game.find().populate('creator', '_id username');
    res.send(games);
  } catch (error) {
    res.status(400).send({ message: 'Error fetching games' });
  }
});

// Authenticate token middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (token == null) return res.status(401).send({ message: 'Access denied' });
  try {
    const verified = jwt.verify(token, 'secret-key');
    req.user = verified;
    next();
  } catch (error) {
    res.status(400).send({ message: 'Invalid token' });
  }
}

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**Frontend (React)**
-------------------

```javascript
// GameCreator.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function GameCreator() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [levels, setLevels] = useState([]);
  const [creator, setCreator] = useState({});

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/games', {
        title,
        description,
        levels,
      }, {
        headers: {
          Authorization: localStorage.getItem('token'),
        },
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Title:
        <input type="text" value={title} onChange={(event) => setTitle(event.target.value)} />
      </label>
      <br />
      <label>
        Description:
        <textarea value={description} onChange={(event) => setDescription(event.target.value)} />
      </label>
      <br />
      <label>
        Levels:
        <input type="text" value={levels.join(',')} onChange={(event) => setLevels(event.target.value.split(','))} />
      </label>
      <br />
      <button type="submit">Create Game</button>
    </form>
  );
}

export default GameCreator;
```

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GameCreator from './GameCreator';

function App() {
  const [games, setGames] = useState([]);
  const [token, setToken] = useState(localStorage.getItem('token'));

  useEffect(() => {
    axios.get('/games')
      .then((response) => {
        setGames(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/login', {
        email: event.target.email.value,
        password: event.target.password.value,
      });
      setToken(response.data.token);
      localStorage.setItem('token', response.data.token);
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  return (
    <div>
      {token ? (
        <div>
          <GameCreator />
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <form onSubmit={handleLogin}>
          <label>
            Email:
            <input type="email" name="email" />
          </label>
          <br />
          <label>
            Password:
            <input type="password" name="password" />
          </label>
          <br />
          <button type="submit">Login</button>
        </form>
      )}
      <h1>Games</h1>
      <ul>
        {games.map((game) => (
          <li key={game._id}>
            <h2>{game.title}</h2>
            <p>{game.description}</p>
            <p>Creator: {game.creator.username}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gemini Game Creator</title>
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```

**package.json**
```json
{
  "name": "gemini-game-creator",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js & react-scripts start"
  },
  "dependencies": {
    "axios": "^0.21.1",
    "bcrypt": "^5.0.1",
    "express": "^4.17.1",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^5.12.3",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "^4.0.3"
  }
}
```
