"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the $DOG token presale described on the webpage, including features like a presale cap and ETH-based token allocation.
Generated: DETERMINISTIC_207152e8f4efe157
Batch ID: 20250612_153420
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

// Import OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for a token
contract TokenPresale is Ownable {
    // Events to log important actions
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Token being sold
    ERC20 public token;

    // Presale parameters
    uint256 public presaleCap; // Maximum amount of ETH that can be raised
    uint256 public tokenExchangeRate; // Tokens per ETH
    uint256 public totalRaised; // Total ETH raised during presale
    bool public presaleEnded; // Status of presale

    // Mapping to track contributions of buyers
    mapping(address => uint256) public contributions;

    // Constructor to initialize the token and presale parameters
    constructor(ERC20 _token, uint256 _presaleCap, uint256 _tokenExchangeRate) {
        require(_presaleCap > 0, "Presale cap should be greater than zero");
        require(_tokenExchangeRate > 0, "Exchange rate should be greater than zero");

        token = _token;
        presaleCap = _presaleCap;
        tokenExchangeRate = _tokenExchangeRate;
        presaleEnded = false;
    }

    // Function to purchase tokens during presale
    function buyTokens() external payable {
        require(!presaleEnded, "Presale has ended");
        require(msg.value > 0, "ETH amount must be greater than zero");
        require(totalRaised + msg.value <= presaleCap, "Presale cap reached");

        // Calculate amount of tokens to allocate
        uint256 tokensToBuy = msg.value * tokenExchangeRate;

        // Update state variables
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Emit an event for successful purchase
        emit TokensPurchased(msg.sender, tokensToBuy);

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokensToBuy);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale already ended");

        presaleEnded = true;
        emit PresaleEnded();
    }

    // Function to withdraw ETH raised during presale
    function withdraw() external onlyOwner {
        require(presaleEnded, "Presale has not ended yet");
        
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner's address
        payable(owner()).transfer(balance);
    }

    // Function to retrieve the current token balance of the contract
    function tokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }

    // Fallback function to accept ETH
    receive() external payable {
        buyTokens();
    }
}
```
