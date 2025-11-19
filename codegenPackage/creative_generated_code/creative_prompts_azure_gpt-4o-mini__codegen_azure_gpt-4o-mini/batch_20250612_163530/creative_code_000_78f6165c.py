"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solnarize-in.pages.dev
Prompt: Generate a smart contract in Solidity for the pre-sale of the $SRIZE token, ensuring it includes features for minimum and maximum buy limits as described on the Solnarize website.
Generated: DETERMINISTIC_78f6165caaa059c8
Batch ID: 20250612_163530
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

contract SRIZEPresale is Ownable {
    // Token to be sold in the presale
    IERC20 public srizeToken;

    // Presale parameters
    uint256 public minimumBuy; // Minimum amount of tokens to buy
    uint256 public maximumBuy; // Maximum amount of tokens to buy
    uint256 public presaleStart; // Start time of the presale
    uint256 public presaleEnd;   // End time of the presale

    // Mapping to track the amount purchased by each address
    mapping(address => uint256) public purchases;

    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        IERC20 _srizeToken,
        uint256 _minimumBuy,
        uint256 _maximumBuy,
        uint256 _presaleStart,
        uint256 _presaleEnd
    ) {
        require(_minimumBuy > 0, "Minimum buy must be greater than 0");
        require(_maximumBuy > _minimumBuy, "Maximum buy must be greater than minimum buy");
        require(_presaleStart < _presaleEnd, "Presale start must be before end");

        srizeToken = _srizeToken;
        minimumBuy = _minimumBuy;
        maximumBuy = _maximumBuy;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 amount) external payable {
        // Validate that the presale is active
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");

        // Check that the amount is within the buy limits
        require(amount >= minimumBuy, "Amount is less than minimum buy limit");
        require(amount <= maximumBuy, "Amount is greater than maximum buy limit");

        // Check that the buyer has not exceeded the maximum purchase limit
        require(purchases[msg.sender] + amount <= maximumBuy, "Total purchase exceeds maximum buy limit");

        // Transfer the equivalent amount of ether to the contract
        // Assuming the token price is 1:1 for simplicity; adjust as necessary
        uint256 totalCost = amount; // Update this according to your pricing model
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Update the purchase record
        purchases[msg.sender] += amount;

        // Transfer tokens to the buyer
        srizeToken.transfer(msg.sender, amount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 balance = srizeToken.balanceOf(address(this));
        require(balance > 0, "No unsold tokens to withdraw");
        srizeToken.transfer(owner(), balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
