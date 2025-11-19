"""
Generated Code Metadata:
========================
Original URL: https://crop-6qi.pages.dev
Prompt: Write a smart contract in Solidity for a cross-game, cross-chain decentralized player network's token sale, with a first-come-first-served allocation mechanism.
Generated: DETERMINISTIC_23f67c1a11b205cb
Batch ID: 20250622_210443
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

/**
 * @title CrossGameTokenSale
 * @dev A smart contract for a token sale with a first-come-first-served allocation mechanism.
 *      Designed for a cross-game, cross-chain decentralized player network.
 */
contract CrossGameTokenSale {
    // Token sale parameters
    address public owner; // Owner of the contract
    uint256 public tokenPrice; // Price per token in wei
    uint256 public maxTokensPerBuyer; // Maximum tokens a buyer can purchase
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Total tokens sold so far

    // Mapping to track buyer allocations
    mapping(address => uint256) public buyerAllocations;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleEnded(address indexed owner, uint256 tokensSold);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if the sale is still active
    modifier saleActive() {
        require(tokensSold < totalTokensForSale, "Token sale has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the token sale parameters.
     * @param _tokenPrice Price per token in wei.
     * @param _maxTokensPerBuyer Maximum tokens a buyer can purchase.
     * @param _totalTokensForSale Total tokens available for sale.
     */
    constructor(
        uint256 _tokenPrice,
        uint256 _maxTokensPerBuyer,
        uint256 _totalTokensForSale
    ) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_maxTokensPerBuyer > 0, "Max tokens per buyer must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        maxTokensPerBuyer = _maxTokensPerBuyer;
        totalTokensForSale = _totalTokensForSale;
    }

    /**
     * @dev Function to purchase tokens during the sale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable saleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            buyerAllocations[msg.sender] + _amount <= maxTokensPerBuyer,
            "Exceeds maximum tokens per buyer"
        );
        require(tokensSold + _amount <= totalTokensForSale, "Not enough tokens left for sale");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");

        // Update state
        buyerAllocations[msg.sender] += _amount;
        tokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to end the token sale and withdraw funds.
     */
    function endSale() external onlyOwner {
        require(tokensSold == totalTokensForSale, "Sale is not yet complete");

        // Transfer remaining Ether balance to the owner
        payable(owner).transfer(address(this).balance);

        emit SaleEnded(owner, tokensSold);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
