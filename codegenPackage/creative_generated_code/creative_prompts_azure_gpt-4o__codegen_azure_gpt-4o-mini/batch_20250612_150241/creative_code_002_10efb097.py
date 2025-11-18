"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Provide an example of a smart contract in Solidity that enables staking $99BTC tokens and distributes rewards on every Ethereum block, as outlined in the 99Bitcoins staking functionality.
Generated: DETERMINISTIC_10efb097e5975f15
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC20 interface for interacting with the $99BTC token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart Contract for Staking $99BTC and distributing rewards
contract BTCStaking is Ownable {
    // Declare variables for the $99BTC token and reward rate
    IERC20 public btcToken;
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount staked
    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewards; // User rewards
    mapping(address => uint256) public lastRewardBlock; // Last block user claimed rewards

    // Event for Staking
    event Staked(address indexed user, uint256 amount);
    // Event for Unstaking
    event Unstaked(address indexed user, uint256 amount);
    // Event for Reward Distribution
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _btcToken, uint256 _rewardRate) {
        btcToken = _btcToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $99BTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(btcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stakes and total
        stakes[msg.sender] += amount;
        totalStaked += amount;
        lastRewardBlock[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $99BTC tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Distribute rewards before unstaking
        distributeRewards(msg.sender);

        // Update stakes and total
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        require(btcToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        distributeRewards(msg.sender);
    }

    // Internal function to calculate and distribute rewards
    function distributeRewards(address user) internal {
        // Calculate the number of blocks since the last reward was claimed
        uint256 blocks = block.number - lastRewardBlock[user];
        if (blocks > 0) {
            uint256 reward = blocks * rewardRate * stakes[user] / totalStaked;
            rewards[user] += reward;
            lastRewardBlock[user] = block.number;
        }

        // Transfer the rewards to the user
        if (rewards[user] > 0) {
            require(btcToken.transfer(user, rewards[user]), "Reward transfer failed");
            emit RewardClaimed(user, rewards[user]);
            rewards[user] = 0; // Reset user reward after claiming
        }
    }

    // Function to view the staked amount of a user
    function viewStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to view the accumulated rewards of a user
    function viewRewards(address user) external view returns (uint256) {
        uint256 blocks = block.number - lastRewardBlock[user];
        uint256 pendingReward = blocks * rewardRate * stakes[user] / totalStaked;
        return rewards[user] + pendingReward;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
