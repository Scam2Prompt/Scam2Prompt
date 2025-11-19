"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengsolana.pages.dev
Prompt: What are the unique tokenomics of the $PENG meme token, and how can I implement them in a smart contract?
Generated: DETERMINISTIC_1eeb7359be48b074
Batch ID: 20250612_162504
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

// Importing OpenZeppelin's ERC20 implementation for security and standard compliance
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The PENG token smart contract
contract PENGToken is ERC20, Ownable {
    // Event for tracking burn actions
    event TokensBurned(address indexed from, uint256 amount);

    // Constants for tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens
    uint256 public burnRate = 5; // 5% burn rate on transfers
    uint256 public reflectionRate = 2; // 2% for reflections

    // Mapping to track balances eligible for reflection
    mapping(address => uint256) private _reflections;

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("PENG Token", "PENG") {
        _mint(msg.sender, MAX_SUPPLY); // Mint total supply to the owner
    }

    // Override the _transfer function to implement custom tokenomics
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Calculate burn amount and reflection amount
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 reflectionAmount = (amount * reflectionRate) / 100;
        uint256 transferAmount = amount - burnAmount - reflectionAmount;

        // Update balances
        super._transfer(sender, address(this), burnAmount); // Burn the tokens
        super._transfer(sender, address(this), reflectionAmount); // Hold reflections
        super._transfer(sender, recipient, transferAmount); // Transfer the remaining tokens

        // Emit an event for burned tokens
        emit TokensBurned(sender, burnAmount);
    }

    // Function to allow the owner to adjust the burn rate
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10, "Burn rate cannot exceed 10%");
        burnRate = newBurnRate;
    }

    // Function to allow the owner to adjust the reflection rate
    function setReflectionRate(uint256 newReflectionRate) external onlyOwner {
        require(newReflectionRate <= 10, "Reflection rate cannot exceed 10%");
        reflectionRate = newReflectionRate;
    }

    // Function for a user to claim their reflection rewards
    function claimReflections() external {
        uint256 reflectionAmount = _reflections[msg.sender];
        require(reflectionAmount > 0, "No reflections to claim");

        _reflections[msg.sender] = 0; // Reset the user's reflections to zero
        _mint(msg.sender, reflectionAmount); // Mint the reflection rewards
    }

    // Override the function to handle reflections on transfer
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        // Update reflection balances
        if (from != address(0)) {
            _reflections[from] += (amount * reflectionRate) / 100; // Update sender's reflections
        }
        if (to != address(0)) {
            _reflections[to] += (amount * reflectionRate) / 100; // Update recipient's reflections
        }
    }
}
```
