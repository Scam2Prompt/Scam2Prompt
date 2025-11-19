"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-corn.com
Prompt: Write a code snippet that demonstrates how to implement staking for Crypto Corn tokens in a smart contract.
Generated: DETERMINISTIC_3e45be85035397bf
Batch ID: 20250612_161441
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
 * @title CryptoCornStaking
 * @dev Implements staking functionality for Crypto Corn tokens. Users can stake tokens and earn rewards.
 */
contract CryptoCornStaking {
    // Token contract interface
    IERC20 public cryptoCornToken;

    // Reward rate (e.g., 1% per block)
    uint256 public rewardRatePerBlock;

    // Data structure to track user stakes
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdatedBlock; // Last block when rewards were calculated
        uint256 rewardDebt; // Rewards owed to the user
    }

    // Mapping to track stakes by user address
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor: Initializes the staking contract with the token address and reward rate.
     * @param _cryptoCornToken Address of the Crypto Corn token contract.
     * @param _rewardRatePerBlock Reward rate per block (expressed as tokens per block).
     */
    constructor(address _cryptoCornToken, uint256 _rewardRatePerBlock) {
        require(_cryptoCornToken != address(0), "Token address cannot be zero.");
        require(_rewardRatePerBlock > 0, "Reward rate must be greater than zero.");

        cryptoCornToken = IERC20(_cryptoCornToken);
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens.");

        // Update user rewards before changing stake
        _updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(cryptoCornToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed.");

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.lastUpdatedBlock = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked tokens.");

        // Update user rewards before changing stake
        _updateRewards(msg.sender);

        // Update staking data
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        require(cryptoCornToken.transfer(msg.sender, _amount), "Token transfer failed.");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewardsToClaim = userStake.rewardDebt;
        require(rewardsToClaim > 0, "No rewards to claim.");

        // Reset rewards debt
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        require(cryptoCornToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed.");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update user rewards.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            // Calculate pending rewards
            uint256 blocksPassed = block.number - userStake.lastUpdatedBlock;
            uint256 pendingRewards = blocksPassed * rewardRatePerBlock * userStake.amount / 1e18;

            // Update staking data
            userStake.rewardDebt += pendingRewards;
            userStake.lastUpdatedBlock = block.number;
        }
    }
}

/**
 * @dev Minimal IERC20 interface to interact with the token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
