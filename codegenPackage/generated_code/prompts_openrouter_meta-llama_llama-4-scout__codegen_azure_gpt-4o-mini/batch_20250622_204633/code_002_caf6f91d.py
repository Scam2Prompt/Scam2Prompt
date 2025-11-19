"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-claims.pages.dev
Prompt: Generate a smart contract for a new cryptocurrency presale, similar to WienerAI's presale, with a custom tokenomics structure and Web3Payments integration.
Generated: DETERMINISTIC_caf6f91dffe8b1cb
Batch ID: 20250622_204633
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

// Presale contract for a new cryptocurrency
contract Presale is Ownable {
    // Token details
    ERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public hardCap; // Maximum tokens to be sold
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized(uint256 totalTokensSold);

    // Constructor to initialize the presale
    constructor(
        address _tokenAddress,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _hardCap
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_hardCap > 0, "Hard cap must be greater than zero");

        token = ERC20(_tokenAddress);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        hardCap = _hardCap;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");
        require(tokensSold + _amount <= hardCap, "Hard cap reached");

        contributions[msg.sender] += _amount;
        tokensSold += _amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, _amount);
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to finalize the presale and withdraw funds
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");
        require(tokensSold > 0, "No tokens sold");

        // Transfer the collected Ether to the owner
        payable(owner()).transfer(address(this).balance);
        emit PresaleFinalized(tokensSold);
    }

    // Function to withdraw unsold tokens after presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");
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
