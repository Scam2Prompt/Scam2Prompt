"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Generate code to create a staking smart contract on Binance Smart Chain (BSC) that mimics the staking rewards system described for OMEME, including dynamic reward percentages.
Generated: DETERMINISTIC_cafee6d038e58116
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the staking smart contract code for Binance Smart Chain (BSC) with dynamic reward percentages implemented in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Staking Contract for Dynamic Rewards
 * @dev Allows users to stake tokens and receive rewards based on dynamic percentages
 */
contract OMEMEStaking {
    // Token interface for interacting with the staking token (BEP-20 compliant)
    interface IBEP20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IBEP20 public stakingToken; // The token users will stake
    address public owner;       // Contract owner

    struct Stake {
        uint256 amount;          // Amount staked by the user
        uint256 rewardDebt;      // Reward debt to calculate pending rewards
        uint256 lastStakeTime;   // Timestamp of the last stake or reward update
    }

    mapping(address => Stake) public stakes;   // Staking data per user
    uint256 public totalStaked;                // Total amount of tokens staked
    uint256 public rewardPercentage;           // Current reward percentage (dynamic)
    uint256 public constant REWARD_INTERVAL = 30 days; // Reward calculation interval
    uint256 public constant MAX_REWARD_PERCENTAGE = 20; // Maximum reward percentage (20%)

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event RewardPercentageUpdated(uint256 newPercentage);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(address _stakingToken) {
        stakingToken = IBEP20(_stakingToken);
        owner = msg.sender;
        rewardPercentage = 5; // Set initial reward percentage to 5%
    }

    /**
     * @notice Users stake tokens in the contract
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Calculate any pending rewards before updating the stake
        _updateRewards(msg.sender);

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastStakeTime = block.timestamp;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Users unstake tokens from the contract
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(amount > 0 && amount <= userStake.amount, "Invalid unstake amount");

        // Calculate and claim any pending rewards
        _updateRewards(msg.sender);
        uint256 pendingRewards = _calculateRewards(msg.sender);
        if (pendingRewards > 0) {
            stakingToken.transfer(msg.sender, pendingRewards);
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        // Update the user's stake
        userStake.amount -= amount;
        if (userStake.amount == 0) {
            userStake.rewardDebt = 0;
        }
        userStake.lastStakeTime = block.timestamp;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Update total staked tokens
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Users can claim their pending rewards
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 pendingRewards = _calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available");

        stakes[msg.sender].rewardDebt += pendingRewards;
        stakingToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Update reward percentage by the owner
     * @param newPercentage The new reward percentage
     */
    function updateRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= MAX_REWARD_PERCENTAGE, "Exceeds max reward percentage");
        rewardPercentage = newPercentage;

        emit RewardPercentageUpdated(newPercentage);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user
     * @param user The address of the user
     * @return The pending rewards
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0 || userStake.lastStakeTime == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.lastStakeTime;
        uint256 reward = (userStake.amount * rewardPercentage * stakingDuration) / (100 * REWARD_INTERVAL);

        return reward - userStake.rewardDebt;
    }

    /**
     * @dev Internal function to update the rewards for a user
     * @param user The address of the user
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 pendingRewards = _calculateRewards(user);
            userStake.rewardDebt += pendingRewards;
            userStake.lastStakeTime = block.timestamp;
        }
    }

    /**
     * @notice Get the pending rewards for a user
     * @param user The address of the user
     * @return The pending rewards
     */
    function getPendingRewards(address user) external view returns (uint256) {
        return _calculateRewards(user);
    }

    /**
     * @notice Emergency withdrawal of all tokens by the owner
     * @dev This function is meant to be used in case of critical issues
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = stakingToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        stakingToken.transfer(owner, contractBalance);
    }
}
```
