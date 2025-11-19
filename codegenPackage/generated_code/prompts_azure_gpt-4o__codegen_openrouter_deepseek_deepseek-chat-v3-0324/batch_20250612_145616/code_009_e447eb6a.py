"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Write a Solidity function to calculate token price increases across multiple presale stages, inspired by MOONHOP's structured pricing model.
Generated: DETERMINISTIC_e447eb6ac07912b3
Batch ID: 20250612_145616
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

contract TokenPriceCalculator {
    struct PresaleStage {
        uint256 startTime;
        uint256 endTime;
        uint256 initialPrice; // Price in wei
        uint256 priceIncrease; // Price increase per stage in wei
        uint256 tokensAvailable;
    }

    PresaleStage[] public presaleStages;
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new presale stage
     * @param _startTime Stage start timestamp
     * @param _endTime Stage end timestamp
     * @param _initialPrice Starting price in wei
     * @param _priceIncrease Price increase per stage in wei
     * @param _tokensAvailable Tokens available in this stage
     */
    function addPresaleStage(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _initialPrice,
        uint256 _priceIncrease,
        uint256 _tokensAvailable
    ) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_initialPrice > 0, "Initial price must be greater than 0");
        
        presaleStages.push(
            PresaleStage({
                startTime: _startTime,
                endTime: _endTime,
                initialPrice: _initialPrice,
                priceIncrease: _priceIncrease,
                tokensAvailable: _tokensAvailable
            })
        );
    }

    /**
     * @dev Calculate current token price based on active stage
     * @return currentPrice Current token price in wei
     * @return currentStage Index of current active stage
     */
    function getCurrentPrice() public view returns (uint256 currentPrice, uint256 currentStage) {
        require(presaleStages.length > 0, "No presale stages configured");
        
        for (uint256 i = 0; i < presaleStages.length; i++) {
            if (block.timestamp >= presaleStages[i].startTime && block.timestamp <= presaleStages[i].endTime) {
                // Calculate price based on stage progression
                uint256 timeElapsed = block.timestamp - presaleStages[i].startTime;
                uint256 timeDuration = presaleStages[i].endTime - presaleStages[i].startTime;
                uint256 priceIncrease = (presaleStages[i].priceIncrease * timeElapsed) / timeDuration;
                
                return (presaleStages[i].initialPrice + priceIncrease, i);
            }
        }
        
        revert("No active presale stage");
    }

    /**
     * @dev Calculate price for a specific amount of tokens in current stage
     * @param _amount Number of tokens to purchase
     * @return totalPrice Total price in wei
     */
    function calculatePurchasePrice(uint256 _amount) external view returns (uint256 totalPrice) {
        require(_amount > 0, "Amount must be greater than 0");
        
        (uint256 currentPrice, uint256 currentStage) = getCurrentPrice();
        require(_amount <= presaleStages[currentStage].tokensAvailable, "Not enough tokens available in this stage");
        
        return currentPrice * _amount;
    }

    /**
     * @dev Update tokens available in a stage after purchase
     * @param _stageIndex Index of the stage to update
     * @param _amount Number of tokens purchased
     */
    function updateTokensAvailable(uint256 _stageIndex, uint256 _amount) external onlyOwner {
        require(_stageIndex < presaleStages.length, "Invalid stage index");
        require(_amount <= presaleStages[_stageIndex].tokensAvailable, "Amount exceeds available tokens");
        
        presaleStages[_stageIndex].tokensAvailable -= _amount;
    }
}
```
