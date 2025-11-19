"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtokencoin.pages.dev
Prompt: Explain how to implement a smart contract for staking $SMOG tokens on Ethereum to earn APY, based on the staking information provided by Smog Token.
Generated: DETERMINISTIC_d6ab554e20cb78f4
Batch ID: 20250612_161420
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
 * @title SMOGStaking
 * @dev A smart contract for staking SMOG tokens to earn an Annual Percentage Yield (APY).
 */
contract SMOGStaking {
    IERC20 public smogToken;  // Interface for the SMOG token
    uint256 public totalStaked; // Total amount of SMOG tokens staked
    uint256 public rewardRate;  // Reward rate for staking (APY in basis points, e.g., 10000 = 100%)
    
    struct Stake {
        uint256 amount;          // Amount of tokens staked by the user
        uint256 startTime;      // Timestamp when the user started staking
        uint256 rewards;        // Accumulated rewards
    }
    
    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake details
    mapping(address => uint256) public lastUpdated; // Last updated timestamp for rewards calculation

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the SMOG token address and the reward rate.
     * @param _smogToken Address of the SMOG token contract.
     * @param _rewardRate Reward rate in basis points.
     */
    constructor(address _smogToken, uint256 _rewardRate) {
        smogToken = IERC20(_smogToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake SMOG tokens to earn rewards.
     * @param amount The amount of SMOG tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(smogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp; // Update the start time
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake SMOG tokens and claim rewards.
     * @param amount The amount of SMOG tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 reward = calculateRewards(msg.sender);
        userStake.rewards += reward; // Accumulate rewards

        // Update the user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        require(smogToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards for the user.
     * @param user The address of the user.
     * @return The calculated reward amount.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 stakedDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * rewardRate * stakedDuration) / (365 days * 10000); // APY calculation

        return reward + userStake.rewards; // Return total rewards including previously accumulated
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewards = 0; // Reset rewards after claiming

        require(smogToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allow contract to receive Ether (if necessary).
     */
    receive() external payable {}
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
