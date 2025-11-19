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

Here’s a clean, well-documented Solidity smart contract implementing the requested functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DOGE20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn rewards distributed over two years.
 */
contract DOGE20Staking {
    // Importing SafeMath to perform safe arithmetic operations.
    using SafeMath for uint256;

    // ERC20 token interface
    IERC20 public doge20Token;

    // Duration of staking rewards (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60; // Two years

    // Total reward pool allocated for the entire staking duration
    uint256 public totalRewardPool;

    // Mapping to track staked amounts and timestamps for users
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public stakingStartTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the DOGE20 token contract.
     * @param _totalRewardPool Total token rewards allocated for staking.
     */
    constructor(IERC20 _token, uint256 _totalRewardPool) {
        require(_totalRewardPool > 0, "Reward pool must be greater than zero");
        doge20Token = _token;
        totalRewardPool = _totalRewardPool;
    }

    /**
     * @dev Function to allow users to stake DOGE20 tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer DOGE20 tokens from the user's wallet to the contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked amount and staking start time
        stakedAmount[msg.sender] = stakedAmount[msg.sender].add(_amount);
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        uint256 amountStaked = stakedAmount[msg.sender];
        require(amountStaked > 0, "No tokens staked");

        // Calculate rewards based on staking duration
        uint256 stakingDuration = block.timestamp.sub(stakingStartTime[msg.sender]);
        uint256 reward = calculateReward(amountStaked, stakingDuration);

        // Reset user's staking data
        stakedAmount[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Transfer staked tokens and rewards back to the user
        require(
            doge20Token.transfer(msg.sender, amountStaked.add(reward)),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, amountStaked, reward);
    }

    /**
     * @dev Internal function to calculate rewards based on staking duration.
     * @param _amountStaked The amount of tokens staked.
     * @param _duration The duration the tokens have been staked for.
     * @return The calculated reward.
     */
    function calculateReward(uint256 _amountStaked, uint256 _duration)
        internal
        view
        returns (uint256)
    {
        if (_duration > REWARD_DURATION) {
            _duration = REWARD_DURATION; // Max reward duration is 2 years
        }

        // Calculate reward proportionally based on duration and the total reward pool
        uint256 reward = _amountStaked.mul(_duration).mul(totalRewardPool).div(REWARD_DURATION);
        return reward;
    }
}

// OpenZeppelin's SafeMath library for safe arithmetic operations.
// SafeMath is deprecated in Solidity >=0.8 but included here for demonstration.
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction underflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) return 0;
        uint256 c = a * b;
        require(c / a == b, "Multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "Division by zero");
        return a / b;
    }
}

// ERC20 interface (Simplified for demonstration purposes)
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code implements a staking smart contract for DOGE20 tokens, including reward distribution over two years. It calculates proportional rewards based on stake duration and handles staking, withdrawal, and reward calculation.
