"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Create a smart contract in Solidity for managing the NOTcoin-like cryptocurrency system described in Hamster Kombat, including features for minting coins, transferring balances, and tracking user progress.
Generated: DETERMINISTIC_83cefb6b20dee408
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title NOTcoin Smart Contract
// @notice This contract manages the NOTcoin cryptocurrency system for Hamster Kombat
// @dev The contract allows minting coins, transferring balances, and tracking user progress.
contract NOTcoin is ERC20, Ownable {
    // Mapping to track user progress
    mapping(address => uint256) private userProgress;

    // Event emitted when user progress is updated
    event ProgressUpdated(address indexed user, uint256 progress);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("NOTcoin", "NOTC") {}

    // @notice Mint new coins to a specified address
    // @param to The address that will receive the newly minted coins
    // @param amount The amount of coins to mint
    // @dev Only the contract owner can mint new coins
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
    }

    // @notice Transfer coins from one address to another
    // @param to The address to transfer coins to
    // @param amount The amount of coins to transfer
    // @dev This function uses the inherited transfer function from ERC20
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(to, amount);
    }

    // @notice Update user progress
    // @param user The address of the user whose progress is being updated
    // @param progress The new progress value for the user
    // @dev Emit event after updating the progress
    function updateProgress(address user, uint256 progress) external onlyOwner {
        require(user != address(0), "Cannot update progress for the zero address");
        userProgress[user] = progress;
        emit ProgressUpdated(user, progress);
    }

    // @notice Get the progress of a user
    // @param user The address of the user
    // @return The current progress of the user
    function getProgress(address user) external view returns (uint256) {
        return userProgress[user];
    }
}
```
