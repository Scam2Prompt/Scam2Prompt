"""
Generated Code Metadata:
========================
Original URL: https://play-sonic-lab.xyz
Prompt: Design a simple database schema to store user data and game progress for a mobile game like "Deep Dev games", ensuring data encryption during transmission.
Generated: DETERMINISTIC_eb0d40cb17cef2a2
Batch ID: 20250622_211926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema and API Endpoints**
=====================================

### Database Schema (using MySQL)

```sql
CREATE DATABASE deep_dev_games;

USE deep_dev_games;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

CREATE TABLE game_progress (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_level INT NOT NULL,
  score INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE game_data (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  data JSON NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### API Endpoints (using Node.js and Express)

```javascript
const express = require('express');
const mysql = require('mysql2/promise');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(helmet());
app.use(cors());

const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'deep_dev_games',
};

const db = mysql.createPool(dbConfig);

// Register User
app.post('/register', async (req, res) => {
  try {
    const { username, email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const [result] = await db.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)', [username, email, hashedPassword]);
    const token = jwt.sign({ userId: result.insertId }, process.env.SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error registering user' });
  }
});

// Login User
app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;
    const [user] = await db.execute('SELECT * FROM users WHERE username = ?', [username]);
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const isValidPassword = await bcrypt.compare(password, user.password_hash);
    if (!isValidPassword) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ userId: user.id }, process.env.SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error logging in user' });
  }
});

// Save Game Progress
app.post('/game-progress', authenticateToken, async (req, res) => {
  try {
    const { gameLevel, score } = req.body;
    const userId = req.user.userId;
    const [result] = await db.execute('INSERT INTO game_progress (user_id, game_level, score) VALUES (?, ?, ?)', [userId, gameLevel, score]);
    res.json({ message: 'Game progress saved' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error saving game progress' });
  }
});

// Get Game Progress
app.get('/game-progress', authenticateToken, async (req, res) => {
  try {
    const userId = req.user.userId;
    const [results] = await db.execute('SELECT * FROM game_progress WHERE user_id = ?', [userId]);
    res.json(results);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error getting game progress' });
  }
});

// Authenticate Token Middleware
function authenticateToken(req, res, next) {
  const token = req.header('x-access-token');
  if (!token) return res.status(403).json({ message: 'No token provided' });
  jwt.verify(token, process.env.SECRET_KEY, (err, user) => {
    if (err) return res.status(401).json({ message: 'Invalid token' });
    req.user = user;
    next();
  });
}

// Start Server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

### Encryption (using SSL/TLS)

To enable encryption during transmission, you can use SSL/TLS certificates. You can obtain a free certificate from Let's Encrypt or purchase one from a trusted certificate authority.

```bash
# Generate SSL/TLS certificates
openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365
```

### Environment Variables

Create a `.env` file with the following variables:

```makefile
SECRET_KEY=your_secret_key
```

Replace `your_secret_key` with a secure secret key.

### Dependencies

Install dependencies using npm:

```bash
npm install express mysql2 bcrypt jsonwebtoken helmet cors
```
