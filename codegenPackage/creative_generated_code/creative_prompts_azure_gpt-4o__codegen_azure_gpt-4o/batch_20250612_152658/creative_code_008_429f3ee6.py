"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teset123214.pages.dev
Prompt: Generate a Solidity contract to implement a fair launch mechanism for $TIMI tokens, adhering to the tokenomics outlined on the webpage.
Generated: DETERMINISTIC_429f3ee69ce7276b
Batch ID: 20250612_152658
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
 * @title TIMI Token Fair Launch Contract
 * @author Expert Programmer
 * @notice This contract handles the fair launch mechanism for $TIMI tokens.
 * @dev Follow best practices for Solidity and ensure security and reliability.
 */
contract TIMIFairLaunch {
    // Tokenomics information
    uint256 public constant SALE_PRICE = 0.01 ether;  // Price of $TIMI per token in ETH
    uint256 public constant MAX_TOKENS = 1_000_000;   // Maximum number of tokens to be sold
    uint256 public constant LAUNCH_DURATION = 7 days; // Duration of the token sale
    uint256 public constant MIN_PURCHASE = 10;        // Minimum number of tokens one can purchase
    uint256 public constant MAX_PURCHASE = 10_000;    // Maximum number of tokens one can purchase

    // Sale and token details
    address public owner;
    uint256 public startTime;
    uint256 public totalTokensSold;
    bool public isPaused;

    // Mapping of buyers to the number of tokens purchased
    mapping(address => uint256) public tokensPurchased;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SalePaused(bool isPaused);
    event Withdrawal(uint256 amount, address indexed recipient);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to ensure that the sale is active
    modifier saleActive() {
        require(block.timestamp >= startTime, "Sale has not started");
        require(block.timestamp <= startTime + LAUNCH_DURATION, "Sale has ended");
        require(!isPaused, "Sale is paused");
        _;
    }

    /**
     * @notice Constructor to initialize the contract
     * @param _startTime The timestamp at which the token sale begins
     */
    constructor(uint256 _startTime) {
        require(_startTime > block.timestamp, "Start time must be in the future");
        startTime = _startTime;
        owner = msg.sender;
        isPaused = false;
    }

    /**
     * @notice Allows users to purchase $TIMI tokens during the fair launch
     * @param _amount The number of tokens the user wants to purchase
     */
    function purchaseTokens(uint256 _amount) external payable saleActive {
        require(_amount >= MIN_PURCHASE, "Purchase amount below minimum limit");
        require(_amount <= MAX_PURCHASE, "Purchase amount exceeds maximum limit");
        require(totalTokensSold + _amount <= MAX_TOKENS, "Not enough tokens left");
        require(msg.value == _amount * SALE_PRICE, "Incorrect ETH sent");

        tokensPurchased[msg.sender] += _amount;
        totalTokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @notice Allows the owner to pause or unpause the sale
     * @param _pause Boolean indicating whether to pause or unpause the sale
     */
    function setPause(bool _pause) external onlyOwner {
        isPaused = _pause;
        emit SalePaused(_pause);
    }

    /**
     * @notice Allows the owner to withdraw the funds collected during the sale
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");

        emit Withdrawal(balance, owner);
    }

    /**
     * @notice Allows users to check the remaining tokens available for sale
     * @return The number of tokens left for sale
     */
    function tokensRemaining() external view returns (uint256) {
        return MAX_TOKENS - totalTokensSold;
    }
}
```
