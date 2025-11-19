"""
Generated Code Metadata:
========================
Original URL: https://milady-dfk.pages.dev
Prompt: Generate a Solidity contract for a token sale mechanism that includes stepped raises and fixed-price pools, similar to the Milady Cult presale structure.
Generated: DETERMINISTIC_a3476a2614ba538b
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenSale
 * @dev A contract for a token sale mechanism with stepped raises and fixed-price pools.
 */
contract TokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Sale parameters
    uint256 public startTime;
    uint256 public endTime;
    uint256 public totalTokensForSale;
    uint256 public tokensSold;
    uint256 public pricePerToken;
    uint256 public raisedAmount;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event SaleFinalized(uint256 totalRaised, uint256 totalTokensSold);

    // Modifiers
    modifier onlyWhileOpen() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the token sale.
     * @param _token Address of the token being sold.
     * @param _startTime Start time of the sale.
     * @param _endTime End time of the sale.
     * @param _totalTokensForSale Total tokens available for sale.
     * @param _pricePerToken Initial price per token.
     */
    constructor(
        address _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _totalTokensForSale,
        uint256 _pricePerToken
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_startTime < _endTime, "Invalid sale time");
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");
        require(_pricePerToken > 0, "Price per token must be greater than zero");

        token = IERC20(_token);
        startTime = _startTime;
        endTime = _endTime;
        totalTokensForSale = _totalTokensForSale;
        pricePerToken = _pricePerToken;
    }

    /**
     * @dev Function to purchase tokens during the sale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable onlyWhileOpen {
        require(amount > 0, "Amount must be greater than zero");
        require(tokensSold.add(amount) <= totalTokensForSale, "Not enough tokens available");
        
        uint256 totalCost = amount.mul(pricePerToken);
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Update state
        tokensSold = tokensSold.add(amount);
        raisedAmount = raisedAmount.add(totalCost);

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        // Emit event
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess Ether
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }
    }

    /**
     * @dev Finalize the sale and withdraw funds.
     */
    function finalizeSale() external onlyOwner {
        require(block.timestamp > endTime, "Sale is still active");
        require(tokensSold > 0, "No tokens sold");

        // Transfer raised funds to the owner
        payable(owner()).transfer(raisedAmount);

        // Emit event
        emit SaleFinalized(raisedAmount, tokensSold);
    }

    /**
     * @dev Function to withdraw unsold tokens after the sale.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > endTime, "Sale is still active");
        uint256 unsoldTokens = totalTokensForSale.sub(tokensSold);
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens back to the owner
        token.transfer(owner(), unsoldTokens);
    }

    /**
     * @dev Function to update the price per token for stepped raises.
     * @param newPrice New price per token.
     */
    function updatePricePerToken(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        pricePerToken = newPrice;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
