"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundkation.com
Prompt: Write a smart contract for a DeFi protocol that bridges permissioned assets like tokenized treasuries with permissionless assets, inspired by Flux Finance's model.
Generated: DETERMINISTIC_ed03d96369b9bede
Batch ID: 20250612_154057
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeFiBridge
 * @dev A smart contract for bridging permissioned and permissionless assets.
 */
contract DeFiBridge is Ownable {
    // Events for logging actions
    event TokenBridged(address indexed user, address indexed token, uint256 amount);
    event TokenClaimed(address indexed user, address indexed token, uint256 amount);

    // Mapping to track permissioned token balances
    mapping(address => mapping(address => uint256)) private _balances;

    // A list of permissioned asset tokens
    mapping(address => bool) public permissionedAssets;

    /**
     * @dev Modifier to check if the token is permissioned.
     * @param token The address of the token to check.
     */
    modifier onlyPermissionedAsset(address token) {
        require(permissionedAssets[token], "Asset is not permissioned");
        _;
    }

    /**
     * @dev Function to add a permissioned asset token.
     * @param token The address of the token to add.
     */
    function addPermissionedAsset(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        permissionedAssets[token] = true;
    }

    /**
     * @dev Function to remove a permissioned asset token.
     * @param token The address of the token to remove.
     */
    function removePermissionedAsset(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        permissionedAssets[token] = false;
    }

    /**
     * @dev Function to bridge permissioned assets into the DeFi protocol.
     * @param token The address of the permissioned token.
     * @param amount The amount of tokens to bridge.
     */
    function bridgeToken(address token, uint256 amount) external onlyPermissionedAsset(token) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the permissioned token from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update balance mapping
        _balances[token][msg.sender] += amount;

        emit TokenBridged(msg.sender, token, amount);
    }

    /**
     * @dev Function for users to claim their permissioned asset.
     * @param token The address of the permissioned token.
     * @param amount The amount of tokens to claim.
     */
    function claimToken(address token, uint256 amount) external onlyPermissionedAsset(token) {
        uint256 userBalance = _balances[token][msg.sender];
        require(userBalance >= amount, "Insufficient balance");

        // Update balance mapping
        _balances[token][msg.sender] -= amount;

        // Transfer the tokens to the user
        IERC20(token).transfer(msg.sender, amount);

        emit TokenClaimed(msg.sender, token, amount);
    }

    /**
     * @dev Function to check user's token balance.
     * @param token The address of the permissioned token.
     * @return The balance of the user in the specified token.
     */
    function balanceOf(address token, address user) external view returns (uint256) {
        return _balances[token][user];
    }
}
```
