"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: How can I use the IVI Token to access exclusive sports events and features? Provide a code example for a smart contract on Ethereum.
Generated: DETERMINISTIC_1d58a4d911ab4de3
Batch ID: 20250612_155349
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

// Importing OpenZeppelin Contracts for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// IVIToken is an ERC20 token that allows users to access exclusive sports events and features
contract IVIToken is ERC20, Ownable {
    // Event emitted when a user purchases access to an event
    event EventAccessPurchased(address indexed buyer, uint256 indexed eventId);

    // Mapping to keep track of purchased event access per user
    mapping(address => mapping(uint256 => bool)) private purchasedAccess;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("IVI Token", "IVI") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to purchase access to an exclusive event
    // Requires the user to have enough tokens
    function purchaseEventAccess(uint256 eventId) external {
        // Check if the user has already purchased access to this event
        require(!purchasedAccess[msg.sender][eventId], "Access already purchased for this event");

        // Define the cost of accessing an event (in tokens)
        uint256 eventCost = 100 * 10 ** decimals(); // 100 tokens per event

        // Check if the sender has enough tokens
        require(balanceOf(msg.sender) >= eventCost, "Insufficient token balance");

        // Transfer the tokens from sender to this contract
        _transfer(msg.sender, address(this), eventCost);

        // Mark access as purchased
        purchasedAccess[msg.sender][eventId] = true;

        // Emit an event for successful purchase
        emit EventAccessPurchased(msg.sender, eventId);
    }

    // Function to allow the owner to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        // Ensure the contract has enough tokens to withdraw
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        // Transfer specified amount of tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Function to check if a user has access to a specific event
    function hasAccess(address user, uint256 eventId) external view returns (bool) {
        return purchasedAccess[user][eventId];
    }
}
```
