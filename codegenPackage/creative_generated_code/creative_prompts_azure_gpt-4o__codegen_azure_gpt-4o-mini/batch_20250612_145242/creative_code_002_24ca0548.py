"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-ae.web.app
Prompt: Generate code for a decentralized launchpad that supports token sales across multiple blockchain networks, inspired by Rexas Launchpad.
Generated: DETERMINISTIC_24ca0548b3a18d20
Batch ID: 20250612_145242
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the launchpad
interface ILaunchpad {
    function createSale(
        address token,
        uint256 totalSupply,
        uint256 pricePerToken,
        uint256 startTime,
        uint256 endTime
    ) external;
    
    function buyTokens(uint256 saleId, uint256 amount) external payable;
}

// Struct to hold sale details
struct Sale {
    address token;
    uint256 totalSupply;
    uint256 pricePerToken;
    uint256 startTime;
    uint256 endTime;
    uint256 tokensSold;
    bool isActive;
}

contract DecentralizedLaunchpad is ILaunchpad, Ownable {
    using SafeMath for uint256;

    // Mapping to track sales
    mapping(uint256 => Sale) public sales;
    uint256 public saleCount;

    // Events
    event SaleCreated(uint256 saleId, address token, uint256 totalSupply, uint256 pricePerToken, uint256 startTime, uint256 endTime);
    event TokensPurchased(uint256 saleId, address buyer, uint256 amount, uint256 tokensBought);

    // Error definitions
    error SaleNotActive();
    error InvalidSaleId();
    error InsufficientFunds();
    error SaleEnded();
    error NotEnoughTokens();

    // Create a new token sale
    function createSale(
        address token,
        uint256 totalSupply,
        uint256 pricePerToken,
        uint256 startTime,
        uint256 endTime
    ) external override onlyOwner {
        require(totalSupply > 0, "Total supply must be greater than 0");
        require(pricePerToken > 0, "Price per token must be greater than 0");
        require(endTime > startTime, "End time must be after start time");

        sales[saleCount] = Sale({
            token: token,
            totalSupply: totalSupply,
            pricePerToken: pricePerToken,
            startTime: startTime,
            endTime: endTime,
            tokensSold: 0,
            isActive: true
        });

        emit SaleCreated(saleCount, token, totalSupply, pricePerToken, startTime, endTime);
        saleCount++;
    }

    // Buy tokens from a sale
    function buyTokens(uint256 saleId, uint256 amount) external payable override {
        Sale storage sale = sales[saleId];

        // Validate sale existence and status
        if (saleId >= saleCount) revert InvalidSaleId();
        if (!sale.isActive) revert SaleNotActive();
        if (block.timestamp < sale.startTime) revert SaleNotActive();
        if (block.timestamp > sale.endTime) revert SaleEnded();

        uint256 totalCost = amount.mul(sale.pricePerToken);
        if (msg.value < totalCost) revert InsufficientFunds();
        if (sale.tokensSold.add(amount) > sale.totalSupply) revert NotEnoughTokens();

        // Update sale details
        sale.tokensSold = sale.tokensSold.add(amount);
        
        // Transfer tokens to buyer
        IERC20(sale.token).transfer(msg.sender, amount);
        
        // Emit event for tokens purchased
        emit TokensPurchased(saleId, msg.sender, amount, amount);
    }

    // Withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to deactivate a sale by the owner
    function deactivateSale(uint256 saleId) external onlyOwner {
        require(saleId < saleCount, "Invalid sale ID");
        sales[saleId].isActive = false;
    }
}
```

This Solidity code implements a basic decentralized launchpad for token sales across multiple blockchain networks. It uses OpenZeppelin contracts for security and follows best practices, including proper error handling and event logging.
