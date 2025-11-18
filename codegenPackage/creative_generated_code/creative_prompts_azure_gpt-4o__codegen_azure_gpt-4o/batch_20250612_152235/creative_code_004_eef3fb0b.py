"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdogai-presale.pages.dev
Prompt: Write a step-by-step guide in Solidity to create a token presale contract with staged price increases, as outlined in the WienerAI presale process.
Generated: DETERMINISTIC_eef3fb0b13c42434
Batch ID: 20250612_152235
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
 * @title TokenPresale
 * @dev A contract for managing token presales with staged price increases.
 */
contract TokenPresale {
    // Address of the token being sold
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Current stage of the presale
    uint256 public currentStage;

    // Mapping to store token prices for each stage
    mapping(uint256 => uint256) public stagePrices;

    // Mapping to store the maximum amount of tokens purchasable in each stage
    mapping(uint256 => uint256) public stageTokenLimits;

    // Mapping to track the total amount of tokens sold per stage
    mapping(uint256 => uint256) public stageTokensSold;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 stage);

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure the presale is active
    modifier presaleActive(uint256 stage) {
        require(stage == currentStage, "Invalid presale stage");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the token being sold
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
        currentStage = 1; // Start at stage 1
    }

    /**
     * @dev Set the token price for a specific stage.
     * @param stage Stage index
     * @param price Price per token in wei for the given stage
     */
    function setStagePrice(uint256 stage, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        stagePrices[stage] = price;
    }

    /**
     * @dev Set the token limit for a specific stage.
     * @param stage Stage index
     * @param limit Maximum amount of tokens purchasable in the given stage
     */
    function setStageTokenLimit(uint256 stage, uint256 limit) external onlyOwner {
        require(limit > 0, "Limit must be greater than zero");
        stageTokenLimits[stage] = limit;
    }

    /**
     * @dev Advance to the next presale stage.
     */
    function advanceStage() external onlyOwner {
        currentStage++;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable presaleActive(currentStage) {
        require(amount > 0, "Amount must be greater than zero");
        uint256 price = stagePrices[currentStage];
        require(price > 0, "Price not set for current stage");

        uint256 totalCost = amount * price;
        require(msg.value >= totalCost, "Insufficient funds sent");
        require(stageTokensSold[currentStage] + amount <= stageTokenLimits[currentStage], "Exceeds stage token limit");

        stageTokensSold[currentStage] += amount;

        // Transfer tokens to the buyer
        require(ERC20(tokenAddress).transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, currentStage);
    }

    /**
     * @dev Withdraw funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     */
    function emergencyWithdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(ERC20(tokenAddress).transfer(owner, amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
