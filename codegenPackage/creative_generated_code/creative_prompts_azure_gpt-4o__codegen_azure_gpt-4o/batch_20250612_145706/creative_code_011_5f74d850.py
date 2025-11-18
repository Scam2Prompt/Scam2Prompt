"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity script to implement a token price increase mechanism during a presale, similar to the countdown timer for $FROP tokens.
Generated: DETERMINISTIC_5f74d8504f7ebbc9
Batch ID: 20250612_145706
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
 * @dev Implements a token presale with a price increase mechanism over time.
 */
contract TokenPresale {
    // Token details
    string public constant TOKEN_NAME = "FROP Token";
    string public constant TOKEN_SYMBOL = "FROP";

    // Basic presale details
    uint256 public constant INITIAL_PRICE = 0.001 ether; // Starting price per token
    uint256 public constant PRICE_INCREMENT = 0.0001 ether; // Price increment after each phase
    uint256 public constant PHASE_DURATION = 1 hours; // Duration of each price phase
    uint256 public constant MAX_TOKENS = 1_000_000; // Maximum tokens available in presale
    uint256 public tokensSold = 0; // Track tokens sold in the presale

    // Contract owner
    address public owner;

    // Start time of the presale
    uint256 public presaleStartTime;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);
    event Withdrawn(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _startTime The timestamp when the presale starts.
     */
    constructor(uint256 _startTime) {
        require(_startTime > block.timestamp, "Start time must be in the future");
        owner = msg.sender;
        presaleStartTime = _startTime;
    }

    /**
     * @dev View the current price per token during the presale.
     * @return Current token price in wei.
     */
    function getCurrentPrice() public view returns (uint256) {
        if (block.timestamp < presaleStartTime) {
            return INITIAL_PRICE;
        }
        uint256 elapsedTime = block.timestamp - presaleStartTime;
        uint256 phaseCount = elapsedTime / PHASE_DURATION;
        return INITIAL_PRICE + (PRICE_INCREMENT * phaseCount);
    }

    /**
     * @dev Purchase tokens during the presale.
     */
    function purchaseTokens(uint256 _amount) external payable presaleActive {
        require(_amount > 0, "Must purchase at least 1 token");
        uint256 currentPrice = getCurrentPrice();
        uint256 totalCost = currentPrice * _amount;

        require(msg.value >= totalCost, "Insufficient ETH sent to purchase tokens");
        require(tokensSold + _amount <= MAX_TOKENS, "Not enough tokens remaining in presale");

        tokensSold += _amount;

        // Refund excess ETH if sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        emit TokensPurchased(msg.sender, _amount, currentPrice);
    }

    /**
     * @dev Withdraw contract funds to the owner's wallet.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");
        payable(owner).transfer(contractBalance);
        emit Withdrawn(contractBalance);
    }

    /**
     * @dev Fallback function to handle accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed, use purchaseTokens()");
    }
}
```
