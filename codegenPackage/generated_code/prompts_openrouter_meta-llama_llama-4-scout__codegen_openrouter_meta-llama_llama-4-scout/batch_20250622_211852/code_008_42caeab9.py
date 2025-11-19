"""
Generated Code Metadata:
========================
Original URL: https://gamees.org
Prompt: "Design a simple API for 3 Patti game development using Node.js."
Generated: DETERMINISTIC_42caeab948e85e0a
Batch ID: 20250622_211852
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
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Define a class for the game
class PattiGame {
  /**
   * Initialize a new game
   */
  constructor() {
    this.deck = this.generateDeck();
    this.players = [];
  }

  /**
   * Generate a standard deck of 52 cards
   * @returns {Array} - A list of card objects
   */
  generateDeck() {
    const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
    const ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'];
    const deck = [];

    for (const suit of suits) {
      for (const rank of ranks) {
        deck.push({ suit, rank });
      }
    }

    return deck;
  }

  /**
   * Add a player to the game
   * @param {string} name - The player's name
   */
  addPlayer(name) {
    this.players.push({ name, hand: [] });
  }

  /**
   * Deal cards to all players
   */
  dealCards() {
    for (const player of this.players) {
      player.hand = [];
      for (let i = 0; i < 3; i++) {
        const randomIndex = Math.floor(Math.random() * this.deck.length);
        player.hand.push(this.deck.splice(randomIndex, 1)[0]);
      }
    }
  }

  /**
   * Get a player's hand
   * @param {string} name - The player's name
   * @returns {Array} - The player's hand
   */
  getPlayerHand(name) {
    const player = this.players.find(p => p.name === name);
    return player ? player.hand : [];
  }
}

// Initialize a new game
const game = new PattiGame();

// API Endpoints

// Add a player to the game
app.post('/players', (req, res) => {
  try {
    const { name } = req.body;
    if (!name) {
      return res.status(400).send({ error: 'Name is required' });
    }
    game.addPlayer(name);
    res.send({ message: `Player ${name} added successfully` });
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Deal cards to all players
app.post('/deal-cards', (req, res) => {
  try {
    game.dealCards();
    res.send({ message: 'Cards dealt successfully' });
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Get a player's hand
app.get('/players/:name/hand', (req, res) => {
  try {
    const { name } = req.params;
    const hand = game.getPlayerHand(name);
    if (!hand) {
      return res.status(404).send({ error: 'Player not found' });
    }
    res.send(hand);
  } catch (error) {
    res.status(500).send({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
