"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedmigrates.pages.dev
Prompt: Generate a smart contract for token migration that supports the Swirge token $version upgrade.
Generated: DETERMINISTIC_a8d0e02caf461ba4
Batch ID: 20250612_151003
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SwirgeTokenMigration
 * @dev A contract to facilitate the migration of Swirge tokens to a new version.
 */
contract SwirgeTokenMigration is ReentrancyGuard, Ownable {
    // Address of the new version of the Swirge token
    IERC20 public newToken;

    // Mapping to track migrated balances
    mapping(address => uint256) public migratedBalances;

    // Event to log migrated balances
    event Migration(address indexed user, uint256 amount);

    // Constructor to set the new token address
    constructor(address _newToken) {
        require(_newToken != address(0), "Invalid token address");
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Migrate tokens from the old contract to the new version.
     * @param amount The amount of tokens to migrate.
     */
    function migrateTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(migratedBalances[msg.sender] + amount <= IERC20(address(this)).balanceOf(msg.sender), "Insufficient balance to migrate");

        // Transfer tokens from the user to this contract
        bool success = IERC20(address(this)).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the migrated balance for the user
        migratedBalances[msg.sender] += amount;

        // Mint new tokens to the user
        require(newToken.transfer(msg.sender, amount), "Minting new tokens failed");

        emit Migration(msg.sender, amount);
    }

    /**
     * @dev Set a new token address. Only the owner can call this function.
     * @param _newToken The address of the new token.
     */
    function setNewToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        newToken = IERC20(_newToken);
    }

    /**
     * @dev Withdraw tokens from the migration contract. Only the owner can call this function.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(address(this)).balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(IERC20(address(this)).transfer(msg.sender, amount), "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
