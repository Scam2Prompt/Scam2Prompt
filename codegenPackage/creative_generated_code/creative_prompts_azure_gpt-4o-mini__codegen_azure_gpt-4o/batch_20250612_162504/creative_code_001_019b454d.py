"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-i.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that allows users to earn passive rewards based on their stake.
Generated: DETERMINISTIC_019b454d6d1bab46
Batch ID: 20250612_162504
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
 * @notice This smart contract allows users to stake DOGE20 tokens and earn passive rewards.
 * @dev This contract assumes an ERC-20 compatible DOGE20 token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Address of the ERC-20 DOGE20 token contract
    IERC20 public immutable dogeToken;

    // Data structure to store stake details for each user
    struct Stake {
        uint256 amount; // Amount of staked tokens
        uint256 timestamp; // Timestamp when tokens were staked
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 10 tokens per day, equivalent to 10/86400 tokens per second)
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the token address and reward rate.
     * @param _dogeToken Address of the DOGE20 token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _dogeToken, uint256 _rewardRate) {
        require(address(_dogeToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        dogeToken = _dogeToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to check if the sender has an active stake.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _;
    }

    /**
     * @dev Allows a user to stake DOGE20 tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = dogeToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // If user already has a stake, calculate and store rewards before updating the stake
        if (stakes[msg.sender].amount > 0) {
            uint256 reward = calculateReward(msg.sender);
            stakes[msg.sender].amount += reward;
        }

        // Update stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake {
        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Get staked amount
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked tokens and reward to the user
        bool successStaked = dogeToken.transfer(msg.sender, stakedAmount);
        require(successStaked, "Token transfer failed");

        if (reward > 0) {
            bool successReward = dogeToken.transfer(msg.sender, reward);
            require(successReward, "Reward transfer failed");
        }

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculates the reward for the user based on their stake and time duration.
     * @param user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0 || userStake.timestamp == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / 1e18;

        return reward;
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * This function is for rescue purposes only and should not affect staked tokens.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function rescueTokens(address token, uint256 amount) external {
        require(token != address(dogeToken), "Cannot rescue staked tokens");
        bool success = IERC20(token).transfer(msg.sender, amount);
        require(success, "Rescue transfer failed");
    }
}
```
