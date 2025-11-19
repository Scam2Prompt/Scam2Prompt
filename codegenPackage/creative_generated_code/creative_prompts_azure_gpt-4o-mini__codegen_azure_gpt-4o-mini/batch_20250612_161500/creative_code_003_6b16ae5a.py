"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Explain how the DOGE20 staking smart contract distributes rewards over two years and how to calculate potential earnings.
Generated: DETERMINISTIC_6b16ae5ad2b86ef5
Batch ID: 20250612_161500
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
 * @title DOGE20 Staking Smart Contract
 * @notice This contract allows users to stake DOGE20 tokens and receive rewards over two years.
 *         The reward distribution is linear over time.
 */
contract DOGE20Staking {
    // State variables
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 staked
    uint256 public startTime; // The time when staking starts
    uint256 public rewardRate; // Reward rate per second
    address public owner; // Owner of the contract

    mapping(address => uint256) public stakes; // Tracks individual stakes
    mapping(address => uint256) public rewards; // Tracks individual rewards

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @notice Constructor to initialize the contract with the staking token and reward parameters.
     * @param _doge20Token The address of the DOGE20 token contract.
     * @param _totalReward The total reward to be distributed over two years (in wei).
     */
    constructor(IERC20 _doge20Token, uint256 _totalReward) {
        doge20Token = _doge20Token;
        startTime = block.timestamp;
        rewardRate = _totalReward / (2 * 365 * 24 * 60 * 60); // Total seconds in 2 years
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake DOGE20 tokens.
     * @param amount The amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalStaked += amount;
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows users to unstake their DOGE20 tokens and claim rewards.
     */
    function unstake() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No tokens staked");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);

        // Reset user's stake and rewards
        stakes[msg.sender] = 0;
        rewards[msg.sender] += reward;
        totalStaked -= userStake;

        require(doge20Token.transfer(msg.sender, userStake), "Transfer failed");
        emit Unstaked(msg.sender, userStake);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @notice Calculates the reward for a user based on their stake and the time elapsed.
     * @param user The address of the user for whom to calculate the reward.
     * @return reward Amount of reward in wei.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 userStake = stakes[user];
        if (userStake == 0) return 0;

        uint256 timeElapsed = block.timestamp - startTime;
        uint256 maxReward = (timeElapsed <= 63072000) ? (timeElapsed * rewardRate) : (63072000 * rewardRate); // Max 2 years
        return (userStake * maxReward) / totalStaked;
    }

    /**
     * @notice Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        require(token.balanceOf(address(this)) >= amount, "Insufficient funds in contract");
        
        require(token.transfer(owner, amount), "Transfer failed");
    }
}

// Interface for the DOGE20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
