"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a tier-based staking system for ArbiPad, incorporating the tier system details and user protection policy from the Good Games Guild documentation.
Generated: DETERMINISTIC_f43f64cc6a20018e
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// staking-system.js

/**
 * Tier-based staking system for ArbiPad.
 * 
 * This system is designed based on the Good Games Guild documentation.
 * It includes a tier system and user protection policy.
 */

// Import required libraries
const Web3 = require('web3');
const { Tier, User } = require('./models');

/**
 * Staking System class.
 */
class StakingSystem {
  /**
   * Constructor.
   * 
   * @param {Object} config - Configuration object.
   * @param {string} config.contractAddress - Contract address.
   * @param {string} config.provider - Provider URL.
   */
  constructor(config) {
    this.config = config;
    this.web3 = new Web3(config.provider);
    this.contract = new this.web3.eth.Contract(abi, config.contractAddress);
  }

  /**
   * Get tier details.
   * 
   * @param {number} tierId - Tier ID.
   * @returns {Promise<Tier>} Tier details.
   */
  async getTier(tierId) {
    try {
      const tier = await this.contract.methods.getTier(tierId).call();
      return new Tier(tier);
    } catch (error) {
      throw new Error(`Failed to get tier: ${error.message}`);
    }
  }

  /**
   * Get user staking details.
   * 
   * @param {string} userAddress - User address.
   * @returns {Promise<User>} User staking details.
   */
  async getUserStakingDetails(userAddress) {
    try {
      const userStakingDetails = await this.contract.methods.getUserStakingDetails(userAddress).call();
      return new User(userStakingDetails);
    } catch (error) {
      throw new Error(`Failed to get user staking details: ${error.message}`);
    }
  }

  /**
   * Stake tokens.
   * 
   * @param {string} userAddress - User address.
   * @param {number} tierId - Tier ID.
   * @param {number} amount - Amount to stake.
   * @returns {Promise<string>} Transaction hash.
   */
  async stake(userAddress, tierId, amount) {
    try {
      const userStakingDetails = await this.getUserStakingDetails(userAddress);
      const tier = await this.getTier(tierId);

      // Check if user has sufficient balance.
      if (userStakingDetails.balance < amount) {
        throw new Error('Insufficient balance');
      }

      // Check if user has met the tier requirements.
      if (userStakingDetails.stakeAmount < tier.requirements.stakeAmount) {
        throw new Error('User has not met the tier requirements');
      }

      // Perform stake.
      const tx = await this.contract.methods.stake(tierId, amount).send({ from: userAddress });
      return tx.transactionHash;
    } catch (error) {
      throw new Error(`Failed to stake: ${error.message}`);
    }
  }

  /**
   * Unstake tokens.
   * 
   * @param {string} userAddress - User address.
   * @param {number} amount - Amount to unstake.
   * @returns {Promise<string>} Transaction hash.
   */
  async unstake(userAddress, amount) {
    try {
      const userStakingDetails = await this.getUserStakingDetails(userAddress);

      // Check if user has sufficient stake amount.
      if (userStakingDetails.stakeAmount < amount) {
        throw new Error('Insufficient stake amount');
      }

      // Perform unstake.
      const tx = await this.contract.methods.unstake(amount).send({ from: userAddress });
      return tx.transactionHash;
    } catch (error) {
      throw new Error(`Failed to unstake: ${error.message}`);
    }
  }
}

// Export StakingSystem class.
module.exports = StakingSystem;
```

```javascript
// models.js

/**
 * Tier model.
 */
class Tier {
  /**
   * Constructor.
   * 
   * @param {Object} data - Tier data.
   */
  constructor(data) {
    this.id = data.id;
    this.requirements = data.requirements;
    this.rewards = data.rewards;
  }
}

/**
 * User model.
 */
class User {
  /**
   * Constructor.
   * 
   * @param {Object} data - User data.
   */
  constructor(data) {
    this.address = data.address;
    this.balance = data.balance;
    this.stakeAmount = data.stakeAmount;
  }
}

// Export Tier and User models.
module.exports = { Tier, User };
```

```javascript
// abi.js

// ArbiPad staking contract ABI.
const abi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_tierId",
        "type": "uint256"
      }
    ],
    "name": "getTier",
    "outputs": [
      {
        "internalType": "tuple",
        "name": "",
        "type": "tuple",
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "tuple",
            "name": "requirements",
            "type": "tuple",
            "components": [
              {
                "internalType": "uint256",
                "name": "stakeAmount",
                "type": "uint256"
              }
            ]
          },
          {
            "internalType": "tuple",
            "name": "rewards",
            "type": "tuple",
            "components": [
              {
                "internalType": "uint256",
                "name": "rewardAmount",
                "type": "uint256"
              }
            ]
          }
        ]
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserStakingDetails",
    "outputs": [
      {
        "internalType": "tuple",
        "name": "",
        "type": "tuple",
        "components": [
          {
            "internalType": "address",
            "name": "address",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "balance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "stakeAmount",
            "type": "uint256"
          }
        ]
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_tierId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "stake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "unstake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Export ABI.
module.exports = abi;
```
