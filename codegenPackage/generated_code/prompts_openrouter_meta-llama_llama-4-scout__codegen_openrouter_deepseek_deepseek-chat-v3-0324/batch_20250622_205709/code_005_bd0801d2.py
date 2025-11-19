"""
Generated Code Metadata:
========================
Original URL: https://app-shibabudz.web.app
Prompt: Write a function in Solidity to create a smart contract for buying and selling BUDZ tokens.
Generated: DETERMINISTIC_bd0801d2bae2b4e7
Batch ID: 20250622_205709
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BUDZToken is ERC20, Ownable {
    using SafeMath for uint256;
    
    uint256 public tokenPrice;
    uint256 public tokensSold;
    
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensSold(address indexed seller, uint256 amount, uint256 revenue);
    event PriceUpdated(uint256 newPrice);
    
    constructor(uint256 initialSupply, uint256 _tokenPrice) ERC20("BUDZ Token", "BUDZ") {
        _mint(msg.sender, initialSupply);
        tokenPrice = _tokenPrice;
    }
    
    function buyTokens(uint256 numberOfTokens) external payable {
        require(numberOfTokens > 0, "Number of tokens must be greater than 0");
        uint256 cost = numberOfTokens.mul(tokenPrice);
        require(msg.value >= cost, "Insufficient ETH sent");
        
        _transfer(owner(), msg.sender, numberOfTokens);
        tokensSold = tokensSold.add(numberOfTokens);
        
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }
        
        emit TokensPurchased(msg.sender, numberOfTokens, cost);
    }
    
    function sellTokens(uint256 numberOfTokens) external {
        require(numberOfTokens > 0, "Number of tokens must be greater than 0");
        require(balanceOf(msg.sender) >= numberOfTokens, "Insufficient token balance");
        
        uint256 revenue = numberOfTokens.mul(tokenPrice);
        _transfer(msg.sender, owner(), numberOfTokens);
        
        payable(msg.sender).transfer(revenue);
        emit TokensSold(msg.sender, numberOfTokens, revenue);
    }
    
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than 0");
        tokenPrice = newPrice;
        emit PriceUpdated(newPrice);
    }
    
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
    
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
    
    function getTokenPrice() external view returns (uint256) {
        return tokenPrice;
    }
    
    function getTokensSold() external view returns (uint256) {
        return tokensSold;
    }
}
```
