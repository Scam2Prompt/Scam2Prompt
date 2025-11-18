"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Develop a smart contract in Solidity for a presale token allocation system similar to MOONHOP's, ensuring security and gradual price increases across 50 stages.
Generated: DETERMINISTIC_af060b6285d44285
Batch ID: 20250612_145616
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
 * @title PresaleToken
 * @dev Smart contract for a presale token allocation system with gradual price increases.
 */
contract PresaleToken {
    // State variables
    address public owner;
    uint256 public totalSupply;
    uint256 public tokensSold;
    uint256 public currentStage;
    uint256 public constant totalStages = 50; // Total number of stages in the presale
    uint256 public constant tokensPerStage = 1000 ether; // Tokens available per stage
    uint256 public basePrice = 0.01 ether; // Base price per token in the first stage
    uint256 public priceIncrement = 0.0001 ether; // Price increment for each stage

    mapping(address => uint256) public balances; // User balances of tokens

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event StageAdvanced(uint256 newStage);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier validPurchase(uint256 amount) {
        require(amount > 0, "Cannot purchase zero tokens");
        require(currentStage < totalStages, "Presale has ended");
        require(tokensSold + amount <= currentStage * tokensPerStage, "Not enough tokens available in this stage");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale
     * @param amount The amount of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable validPurchase(amount) {
        uint256 tokenPrice = getCurrentTokenPrice();
        uint256 totalCost = tokenPrice * amount;

        require(msg.value >= totalCost, "Insufficient funds sent");
        
        // Transfer tokens and update state
        balances[msg.sender] += amount;
        tokensSold += amount;

        // Refund excess Ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        emit TokensPurchased(msg.sender, amount, totalCost);
        
        // Check if we need to advance to the next stage
        if (tokensSold >= currentStage * tokensPerStage) {
            advanceStage();
        }
    }

    /**
     * @dev Function to advance to the next stage of the presale
     */
    function advanceStage() internal {
        require(currentStage < totalStages, "Already at the final stage");
        currentStage++;
        emit StageAdvanced(currentStage);
    }

    /**
     * @dev Function to get the current price per token
     * @return The current price of a token in wei
     */
    function getCurrentTokenPrice() public view returns (uint256) {
        return basePrice + (currentStage * priceIncrement);
    }

    /**
     * @dev Function to withdraw funds from the contract
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Function to retrieve the contract's balance
     * @return The balance of the contract in wei
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to get the number of tokens held by a specific address
     * @param user The address to query the balance of
     * @return The number of tokens held by the user
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
