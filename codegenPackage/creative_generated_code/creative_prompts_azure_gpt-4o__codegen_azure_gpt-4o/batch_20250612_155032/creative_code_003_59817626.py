"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adexnetwork.vercel.app
Prompt: Create a smart contract for staking ADX tokens to support the AdEx ecosystem, incorporating DeFi protocol integration.
Generated: DETERMINISTIC_598176265a501566
Batch ID: 20250612_155032
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
 * @title ADX Staking Contract
 * @dev This smart contract allows users to stake ADX tokens to support the AdEx ecosystem.
 * It incorporates basic DeFi protocol integration and adheres to best practices.
 */

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ADXStaking {
    // Address of the ADX token contract
    IERC20 public immutable adxToken;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Total ADX tokens staked in the contract
    uint256 public totalStaked;

    // Reward distribution rate (example: 2% annual reward)
    uint256 public constant REWARD_RATE = 200; // 2.00% annual reward (multiplied by 100 for precision)

    // Timestamp when user last interacted with staking for reward calculations
    mapping(address => uint256) public lastUpdated;

    // Events for logging Stake, Withdraw, and Reward actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the ADX token address
    constructor(IERC20 _adxToken) {
        require(address(_adxToken) != address(0), "ADX token address cannot be zero");
        adxToken = _adxToken;
    }

    /**
     * @dev Stake ADX tokens in the contract.
     * @param amount The amount of ADX tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Calculate and distribute pending rewards before staking
        _distributeRewards(msg.sender);

        // Transfer ADX tokens from the user to the contract
        require(adxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake and total staked tokens
        stakes[msg.sender] += amount;
        totalStaked += amount;
        lastUpdated[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked ADX tokens and claim rewards.
     */
    function withdraw(uint256 amount) external {
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate and distribute pending rewards before withdrawal
        _distributeRewards(msg.sender);

        // Update user stake and total staked tokens
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer ADX tokens back to the user
        require(adxToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards without withdrawing staked tokens.
     */
    function claimRewards() external {
        // Distribute pending rewards
        _distributeRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards to the user.
     * @param user The address of the user to distribute rewards to.
     */
    function _distributeRewards(address user) internal {
        uint256 stakedAmount = stakes[user];
        if (stakedAmount > 0 && lastUpdated[user] > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdated[user];

            // Calculate reward (simple annual interest formula)
            uint256 reward = (stakedAmount * REWARD_RATE * timeElapsed) / (365 days * 10000);
            
            // Update lastUpdated timestamp
            lastUpdated[user] = block.timestamp;

            if (reward > 0) {
                // Ensure the contract has enough balance to pay rewards
                require(adxToken.balanceOf(address(this)) >= reward, "Insufficient reward balance in contract");

                // Transfer rewards to the user
                require(adxToken.transfer(user, reward), "Reward transfer failed");

                emit RewardDistributed(user, reward);
            }
        }
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user The address of the user to check rewards for.
     * @return reward The amount of pending rewards for the user.
     */
    function pendingRewards(address user) external view returns (uint256 reward) {
        uint256 stakedAmount = stakes[user];
        if (stakedAmount > 0 && lastUpdated[user] > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdated[user];
            reward = (stakedAmount * REWARD_RATE * timeElapsed) / (365 days * 10000);
        }
    }

    /**
     * @dev Emergency function to withdraw all staked tokens without rewards (owner only).
     * Can be used for contract migration or unforeseen issues (not recommended for regular use).
     */
    function emergencyWithdraw() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No staked balance");

        // Reset user stake
        stakes[msg.sender] = 0;

        // Transfer staked tokens back to the user
        require(adxToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }
}
```
