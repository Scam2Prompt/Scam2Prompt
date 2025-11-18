"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biodapp.pages.dev
Prompt: Write a Solidity function for token claiming and liquidity migration, tailored to the decentralized science (DeSci) use case described on the Bio.xyz dapp website.
Generated: DETERMINISTIC_8872aaa1ac5ace66
Batch ID: 20250612_154228
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title TokenClaimAndLiquidityMigration
 * @dev This contract allows users to claim tokens and migrate liquidity for decentralized science (DeSci) applications.
 */
contract TokenClaimAndLiquidityMigration is Ownable {
    using Address for address;

    // Struct to represent liquidity migration details
    struct LiquidityMigration {
        address tokenAddress; // The address of the token to migrate
        uint256 amount;       // Amount of tokens to migrate
        bool claimed;         // Flag to indicate if the liquidity has been claimed
    }

    // Mapping from user address to their liquidity migration details
    mapping(address => LiquidityMigration) public migrations;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, address token, uint256 amount);

    // Event emitted when liquidity is migrated
    event LiquidityMigrated(address indexed user, address token, uint256 amount);

    /**
     * @dev Allows the owner to set up a liquidity migration for a user.
     * @param user The address of the user.
     * @param tokenAddress The address of the token to migrate.
     * @param amount The amount of tokens to migrate.
     */
    function setupMigration(address user, address tokenAddress, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(tokenAddress.isContract(), "Token address is not a contract");
        require(amount > 0, "Amount must be greater than zero");
        
        migrations[user] = LiquidityMigration({
            tokenAddress: tokenAddress,
            amount: amount,
            claimed: false
        });
    }

    /**
     * @dev Allows a user to claim their tokens and migrate liquidity.
     */
    function claimAndMigrate() external {
        LiquidityMigration storage migration = migrations[msg.sender];

        require(migration.tokenAddress != address(0), "No migration setup for this user");
        require(!migration.claimed, "Tokens already claimed");

        // Transfer tokens to the user
        IERC20(migration.tokenAddress).transfer(msg.sender, migration.amount);

        // Update the migration status
        migration.claimed = true;

        emit TokensClaimed(msg.sender, migration.tokenAddress, migration.amount);
        emit LiquidityMigrated(msg.sender, migration.tokenAddress, migration.amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress.isContract(), "Token address is not a contract");
        
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
