"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeversehubs.pages.dev
Prompt: Generate Solidity code for a smart contract that adheres to SAFU rules, including a refund mechanism within 12 hours after token listing, as outlined on the DOGEVERSE platform.
Generated: DETERMINISTIC_28f7ff0f6f8a0a43
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title SAFUCompliantToken
 * @dev This smart contract adheres to SAFU rules, including a refund mechanism
 *      within 12 hours after token listing.
 */
contract SAFUCompliantToken {
    // Events
    event TokenPurchased(address indexed buyer, uint256 amount);
    event RefundIssued(address indexed buyer, uint256 amount);
    event ListingTimeUpdated(uint256 newListingTime);

    // State variables
    address public owner; // Contract owner
    uint256 public listingTime; // UNIX timestamp of the token listing time
    uint256 public constant REFUND_PERIOD = 12 hours; // Refund period (12 hours)
    uint256 public tokenPrice = 0.01 ether; // Price per token (modifiable if needed)

    mapping(address => uint256) public balances; // Tracks token balances
    mapping(address => uint256) public purchaseTimestamps; // Tracks the purchase times

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    modifier withinRefundPeriod() {
        require(block.timestamp <= listingTime + REFUND_PERIOD, "Refund period has expired.");
        _;
    }

    modifier validPurchase() {
        require(msg.value > 0, "Purchase value must be greater than zero.");
        require(listingTime > 0 && block.timestamp >= listingTime, "Tokens are not available for purchase.");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Allows the owner to set the token listing time.
     * @param _listingTime The UNIX timestamp of the listing time.
     */
    function setListingTime(uint256 _listingTime) external onlyOwner {
        require(_listingTime > block.timestamp, "Listing time must be in the future.");
        listingTime = _listingTime;
        emit ListingTimeUpdated(_listingTime);
    }

    /**
     * @dev Allows users to purchase tokens.
     */
    function purchaseTokens() external payable validPurchase {
        uint256 tokensToPurchase = msg.value / tokenPrice; // Calculate tokens based on ether sent
        require(tokensToPurchase > 0, "Insufficient funds for token purchase.");

        balances[msg.sender] += tokensToPurchase; // Update the buyer's balance
        purchaseTimestamps[msg.sender] = block.timestamp; // Record the purchase time

        emit TokenPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Allows users to request a refund within the 12-hour refund period after token listing.
     */
    function requestRefund() external withinRefundPeriod {
        uint256 purchaserTokens = balances[msg.sender];
        require(purchaserTokens > 0, "You have no tokens to refund.");

        uint256 refundAmount = purchaserTokens * tokenPrice; // Calculate refund amount
        require(address(this).balance >= refundAmount, "Insufficient contract balance to issue refund.");

        balances[msg.sender] = 0; // Reset the buyer's token balance
        purchaseTimestamps[msg.sender] = 0; // Reset the purchase timestamp
        payable(msg.sender).transfer(refundAmount); // Send refund to the buyer

        emit RefundIssued(msg.sender, refundAmount);
    }

    /**
     * @dev Fallback function to accept payment directly to the contract.
     */
    receive() external payable {
        revert("Direct payments not allowed. Use purchaseTokens()");
    }

    /**
     * @dev Allows the owner to withdraw excess funds from the contract after the refund period.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > listingTime + REFUND_PERIOD, "Withdrawals only allowed after refund period.");

        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal.");

        payable(owner).transfer(contractBalance);
    }
}
```
