"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ambient-claim.live
Prompt: Create a Solidity-based token sale contract that includes early participant bonuses and fair pricing, aligned with Ambient Finance's ICO strategy.
Generated: DETERMINISTIC_239845be2d6c0261
Batch ID: 20250612_152249
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

contract TokenSale {
    // Basic declarations
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensSold; // Total tokens sold
    uint256 public constant MAX_SUPPLY = 1000000; // Maximum token supply
    uint256 public constant BONUS_PERIOD = 7 days; // Early bonus period duration
    uint256 public constant BONUS_RATE = 20; // Bonus percentage (20%)

    uint256 public saleStartTime; // Start time of the token sale

    mapping(address => uint256) public balances; // Tracks token balances for participants

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event SaleStarted(uint256 startTime);
    event SaleEnded(uint256 endTime);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation.");
        _;
    }

    modifier saleIsActive() {
        require(saleStartTime > 0 && block.timestamp < saleStartTime + BONUS_PERIOD, "Sale is not active.");
        _;
    }

    modifier validPurchase(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero.");
        require(totalTokensSold + amount <= MAX_SUPPLY, "Purchase exceeds maximum token supply.");
        _;
    }

    constructor(uint256 _tokenPrice) {
        require(_tokenPrice > 0, "Token price must be greater than zero.");
        owner = msg.sender; // Set contract deployer as owner
        tokenPrice = _tokenPrice; // Set the token price
    }

    // Start the token sale
    function startSale() external onlyOwner {
        require(saleStartTime == 0, "Sale already started.");
        saleStartTime = block.timestamp; // Record the start time
        emit SaleStarted(saleStartTime);
    }

    // End the token sale
    function endSale() external onlyOwner {
        require(saleStartTime > 0, "Sale has not started yet.");
        require(block.timestamp >= saleStartTime + BONUS_PERIOD, "Bonus period is not over yet.");
        saleStartTime = 0; // Reset the sale start time
        emit SaleEnded(block.timestamp);
    }

    // Purchase tokens
    function purchaseTokens(uint256 amount) external payable saleIsActive validPurchase(amount) {
        uint256 cost = calculateCost(amount);
        require(msg.value >= cost, "Insufficient ETH sent.");

        // Update state
        totalTokensSold += amount;
        balances[msg.sender] += amount;

        // Refund excess ETH, if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        emit TokensPurchased(msg.sender, amount, cost);
    }

    // Calculate token cost with early bird bonus, if applicable
    function calculateCost(uint256 amount) public view returns (uint256) {
        uint256 baseCost = amount * tokenPrice;

        // Apply bonus if within the bonus period
        if (block.timestamp <= saleStartTime + BONUS_PERIOD) {
            uint256 bonus = (baseCost * BONUS_RATE) / 100;
            return baseCost - bonus;
        }

        return baseCost;
    }

    // Withdraw funds collected from the token sale
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal.");
        payable(owner).transfer(contractBalance); // Transfer funds to the owner
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external {
        revert("Use purchaseTokens function to buy tokens.");
    }

    receive() external payable {
        revert("Use purchaseTokens function to buy tokens.");
    }
}
```
