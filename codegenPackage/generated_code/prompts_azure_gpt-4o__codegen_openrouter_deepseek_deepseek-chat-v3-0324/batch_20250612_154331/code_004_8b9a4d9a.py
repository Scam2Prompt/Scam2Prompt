"""
Generated Code Metadata:
========================
Original URL: https://get-trump-gift.pages.dev
Prompt: Create a smart contract on Solana that allows users to deposit Ethereum and receive "$TRUMP" tokens, simulating the functionality described on the site.
Generated: DETERMINISTIC_8b9a4d9aaaee8e2c
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TRUMP Token Contract
 * @dev ERC20 token contract that mints TRUMP tokens when users deposit ETH
 */
contract TrumpToken is ERC20, Ownable {
    uint256 public constant TOKEN_PRICE = 0.0001 ether; // Price per TRUMP token in ETH
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    /**
     * @dev Constructor that initializes the ERC20 token
     */
    constructor() ERC20("TRUMP", "TRUMP") {
        _mint(msg.sender, MAX_SUPPLY / 2); // Mint initial supply to contract owner
    }

    /**
     * @dev Function to buy TRUMP tokens by sending ETH
     */
    function buyTokens() external payable {
        require(msg.value > 0, "TrumpToken: ETH amount must be greater than 0");
        
        uint256 tokenAmount = msg.value / TOKEN_PRICE;
        require(tokenAmount > 0, "TrumpToken: ETH amount too small to buy tokens");
        
        require(totalSupply() + tokenAmount <= MAX_SUPPLY, "TrumpToken: Max supply exceeded");
        
        _mint(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Function to withdraw ETH from the contract
     * @notice Only owner can call this function
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "TrumpToken: No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to reject direct ETH transfers
     */
    receive() external payable {
        buyTokens();
    }
}
```
