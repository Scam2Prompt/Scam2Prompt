"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Develop a REST API endpoint in Node.js that retrieves and calculates a user's claimable $SCOTTY rewards based on their staked balance and percentage of the staking pool.
Generated: DETERMINISTIC_69b1bd2b23b5632a
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Middleware to parse JSON
app.use(bodyParser.json());

// Mock database for users and staking pool
const users = {
  user1: { stakedBalance: 100 }, // Example user data
  user2: { stakedBalance: 50 },
};

const stakingPool = {
  totalStaked: 5000, // Total staked amount in the pool
  rewardPool: 1000, // Total rewards available for distribution
};

// Utility function to calculate rewards
function calculateRewards(stakedBalance, totalStaked, rewardPool) {
  if (totalStaked === 0) return 0; // Avoid division by zero
  return (stakedBalance / totalStaked) * rewardPool;
}

// REST API endpoint to retrieve claimable rewards
app.get('/api/rewards/:username', (req, res) => {
  const { username } = req.params;

  try {
    // Check if the user exists
    const user = users[username];
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Calculate claimable rewards
    const claimableRewards = calculateRewards(
      user.stakedBalance,
      stakingPool.totalStaked,
      stakingPool.rewardPool
    );

    // Respond with calculated rewards
    return res.status(200).json({
      username,
      stakedBalance: user.stakedBalance,
      claimableRewards,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error calculating rewards:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
