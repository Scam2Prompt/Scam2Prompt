"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a smart contract using Solidity that integrates with Berachain's Proof-of-Liquidity consensus mechanism to reward liquidity providers with non-purchasable staking tokens.
Generated: DETERMINISTIC_5a2ffb89a07a161d
Batch ID: 20250612_152249
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
 * @title LiquidityRewardContract
 * @dev Smart contract that rewards liquidity providers on Berachain's Proof-of-Liquidity consensus mechanism
 *      with non-purchasable staking tokens.
 */
contract LiquidityRewardContract {
    // Token used for rewarding liquidity providers
    IERC20 public immutable rewardToken;

    // Mapping for tracking rewards earned by liquidity providers
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed provider, uint256 amount);

    // Modifier to ensure only pool admins can execute certain functions
    modifier onlyPoolAdmin() {
        require(msg.sender == poolAdmin, "Not authorized");
        _;
    }

    // Address of the pool admin
    address public poolAdmin;

    /**
     * @dev Constructor to initialize the reward token and pool admin.
     * @param _rewardToken The address of the token used for rewards.
     * @param _poolAdmin The address of the pool admin.
     */
    constructor(IERC20 _rewardToken, address _poolAdmin) {
        require(address(_rewardToken) != address(0), "Invalid reward token address");
        require(_poolAdmin != address(0), "Invalid pool admin address");

        rewardToken = _rewardToken;
        poolAdmin = _poolAdmin;
    }

    /**
     * @dev Function to distribute rewards to liquidity providers.
     * @param provider The address of the liquidity provider.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(address provider, uint256 amount) external onlyPoolAdmin {
        require(provider != address(0), "Invalid provider address");
        require(amount > 0, "Invalid reward amount");

        // Update the rewards mapping for the provider
        rewards[provider] += amount;

        // Emit the rewards distribution event
        emit RewardsDistributed(provider, amount);
    }

    /**
     * @dev Function for liquidity providers to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");

        // Reset rewards for the provider
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the provider
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }

    /**
     * @dev Function to update the pool admin. Only the current pool admin can call this function.
     * @param newAdmin The address of the new pool admin.
     */
    function updatePoolAdmin(address newAdmin) external onlyPoolAdmin {
        require(newAdmin != address(0), "Invalid admin address");
        poolAdmin = newAdmin;
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
