"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to the stakers' pool share over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_c5f9c2f653c25906
Batch ID: 20250612_152710
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
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and receive rewards proportionally
 * to their share in the staking pool over a two-year period. The rewards are distributed
 * by the contract owner periodically.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Duration of the staking rewards distribution (2 years in seconds)
    uint256 public constant REWARD_PERIOD = 2 * 365 * 24 * 60 * 60;

    // Start and end timestamps of the staking rewards
    uint256 public immutable startTime;
    uint256 public immutable endTime;

    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Reward pool allocated by the contract owner
    uint256 public immutable rewardPool;

    // Mapping from staker address to staked amount
    mapping(address => uint256) public stakedAmounts;

    // Mapping from staker address to their reward debt
    mapping(address => uint256) public rewardDebts;

    // Events for staking, withdrawing, and claiming rewards
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);

    // Modifier to ensure staking is only active within the reward period
    modifier onlyDuringRewardPeriod() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Staking is not active");
        _;
    }

    // Modifier to ensure function is called outside the reward period
    modifier onlyAfterRewardPeriod() {
        require(block.timestamp > endTime, "Reward period not ended");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardPool Total reward tokens allocated by the contract owner.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        doge20Token = _doge20Token;
        rewardPool = _rewardPool;
        startTime = block.timestamp;
        endTime = block.timestamp + REWARD_PERIOD;
    }

    /**
     * @dev Function to allow users to stake DOGE20 tokens.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external onlyDuringRewardPeriod {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer DOGE20 tokens from the sender to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the staker's staked amount and total staked amount
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to withdraw their staked tokens.
     * @param amount Amount of DOGE20 tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staker's staked amount and total staked amount
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens from the contract to the sender
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to claim their proportional rewards.
     */
    function claimRewards() external onlyAfterRewardPeriod {
        require(stakedAmounts[msg.sender] > 0, "No staked tokens");

        // Calculate the user's share of the reward pool
        uint256 userReward = (rewardPool * stakedAmounts[msg.sender]) / totalStaked;

        // Ensure rewards are not double-claimed
        require(rewardDebts[msg.sender] == 0, "Rewards already claimed");

        // Update reward debt to prevent re-claiming
        rewardDebts[msg.sender] = userReward;

        // Transfer the user's reward tokens
        require(doge20Token.transfer(msg.sender, userReward), "Token transfer failed");

        // Emit reward claim event
        emit RewardClaimed(msg.sender, userReward);
    }
}
```
