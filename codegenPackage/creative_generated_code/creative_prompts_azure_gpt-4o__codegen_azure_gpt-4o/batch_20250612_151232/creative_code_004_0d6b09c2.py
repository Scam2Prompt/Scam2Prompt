"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Provide code in Solidity for a presale smart contract that mimics WienerAI’s functionality, including stages with increasing token prices and a mechanism to track presale token allocations.
Generated: DETERMINISTIC_0d6b09c269ecbb9f
Batch ID: 20250612_151232
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
 * @title Presale Contract for WienerAI Tokens
 * @dev This contract implements a token presale with stages of increasing token prices and allocation tracking.
 */
contract WienerAIPresale {
    // Owner of the contract
    address public owner;

    // Token price stages (in wei per token)
    uint256[] public priceStages;

    // Total tokens allocated during presale
    mapping(address => uint256) public presaleAllocations;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Current stage
    uint256 public currentStage;

    // Maximum tokens allowed for presale
    uint256 public maxPresaleTokens;

    // Event for presale purchase
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        uint256[] memory _priceStages,
        uint256 _maxPresaleTokens
    ) {
        require(_priceStages.length > 0, "Price stages must be provided");
        require(_maxPresaleTokens > 0, "Max presale tokens must be greater than 0");

        owner = msg.sender;
        priceStages = _priceStages;
        maxPresaleTokens = _maxPresaleTokens;
        currentStage = 0;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(currentStage < priceStages.length, "Presale has ended");
        require(_amount > 0, "Token amount must be greater than zero");
        
        uint256 totalCost = _amount * priceStages[currentStage];
        require(msg.value >= totalCost, "Insufficient payment");
        require(totalTokensSold + _amount <= maxPresaleTokens, "Presale token limit reached");

        // Allocate tokens to buyer
        presaleAllocations[msg.sender] += _amount;
        totalTokensSold += _amount;

        // Refund excess payment if applicable
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        emit TokensPurchased(msg.sender, _amount, totalCost);
    }

    /**
     * @dev Advance to the next stage of the presale.
     */
    function advanceStage() external onlyOwner {
        require(currentStage < priceStages.length - 1, "Already at the last stage");
        currentStage++;
    }

    /**
     * @dev Withdraw funds collected during the presale.
     * @param _amount Amount to withdraw (in wei).
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Get the current token price.
     * @return Price of one token in the current stage, in wei.
     */
    function getCurrentTokenPrice() external view returns (uint256) {
        require(currentStage < priceStages.length, "Presale has ended");
        return priceStages[currentStage];
    }

    /**
     * @dev Get the total tokens allocated to a specific buyer.
     * @param _buyer Address of the buyer.
     * @return Total tokens allocated to the buyer.
     */
    function getTokensAllocated(address _buyer) external view returns (uint256) {
        return presaleAllocations[_buyer];
    }

    // Fallback and receive functions to handle unexpected Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    fallback() external payable {
        revert("Fallback function invoked");
    }
}
```
