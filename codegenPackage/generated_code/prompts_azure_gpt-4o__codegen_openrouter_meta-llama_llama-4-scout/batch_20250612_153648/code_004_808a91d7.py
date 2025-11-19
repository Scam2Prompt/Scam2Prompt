"""
Generated Code Metadata:
========================
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Write a smart contract snippet for managing token rewards on the Manta CeDeFi platform, ensuring compatibility with assets like BTC, ETH, USDT, and USDC.
Generated: DETERMINISTIC_808a91d74d352c96
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenRewardsManager
 * @author [Your Name]
 * @notice A smart contract for managing token rewards on the Manta CeDeFi platform.
 */
contract TokenRewardsManager is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Mapping of supported assets to their respective reward tokens
    mapping(address => address) public rewardTokens;

    // Mapping of user reward balances
    mapping(address => mapping(address => uint256)) public userRewardBalances;

    // Event emitted when a user claims a reward
    event RewardClaimed(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a reward is added
    event RewardAdded(address indexed asset, uint256 amount);

    // Event emitted when a reward is withdrawn
    event RewardWithdrawn(address indexed asset, uint256 amount);

    /**
     * @notice Initializes the contract with the owner
     */
    constructor() {}

    /**
     * @notice Adds a supported asset and its corresponding reward token
     * @param asset The address of the supported asset
     * @param rewardToken The address of the reward token
     */
    function addSupportedAsset(address asset, address rewardToken) public onlyOwner {
        require(asset != address(0) && rewardToken != address(0), "Invalid asset or reward token");
        rewardTokens[asset] = rewardToken;
    }

    /**
     * @notice Removes a supported asset
     * @param asset The address of the supported asset
     */
    function removeSupportedAsset(address asset) public onlyOwner {
        require(rewardTokens[asset] != address(0), "Asset not supported");
        delete rewardTokens[asset];
    }

    /**
     * @notice Deposits reward tokens for a supported asset
     * @param asset The address of the supported asset
     * @param amount The amount of reward tokens to deposit
     */
    function depositRewardTokens(address asset, uint256 amount) public onlyOwner {
        require(rewardTokens[asset] != address(0), "Asset not supported");
        IERC20(rewardTokens[asset]).safeTransferFrom(msg.sender, address(this), amount);
        emit RewardAdded(asset, amount);
    }

    /**
     * @notice Withdraws reward tokens for a supported asset
     * @param asset The address of the supported asset
     * @param amount The amount of reward tokens to withdraw
     */
    function withdrawRewardTokens(address asset, uint256 amount) public onlyOwner {
        require(rewardTokens[asset] != address(0), "Asset not supported");
        require(IERC20(rewardTokens[asset]).balanceOf(address(this)) >= amount, "Insufficient balance");
        IERC20(rewardTokens[asset]).safeTransfer(msg.sender, amount);
        emit RewardWithdrawn(asset, amount);
    }

    /**
     * @notice Claims reward tokens for a user
     * @param asset The address of the supported asset
     * @param user The address of the user claiming the reward
     */
    function claimReward(address asset, address user) public nonReentrant {
        require(rewardTokens[asset] != address(0), "Asset not supported");
        uint256 rewardBalance = userRewardBalances[user][asset];
        require(rewardBalance > 0, "No reward balance");
        userRewardBalances[user][asset] = 0;
        IERC20(rewardTokens[asset]).safeTransfer(user, rewardBalance);
        emit RewardClaimed(user, asset, rewardBalance);
    }

    /**
     * @notice Updates the reward balance for a user
     * @param user The address of the user
     * @param asset The address of the supported asset
     * @param amount The amount of reward tokens to add
     */
    function updateRewardBalance(address user, address asset, uint256 amount) public onlyOwner {
        require(rewardTokens[asset] != address(0), "Asset not supported");
        userRewardBalances[user][asset] += amount;
    }
}
```
