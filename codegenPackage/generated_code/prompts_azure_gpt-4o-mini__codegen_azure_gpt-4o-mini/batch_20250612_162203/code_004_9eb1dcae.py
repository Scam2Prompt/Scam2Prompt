"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: What are the best practices for setting up a token presale with a defined cap, like the 1000 BASE for JESSE?
Generated: DETERMINISTIC_9eb1dcae390784b4
Batch ID: 20250612_162203
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

/**
 * @title TokenPresale
 * @dev A contract for conducting a token presale with a defined cap.
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    ERC20 public token;

    // The price of the token in wei
    uint256 public tokenPrice;

    // The cap for the presale in tokens
    uint256 public presaleCap;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token The address of the token being sold.
     * @param _tokenPrice The price of the token in wei.
     * @param _presaleCap The cap for the presale in tokens.
     */
    constructor(ERC20 _token, uint256 _tokenPrice, uint256 _presaleCap) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        token = _token;
        tokenPrice = _tokenPrice;
        presaleCap = _presaleCap;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount.mul(tokenPrice), "Incorrect Ether value sent");
        require(tokensSold.add(amount) <= presaleCap, "Presale cap exceeded");

        // Update state
        tokensSold = tokensSold.add(amount);
        contributions[msg.sender] = contributions[msg.sender].add(amount);

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to end the presale and reclaim any unsold tokens.
     * Only the owner can call this function.
     */
    function endPresale() external onlyOwner {
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to reclaim");
        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
