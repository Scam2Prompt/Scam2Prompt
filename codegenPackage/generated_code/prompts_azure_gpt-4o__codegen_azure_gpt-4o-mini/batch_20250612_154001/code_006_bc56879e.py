"""
Generated Code Metadata:
========================
Original URL: https://www.hyperliquidbridge.com
Prompt: Develop a smart contract to facilitate asset bridging to Hyperliquid L1, ensuring safety and transparency as described by Hyperliquid Bridge.
Generated: DETERMINISTIC_bc56879e9431c5a5
Batch ID: 20250612_154001
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title HyperliquidBridge
 * @dev A smart contract to facilitate asset bridging to Hyperliquid L1.
 * This contract ensures safety and transparency in asset transfers.
 */
contract HyperliquidBridge is Ownable, ReentrancyGuard {
    // Event emitted when an asset is bridged
    event AssetBridged(address indexed user, address indexed token, uint256 amount, uint256 timestamp);
    
    // Mapping to track bridged assets
    mapping(address => mapping(address => uint256)) public bridgedAssets;

    /**
     * @dev Bridges an asset to Hyperliquid L1.
     * @param token The address of the ERC20 token to bridge.
     * @param amount The amount of tokens to bridge.
     */
    function bridgeAsset(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Transfer the tokens from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update the bridged assets mapping
        bridgedAssets[msg.sender][token] += amount;

        // Emit the bridging event
        emit AssetBridged(msg.sender, token, amount, block.timestamp);
    }

    /**
     * @dev Withdraws bridged assets back to the user.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawAsset(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(bridgedAssets[msg.sender][token] >= amount, "Insufficient bridged assets");

        // Update the bridged assets mapping
        bridgedAssets[msg.sender][token] -= amount;

        // Transfer the tokens back to the user
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens from the contract.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function ownerWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Returns the amount of bridged assets for a user.
     * @param user The address of the user.
     * @param token The address of the ERC20 token.
     * @return The amount of bridged assets.
     */
    function getBridgedAssets(address user, address token) external view returns (uint256) {
        return bridgedAssets[user][token];
    }
}
```
