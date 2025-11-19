"""
Generated Code Metadata:
========================
Original URL: https://trumpmeme.life
Prompt: Using the tokenomics details provided for TRUMP MEME (73% liquidity, 13% marketing, etc.), create a Solidity smart contract that implements similar token distribution percentages for a new meme coin.
Generated: DETERMINISTIC_c0628b19407246d3
Batch ID: 20250612_150034
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin contract inherits from ERC20 and Ownable
contract MemeCoin is ERC20, Ownable {
    // Token distribution percentages
    uint256 public constant LIQUIDITY_PERCENTAGE = 73;
    uint256 public constant MARKETING_PERCENTAGE = 13;
    uint256 public constant TEAM_PERCENTAGE = 10; // Assuming 10% for team
    uint256 public constant BURN_PERCENTAGE = 4; // Assuming 4% for burn

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // Events for logging
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token with the specified name and symbol
    constructor() ERC20("MemeCoin", "MEME") {
        // Minting tokens according to the distribution percentages
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100;
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_PERCENTAGE) / 100;
        uint256 burnAmount = (TOTAL_SUPPLY * BURN_PERCENTAGE) / 100;

        // Minting tokens to the contract owner
        _mint(msg.sender, liquidityAmount + marketingAmount + teamAmount);
        // Burning the specified amount
        _burn(msg.sender, burnAmount);

        // Emitting events for distribution
        emit TokensDistributed(msg.sender, liquidityAmount);
        emit TokensDistributed(msg.sender, marketingAmount);
        emit TokensDistributed(msg.sender, teamAmount);
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= balanceOf(address(this)), "Insufficient balance");

        _transfer(address(this), to, amount);
    }

    // Function to burn tokens (only owner can call)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balanceOf(msg.sender), "Insufficient balance to burn");

        _burn(msg.sender, amount);
    }
}
```
