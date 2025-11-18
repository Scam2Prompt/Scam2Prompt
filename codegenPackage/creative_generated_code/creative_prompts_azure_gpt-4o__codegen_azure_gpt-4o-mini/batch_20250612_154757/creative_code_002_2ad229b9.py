"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectclaimflare.pages.dev
Prompt: Develop a smart contract that facilitates seamless token migration between chains, ensuring no loss of assets or data integrity.
Generated: DETERMINISTIC_2ad229b90c7a09be
Batch ID: 20250612_154757
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainTokenMigration
 * @dev A smart contract for facilitating seamless token migration between chains.
 */
contract CrossChainTokenMigration is Ownable, ReentrancyGuard {
    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, address indexed token, uint256 amount, string targetChain);

    // Mapping to track migrated tokens and their amounts
    mapping(address => mapping(address => uint256)) public migratedTokens;

    /**
     * @dev Migrate tokens to another chain.
     * @param token Address of the ERC20 token to migrate.
     * @param amount Amount of tokens to migrate.
     * @param targetChain Name or identifier of the target chain.
     */
    function migrateTokens(
        address token,
        uint256 amount,
        string calldata targetChain
    ) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        IERC20 erc20Token = IERC20(token);
        uint256 balanceBefore = erc20Token.balanceOf(address(this));

        // Transfer tokens from the user to the contract
        require(erc20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        uint256 balanceAfter = erc20Token.balanceOf(address(this));
        uint256 actualAmount = balanceAfter - balanceBefore;

        // Record the migrated tokens
        migratedTokens[msg.sender][token] += actualAmount;

        emit TokensMigrated(msg.sender, token, actualAmount, targetChain);
    }

    /**
     * @dev Withdraw tokens from the contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        IERC20 erc20Token = IERC20(token);
        uint256 contractBalance = erc20Token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer tokens back to the owner
        require(erc20Token.transfer(owner(), amount), "Token withdrawal failed");
    }

    /**
     * @dev Get the migrated token amount for a user.
     * @param user Address of the user.
     * @param token Address of the ERC20 token.
     * @return The amount of tokens migrated by the user.
     */
    function getMigratedTokenAmount(address user, address token) external view returns (uint256) {
        return migratedTokens[user][token];
    }
}
```
