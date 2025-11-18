"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a Solidity contract to implement a token presale for $99BTC, including features for price increases at different stages and wallet connection functionality.
Generated: DETERMINISTIC_52f8ef06f8684699
Batch ID: 20250612_154057
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Presale Contract for $99BTC Token
 * @dev This contract implements a presale mechanism with price increases at different stages.
 */
contract Presale is Ownable {
    IERC20 public token; // The token being sold
    uint256 public startTime; // Start time of the presale
    uint256 public endTime; // End time of the presale
    uint256 public price; // Current price of the token in wei
    uint256 public tokensSold; // Total number of tokens sold
    uint256 public constant INITIAL_PRICE = 0.01 ether; // Initial price of the token
    uint256 public constant PRICE_INCREMENT_STAGE1 = 0.02 ether; // Price for stage 1
    uint256 public constant STAGE_DURATION = 1 days; // Duration of each stage
    uint256 public constant MAX_TOKENS = 10000 * 10**18; // Max tokens available for sale

    enum SaleStage { Stage1, Stage2, Stage3 }
    SaleStage public currentStage;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PriceUpdated(uint256 newPrice);

    constructor(address _token, uint256 _duration) {
        token = IERC20(_token);
        startTime = block.timestamp;
        endTime = startTime + _duration;
        price = INITIAL_PRICE;
        currentStage = SaleStage.Stage1;
    }

    modifier onlyWhileOpen() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale is not active");
        _;
    }

    modifier onlyValidPurchase(uint256 amount) {
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold + amount <= MAX_TOKENS, "Not enough tokens available");
        _;
    }

    /**
     * @dev Buy tokens during the presale
     * @param amount The amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable onlyWhileOpen onlyValidPurchase(amount) {
        uint256 totalCost = price * amount;
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Update tokens sold
        tokensSold += amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);

        // Refund any excess Ether sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        // Update the price if applicable
        updatePrice();
    }

    /**
     * @dev Update the price based on the current stage
     */
    function updatePrice() internal {
        if (currentStage == SaleStage.Stage1 && block.timestamp >= startTime + STAGE_DURATION) {
            price = PRICE_INCREMENT_STAGE1;
            currentStage = SaleStage.Stage2;
            emit PriceUpdated(price);
        }
        // Additional stages can be added here
    }

    /**
     * @dev Withdraw funds from the presale
     */
    function withdraw() external onlyOwner {
        require(block.timestamp > endTime, "Presale is still ongoing");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether transfers
     */
    receive() external payable {
        // Accept Ether directly
    }
}
```
