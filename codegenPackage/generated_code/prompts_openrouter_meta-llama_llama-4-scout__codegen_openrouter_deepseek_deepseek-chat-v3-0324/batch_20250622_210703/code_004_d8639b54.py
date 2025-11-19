"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Create a RESTful API using Node.js and Express.js to manage handball tournament brackets, teams, and player statistics, considering the requirements of a club like RK Kočevje.
Generated: DETERMINISTIC_d8639b54498d422c
Batch ID: 20250622_210703
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
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Initialize Express app
const app = express();

// Middleware
app.use(cors());
app.use(helmet());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/handball_tournament', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('MongoDB connected successfully'))
.catch(err => console.error('MongoDB connection error:', err));

// Models
const Team = mongoose.model('Team', new mongoose.Schema({
  name: { type: String, required: true, unique: true },
  coach: String,
  foundedYear: Number,
  homeCourt: String,
  players: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Player' }],
  createdAt: { type: Date, default: Date.now }
}));

const Player = mongoose.model('Player', new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  birthDate: Date,
  position: String,
  jerseyNumber: { type: Number, min: 1, max: 99 },
  team: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
  stats: {
    goals: { type: Number, default: 0 },
    assists: { type: Number, default: 0 },
    yellowCards: { type: Number, default: 0 },
    redCards: { type: Number, default: 0 },
    matchesPlayed: { type: Number, default: 0 }
  },
  createdAt: { type: Date, default: Date.now }
}));

const Tournament = mongoose.model('Tournament', new mongoose.Schema({
  name: { type: String, required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true },
  location: String,
  teams: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Team' }],
  brackets: [{
    name: String,
    matches: [{
      team1: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
      team2: { type: mongoose.Schema.Types.ObjectId, ref: 'Team' },
      score1: Number,
      score2: Number,
      date: Date,
      completed: { type: Boolean, default: false }
    }]
  }],
  createdAt: { type: Date, default: Date.now }
}));

// Routes
const router = express.Router();

// Teams routes
router.route('/teams')
  .get(async (req, res) => {
    try {
      const teams = await Team.find().populate('players');
      res.json(teams);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const team = new Team(req.body);
      await team.save();
      res.status(201).json(team);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

router.route('/teams/:id')
  .get(async (req, res) => {
    try {
      const team = await Team.findById(req.params.id).populate('players');
      if (!team) return res.status(404).json({ error: 'Team not found' });
      res.json(team);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const team = await Team.findByIdAndUpdate(req.params.id, req.body, { new: true });
      if (!team) return res.status(404).json({ error: 'Team not found' });
      res.json(team);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const team = await Team.findByIdAndDelete(req.params.id);
      if (!team) return res.status(404).json({ error: 'Team not found' });
      res.json({ message: 'Team deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Players routes
router.route('/players')
  .get(async (req, res) => {
    try {
      const players = await Player.find().populate('team');
      res.json(players);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const player = new Player(req.body);
      await player.save();
      res.status(201).json(player);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

router.route('/players/:id')
  .get(async (req, res) => {
    try {
      const player = await Player.findById(req.params.id).populate('team');
      if (!player) return res.status(404).json({ error: 'Player not found' });
      res.json(player);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const player = await Player.findByIdAndUpdate(req.params.id, req.body, { new: true });
      if (!player) return res.status(404).json({ error: 'Player not found' });
      res.json(player);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const player = await Player.findByIdAndDelete(req.params.id);
      if (!player) return res.status(404).json({ error: 'Player not found' });
      res.json({ message: 'Player deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Tournaments routes
router.route('/tournaments')
  .get(async (req, res) => {
    try {
      const tournaments = await Tournament.find().populate('teams').populate('brackets.matches.team1 brackets.matches.team2');
      res.json(tournaments);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .post(async (req, res) => {
    try {
      const tournament = new Tournament(req.body);
      await tournament.save();
      res.status(201).json(tournament);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });

router.route('/tournaments/:id')
  .get(async (req, res) => {
    try {
      const tournament = await Tournament.findById(req.params.id)
        .populate('teams')
        .populate('brackets.matches.team1 brackets.matches.team2');
      if (!tournament) return res.status(404).json({ error: 'Tournament not found' });
      res.json(tournament);
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  })
  .put(async (req, res) => {
    try {
      const tournament = await Tournament.findByIdAndUpdate(req.params.id, req.body, { new: true })
        .populate('teams')
        .populate('brackets.matches.team1 brackets.matches.team2');
      if (!tournament) return res.status(404).json({ error: 'Tournament not found' });
      res.json(tournament);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  })
  .delete(async (req, res) => {
    try {
      const tournament = await Tournament.findByIdAndDelete(req.params.id);
      if (!tournament) return res.status(404).json({ error: 'Tournament not found' });
      res.json({ message: 'Tournament deleted successfully' });
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });

// Tournament bracket operations
router.route('/tournaments/:id/brackets')
  .post(async (req, res) => {
    try {
      const tournament = await Tournament.findById(req.params.id);
      if (!tournament) return res.status(404).json({ error: 'Tournament not found' });
      
      tournament.brackets
