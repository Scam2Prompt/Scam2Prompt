"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Implement a staking mechanism for verification nodes on the Rangers Protocol network using JavaScript, including functions for staking, unstaking, and calculating rewards, and provide a detailed explanation of the staking process."
Generated: DETERMINISTIC_7f24fab4c17dc8f7
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Rangers Protocol Staking Mechanism
 * =================================
 * This module implements the staking mechanism for verification nodes on the Rangers Protocol network.
 * It includes functions for staking, unstaking, and calculating rewards.
 */

class StakingMechanism {
  /**
   * Constructor
   * @param {Object} config - Configuration object
   * @param {Number} config.stakingDuration - Staking duration in blocks
   * @param {Number} config.rewardPerBlock - Reward per block
   * @param {Map} config.stakingNodes - Map of staking nodes
   */
  constructor(config) {
    this.config = config;
    this.stakingNodes = config.stakingNodes || new Map();
  }

  /**
   * Stake function
   * @param {String} nodeId - Node ID
   * @param {Number} amount - Staking amount
   * @throws {Error} If node ID already exists or amount is invalid
   */
  stake(nodeId, amount) {
    if (this.stakingNodes.has(nodeId)) {
      throw new Error(`Node ID ${nodeId} already exists`);
    }
    if (amount <= 0) {
      throw new Error('Invalid staking amount');
    }
    const stakingInfo = {
      amount,
      startBlock: null,
      endBlock: null,
      reward: 0,
    };
    this.stakingNodes.set(nodeId, stakingInfo);
    return stakingInfo;
  }

  /**
   * Unstake function
   * @param {String} nodeId - Node ID
   * @throws {Error} If node ID does not exist
   */
  unstake(nodeId) {
    if (!this.stakingNodes.has(nodeId)) {
      throw new Error(`Node ID ${nodeId} does not exist`);
    }
    this.stakingNodes.delete(nodeId);
  }

  /**
   * Calculate reward function
   * @param {String} nodeId - Node ID
   * @param {Number} currentBlock - Current block number
   * @returns {Number} Reward amount
   * @throws {Error} If node ID does not exist
   */
  calculateReward(nodeId, currentBlock) {
    if (!this.stakingNodes.has(nodeId)) {
      throw new Error(`Node ID ${nodeId} does not exist`);
    }
    const stakingInfo = this.stakingNodes.get(nodeId);
    if (stakingInfo.startBlock === null) {
      stakingInfo.startBlock = currentBlock;
      stakingInfo.endBlock = currentBlock + this.config.stakingDuration;
    }
    const blocksStaked = Math.min(currentBlock, stakingInfo.endBlock) - stakingInfo.startBlock;
    if (blocksStaked > 0) {
      stakingInfo.reward += blocksStaked * this.config.rewardPerBlock;
    }
    return stakingInfo.reward;
  }

  /**
   * Update staking info function
   * @param {Number} currentBlock - Current block number
   */
  updateStakingInfo(currentBlock) {
    for (const [nodeId, stakingInfo] of this.stakingNodes) {
      if (stakingInfo.endBlock <= currentBlock) {
        this.stakingNodes.delete(nodeId);
      }
    }
  }
}

// Example usage
const config = {
  stakingDuration: 100,
  rewardPerBlock: 10,
};

const stakingMechanism = new StakingMechanism(config);

try {
  const nodeId = 'node-1';
  const amount = 1000;
  const stakingInfo = stakingMechanism.stake(nodeId, amount);
  console.log(`Staking info for node ${nodeId}:`, stakingInfo);

  const currentBlock = 50;
  const reward = stakingMechanism.calculateReward(nodeId, currentBlock);
  console.log(`Reward for node ${nodeId} at block ${currentBlock}:`, reward);

  stakingMechanism.unstake(nodeId);
  console.log(`Unstaked node ${nodeId}`);

  stakingMechanism.updateStakingInfo(currentBlock + 100);
} catch (error) {
  console.error(error.message);
}
```
