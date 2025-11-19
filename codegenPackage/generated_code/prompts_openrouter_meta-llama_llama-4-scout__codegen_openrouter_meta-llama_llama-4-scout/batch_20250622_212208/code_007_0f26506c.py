"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Design a basic token rewards system using Node.js and a database to manage user rewards and referrals for the Initia Network ($INIT) token.
Generated: DETERMINISTIC_0f26506cd78e7f29
Batch ID: 20250622_212208
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
const mysql = require('mysql2/promise');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Create a new Express app
const app = express();
app.use(express.json());

// Database connection settings
const dbHost = process.env.DB_HOST;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;
const dbName = process.env.DB_NAME;

// Create a database connection pool
const db = mysql.createPool({
  host: dbHost,
  user: dbUser,
  password: dbPassword,
  database: dbName,
  connectionLimit: 10
});

// Create tables if they don't exist
async function createTables() {
  try {
    await db.execute(`
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        address VARCHAR(255) NOT NULL,
        referrer_id INT,
        PRIMARY KEY (id),
        FOREIGN KEY (referrer_id) REFERENCES users(id)
      );
    `);

    await db.execute(`
      CREATE TABLE IF NOT EXISTS rewards (
        id INT AUTO_INCREMENT,
        user_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users(id)
      );
    `);
  } catch (error) {
    console.error('Error creating tables:', error);
  }
}

// Initialize the database
createTables();

// Get a user by address
async function getUserByAddress(address) {
  try {
    const [user] = await db.execute('SELECT * FROM users WHERE address = ?', [address]);
    return user;
  } catch (error) {
    console.error('Error getting user by address:', error);
    return null;
  }
}

// Register a new user
async function registerUser(address, referrerAddress) {
  try {
    const referrer = await getUserByAddress(referrerAddress);
    const result = await db.execute(`
      INSERT INTO users (address, referrer_id)
      VALUES (?, ?);
    `, [address, referrer ? referrer.id : null]);
    return result[0].insertId;
  } catch (error) {
    console.error('Error registering user:', error);
    return null;
  }
}

// Get user rewards
async function getUserRewards(userId) {
  try {
    const [rewards] = await db.execute(`
      SELECT * FROM rewards
      WHERE user_id = ?
      ORDER BY timestamp DESC;
    `, [userId]);
    return rewards;
  } catch (error) {
    console.error('Error getting user rewards:', error);
    return [];
  }
}

// Distribute rewards
async function distributeRewards(userId, amount) {
  try {
    await db.execute(`
      INSERT INTO rewards (user_id, amount)
      VALUES (?, ?);
    `, [userId, amount]);
  } catch (error) {
    console.error('Error distributing rewards:', error);
  }
}

// Referral rewards
async function referralRewards(referrerId, amount) {
  try {
    await distributeRewards(referrerId, amount);
  } catch (error) {
    console.error('Error distributing referral rewards:', error);
  }
}

// API endpoints
app.post('/register', async (req, res) => {
  try {
    const { address, referrerAddress } = req.body;
    const userId = await registerUser(address, referrerAddress);
    if (userId) {
      res.json({ userId });
    } else {
      res.status(400).json({ error: 'Failed to register user' });
    }
  } catch (error) {
    console.error('Error registering user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/rewards/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const rewards = await getUserRewards(userId);
    res.json(rewards);
  } catch (error) {
    console.error('Error getting user rewards:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/distribute-rewards', async (req, res) => {
  try {
    const { userId, amount } = req.body;
    await distributeRewards(userId, amount);
    res.json({ message: 'Rewards distributed successfully' });
  } catch (error) {
    console.error('Error distributing rewards:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
