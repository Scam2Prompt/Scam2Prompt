"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wieneraiclaim.pages.dev
Prompt: Provide code in Solidity for a presale contract that increases token price at specific intervals, mimicking the staged price increase mechanism described in the WienerAI presale.
Generated: DETERMINISTIC_2abaf442eddd361f
Batch ID: 20250612_151117
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

/**
 * @title Presale Contract
 * @dev A token presale contract with staged price increases at specific intervals.
 */
contract TokenPresale {
    // Address of the token owner
    address public owner;

    // Token price (in wei per token)
    uint256 public tokenPrice;

    // Start time of the presale
    uint256 public presaleStartTime;

    // Duration of each stage (in seconds)
    uint256 public stageDuration;

    // Price increment per stage (in wei)
    uint256 public priceIncrement;

    // Maximum number of stages
    uint256 public maxStages;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize presale parameters.
     * @param _initialPrice Initial token price in wei
     * @param _stageDuration Duration of each stage in seconds
     * @param _priceIncrement Price increment per stage in wei
     * @param _maxStages Maximum number of stages
     */
    constructor(
        uint256 _initialPrice,
        uint256 _stageDuration,
        uint256 _priceIncrement,
        uint256 _maxStages
    ) {
        require(_initialPrice > 0, "Initial price must be positive");
        require(_stageDuration > 0, "Stage duration must be positive");
        require(_priceIncrement > 0, "Price increment must be positive");
        require(_maxStages > 0, "Max stages must be positive");

        owner = msg.sender;
        tokenPrice = _initialPrice;
        stageDuration = _stageDuration;
        priceIncrement = _priceIncrement;
        maxStages = _maxStages;
        presaleStartTime = block.timestamp;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param tokenAmount Number of tokens to purchase
     */
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "Token amount must be positive");

        uint256 currentStage = getCurrentStage();
        require(currentStage <= maxStages, "Presale has ended");

        uint256 currentPrice = getCurrentPrice();
        uint256 cost = tokenAmount * currentPrice;

        require(msg.value >= cost, "Insufficient funds sent");

        // Refund excess funds if overpaid
        uint256 excess = msg.value - cost;
        if (excess > 0) {
            payable(msg.sender).transfer(excess);
        }

        // Emit event for transparency
        emit TokensPurchased(msg.sender, tokenAmount, cost);

        // Logic to transfer tokens should be added here
        // e.g., integrating with an ERC20 token contract
    }

    /**
     * @dev Get the current stage based on time elapsed.
     * @return Current stage number
     */
    function getCurrentStage() public view returns (uint256) {
        uint256 elapsed = block.timestamp - presaleStartTime;
        return (elapsed / stageDuration) + 1;
    }

    /**
     * @dev Get the current token price based on the stage.
     * @return Current token price in wei
     */
    function getCurrentPrice() public view returns (uint256) {
        uint256 currentStage = getCurrentStage();
        if (currentStage > maxStages) {
            return tokenPrice + (maxStages - 1) * priceIncrement;
        }
        return tokenPrice + (currentStage - 1) * priceIncrement;
    }

    /**
     * @dev Withdraw funds to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Update presale parameters. Can only be called by the owner.
     * @param _newPrice New initial price in wei
     * @param _newStageDuration New stage duration in seconds
     * @param _newPriceIncrement New price increment in wei
     * @param _newMaxStages New maximum number of stages
     */
    function updatePresaleParameters(
        uint256 _newPrice,
        uint256 _newStageDuration,
        uint256 _newPriceIncrement,
        uint256 _newMaxStages
    ) external onlyOwner {
        require(_newPrice > 0, "Initial price must be positive");
        require(_newStageDuration > 0, "Stage duration must be positive");
        require(_newPriceIncrement > 0, "Price increment must be positive");
        require(_newMaxStages > 0, "Max stages must be positive");

        tokenPrice = _newPrice;
        stageDuration = _newStageDuration;
        priceIncrement = _newPriceIncrement;
        maxStages = _newMaxStages;
    }
}
```
