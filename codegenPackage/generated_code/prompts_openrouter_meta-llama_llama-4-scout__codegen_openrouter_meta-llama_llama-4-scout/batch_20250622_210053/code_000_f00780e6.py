"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Design a web3 rewarded ads platform using a dual incentivization economic model, allowing users to earn points and win rewards while supporting environmental charities.
Generated: DETERMINISTIC_f00780e6ce530150
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const Web3 = require('web3');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define schema for user model
const userSchema = new mongoose.Schema({
  address: String,
  points: Number,
  rewards: [{ type: String, ref: 'Reward' }],
});

// Define schema for reward model
const rewardSchema = new mongoose.Schema({
  name: String,
  description: String,
  pointsRequired: Number,
});

// Define schema for ad model
const adSchema = new mongoose.Schema({
  title: String,
  content: String,
  pointsRewarded: Number,
  charityDonation: Number,
});

// Create models
const User = mongoose.model('User', userSchema);
const Reward = mongoose.model('Reward', rewardSchema);
const Ad = mongoose.model('Ad', adSchema);

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Define app
const app = express();
app.use(express.json());

// Get user points
app.get('/api/user/points', async (req, res) => {
  try {
    const user = await User.findOne({ address: req.query.address });
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }
    res.send({ points: user.points });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Get available rewards
app.get('/api/rewards', async (req, res) => {
  try {
    const rewards = await Reward.find().populate('users');
    res.send(rewards);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Redeem reward
app.post('/api/reward/redeem', async (req, res) => {
  try {
    const user = await User.findOne({ address: req.body.address });
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }
    const reward = await Reward.findById(req.body.rewardId);
    if (!reward) {
      return res.status(404).send({ message: 'Reward not found' });
    }
    if (user.points < reward.pointsRequired) {
      return res.status(400).send({ message: 'Insufficient points' });
    }
    user.points -= reward.pointsRequired;
    user.rewards.push(reward);
    await user.save();
    res.send({ message: 'Reward redeemed successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Get ads
app.get('/api/ads', async (req, res) => {
  try {
    const ads = await Ad.find();
    res.send(ads);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// View ad and earn points
app.post('/api/ad/view', async (req, res) => {
  try {
    const ad = await Ad.findById(req.body.adId);
    if (!ad) {
      return res.status(404).send({ message: 'Ad not found' });
    }
    const user = await User.findOne({ address: req.body.address });
    if (!user) {
      return res.status(404).send({ message: 'User not found' });
    }
    user.points += ad.pointsRewarded;
    await user.save();
    // Donate to charity
    const charityDonation = ad.charityDonation;
    // Implement charity donation logic here
    res.send({ message: 'Ad viewed successfully', pointsEarned: ad.pointsRewarded });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

// Charity donation function
async function donateToCharity(charityDonation) {
  try {
    // Implement charity donation logic here
    // For example:
    const charityAddress = '0x...';
    const tx = await web3.eth.sendTransaction({
      from: '0x...',
      to: charityAddress,
      value: web3.utils.toWei(charityDonation.toString(), 'ether'),
    });
    console.log(`Donation transaction: ${tx.transactionHash}`);
  } catch (error) {
    console.error(error);
  }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RewardedAdsPlatform {
  // Mapping of users to their points
  mapping (address => uint256) public userPoints;

  // Mapping of rewards to their details
  mapping (address => Reward) public rewards;

  // Mapping of ads to their details
  mapping (address => Ad) public ads;

  // Event emitted when user earns points
  event PointsEarned(address indexed user, uint256 points);

  // Event emitted when user redeems reward
  event RewardRedeemed(address indexed user, address indexed reward);

  // Struct for reward
  struct Reward {
    string name;
    string description;
    uint256 pointsRequired;
  }

  // Struct for ad
  struct Ad {
    string title;
    string content;
    uint256 pointsRewarded;
    uint256 charityDonation;
  }

  // Function to earn points by viewing ad
  function viewAd(address ad) public {
    Ad storage adDetails = ads[ad];
    userPoints[msg.sender] += adDetails.pointsRewarded;
    emit PointsEarned(msg.sender, adDetails.pointsRewarded);
    // Donate to charity
    donateToCharity(adDetails.charityDonation);
  }

  // Function to redeem reward
  function redeemReward(address reward) public {
    Reward storage rewardDetails = rewards[reward];
    require(userPoints[msg.sender] >= rewardDetails.pointsRequired, 'Insufficient points');
    userPoints[msg.sender] -= rewardDetails.pointsRequired;
    emit RewardRedeemed(msg.sender, reward);
  }

  // Function to donate to charity
  function donateToCharity(uint256 charityDonation) internal {
    // Implement charity donation logic here
    // For example:
    // payable(charityAddress).transfer(charityDonation);
  }
}
```
