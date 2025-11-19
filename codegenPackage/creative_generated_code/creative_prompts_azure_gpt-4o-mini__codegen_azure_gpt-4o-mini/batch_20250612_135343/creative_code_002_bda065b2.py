"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogemob.pages.dev
Prompt: Create a Solidity smart contract that implements a simple buy and sell mechanism for the DOGEMOB token, ensuring a 0% buy and sell tax.
Generated: DETERMINISTIC_bda065b255b6011f
Batch ID: 20250612_135343
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

/**
 * @title DogeMobTokenMarket
 * @dev A simple smart contract for buying and selling DOGEMOB tokens
 */
contract DogeMobTokenMarket is Ownable {
    IERC20 public dogeMobToken; // The DOGEMOB token contract reference
    uint256 public tokenPrice;  // Price of the DOGEMOB token in wei

    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);
    event TokensSold(address indexed seller, uint256 tokensSold, uint256 amountReceived);

    /**
     * @dev Constructor to set the DOGEMOB token contract address and initial token price
     * @param _dogeMobToken Address of the DOGEMOB token contract
     * @param _tokenPrice Initial price of the token in wei
     */
    constructor(IERC20 _dogeMobToken, uint256 _tokenPrice) {
        require(address(_dogeMobToken) != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        
        dogeMobToken = _dogeMobToken;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Allows users to buy DOGEMOB tokens
     */
    function buyTokens(uint256 _tokenAmount) external payable {
        require(msg.value == _tokenAmount * tokenPrice, "Incorrect ETH amount sent");
        
        // Transfer tokens to the buyer
        require(dogeMobToken.balanceOf(address(this)) >= _tokenAmount, "Not enough tokens in contract");
        require(dogeMobToken.transfer(msg.sender, _tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, _tokenAmount);
    }

    /**
     * @dev Allows users to sell their DOGEMOB tokens
     */
    function sellTokens(uint256 _tokenAmount) external {
        require(_tokenAmount > 0, "Must sell at least one token");
        
        // Calculate the amount of ETH to return
        uint256 amountToReturn = _tokenAmount * tokenPrice;
        require(address(this).balance >= amountToReturn, "Not enough ETH in contract");

        // Transfer tokens from the seller to the contract
        require(dogeMobToken.transferFrom(msg.sender, address(this), _tokenAmount), "Token transfer failed");

        // Transfer ETH to the seller
        payable(msg.sender).transfer(amountToReturn);

        emit TokensSold(msg.sender, _tokenAmount, amountToReturn);
    }

    /**
     * @dev Allows the owner to withdraw ETH from the contract
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Allows the owner to set a new token price
     * @param _newPrice New price of the DOGEMOB token in wei
     */
    function setTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }
}
```
