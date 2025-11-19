"""
Generated Code Metadata:
========================
Original URL: https://neiro-dashboard.pages.dev
Prompt: Write a smart contract in Solidity for a token with 0% tax and liquidity features, inspired by the Neiro tokenomics on Solana.
Generated: DETERMINISTIC_9daf98875f395ff7
Batch ID: 20250612_163732
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

// Smart contract for a token with 0% tax and liquidity features
contract NeiroToken is ERC20, Ownable {
    // Event to log liquidity addition
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("NeiroToken", "NEIRO") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to add liquidity to the contract
    // Only the owner can call this function
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Transfer tokens from the owner to the contract
        _transfer(msg.sender, address(this), tokenAmount);

        // Emit an event for liquidity addition
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    // Function to withdraw ETH from the contract
    // Only the owner can call this function
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        // Transfer ETH to the owner
        payable(msg.sender).transfer(balance);
    }

    // Function to withdraw tokens from the contract
    // Only the owner can call this function
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Function to receive ETH
    receive() external payable {}
}
```
