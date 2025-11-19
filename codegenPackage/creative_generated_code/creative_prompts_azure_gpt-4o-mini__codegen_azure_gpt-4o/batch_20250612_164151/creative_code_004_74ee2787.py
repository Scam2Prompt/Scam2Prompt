"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-sale.pages.dev
Prompt: Develop a Solidity contract that allows users to stake their $PEPU tokens and receive rewards on the Pepe Unchained blockchain.
Generated: DETERMINISTIC_74ee27877327910f
Batch ID: 20250612_164151
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

/**
 * @title PepuStakingContract
 * @dev A contract that allows users to stake $PEPU tokens and receive rewards.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PepuStakingContract {
    // $PEPU token contract address
    IERC20 public pepuToken;

    // Reward rate (e.g., tokens rewarded per second staked)
    uint256 public rewardRate;

    // Record of staked balances and reward data for each user
    struct StakeInfo {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Rewards accrued but not yet withdrawn
        uint256 lastUpdated; // Last timestamp the stake was updated
    }

    // Mapping from user address to their stake information
    mapping(address => StakeInfo) public stakes;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event WithdrawnStake(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Constructor to initialize the contract
    constructor(address _pepuToken, uint256 _rewardRate) {
        require(_pepuToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        pepuToken = IERC20(_pepuToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Function accessible only to contract owner");
        _;
    }

    // Modifier to ensure a non-zero amount is provided
    modifier nonZero(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Function to calculate pending rewards for a user
    function _calculateReward(address user) internal view returns (uint256) {
        StakeInfo memory stake = stakes[user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 accruedTime = block.timestamp - stake.lastUpdated;
        uint256 reward = (stake.amount * rewardRate * accruedTime) / 1e18;
        return reward + stake.rewardDebt;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external nonZero(amount) {
        pepuToken.transferFrom(msg.sender, address(this), amount);

        StakeInfo storage stake = stakes[msg.sender];
        uint256 pendingRewards = _calculateReward(msg.sender);

        stake.amount += amount;
        stake.rewardDebt = pendingRewards;
        stake.lastUpdated = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens (without claiming rewards)
    function withdrawStake(uint256 amount) external nonZero(amount) {
        StakeInfo storage stake = stakes[msg.sender];
        require(stake.amount >= amount, "Insufficient staked balance");

        uint256 pendingRewards = _calculateReward(msg.sender);

        stake.amount -= amount;
        stake.rewardDebt = pendingRewards;
        stake.lastUpdated = block.timestamp;

        totalStaked -= amount;

        pepuToken.transfer(msg.sender, amount);
        emit WithdrawnStake(msg.sender, amount);
    }

    // Function to claim rewards only
    function claimRewards() external {
        StakeInfo storage stake = stakes[msg.sender];
        uint256 rewards = _calculateReward(msg.sender);
        require(rewards > 0, "No rewards available");

        stake.rewardDebt = 0;
        stake.lastUpdated = block.timestamp;

        pepuToken.transfer(msg.sender, rewards);
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to withdraw staked tokens and claim rewards simultaneously
    function exit() external {
        StakeInfo storage stake = stakes[msg.sender];
        uint256 rewards = _calculateReward(msg.sender);
        uint256 amount = stake.amount;

        require(amount > 0 || rewards > 0, "No staked tokens or rewards available");

        stake.amount = 0;
        stake.rewardDebt = 0;
        stake.lastUpdated = block.timestamp;

        totalStaked -= amount;

        if (amount > 0) {
            pepuToken.transfer(msg.sender, amount);
            emit WithdrawnStake(msg.sender, amount);
        }

        if (rewards > 0) {
            pepuToken.transfer(msg.sender, rewards);
            emit RewardClaimed(msg.sender, rewards);
        }
    }

    // Function to retrieve the total rewards of a user (including pending rewards)
    function totalRewards(address user) external view returns (uint256) {
        return _calculateReward(user);
    }

    // Function to retrieve the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
