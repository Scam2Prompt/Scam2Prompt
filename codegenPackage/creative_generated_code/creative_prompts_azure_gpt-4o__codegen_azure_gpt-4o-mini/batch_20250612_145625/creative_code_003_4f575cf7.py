"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiindogsclub.pages.dev
Prompt: Create a smart contract on ERC20 for facilitating token purchases during the Bitcoin Dogs presale, ensuring compatibility with the BRC20 wallet claiming process.
Generated: DETERMINISTIC_4f575cf72be1d9b4
Batch ID: 20250612_145625
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BitcoinDogsPresaleToken
 * @dev A smart contract for the Bitcoin Dogs token presale using ERC20 standards.
 */
contract BitcoinDogsPresaleToken is ERC20, Ownable {
    // Mapping to track the amount of tokens each address has purchased
    mapping(address => uint256) public purchasedTokens;

    // Presale parameters
    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per token in wei
    uint256 public constant MAX_TOKENS = 1000000 * 10**decimals(); // Total tokens available for presale
    uint256 public totalTokensSold;

    // Event to log token purchase transactions
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to mint initial supply to the contract owner
    constructor() ERC20("Bitcoin Dogs", "BITDOG") {
        _mint(address(this), MAX_TOKENS); // Mint tokens to the contract itself
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * TOKEN_PRICE, "Incorrect Ether value sent");
        require(totalTokensSold + amount <= MAX_TOKENS, "Not enough tokens left for presale");

        // Update state
        totalTokensSold += amount;
        purchasedTokens[msg.sender] += amount;

        // Transfer tokens from the contract to the buyer
        _transfer(address(this), msg.sender, amount);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw Ether from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to claim any unclaimed tokens after the presale ends.
     * @param amount The amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(purchasedTokens[msg.sender] >= amount, "Insufficient purchased tokens");
        
        // Update state
        purchasedTokens[msg.sender] -= amount;

        // Transfer tokens to the claimant
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Fallback function to prevent Ether from being sent directly to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```

This code provides a basic structure for an ERC20 token contract that facilitates token purchases during a presale. It includes functions for purchasing tokens, withdrawing funds, and claiming purchased tokens, along with necessary error handling and documentation.
