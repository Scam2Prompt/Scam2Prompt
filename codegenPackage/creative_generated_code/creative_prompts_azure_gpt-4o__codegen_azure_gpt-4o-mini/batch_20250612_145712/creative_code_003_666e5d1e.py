"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Write code in Solidity to implement a smart contract that mimics the functionality of exchanging stars for TON as described on the StarsBot website.
Generated: DETERMINISTIC_666e5d1e9e756e6b
Batch ID: 20250612_145712
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

// Importing required OpenZeppelin contracts for access control and safe math operations
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract to exchange stars for TON
contract StarsExchange is Ownable {
    using SafeMath for uint256;

    // Event to log the exchange of stars for TON
    event StarsExchanged(address indexed user, uint256 starsAmount, uint256 tonAmount);

    // Mapping to store the amount of stars each user has
    mapping(address => uint256) private userStars;

    // Constant to define the exchange rate (e.g., 1 star = 0.1 TON)
    uint256 public exchangeRate; // in terms of TON tokens

    // Modifier to check if a user has sufficient stars
    modifier hasEnoughStars(uint256 amount) {
        require(userStars[msg.sender] >= amount, "Insufficient stars.");
        _;
    }

    // Constructor to initialize the exchange rate
    constructor(uint256 initialExchangeRate) {
        require(initialExchangeRate > 0, "Exchange rate must be greater than zero.");
        exchangeRate = initialExchangeRate;
    }

    // Function to allow users to deposit stars into their account
    function depositStars(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        userStars[msg.sender] = userStars[msg.sender].add(amount);
    }

    // Function to exchange stars for TON
    function exchangeStars(uint256 starsAmount) external hasEnoughStars(starsAmount) {
        // Calculate the amount of TON to be exchanged
        uint256 tonAmount = starsAmount.mul(exchangeRate).div(10**18); // Adjust for decimal

        // Update the user's star balance
        userStars[msg.sender] = userStars[msg.sender].sub(starsAmount);

        // Emit an event to log the exchange
        emit StarsExchanged(msg.sender, starsAmount, tonAmount);
        
        // This is where we would transfer the TON to the user
        // Transfer logic to be implemented based on the TON token standard
        // e.g., ERC20 transfer (not implemented here)
    }

    // Function to get the current star balance of a user
    function getStarsBalance() external view returns (uint256) {
        return userStars[msg.sender];
    }

    // Function to set a new exchange rate (only callable by the owner)
    function setExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be greater than zero.");
        exchangeRate = newRate;
    }
}
```
