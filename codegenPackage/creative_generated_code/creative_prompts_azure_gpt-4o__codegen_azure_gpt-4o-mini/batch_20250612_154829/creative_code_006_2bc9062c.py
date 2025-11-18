"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Develop a Solidity smart contract to handle token distribution during the presale, ensuring that buyers receive their $SOPH tokens immediately after payment confirmation.
Generated: DETERMINISTIC_2bc9062c7db079d7
Batch ID: 20250612_154829
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

contract SOPHPresale is Ownable {
    using SafeMath for uint256;

    // Token to be distributed
    IERC20 public sopToken;

    // Presale parameters
    uint256 public rate; // Tokens per wei
    uint256 public presaleEndTime; // End time for presale
    uint256 public totalTokensSold; // Total tokens sold during presale
    uint256 public constant MAX_TOKENS = 10000 * 10**18; // Max tokens available for presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);

    // Constructor to initialize the contract with the token address and presale rate
    constructor(IERC20 _sopToken, uint256 _rate, uint256 _duration) {
        require(address(_sopToken) != address(0), "Invalid token address");
        require(_rate > 0, "Rate must be greater than zero");
        
        sopToken = _sopToken;
        rate = _rate;
        presaleEndTime = block.timestamp.add(_duration);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyTokens();
    }

    // Function to buy tokens
    function buyTokens() public payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Send Ether to buy tokens");

        uint256 tokensToBuy = msg.value.mul(rate);
        require(totalTokensSold.add(tokensToBuy) <= MAX_TOKENS, "Exceeds maximum tokens available");

        totalTokensSold = totalTokensSold.add(tokensToBuy);

        // Transfer tokens to the buyer
        sopToken.transfer(msg.sender, tokensToBuy);

        emit TokensPurchased(msg.sender, msg.value, tokensToBuy);
    }

    // Function for owner to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }

    // Function to withdraw unsold tokens after presale ends (if any)
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");

        uint256 unsoldTokens = MAX_TOKENS.sub(totalTokensSold);
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        sopToken.transfer(owner(), unsoldTokens);
    }
}
```
