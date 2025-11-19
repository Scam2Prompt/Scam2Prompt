"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Develop a smart contract that supports fair token launches, inspired by CowSwap's "Fair Sales" concept.
Generated: DETERMINISTIC_8bd312333bf812a1
Batch ID: 20250612_150858
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// FairToken is an ERC20 token that supports fair token launches
contract FairToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when a new sale is created
    event SaleCreated(uint256 indexed saleId, uint256 tokenAmount, uint256 pricePerToken, uint256 startTime, uint256 endTime);
    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 indexed saleId, uint256 amountSpent, uint256 tokensReceived);

    struct Sale {
        uint256 tokenAmount; // Total amount of tokens for sale
        uint256 pricePerToken; // Price per token in wei
        uint256 startTime; // Start time of the sale
        uint256 endTime; // End time of the sale
        bool isActive; // Sale status
    }

    // Mapping of saleId to Sale details
    mapping(uint256 => Sale) public sales;
    uint256 public saleCount; // Counter for sales

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to create a new sale
    function createSale(uint256 tokenAmount, uint256 pricePerToken, uint256 duration) external onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(pricePerToken > 0, "Price per token must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from owner to contract for the sale
        _transfer(msg.sender, address(this), tokenAmount);

        // Create a new sale
        saleCount++;
        sales[saleCount] = Sale({
            tokenAmount: tokenAmount,
            pricePerToken: pricePerToken,
            startTime: block.timestamp,
            endTime: block.timestamp.add(duration),
            isActive: true
        });

        emit SaleCreated(saleCount, tokenAmount, pricePerToken, block.timestamp, block.timestamp.add(duration));
    }

    // Function to purchase tokens during a sale
    function purchaseTokens(uint256 saleId, uint256 tokenAmount) external payable {
        Sale storage sale = sales[saleId];

        // Validate sale
        require(sale.isActive, "Sale is not active");
        require(block.timestamp >= sale.startTime && block.timestamp <= sale.endTime, "Sale is not active");
        require(tokenAmount > 0 && tokenAmount <= sale.tokenAmount, "Invalid token amount");
        require(msg.value == tokenAmount.mul(sale.pricePerToken), "Incorrect Ether value sent");

        // Update sale details
        sale.tokenAmount = sale.tokenAmount.sub(tokenAmount);

        // Transfer tokens to buyer
        _transfer(address(this), msg.sender, tokenAmount);

        // Emit purchase event
        emit TokensPurchased(msg.sender, saleId, msg.value, tokenAmount);

        // If no tokens left, deactivate the sale
        if (sale.tokenAmount == 0) {
            sale.isActive = false;
        }
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(msg.sender).transfer(balance);
    }

    // Function to get sale details
    function getSaleDetails(uint256 saleId) external view returns (Sale memory) {
        return sales[saleId];
    }
}
```
