"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the $DOG presale, including features like a presale cap, ETH-to-token conversion rates, and wallet connection functionality.
Generated: DETERMINISTIC_22b96ecbf2f521cc
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

// Interface for ERC20 token functions
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenPresale {
    // State variables
    IERC20 public token; // Token being sold
    address public owner; // Owner of the presale contract
    uint256 public presaleCap; // Max amount of ETH that can be raised
    uint256 public totalRaised; // Total amount raised in ETH
    uint256 public tokenPrice; // Price of one token in wei
    mapping(address => uint256) public contributions; // Track individual contributions

    // Events to emit during presale
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 spentETH);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensSold);
    
    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the presale
    constructor(
        address _token,
        uint256 _presaleCap,
        uint256 _tokenPrice
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presaleCap > 0, "Presale cap must be greater than 0");
        require(_tokenPrice > 0, "Token price must be greater than 0");

        token = IERC20(_token);
        presaleCap = _presaleCap;
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to buy tokens");
        require(totalRaised + msg.value <= presaleCap, "Presale cap reached");

        // Calculate how many tokens the buyer will receive
        uint256 amountToBuy = msg.value / tokenPrice;
        require(amountToBuy > 0, "Insufficient ETH to buy tokens");

        // Update state
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, amountToBuy), "Token transfer failed");

        emit TokensPurchased(msg.sender, amountToBuy, msg.value);
    }

    // Function to finalize presale and withdraw funds
    function finalizePresale() external onlyOwner {
        require(totalRaised > 0, "No funds to withdraw");

        // Transfer ETH raised to the owner
        payable(owner).transfer(address(this).balance);
        
        emit PresaleFinalized(totalRaised, token.totalSupply() - token.balanceOf(address(this)));
    }

    // Function to withdraw remaining tokens after the presale
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens to withdraw");
        
        require(token.transfer(owner, remainingTokens), "Token transfer failed");
    }

    // Fallback function to accept ETH
    receive() external payable {
        buyTokens();
    }
}
```
