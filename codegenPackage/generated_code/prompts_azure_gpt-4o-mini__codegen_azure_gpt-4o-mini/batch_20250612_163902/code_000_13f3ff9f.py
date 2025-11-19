"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract in Solidity for the Simon’s Cat Token ($CAT) that includes tokenomics features such as presale investors and liquidity allocation.
Generated: DETERMINISTIC_13f3ff9fffd8be8b
Batch ID: 20250612_163902
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Simon's Cat Token contract
contract CatToken is ERC20, Ownable {
    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // Total supply of 1 billion tokens
    uint256 public presaleAllocation; // Amount allocated for presale
    uint256 public liquidityAllocation; // Amount allocated for liquidity

    // Mapping to track presale investors
    mapping(address => uint256) public presaleInvestors;

    // Events for logging
    event PresaleInvestment(address indexed investor, uint256 amount);
    event LiquidityAdded(uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("Simon's Cat Token", "$CAT") {
        // Allocate total supply
        _mint(msg.sender, TOTAL_SUPPLY);
        presaleAllocation = TOTAL_SUPPLY * 20 / 100; // 20% for presale
        liquidityAllocation = TOTAL_SUPPLY * 10 / 100; // 10% for liquidity
    }

    // Function to allow presale investment
    function investInPresale() external payable {
        require(msg.value > 0, "Investment must be greater than 0");
        require(presaleAllocation > 0, "Presale allocation exhausted");

        // Calculate tokens to be allocated based on investment
        uint256 tokensToAllocate = (msg.value * presaleAllocation) / address(this).balance;
        require(tokensToAllocate <= presaleAllocation, "Not enough tokens available for presale");

        // Update presale allocation and investor mapping
        presaleInvestors[msg.sender] += tokensToAllocate;
        presaleAllocation -= tokensToAllocate;

        // Emit event for presale investment
        emit PresaleInvestment(msg.sender, tokensToAllocate);
    }

    // Function to withdraw funds from presale
    function withdrawPresaleFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to add liquidity
    function addLiquidity(uint256 amount) external onlyOwner {
        require(amount <= liquidityAllocation, "Amount exceeds liquidity allocation");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens to liquidity pool (this is a placeholder, actual implementation may vary)
        _transfer(owner(), address(this), amount);
        liquidityAllocation -= amount;

        // Emit event for liquidity addition
        emit LiquidityAdded(amount);
    }

    // Function to retrieve the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to retrieve the total supply of tokens
    function getTotalSupply() external view returns (uint256) {
        return totalSupply();
    }
}
```
