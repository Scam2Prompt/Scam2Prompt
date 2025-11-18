"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptexbit.com
Prompt: Develop a smart contract in Solidity for managing CryptexBit's token sale, ensuring transparency and fairness as described in their token structure.
Generated: DETERMINISTIC_a87285072c2edde8
Batch ID: 20250612_150920
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CryptexBitTokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Token price in wei
    uint256 public tokenPrice;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Sale state
    bool public isSaleActive;

    // Events
    event TokenPurchased(address indexed buyer, uint256 amount);
    event SaleStateChanged(bool isActive);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the token sale
    constructor(IERC20 _token, uint256 _tokenPrice) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        
        token = _token;
        tokenPrice = _tokenPrice;
        isSaleActive = false;
    }

    // Function to start or stop the token sale
    function setSaleState(bool _isActive) external onlyOwner {
        isSaleActive = _isActive;
        emit SaleStateChanged(_isActive);
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 _amount) external payable {
        require(isSaleActive, "Token sale is not active");
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == _amount.mul(tokenPrice), "Incorrect Ether value sent");
        
        uint256 tokenAmount = _amount;
        require(token.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in the contract");

        // Transfer tokens to the buyer
        tokensSold = tokensSold.add(tokenAmount);
        token.transfer(msg.sender, tokenAmount);
        emit TokenPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw Ether from the contract
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }

    // Function to withdraw unsold tokens after the sale
    function withdrawUnsoldTokens() external onlyOwner {
        require(!isSaleActive, "Token sale is still active");

        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
        emit TokensWithdrawn(owner(), unsoldTokens);
    }

    // Function to check the contract balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
