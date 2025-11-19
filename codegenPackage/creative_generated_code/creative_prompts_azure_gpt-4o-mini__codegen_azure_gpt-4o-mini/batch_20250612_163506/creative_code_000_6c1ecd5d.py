"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpool.live
Prompt: How can I implement a smart contract for an Initial DEX Offering (IDO) similar to those on Launchpool.live?
Generated: DETERMINISTIC_6c1ecd5d898f3584
Batch ID: 20250612_163506
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title IDOContract
 * @dev A smart contract for managing an Initial DEX Offering (IDO).
 */
contract IDOContract is Ownable {
    using SafeMath for uint256;

    // Token to sell during the IDO
    IERC20 public saleToken;
    // Token used for purchasing the sale token
    IERC20 public paymentToken;

    // Start and end time for the IDO
    uint256 public startTime;
    uint256 public endTime;

    // Total tokens available for sale and how much has been sold
    uint256 public totalTokens;
    uint256 public tokensSold;

    // Mapping of addresses to their contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Withdrawn(address indexed owner, uint256 amount);

    /**
     * @param _saleToken Address of the sale token (ERC20)
     * @param _paymentToken Address of the payment token (ERC20)
     * @param _startTime Start time of the IDO
     * @param _endTime End time of the IDO
     * @param _totalTokens Total tokens available for sale
     */
    constructor(
        IERC20 _saleToken,
        IERC20 _paymentToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _totalTokens
    ) {
        require(address(_saleToken) != address(0), "Invalid sale token address");
        require(address(_paymentToken) != address(0), "Invalid payment token address");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        saleToken = _saleToken;
        paymentToken = _paymentToken;
        startTime = _startTime;
        endTime = _endTime;
        totalTokens = _totalTokens;
        tokensSold = 0;
    }

    /**
     * @dev Purchase tokens with payment token
     * @param amount Amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external {
        require(block.timestamp >= startTime, "IDO has not started yet");
        require(block.timestamp <= endTime, "IDO has already ended");
        require(amount > 0, "Amount must be greater than zero");
        require(tokensSold.add(amount) <= totalTokens, "Not enough tokens available");

        // Calculate the cost in payment tokens
        uint256 cost = amount; // Assuming 1:1 ratio for simplicity, adjust as needed

        // Transfer payment tokens from buyer to this contract
        require(paymentToken.transferFrom(msg.sender, address(this), cost), "Payment transfer failed");

        // Transfer sale tokens to buyer
        require(saleToken.transfer(msg.sender, amount), "Token transfer failed");

        // Update the state
        contributions[msg.sender] = contributions[msg.sender].add(amount);
        tokensSold = tokensSold.add(amount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No tokens available for withdrawal");

        // Transfer payment tokens to owner
        require(paymentToken.transfer(owner(), balance), "Withdrawal failed");

        emit Withdrawn(owner(), balance);
    }

    /**
     * @dev Get the remaining tokens available for sale
     */
    function remainingTokens() external view returns (uint256) {
        return totalTokens.sub(tokensSold);
    }
}
```
