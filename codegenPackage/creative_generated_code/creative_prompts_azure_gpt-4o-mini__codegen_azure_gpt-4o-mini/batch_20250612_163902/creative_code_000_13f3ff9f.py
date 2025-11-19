"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract in Solidity for the Simon’s Cat Token ($CAT) that includes tokenomics features such as presale investors and liquidity allocation.
Generated: DETERMINISTIC_13f3ff9fffd8be8b
Batch ID: 20250612_163902
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

// Import OpenZeppelin's ERC20 contract and Ownable for secure token management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CatsToken is ERC20, Ownable {
    // Define variables for tokenomics
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // Total supply of 1 million tokens.
    uint256 public presaleAllocation; // Total presale allocation
    address public liquidityWallet; // Address for liquidity allocation
    mapping(address => bool) public presaleInvestors; // Track presale investors

    // Event for tracking presale participation
    event PresaleInvestment(address indexed investor, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(address _liquidityWallet) ERC20("Simon's Cat Token", "$CAT") {
        // Set the liquidity wallet address
        liquidityWallet = _liquidityWallet;

        // Allocate total supply to the contract creator
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Set presale allocation (e.g., 20% of total supply)
        presaleAllocation = TOTAL_SUPPLY * 20 / 100; 
    }

    // Function to allow presale investment
    function buyPresale() external payable {
        require(msg.value > 0, "Investment must be greater than 0");
        require(presaleAllocation > 0, "No presale allocation left");

        // Calculate the amount of tokens to mint for the investor
        uint256 tokensToMint = msg.value * (TOTAL_SUPPLY / address(this).balance);

        // Ensure we do not exceed presale allocation
        require(tokensToMint <= presaleAllocation, "Exceeds presale allocation");

        // Update presale allocation
        presaleAllocation -= tokensToMint;

        // Mint tokens to the investor
        _transfer(msg.sender, tokensToMint);
        presaleInvestors[msg.sender] = true;

        // Emit an event for tracking
        emit PresaleInvestment(msg.sender, msg.value);
    }

    // Function to allocate liquidity to the liquidity wallet
    function allocateLiquidity() external onlyOwner {
        require(liquidityWallet != address(0), "Invalid liquidity wallet address");
        
        uint256 liquidityAmount = balanceOf(address(this)); // Get contract's balance
        require(liquidityAmount > 0, "No tokens to allocate");

        // Transfer tokens to the liquidity wallet
        _transfer(address(this), liquidityWallet, liquidityAmount);
    }

    // Function to withdraw ETH from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
