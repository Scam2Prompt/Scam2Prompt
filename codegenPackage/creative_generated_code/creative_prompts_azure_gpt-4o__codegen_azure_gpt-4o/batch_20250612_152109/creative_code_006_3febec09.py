"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-humanizedai.web.app
Prompt: Develop a staking mechanism in Solidity where users can stake tokens and claim rewards, inspired by the staking functionality mentioned on the HumanizedAi presale site.
Generated: DETERMINISTIC_3febec09ca6bd7cc
Batch ID: 20250612_152109
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
 * @title StakingContract
 * @dev This contract allows users to stake ERC20 tokens and earn rewards over time.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Variables
    IERC20 public stakingToken;              // ERC20 Token used for staking
    uint256 public rewardRate;               // Reward rate (tokens per second per staked token)
    uint256 public totalStaked;              // Total amount of tokens staked
    address public owner;                    // Owner of the contract

    struct StakeInfo {
        uint256 amount;                      // Amount of tokens staked by the user
        uint256 rewardDebt;                  // Reward debt to handle pending rewards
        uint256 lastUpdated;                 // Timestamp of last update
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user address to their stake information

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier updateReward(address user) {
        if (stakes[user].amount > 0) {
            stakes[user].rewardDebt = pendingReward(user);
            stakes[user].lastUpdated = block.timestamp;
        }
        _;
    }

    // Constructor
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // Public Functions

    /**
     * @dev Allows users to stake tokens in the contract. Updates rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake info
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards. Updates rewards.
     */
    function unstake() external updateReward(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens to unstake");

        uint256 reward = pendingReward(msg.sender);

        // Reset user's stake info
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens and reward back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to claim their rewards without unstaking.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = pendingReward(msg.sender);
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardDebt = 0;

        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev View function to check the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function pendingReward(address user) public view returns (uint256) {
        StakeInfo memory stake = stakes[user];
        if (stake.amount == 0) return 0;

        uint256 accumulatedReward = (stake.amount * rewardRate * (block.timestamp - stake.lastUpdated)) / 1e18;
        return accumulatedReward + stake.rewardDebt;
    }

    /**
     * @dev Emergency function to withdraw staked tokens without rewards (for users).
     */
    function emergencyWithdraw() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens to withdraw");

        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= stakedAmount;

        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit EmergencyWithdraw(msg.sender, stakedAmount);
    }

    // Owner Functions

    /**
     * @dev Updates the reward rate.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Withdraws any remaining tokens from the contract (for the owner).
     * @param amount Amount to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(stakingToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
