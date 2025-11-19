"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a basic leaderboard system using a database and a programming language like JavaScript, inspired by Big Time's $BIGTIME leaderboard.
Generated: DETERMINISTIC_3f9928f3f290b0cf
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// leaderboard.js
// Basic leaderboard system using SQLite database and Node.js
// Inspired by Big Time's $BIGTIME leaderboard

const sqlite3 = require('sqlite3').verbose();
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the application
const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());

// Database setup
const db = new sqlite3.Database('./leaderboard.db', (err) => {
    if (err) {
        console.error('Database connection error:', err.message);
    } else {
        console.log('Connected to the leaderboard database');
        initializeDatabase();
    }
});

// Initialize database tables
function initializeDatabase() {
    db.run(`
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            score INTEGER DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    `, (err) => {
        if (err) {
            console.error('Error creating players table:', err.message);
        }
    });
}

// API Endpoints

/**
 * Add or update player score
 * POST /api/leaderboard
 * Body: { "username": "string", "score": number }
 */
app.post('/api/leaderboard', (req, res) => {
    const { username, score } = req.body;
    
    if (!username || score === undefined) {
        return res.status(400).json({ error: 'Username and score are required' });
    }

    db.run(`
        INSERT INTO players (username, score) 
        VALUES (?, ?)
        ON CONFLICT(username) DO UPDATE SET 
            score = score + excluded.score,
            last_updated = CURRENT_TIMESTAMP
    `, [username, score], function(err) {
        if (err) {
            console.error('Error updating leaderboard:', err.message);
            return res.status(500).json({ error: 'Failed to update leaderboard' });
        }
        
        res.status(200).json({ 
            message: 'Leaderboard updated successfully',
            changes: this.changes
        });
    });
});

/**
 * Get top players
 * GET /api/leaderboard?limit=10
 */
app.get('/api/leaderboard', (req, res) => {
    const limit = parseInt(req.query.limit) || 10;
    
    db.all(`
        SELECT username, score 
        FROM players 
        ORDER BY score DESC 
        LIMIT ?
    `, [limit], (err, rows) => {
        if (err) {
            console.error('Error fetching leaderboard:', err.message);
            return res.status(500).json({ error: 'Failed to fetch leaderboard' });
        }
        
        res.status(200).json(rows);
    });
});

/**
 * Get player rank
 * GET /api/leaderboard/:username
 */
app.get('/api/leaderboard/:username', (req, res) => {
    const { username } = req.params;
    
    db.get(`
        SELECT username, score, 
        (SELECT COUNT(*) FROM players p2 WHERE p2.score > p1.score) + 1 as rank
        FROM players p1
        WHERE username = ?
    `, [username], (err, row) => {
        if (err) {
            console.error('Error fetching player rank:', err.message);
            return res.status(500).json({ error: 'Failed to fetch player rank' });
        }
        
        if (!row) {
            return res.status(404).json({ error: 'Player not found' });
        }
        
        res.status(200).json(row);
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error('Unhandled error:', err);
    res.status(500).json({ error: 'Internal server error' });
});

// Start the server
app.listen(port, () => {
    console.log(`Leaderboard server running on port ${port}`);
});

// Close database connection on process exit
process.on('SIGINT', () => {
    db.close((err) => {
        if (err) {
            console.error('Error closing database:', err.message);
        } else {
            console.log('Database connection closed');
        }
        process.exit(0);
    });
});
```
