"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Develop a Solidity contract for the $MGLS token presale, including functionality for tracking token purchases and ensuring compliance with the tokenomics described on the website.
Generated: DETERMINISTIC_30b6b31510fc5729
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale Contract for $MGLS Token
contract MGLSPresale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start timestamp
    uint256 public presaleEnd; // Presale end timestamp
    uint256 public tokenPrice; // Price per token in wei
    uint256 public tokensSold; // Total tokens sold during presale

    // Mapping to track individual purchases
    mapping(address => uint256) public purchases;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor to initialize presale details
    constructor(ERC20 _token, uint256 _presaleStart, uint256 _presaleEnd, uint256 _tokenPrice) {
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = _token;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
    }

    // Modifier to check if the presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 amount) external payable isPresaleActive {
        uint256 cost = amount * tokenPrice;
        require(msg.value >= cost, "Insufficient funds sent");
        require(amount > 0, "Must purchase at least one token");

        // Transfer tokens to buyer
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available for sale");

        purchases[msg.sender] += amount;
        tokensSold += amount;

        // Transfer tokens from contract to buyer
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, cost);
    }

    // Function to withdraw the collected funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        presaleEnd = block.timestamp; // End the presale immediately
    }

    // Function to set a new token price
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero");
        tokenPrice = newPrice;
    }

    // Fallback function to prevent sending ether directly to contract
    receive() external payable {
        revert("Direct ether transfers not allowed.");
    }

    // Function to get the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
