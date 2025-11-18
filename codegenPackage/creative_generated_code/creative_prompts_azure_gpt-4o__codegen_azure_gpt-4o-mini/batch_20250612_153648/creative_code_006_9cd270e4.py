"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogodoges.pages.dev
Prompt: Provide code to implement a token presale mechanism with multiple stages, including price adjustments and transaction processing, as described in the Dogodoge presale stages.
Generated: DETERMINISTIC_9cd270e4d76e8322
Batch ID: 20250612_153648
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

contract TokenPresale {
    // State variables
    address public owner;
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokensSold;
    uint256 public totalTokens;
    uint256 public tokenPrice; // Price per token in wei
    mapping(address => uint256) public contributions;

    enum SaleStage { NOT_STARTED, STAGE_ONE, STAGE_TWO, STAGE_THREE, ENDED }
    SaleStage public currentStage;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStageUpdated(SaleStage newStage);

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the presale
    constructor(uint256 _totalTokens, uint256 _presaleDuration) {
        owner = msg.sender;
        totalTokens = _totalTokens;
        presaleStart = block.timestamp;
        presaleEnd = presaleStart + _presaleDuration;
        currentStage = SaleStage.STAGE_ONE;
        tokenPrice = 0.01 ether; // Starting price for stage one
    }

    // Function to purchase tokens during presale
    function buyTokens(uint256 tokenAmount) external payable {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(currentStage != SaleStage.ENDED, "Presale has ended");
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether sent");
        require(tokensSold + tokenAmount <= totalTokens, "Not enough tokens available");

        // Record contribution
        contributions[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to update the presale stage and price
    function updatePresaleStage(SaleStage newStage) external onlyOwner {
        require(newStage > currentStage && newStage != SaleStage.ENDED, "Invalid stage transition");

        currentStage = newStage;

        // Adjust token price based on the stage
        if (newStage == SaleStage.STAGE_TWO) {
            tokenPrice = 0.02 ether; // Price for stage two
        } else if (newStage == SaleStage.STAGE_THREE) {
            tokenPrice = 0.03 ether; // Price for stage three
        } else if (newStage == SaleStage.ENDED) {
            tokenPrice = 0; // No more purchases allowed
        }

        emit PresaleStageUpdated(newStage);
    }

    // Function to withdraw funds collected during the presale
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale not yet ended");
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct payments not allowed. Use the buyTokens function.");
    }

    // Function to get presale details
    function getPresaleDetails() external view returns (uint256, uint256, uint256, SaleStage) {
        return (tokensSold, totalTokens, tokenPrice, currentStage);
    }
}
```
