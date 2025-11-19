"""
Generated Code Metadata:
========================
Original URL: https://dogeversehubs.pages.dev
Prompt: Generate a smart contract in Solidity to create a refund mechanism for investors within 12 hours after listing on a decentralized exchange, similar to TrustPad's SAFU rules.
Generated: DETERMINISTIC_fc07b08c2c786ed9
Batch ID: 20250622_204837
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RefundMechanism is Ownable {
    struct Investor {
        uint256 amountInvested;
        uint256 amountRefunded;
        bool hasRefunded;
    }

    IERC20 public token;
    uint256 public listingTime;
    uint256 public constant REFUND_PERIOD = 12 hours;
    bool public isRefundActive;

    mapping(address => Investor) public investors;

    event InvestmentRecorded(address indexed investor, uint256 amount);
    event RefundProcessed(address indexed investor, uint256 amount);
    event RefundPeriodEnded();
    event TokensWithdrawn(address indexed owner, uint256 amount);

    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    modifier onlyDuringRefundPeriod() {
        require(isRefundActive, "Refund period is not active");
        require(block.timestamp <= listingTime + REFUND_PERIOD, "Refund period has ended");
        _;
    }

    modifier onlyAfterRefundPeriod() {
        require(block.timestamp > listingTime + REFUND_PERIOD, "Refund period has not ended yet");
        _;
    }

    function setListingTime() external onlyOwner {
        require(listingTime == 0, "Listing time already set");
        listingTime = block.timestamp;
        isRefundActive = true;
    }

    function recordInvestment(address investor, uint256 amount) external onlyOwner {
        require(investor != address(0), "Investor address cannot be zero");
        require(amount > 0, "Investment amount must be greater than zero");
        require(!investors[investor].hasRefunded, "Investor has already refunded");

        investors[investor].amountInvested += amount;
        emit InvestmentRecorded(investor, amount);
    }

    function requestRefund() external onlyDuringRefundPeriod {
        address investor = msg.sender;
        Investor storage investorInfo = investors[investor];

        require(investorInfo.amountInvested > 0, "No investment to refund");
        require(!investorInfo.hasRefunded, "Already refunded");

        uint256 refundAmount = investorInfo.amountInvested;
        investorInfo.amountRefunded = refundAmount;
        investorInfo.hasRefunded = true;

        require(token.transfer(investor, refundAmount), "Refund transfer failed");
        emit RefundProcessed(investor, refundAmount);
    }

    function endRefundPeriod() external onlyOwner onlyDuringRefundPeriod {
        require(block.timestamp > listingTime + REFUND_PERIOD, "Refund period not yet ended");
        isRefundActive = false;
        emit RefundPeriodEnded();
    }

    function withdrawTokens() external onlyOwner onlyAfterRefundPeriod {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(token.transfer(owner(), balance), "Token transfer failed");
        emit TokensWithdrawn(owner(), balance);
    }

    function getRefundStatus(address investor) external view returns (uint256 invested, uint256 refunded, bool hasRefunded) {
        Investor memory investorInfo = investors[investor];
        return (
            investorInfo.amountInvested,
            investorInfo.amountRefunded,
            investorInfo.hasRefunded
        );
    }
}
```
