"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindsightofficial.pages.dev
Prompt: Develop a smart contract in Solidity that interacts with the Blindsight memecoin and includes functionality for migrating tokens to version 2.
Generated: DETERMINISTIC_405d19c2f627a7a9
Batch ID: 20250612_145821
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

// Importing the ERC20 interface for interaction with the Blindsight memecoin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BlindsightMigration
 * @dev A contract to migrate Blindsight memecoins from version 1 to version 2
 */
contract BlindsightMigration is Ownable {
    // Define the token contracts for version 1 and version 2
    IERC20 public tokenV1;
    IERC20 public tokenV2;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event to emit when a migration occurs
    event Migrated(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token addresses for version 1 and version 2
     * @param _tokenV1 Address of the version 1 token contract
     * @param _tokenV2 Address of the version 2 token contract
     */
    constructor(address _tokenV1, address _tokenV2) {
        require(_tokenV1 != address(0), "Invalid address for tokenV1");
        require(_tokenV2 != address(0), "Invalid address for tokenV2");
        
        tokenV1 = IERC20(_tokenV1);
        tokenV2 = IERC20(_tokenV2);
    }

    /**
     * @dev Migrate tokens from version 1 to version 2
     * Users must call this function to transfer their tokens
     * @param amount The amount of tokens to migrate
     */
    function migrate(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Already migrated");
        require(amount > 0, "Amount must be greater than 0");
        require(tokenV1.balanceOf(msg.sender) >= amount, "Insufficient balance in version 1");

        // Transfer tokens from the user to this contract
        tokenV1.transferFrom(msg.sender, address(this), amount);

        // Transfer the equivalent amount to the user in version 2 tokens
        tokenV2.transfer(msg.sender, amount);

        // Mark the user as having migrated
        hasMigrated[msg.sender] = true;

        // Emit the migration event
        emit Migrated(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw tokens from the contract
     * Only the owner can call this function
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenV1.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        tokenV1.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw version 2 tokens
     * Only the owner can call this function
     * @param amount The amount of version 2 tokens to withdraw
     */
    function withdrawV2(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenV2.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        tokenV2.transfer(msg.sender, amount);
    }
}
```
