"""
Generated Code Metadata:
========================
Original URL: https://idegensolutionmeme.pages.dev
Prompt: "Write a smart contract in Solidity for managing token sales, including dynamic pricing and allocation of tokens to liquidity pools."
Generated: DETERMINISTIC_0cec9a5f1fa88117
Batch ID: 20250622_211620
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenSale contract for managing token sales with dynamic pricing and liquidity allocation
contract TokenSale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public startTime; // Sale start time
    uint256 public endTime; // Sale end time
    uint256 public basePrice; // Base price of the token in wei
    uint256 public priceIncrement; // Price increment for each token sold
    uint256 public tokensSold; // Total tokens sold
    uint256 public liquidityPoolAllocation; // Percentage of tokens allocated to liquidity pool

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event LiquidityPoolFunded(uint256 amount);

    // Constructor to initialize the token sale
    constructor(
        address _tokenAddress,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _basePrice,
        uint256 _priceIncrement,
        uint256 _liquidityPoolAllocation
    ) {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_basePrice > 0, "Base price must be greater than zero");
        require(_liquidityPoolAllocation <= 100, "Allocation must be between 0 and 100");

        token = ERC20(_tokenAddress);
        startTime = _startTime;
        endTime = _endTime;
        basePrice = _basePrice;
        priceIncrement = _priceIncrement;
        liquidityPoolAllocation = _liquidityPoolAllocation;
    }

    // Modifier to check if the sale is active
    modifier saleActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale is not active");
        _;
    }

    // Function to calculate the current price of the token
    function currentPrice() public view returns (uint256) {
        return basePrice + (tokensSold * priceIncrement);
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 _amount) external payable saleActive {
        uint256 totalCost = currentPrice() * _amount;
        require(msg.value >= totalCost, "Insufficient funds sent");

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= _amount, "Not enough tokens available");
        tokensSold += _amount;
        token.transfer(msg.sender, _amount);

        // Emit event for tokens purchased
        emit TokensPurchased(msg.sender, _amount, totalCost);

        // Allocate tokens to liquidity pool if applicable
        if (liquidityPoolAllocation > 0) {
            uint256 liquidityAmount = (_amount * liquidityPoolAllocation) / 100;
            token.transfer(owner(), liquidityAmount);
            emit LiquidityPoolFunded(liquidityAmount);
        }

        // Refund excess ether if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after the sale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale is still active");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ether transfers not allowed");
    }
}
```
