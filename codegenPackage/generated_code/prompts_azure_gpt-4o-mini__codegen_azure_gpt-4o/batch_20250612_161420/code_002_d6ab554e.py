"""
Generated Code Metadata:
========================
Original URL: https://smogtokencoin.pages.dev
Prompt: Explain how to implement a smart contract for staking $SMOG tokens on Ethereum to earn APY, based on the staking information provided by Smog Token.
Generated: DETERMINISTIC_d6ab554e20cb78f4
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SMOGTokenStaking
 * @dev A smart contract for staking SMOG tokens to earn APY rewards.
 * Users can deposit SMOG tokens, earn rewards based on APY, and withdraw their stake and rewards.
 */
contract SMOGTokenStaking {
    // ERC20 interface for SMOG token
    IERC20 public smogToken;

    // APY percentage (e.g., 10% APY = 10)
    uint256 public apy;

    // Duration for APY calculation (in seconds)
    uint256 public apyDuration = 365 days;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Mapping to track user reward balances
    mapping(address => uint256) public rewards;

    // Mapping to track the last staking timestamp for each user
    mapping(address => uint256) public lastStakedTimestamp;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens and rewards
    event Withdrawn(address indexed user, uint256 stakeAmount, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the contract with the SMOG token address and APY.
     * @param _smogToken Address of the SMOG token contract.
     * @param _apy Annual Percentage Yield (APY) for staking rewards.
     */
    constructor(IERC20 _smogToken, uint256 _apy) {
        require(address(_smogToken) != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        smogToken = _smogToken;
        apy = _apy;
    }

    /**
     * @dev Stake SMOG tokens to earn rewards.
     * @param amount Amount of SMOG tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer SMOG tokens from the user to the contract
        require(smogToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake and last staked timestamp
        stakes[msg.sender] += amount;
        lastStakedTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and earned rewards.
     */
    function withdraw() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No stake to withdraw");

        // Update rewards for the user before withdrawing
        _updateRewards(msg.sender);

        uint256 userReward = rewards[msg.sender];

        // Reset user's stake and rewards
        stakes[msg.sender] = 0;
        rewards[msg.sender] = 0;

        // Transfer staked tokens and rewards to the user
        require(smogToken.transfer(msg.sender, userStake + userReward), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake, userReward);
    }

    /**
     * @dev Internal function to update rewards for a user based on their stake and APY.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 userStake = stakes[user];
        if (userStake > 0) {
            uint256 timeElapsed = block.timestamp - lastStakedTimestamp[user];
            uint256 reward = (userStake * apy * timeElapsed) / (100 * apyDuration);
            rewards[user] += reward;
            lastStakedTimestamp[user] = block.timestamp;
        }
    }

    /**
     * @dev Get the total rewards earned by a user.
     * @param user Address of the user.
     * @return Total rewards earned by the user.
     */
    function getRewards(address user) external view returns (uint256) {
        uint256 userStake = stakes[user];
        if (userStake > 0) {
            uint256 timeElapsed = block.timestamp - lastStakedTimestamp[user];
            uint256 reward = (userStake * apy * timeElapsed) / (100 * apyDuration);
            return rewards[user] + reward;
        }
        return rewards[user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
