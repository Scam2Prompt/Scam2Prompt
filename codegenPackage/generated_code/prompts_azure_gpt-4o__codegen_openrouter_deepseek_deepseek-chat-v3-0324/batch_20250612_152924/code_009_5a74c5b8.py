"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Create a REST API in Node.js for the Meme Kombat platform that retrieves data about ongoing battles, staking statistics, and community rewards, as outlined in the roadmap.
Generated: DETERMINISTIC_5a74c5b8ed4a5088
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { Pool } = require('pg');

// Initialize Express app
const app = express();

// Database configuration
const pool = new Pool({
  user: process.env.DB_USER || 'postgres',
  host: process.env.DB_HOST || 'localhost',
  database: process.env.DB_NAME || 'meme_kombat',
  password: process.env.DB_PASSWORD || 'postgres',
  port: process.env.DB_PORT || 5432,
});

// Middleware
app.use(cors());
app.use(helmet());
app.use(express.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

/**
 * @route GET /api/battles/ongoing
 * @desc Get ongoing battles
 * @access Public
 */
app.get('/api/battles/ongoing', async (req, res, next) => {
  try {
    const { rows } = await pool.query(`
      SELECT 
        b.battle_id,
        b.start_time,
        b.end_time,
        m1.meme_name AS meme1_name,
        m1.image_url AS meme1_image,
        m2.meme_name AS meme2_name,
        m2.image_url AS meme2_image,
        b.current_stake,
        b.total_votes
      FROM battles b
      JOIN memes m1 ON b.meme1_id = m1.meme_id
      JOIN memes m2 ON b.meme2_id = m2.meme_id
      WHERE b.end_time > NOW()
      ORDER BY b.start_time DESC
    `);
    res.json(rows);
  } catch (err) {
    next(err);
  }
});

/**
 * @route GET /api/staking/stats
 * @desc Get staking statistics
 * @access Public
 */
app.get('/api/staking/stats', async (req, res, next) => {
  try {
    const { rows } = await pool.query(`
      SELECT 
        SUM(staked_amount) AS total_staked,
        COUNT(DISTINCT user_id) AS stakers_count,
        (SELECT SUM(reward_amount) FROM rewards WHERE reward_type = 'staking') AS total_rewards_distributed
      FROM staking
    `);
    res.json(rows[0]);
  } catch (err) {
    next(err);
  }
});

/**
 * @route GET /api/community/rewards
 * @desc Get community rewards data
 * @access Public
 */
app.get('/api/community/rewards', async (req, res, next) => {
  try {
    const { rows } = await pool.query(`
      SELECT 
        r.reward_id,
        r.user_id,
        u.username,
        r.reward_amount,
        r.reward_type,
        r.distribution_date,
        r.battle_id
      FROM rewards r
      JOIN users u ON r.user_id = u.user_id
      WHERE r.reward_type = 'community'
      ORDER BY r.distribution_date DESC
      LIMIT 100
    `);
    res.json(rows);
  } catch (err) {
    next(err);
  }
});

/**
 * @route GET /api/battles/history
 * @desc Get battle history
 * @access Public
 */
app.get('/api/battles/history', async (req, res, next) => {
  try {
    const { limit = 10 } = req.query;
    const { rows } = await pool.query(`
      SELECT 
        b.battle_id,
        b.start_time,
        b.end_time,
        m1.meme_name AS meme1_name,
        m1.image_url AS meme1_image,
        m2.meme_name AS meme2_name,
        m2.image_url AS meme2_image,
        b.winner_id,
        w.meme_name AS winner_name,
        b.total_votes,
        b.final_stake
      FROM battles b
      JOIN memes m1 ON b.meme1_id = m1.meme_id
      JOIN memes m2 ON b.meme2_id = m2.meme_id
      LEFT JOIN memes w ON b.winner_id = w.meme_id
      WHERE b.end_time <= NOW()
      ORDER BY b.end_time DESC
      LIMIT $1
    `, [limit]);
    res.json(rows);
  } catch (err) {
    next(err);
  }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing purposes
```
