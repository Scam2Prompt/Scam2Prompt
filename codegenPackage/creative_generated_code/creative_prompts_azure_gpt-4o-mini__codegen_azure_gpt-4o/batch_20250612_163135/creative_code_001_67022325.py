"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: How can I use the Gouda token in a smart contract for a fair sale on CowSwap?
Generated: DETERMINISTIC_6702232594355699
Batch ID: 20250612_163135
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
 * @title GoudaTokenFairSale
 * @dev A smart contract for a fair token sale on CowSwap using Gouda tokens.
 * This contract ensures proper tracking of purchases and fair distribution of tokens.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract GoudaTokenFairSale {
    // The Gouda token contract address
    IERC20 public immutable goudaToken;

    // Owner of the contract
    address public owner;

    // Sale parameters
    uint256 public pricePerToken; // Price per token in wei
    uint256 public saleStartTime; // Start time of the sale (Unix timestamp)
    uint256 public saleEndTime; // End time of the sale (Unix timestamp)

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PriceUpdated(uint256 oldPrice, uint256 newPrice);
    event SaleTimeUpdated(uint256 oldStartTime, uint256 oldEndTime, uint256 newStartTime, uint256 newEndTime);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier saleActive() {
        require(block.timestamp >= saleStartTime, "Sale has not started yet");
        require(block.timestamp <= saleEndTime, "Sale has ended");
        _;
    }

    /**
     * @dev Constructor to set the Gouda token address and initial parameters.
     * @param _goudaToken Address of the Gouda token contract.
     * @param _pricePerToken Initial price per token in wei.
     * @param _saleStartTime Start time of the sale (Unix timestamp).
     * @param _saleEndTime End time of the sale (Unix timestamp).
     */
    constructor(
        address _goudaToken,
        uint256 _pricePerToken,
        uint256 _saleStartTime,
        uint256 _saleEndTime
    ) {
        require(_goudaToken != address(0), "Invalid Gouda token address");
        require(_pricePerToken > 0, "Price per token must be greater than 0");
        require(_saleStartTime < _saleEndTime, "Start time must be less than end time");
        
        goudaToken = IERC20(_goudaToken);
        pricePerToken = _pricePerToken;
        saleStartTime = _saleStartTime;
        saleEndTime = _saleEndTime;
        owner = msg.sender;
    }

    /**
     * @dev Purchase Gouda tokens during the sale.
     * Caller must send enough ETH to cover the token cost.
     * @param tokenAmount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 tokenAmount) external payable saleActive {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        uint256 cost = tokenAmount * pricePerToken;
        require(msg.value >= cost, "Insufficient ETH sent");

        // Check contract has enough tokens to sell
        uint256 contractBalance = goudaToken.balanceOf(address(this));
        require(contractBalance >= tokenAmount, "Not enough Gouda tokens available");

        // Transfer tokens to buyer
        goudaToken.transfer(msg.sender, tokenAmount);

        // Refund excess ETH if sent more than cost
        if (msg.value > cost) {
            uint256 refund = msg.value - cost;
            payable(msg.sender).transfer(refund);
        }

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Update the price per token.
     * Only callable by the contract owner.
     * @param newPrice New price per token in wei.
     */
    function updatePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price per token must be greater than 0");
        uint256 oldPrice = pricePerToken;
        pricePerToken = newPrice;
        emit PriceUpdated(oldPrice, newPrice);
    }

    /**
     * @dev Update the sale start and end times.
     * Only callable by the contract owner.
     * @param newStartTime New start time of the sale (Unix timestamp).
     * @param newEndTime New end time of the sale (Unix timestamp).
     */
    function updateSaleTime(uint256 newStartTime, uint256 newEndTime) external onlyOwner {
        require(newStartTime < newEndTime, "Start time must be less than end time");
        uint256 oldStartTime = saleStartTime;
        uint256 oldEndTime = saleEndTime;
        saleStartTime = newStartTime;
        saleEndTime = newEndTime;
        emit SaleTimeUpdated(oldStartTime, oldEndTime, newStartTime, newEndTime);
    }

    /**
     * @dev Withdraw collected ETH from the sale.
     * Only callable by the contract owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraw unsold Gouda tokens from the contract.
     * Only callable by the contract owner after the sale has ended.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale has not ended yet");
        uint256 unsoldTokens = goudaToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No tokens to withdraw");
        goudaToken.transfer(owner, unsoldTokens);
    }
}
```
