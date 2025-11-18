"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdog-claim.pages.dev
Prompt: Create a function in Solidity that implements staking logic for $WAI tokens, including calculating rewards based on APY.
Generated: DETERMINISTIC_bccf0d7cc5b968c2
Batch ID: 20250612_151117
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
 * @title Staking Contract for $WAI Token
 * @dev Implements staking mechanism with reward calculation based on APY
 */
contract WAIStaking {
    IERC20 public immutable waiToken; // Reference to the $WAI token contract
    uint256 public immutable apy; // Annual Percentage Yield (APY) for reward calculation (e.g., 5% APY = 500)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 reward; // Accumulated rewards for the stake
    }

    mapping(address => Stake) public stakes; // Mapping of stakes by user address

    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $WAI token and APY
     * @param _waiToken Address of the $WAI token contract
     * @param _apy Annual Percentage Yield (multiplied by 100, e.g., 5% APY = 500)
     */
    constructor(IERC20 _waiToken, uint256 _apy) {
        require(address(_waiToken) != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        waiToken = _waiToken;
        apy = _apy;
    }

    /**
     * @dev Stake $WAI tokens in the contract
     * @param amount Amount of $WAI tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the user to the contract
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate rewards for any existing stake
        _updateRewards(msg.sender);

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 reward = userStake.reward;
        require(reward > 0, "No rewards available");

        userStake.reward = 0; // Reset rewards to zero

        // Transfer rewards to the user
        require(waiToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 amountToUnstake = userStake.amount;
        uint256 reward = userStake.reward;

        require(amountToUnstake > 0, "No tokens staked");

        // Reset user's stake
        userStake.amount = 0;
        userStake.reward = 0;

        // Transfer staked tokens and rewards to the user
        require(waiToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        if (reward > 0) {
            require(waiToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Internal function to update rewards based on APY
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return;
        }

        // Calculate time difference in seconds
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate rewards based on APY formula
        // rewards = (staked amount * APY * time elapsed in seconds) / (365 days * 10000)
        uint256 reward = (userStake.amount * apy * stakingDuration) / (365 days * 10000);

        userStake.reward += reward;
        userStake.startTime = block.timestamp; // Reset startTime for the next reward calculation
    }
}

/**
 * @dev Basic interface for ERC20 token
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
