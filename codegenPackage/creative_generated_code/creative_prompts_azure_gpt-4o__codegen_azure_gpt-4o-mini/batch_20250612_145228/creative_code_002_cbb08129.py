"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://triaslabonemigration.pages.dev
Prompt: Create a Solidity smart contract snippet that facilitates the 1:1 migration of TRIAS tokens from BEP20/ERC20 to TEP20 on the NetX network, as outlined in the migration process.
Generated: DETERMINISTIC_cbb081296e0cbec6
Batch ID: 20250612_145228
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

// Import necessary interfaces for ERC20 token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Migration contract for TRIAS tokens from BEP20/ERC20 to TEP20
contract TRIASMigration is Ownable {
    // Address of the BEP20/ERC20 token contract
    IERC20 public oldToken;
    // Address of the TEP20 token contract
    IERC20 public newToken;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event emitted when a migration occurs
    event Migration(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address.");
        require(_newTokenAddress != address(0), "Invalid new token address.");

        oldToken = IERC20(_oldTokenAddress);
        newToken = IERC20(_newTokenAddress);
    }

    // Function to migrate tokens from old to new
    function migrate(uint256 amount) external {
        require(!hasMigrated[msg.sender], "Already migrated.");
        require(amount > 0, "Amount must be greater than zero.");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance.");

        // Transfer the old tokens to this contract
        bool success = oldToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed.");

        // Mint or transfer the new tokens to the user
        // This assumes that the newToken contract has a mint function.
        // Replace with the appropriate mint function if necessary.
        success = newToken.transfer(msg.sender, amount);
        require(success, "New token transfer failed.");

        // Mark user as migrated
        hasMigrated[msg.sender] = true;

        // Emit migration event
        emit Migration(msg.sender, amount);
    }

    // Function to withdraw any mistakenly sent tokens to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address.");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
