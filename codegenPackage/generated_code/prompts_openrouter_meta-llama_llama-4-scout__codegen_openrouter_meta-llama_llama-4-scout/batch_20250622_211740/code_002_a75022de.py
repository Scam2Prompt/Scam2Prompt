"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.live
Prompt: Generate a RESTful API endpoint in Node.js for handling sports betting transactions, including bonus calculations and cashback rewards, inspired by BaxBet's loyalty programs.
Generated: DETERMINISTIC_a75022de1106af63
Batch ID: 20250622_211740
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
const { ObjectId } = mongoose.Schema;

// Connect to MongoDB
mongoose.connect('mongodb://localhost/baxbet', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for User model
const userSchema = new mongoose.Schema({
  id: String,
  balance: Number,
  loyaltyPoints: Number,
  bets: [{ type: ObjectId, ref: 'Bet' }]
});

// Define schema for Bet model
const betSchema = new mongoose.Schema({
  id: String,
  userId: { type: ObjectId, ref: 'User' },
  amount: Number,
  outcome: String,
  bonus: Number
});

// Create models
const User = mongoose.model('User', userSchema);
const Bet = mongoose.model('Bet', betSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Endpoint to place a bet
app.post('/bets', async (req, res) => {
  try {
    const { userId, amount, outcome } = req.body;
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }

    // Calculate bonus
    const bonus = calculateBonus(amount);

    // Create new bet
    const bet = new Bet({ userId, amount, outcome, bonus });
    await bet.save();

    // Update user's balance and loyalty points
    user.balance -= amount;
    user.loyaltyPoints += bonus;
    await user.save();

    res.send({ message: 'Bet placed successfully', bet });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Endpoint to calculate cashback rewards
app.get('/cashback/:userId', async (req, res) => {
  try {
    const userId = req.params.userId;
    const user = await User.findById(userId).populate('bets');
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }

    // Calculate cashback
    const cashback = calculateCashback(user.bets);

    res.send({ cashback });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Helper function to calculate bonus
function calculateBonus(amount) {
  // Bonus calculation logic (example: 10% bonus for bets over $100)
  if (amount > 100) {
    return amount * 0.1;
  }
  return 0;
}

// Helper function to calculate cashback
function calculateCashback(bets) {
  // Cashback calculation logic (example: 5% cashback for lost bets)
  const lostBets = bets.filter(bet => bet.outcome === 'lost');
  const totalLostAmount = lostBets.reduce((acc, bet) => acc + bet.amount, 0);
  return totalLostAmount * 0.05;
}

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
