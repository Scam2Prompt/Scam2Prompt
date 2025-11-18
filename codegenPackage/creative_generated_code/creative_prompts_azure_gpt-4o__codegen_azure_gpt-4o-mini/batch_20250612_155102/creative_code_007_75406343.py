"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Generate a Solidity smart contract that incorporates KYC verification and prevents participation by whales, inspired by $GROK's presale strategy.
Generated: DETERMINISTIC_75406343f33aea85
Batch ID: 20250612_155102
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

contract KYCVerificationPresale {
    // Define state variables
    address public owner;
    uint256 public maxPurchaseAmount;
    uint256 public totalRaised;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    // Maps to store KYC status and purchase amounts
    mapping(address => bool) public isKYCVerified;
    mapping(address => uint256) public purchaseAmounts;

    // Event emitted when a purchase is made
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to check if the caller is KYC verified
    modifier onlyKYCVerified() {
        require(isKYCVerified[msg.sender], "KYC verification required");
        _;
    }

    // Modifier to check presale time window
    modifier duringPresale() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _maxPurchaseAmount, uint256 _presaleDuration) {
        owner = msg.sender;
        maxPurchaseAmount = _maxPurchaseAmount;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    // Function to set KYC status (only accessible by owner)
    function setKYCStatus(address _user, bool _status) external onlyOwner {
        isKYCVerified[_user] = _status;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens() external payable onlyKYCVerified duringPresale {
        uint256 amountToBuy = msg.value; // Amount paid by the buyer
        
        // Check if the purchase exceeds the max purchase limit
        require(amountToBuy <= maxPurchaseAmount, "Purchase exceeds max limit");
        
        // Check if the buyer is a whale (if they have already purchased the max amount)
        require(purchaseAmounts[msg.sender] + amountToBuy <= maxPurchaseAmount, "Whale limit exceeded");

        // Update the total raised and the buyer's purchase amount
        totalRaised += amountToBuy;
        purchaseAmounts[msg.sender] += amountToBuy;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, amountToBuy);
    }

    // Function to withdraw funds by the owner
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to check KYC status of an address
    function checkKYCStatus(address _user) external view returns (bool) {
        return isKYCVerified[_user];
    }

    // Function to check total raised amount
    function getTotalRaised() external view returns (uint256) {
        return totalRaised;
    }
}
```
