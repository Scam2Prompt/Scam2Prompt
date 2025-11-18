"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Generate a Solidity smart contract for DOGE20 presale, ensuring fair token distribution and wallet validation.
Generated: DETERMINISTIC_0d68b1c9cacbf761
Batch ID: 20250612_153400
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

contract DOGE20Presale {
    // State variables
    address public owner;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public tokensSold;
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** 18; // Total tokens available for presale
    mapping(address => uint256) public balances;
    
    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalSpent);
    event PresaleEnded(uint256 totalTokensSold);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the presale
    constructor(uint256 _tokenPrice) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        owner = msg.sender;
        tokenPrice = _tokenPrice;
    }
    
    // Function to buy tokens
    function buyTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "You must buy at least one token");
        require(tokensSold + tokenAmount <= MAX_TOKENS, "Not enough tokens left for sale");
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether value sent");

        // Update the state
        balances[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        emit PresaleEnded(tokensSold);
        
        // Transfer funds to owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to check the contract's token balance
    function getTokenBalance() external view returns (uint256) {
        return MAX_TOKENS - tokensSold;
    }

    // Function to withdraw accidentally sent ERC20 tokens
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Invalid amount");
        
        // Transfer ERC20 tokens back to owner
        IERC20(tokenAddress).transfer(owner, amount);
    }
    
    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}

// ERC20 interface for token withdrawal
interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
}
```
