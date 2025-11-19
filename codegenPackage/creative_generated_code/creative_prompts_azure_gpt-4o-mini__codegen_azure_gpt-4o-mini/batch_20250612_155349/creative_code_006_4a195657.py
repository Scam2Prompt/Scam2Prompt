"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: Provide a code example for a decentralized application (dApp) that allows users to buy IVI Tokens with various cryptocurrencies.
Generated: DETERMINISTIC_4a1956575b4ee00b
Batch ID: 20250612_155349
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract IVIToken is IERC20, Ownable {
    string public name = "IVI Token";
    string public symbol = "IVI";
    uint8 public decimals = 18;
    uint256 private totalSupply_ = 1000000 * (10 ** uint256(decimals));
    
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowed;

    constructor() {
        balances[msg.sender] = totalSupply_;
    }

    function totalSupply() external view override returns (uint256) {
        return totalSupply_;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        allowed[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowed[sender][msg.sender] >= amount, "Allowance exceeded");
        
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowed[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return allowed[owner][spender];
    }
}

contract TokenSale is Ownable {
    IVIToken public token;
    uint256 public price; // Price in wei per IVI token

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    constructor(IVIToken _token, uint256 _price) {
        token = _token;
        price = _price;
    }

    // Purchase IVI tokens with Ether
    function buyTokens(uint256 tokenAmount) external payable {
        uint256 totalCost = tokenAmount * price;
        require(msg.value >= totalCost, "Insufficient ETH sent");

        uint256 excess = msg.value - totalCost;
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in the reserve");

        token.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount, totalCost);
        
        // Refund excess Ether if applicable
        if (excess > 0) {
            payable(msg.sender).transfer(excess);
        }
    }

    // Owner can withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Allow owner to update the price of tokens
    function setPrice(uint256 newPrice) external onlyOwner {
        price = newPrice;
    }

    // Allow the owner to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens in contract");
        token.transfer(owner(), amount);
    }
}
```
