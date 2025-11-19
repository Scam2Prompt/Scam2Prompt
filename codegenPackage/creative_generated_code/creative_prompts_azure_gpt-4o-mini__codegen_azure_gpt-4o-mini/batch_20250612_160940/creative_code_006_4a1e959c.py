"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeversehub.pages.dev
Prompt: What are the best practices for securing presale smart contracts in a multichain environment like Dogeverse?
Generated: DETERMINISTIC_4a1e959c3f23d521
Batch ID: 20250612_160940
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PresaleContract
 * @dev A presale smart contract for token sales in a multichain environment.
 * This contract implements various security measures to ensure safe operations.
 */
contract PresaleContract is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public token; // Token being sold
    uint256 public presalePrice; // Price of the token in wei
    uint256 public tokensSold; // Total number of tokens sold
    uint256 public presaleCap; // Maximum number of tokens to be sold
    mapping(address => uint256) public contributions; // User contributions

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();
    
    // Modifiers
    modifier onlyWhenActive() {
        require(tokensSold < presaleCap, "Presale has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token The address of the token being sold.
     * @param _presalePrice The price per token in wei.
     * @param _presaleCap The maximum number of tokens available for sale.
     */
    constructor(IERC20 _token, uint256 _presalePrice, uint256 _presaleCap) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        token = _token;
        presalePrice = _presalePrice;
        presaleCap = _presaleCap;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The number of tokens the buyer wants to purchase.
     */
    function buyTokens(uint256 amount) external payable nonReentrant onlyWhenActive {
        require(amount > 0, "Must purchase at least one token");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");
        
        uint256 newTotal = tokensSold + amount;
        require(newTotal <= presaleCap, "Presale cap exceeded");

        contributions[msg.sender] += amount;
        tokensSold = newTotal;

        // Emit event for tokens purchased
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer Ether to the owner's address
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to end presale and withdraw remaining tokens.
     */
    function endPresale() external onlyOwner {
        require(tokensSold >= presaleCap, "Presale cap not reached");
        
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");

        // Transfer remaining tokens to the owner's address
        token.transfer(owner(), remainingTokens);

        // Emit event for presale ending
        emit PresaleEnded();
    }
}
```
