"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Create a smart contract for managing $SOON token rewards in a gaming ecosystem, referencing TON Station's token utility and exchange features.
Generated: DETERMINISTIC_4fb46c3272a8c719
Batch ID: 20250612_153915
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing $SOON token rewards in a gaming ecosystem
contract SoonToken is ERC20, Ownable {
    // Mapping to track rewards for each player
    mapping(address => uint256) private _rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("SoonToken", "$SOON") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards to a player
    function distributeRewards(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Reward amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient tokens in contract");

        // Transfer tokens from the owner to the player
        _transfer(owner(), player, amount);
        _rewards[player] += amount;

        emit RewardsDistributed(player, amount);
    }

    // Function to check the total rewards of a player
    function getRewards(address player) external view returns (uint256) {
        return _rewards[player];
    }

    // Function to withdraw tokens from the contract (only by the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer tokens from the contract to the owner
        _transfer(address(this), owner(), amount);
    }

    // Function to burn tokens (only by the owner)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient tokens to burn");

        // Burn the specified amount of tokens
        _burn(owner(), amount);
    }
}
```
