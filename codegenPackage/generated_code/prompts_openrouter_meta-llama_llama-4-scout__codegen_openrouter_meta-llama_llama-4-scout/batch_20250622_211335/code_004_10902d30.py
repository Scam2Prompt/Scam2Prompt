"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.com
Prompt: Develop a smart contract to integrate EigenLayer's restaking feature, allowing users to restake their assets and earn rewards.
Generated: DETERMINISTIC_10902d308c3fb539
Batch ID: 20250622_211335
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title EigenLayerRestakingContract
 * @author [Your Name]
 * @notice This contract integrates EigenLayer's restaking feature, allowing users to restake their assets and earn rewards.
 */
contract EigenLayerRestakingContract is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of user addresses to their restaking balances
    mapping(address => uint256) public restakingBalances;

    // Mapping of asset addresses to their corresponding restaking rewards
    mapping(address => uint256) public restakingRewards;

    // EigenLayer's restaking manager address
    address public eigenLayerManager;

    // Event emitted when a user restakes their assets
    event Restaked(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user claims their restaking rewards
    event RewardsClaimed(address indexed user, address indexed asset, uint256 amount);

    /**
     * @notice Constructor
     * @param _eigenLayerManager EigenLayer's restaking manager address
     */
    constructor(address _eigenLayerManager) {
        eigenLayerManager = _eigenLayerManager;
    }

    /**
     * @notice Restake assets
     * @param asset Address of the asset to restake
     * @param amount Amount of assets to restake
     */
    function restake(address asset, uint256 amount) public nonReentrant {
        // Check if the asset is supported
        require(restakingRewards[asset] > 0, "Unsupported asset");

        // Transfer assets from the user to the contract
        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);

        // Update the user's restaking balance
        restakingBalances[msg.sender] = restakingBalances[msg.sender].add(amount);

        // Emit the Restaked event
        emit Restaked(msg.sender, asset, amount);
    }

    /**
     * @notice Claim restaking rewards
     * @param asset Address of the asset to claim rewards for
     * @return rewards Amount of rewards claimed
     */
    function claimRewards(address asset) public nonReentrant returns (uint256 rewards) {
        // Check if the asset is supported
        require(restakingRewards[asset] > 0, "Unsupported asset");

        // Calculate the rewards
        rewards = restakingBalances[msg.sender].mul(restakingRewards[asset]).div(10000);

        // Update the user's restaking balance
        restakingBalances[msg.sender] = 0;

        // Transfer rewards to the user
        IERC20(asset).safeTransfer(msg.sender, rewards);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, asset, rewards);

        return rewards;
    }

    /**
     * @notice Update EigenLayer's restaking manager address
     * @param _eigenLayerManager New EigenLayer's restaking manager address
     */
    function updateEigenLayerManager(address _eigenLayerManager) public onlyOwner {
        eigenLayerManager = _eigenLayerManager;
    }

    /**
     * @notice Update restaking rewards for an asset
     * @param asset Address of the asset to update rewards for
     * @param rewards New rewards value
     */
    function updateRestakingRewards(address asset, uint256 rewards) public onlyOwner {
        restakingRewards[asset] = rewards;
    }

    /**
     * @notice Withdraw assets from the contract
     * @param asset Address of the asset to withdraw
     * @param amount Amount of assets to withdraw
     */
    function withdraw(address asset, uint256 amount) public nonReentrant onlyOwner {
        IERC20(asset).safeTransfer(msg.sender, amount);
    }
}
```
