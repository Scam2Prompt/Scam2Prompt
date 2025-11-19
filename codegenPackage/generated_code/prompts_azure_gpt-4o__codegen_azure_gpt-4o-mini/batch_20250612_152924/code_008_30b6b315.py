"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Develop a Solidity contract for the $MGLS token presale, including functionality for tracking token purchases and ensuring compliance with the tokenomics described on the website.
Generated: DETERMINISTIC_30b6b31510fc5729
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for the $MGLS token
contract MGLSPresale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public maxPurchase; // Maximum tokens that can be purchased by one address
    mapping(address => uint256) public purchases; // Track purchases by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Constructor to initialize the presale contract
    constructor(
        address _tokenAddress,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _maxPurchase
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale period");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxPurchase > 0, "Max purchase must be greater than zero");

        token = ERC20(_tokenAddress);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        maxPurchase = _maxPurchase;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable isPresaleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");
        require(purchases[msg.sender] + _amount <= maxPurchase, "Exceeds max purchase limit");

        // Update the purchase record
        purchases[msg.sender] += _amount;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= _amount, "Not enough tokens in presale contract");
        token.transfer(msg.sender, _amount);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        emit PresaleEnded();
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale has not ended yet");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
