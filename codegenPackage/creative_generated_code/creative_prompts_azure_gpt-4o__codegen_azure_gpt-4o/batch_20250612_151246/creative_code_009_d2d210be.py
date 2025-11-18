"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Generate a Solidity contract for managing token presales with multiple stages, where the price increases at each stage, as described in WienerAI's presale process.
Generated: DETERMINISTIC_d2d210be2ae75e89
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TokenPresale
 * @dev Contract for managing token presales with multiple stages where the price increases at each stage.
 */
contract TokenPresale {
    // Address of the token seller (owner)
    address public owner;

    // Token price in wei for each stage
    uint256[] public stagePrices;

    // Current stage of the presale
    uint256 public currentStage;

    // Tokens sold in each stage
    mapping(uint256 => uint256) public tokensSold;

    // Maximum tokens allowed to be sold in each stage
    uint256[] public stageLimits;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 stage);

    // Event emitted when the presale stage changes
    event StageAdvanced(uint256 newStage);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256[] memory _stagePrices, uint256[] memory _stageLimits) {
        require(_stagePrices.length > 0, "Stage prices must be defined");
        require(_stagePrices.length == _stageLimits.length, "Stage prices and limits must match");

        owner = msg.sender;
        stagePrices = _stagePrices;
        stageLimits = _stageLimits;
        currentStage = 0;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(currentStage < stagePrices.length, "Presale has ended");
        require(amount > 0, "Token amount must be greater than 0");

        uint256 stagePrice = stagePrices[currentStage];
        uint256 totalCost = stagePrice * amount;

        require(msg.value >= totalCost, "Insufficient funds sent");
        require(tokensSold[currentStage] + amount <= stageLimits[currentStage], "Stage limit exceeded");

        // Update tokens sold
        tokensSold[currentStage] += amount;

        // Refund any excess funds sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        emit TokensPurchased(msg.sender, amount, currentStage);
    }

    /**
     * @dev Function to advance to the next presale stage.
     * Can only be called by the owner.
     */
    function advanceStage() external onlyOwner {
        require(currentStage < stagePrices.length - 1, "Already at the last stage");
        currentStage++;
        emit StageAdvanced(currentStage);
    }

    /**
     * @dev Function to withdraw funds collected during the presale.
     * Can only be called by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Function to end the presale.
     * Can only be called by the owner.
     */
    function endPresale() external onlyOwner {
        require(currentStage < stagePrices.length, "Presale already ended");
        currentStage = stagePrices.length;
    }

    /**
     * @dev Fallback function to receive funds sent directly to the contract.
     */
    receive() external payable {
        revert("Direct payments not allowed. Use purchaseTokens()");
    }

    /**
     * @dev Function to get the number of stages in the presale.
     * @return Number of presale stages.
     */
    function totalStages() external view returns (uint256) {
        return stagePrices.length;
    }
}
```
