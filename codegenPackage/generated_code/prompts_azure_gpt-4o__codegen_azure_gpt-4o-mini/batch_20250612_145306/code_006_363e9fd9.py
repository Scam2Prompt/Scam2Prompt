"""
Generated Code Metadata:
========================
Original URL: https://moonflip-presale.vercel.app
Prompt: Create a smart contract template for managing token presales in a decentralized exchange (DEX) inspired by Moon Flip AI DEX.
Generated: DETERMINISTIC_363e9fd93c6c3c48
Batch ID: 20250612_145306
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

// Smart contract for managing token presales
contract TokenPresale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public maxTokens; // Maximum tokens available for presale
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalTokensSold);

    // Constructor to initialize the presale
    constructor(
        address _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _maxTokens
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokens > 0, "Max tokens must be greater than zero");

        token = ERC20(_token);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        maxTokens = _maxTokens;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");
        require(tokensSold + _amount <= maxTokens, "Exceeds max tokens available");

        // Update state
        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, _amount);

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");

        // Transfer the collected Ether to the owner
        payable(owner()).transfer(address(this).balance);

        emit PresaleEnded(tokensSold);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");
        uint256 unsoldTokens = maxTokens - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens back to the owner
        token.transfer(owner(), unsoldTokens);
    }

    // Function to check the presale status
    function isPresaleActiveCheck() external view returns (bool) {
        return (block.timestamp >= presaleStart && block.timestamp <= presaleEnd);
    }
}
```
