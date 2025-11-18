"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-qdclhqzos-miketoken.vercel.app
Prompt: Write a Solidity contract for launching a token presale with 35% allocation, following the tokenomics distribution described for Mike Token.
Generated: DETERMINISTIC_117aaed313863f43
Batch ID: 20250612_154432
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
 * @title MikeTokenPresale
 * @dev Contract for launching a presale of the Mike Token with 35% allocation.
 */
contract MikeTokenPresale is Ownable {
    // State variables
    IERC20 public token; // Token being sold
    uint256 public presaleEndTime; // End time of the presale
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public totalTokensSold; // Total tokens sold in the presale
    uint256 public presaleAllocation; // Total tokens allocated for presale
    mapping(address => uint256) public contributions; // Tracking contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 totalTokensSold);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _presaleEndTime End time for the presale in Unix timestamp.
     * @param _tokenPrice Price of one token in wei.
     * @param _presaleAllocation Total tokens allocated for presale.
     */
    constructor(IERC20 _token, uint256 _presaleEndTime, uint256 _tokenPrice, uint256 _presaleAllocation) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleEndTime > block.timestamp, "End time must be in the future");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleAllocation > 0, "Presale allocation must be greater than zero");

        token = _token;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        presaleAllocation = _presaleAllocation;
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");
        require(totalTokensSold + amount <= presaleAllocation, "Exceeds presale allocation");

        // Update state
        contributions[msg.sender] += amount;
        totalTokensSold += amount;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Ends the presale and transfers the remaining tokens to the owner.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");

        // Transfer remaining tokens to owner
        uint256 remainingTokens = presaleAllocation - totalTokensSold;
        if (remainingTokens > 0) {
            require(token.transfer(owner(), remainingTokens), "Token transfer failed");
        }

        emit PresaleEnded(totalTokensSold);
    }

    /**
     * @dev Allows the owner to withdraw collected Ether from the presale.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
