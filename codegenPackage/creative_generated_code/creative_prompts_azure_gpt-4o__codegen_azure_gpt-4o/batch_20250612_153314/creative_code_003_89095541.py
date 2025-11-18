"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasclub.xyz
Prompt: Create a smart contract in Solidity for managing FEG token staking on Binance Smart Chain, considering the transition details discussed.
Generated: DETERMINISTIC_89095541cb61ee25
Batch ID: 20250612_153314
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
 * @title FEG Token Staking Contract
 * @dev This contract allows users to stake FEG tokens and earn rewards.
 * It supports staking, withdrawing, and viewing the staking balance.
 */
contract FEGTokenStaking {
    // FEG token contract address
    address public immutable tokenAddress;

    // Reward rate (example: 5% annualized reward rate)
    uint256 public constant REWARD_RATE = 500; // Basis points (5%)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Track user staked balances and their last staking timestamp
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private lastStakedTimestamp;

    // Total staked balance in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to check if the caller has staked tokens
    modifier hasStake(address user) {
        require(stakedBalances[user] > 0, "No staked tokens found");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract with the token address.
     * @param _tokenAddress The address of the FEG token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Stake FEG tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the caller to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Calculate rewards if user has previously staked
        if (stakedBalances[msg.sender] > 0) {
            uint256 reward = calculateReward(msg.sender);
            if (reward > 0) {
                IERC20(tokenAddress).transfer(msg.sender, reward);
                emit RewardClaimed(msg.sender, reward);
            }
        }

        // Update staking balance and timestamp
        stakedBalances[msg.sender] += amount;
        lastStakedTimestamp[msg.sender] = block.timestamp;
        
        // Update total staked balance
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards.
     */
    function withdraw() external hasStake(msg.sender) {
        uint256 userBalance = stakedBalances[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        // Reset user's staking balance and timestamp
        stakedBalances[msg.sender] = 0;
        lastStakedTimestamp[msg.sender] = 0;

        // Update total staked balance
        totalStaked -= userBalance;

        // Transfer staked tokens and rewards to the caller
        IERC20(tokenAddress).transfer(msg.sender, userBalance + reward);

        emit Withdrawn(msg.sender, userBalance);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a user based on their staked balance and duration.
     * @param user The address of the user.
     * @return The reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 duration = block.timestamp - lastStakedTimestamp[user];
        uint256 reward = (stakedBalances[user] * REWARD_RATE * duration) / (SECONDS_IN_YEAR * 10000);
        return reward;
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function stakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
