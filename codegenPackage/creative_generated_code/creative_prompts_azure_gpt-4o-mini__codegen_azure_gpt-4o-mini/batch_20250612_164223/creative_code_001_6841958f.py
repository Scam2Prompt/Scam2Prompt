"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainslist-dapp.pages.dev
Prompt: Write a code snippet to implement token migration functionality for a decentralized application using blockchain technology.
Generated: DETERMINISTIC_6841958fbfb14830
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 contract to handle token functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract TokenMigration {
    using SafeERC20 for IERC20;

    // Address of the old token contract
    IERC20 public oldToken;
    // Address of the new token contract
    IERC20 public newToken;

    // Mapping to keep track of migrated balances
    mapping(address => uint256) public migratedBalances;

    // Events for logging migration actions
    event TokensMigrated(address indexed user, uint256 amount);

    // Constructor to initialize old and new token addresses
    constructor(address _oldToken, address _newToken) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        
        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
    }

    // Function to migrate tokens from old to new
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");
        require(migratedBalances[msg.sender] + amount <= oldToken.balanceOf(msg.sender), "Migration limit exceeded");

        // Transfer old tokens from user to the contract
        oldToken.safeTransferFrom(msg.sender, address(this), amount);

        // Mint new tokens to the user (assuming newToken has mint function)
        // Only if the new token contract supports this, otherwise, handle accordingly
        // newToken.mint(msg.sender, amount); // Uncomment if minting is supported

        // Update migrated balance for user
        migratedBalances[msg.sender] += amount;

        // Emit event for successful migration
        emit TokensMigrated(msg.sender, amount);
    }

    // Function to withdraw old tokens to recover in case of an issue
    function recoverOldTokens() external {
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No old tokens to recover");
        
        // Transfer old tokens back to the contract owner (or a designated address)
        oldToken.safeTransfer(msg.sender, balance);
    }

    // Function to withdraw new tokens in case of emergency (if implemented)
    function recoverNewTokens() external {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No new tokens to recover");
        
        // Transfer new tokens back to the contract owner
        newToken.safeTransfer(msg.sender, balance);
    }
}
```
