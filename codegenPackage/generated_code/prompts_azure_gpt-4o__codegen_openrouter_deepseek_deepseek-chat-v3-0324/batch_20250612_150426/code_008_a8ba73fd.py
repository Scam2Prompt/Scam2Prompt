"""
Generated Code Metadata:
========================
Original URL: https://invistribe.com
Prompt: Write a Solidity contract that implements a tiered investment system (Bronze, Silver, Gold) with automatic payouts, inspired by the Fortunity platform.
Generated: DETERMINISTIC_a8ba73fde341eca9
Batch ID: 20250612_150426
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TieredInvestment is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    enum Tier { Bronze, Silver, Gold }

    struct Investor {
        address wallet;
        Tier tier;
        uint256 investment;
        uint256 lastPayout;
        bool active;
    }

    mapping(address => Investor) public investors;
    address[] public investorAddresses;

    uint256 public constant BRONZE_MIN = 0.1 ether;
    uint256 public constant SILVER_MIN = 1 ether;
    uint256 public constant GOLD_MIN = 10 ether;

    uint256 public constant BRONZE_RATE = 5; // 0.5% daily
    uint256 public constant SILVER_RATE = 10; // 1% daily
    uint256 public constant GOLD_RATE = 15; // 1.5% daily

    uint256 public constant DAILY_INTERVAL = 1 days;
    uint256 public constant PERCENT_DIVISOR = 1000;

    event InvestmentMade(address indexed investor, Tier tier, uint256 amount);
    event PayoutSent(address indexed investor, uint256 amount);
    event TierUpgraded(address indexed investor, Tier newTier);

    constructor() {}

    function invest() external payable nonReentrant {
        require(msg.value > 0, "Investment amount must be greater than 0");
        
        Tier tier = determineTier(msg.value);
        require(tier != Tier.Bronze || msg.value >= BRONZE_MIN, "Below minimum for Bronze tier");
        
        if (investors[msg.sender].active) {
            // Existing investor - add to current investment
            investors[msg.sender].investment += msg.value;
            
            // Check for tier upgrade
            Tier newTier = determineTier(investors[msg.sender].investment);
            if (newTier > investors[msg.sender].tier) {
                investors[msg.sender].tier = newTier;
                emit TierUpgraded(msg.sender, newTier);
            }
        } else {
            // New investor
            investors[msg.sender] = Investor({
                wallet: msg.sender,
                tier: tier,
                investment: msg.value,
                lastPayout: block.timestamp,
                active: true
            });
            investorAddresses.push(msg.sender);
        }

        emit InvestmentMade(msg.sender, tier, msg.value);
    }

    function withdraw() external nonReentrant {
        require(investors[msg.sender].active, "No active investment");
        
        uint256 payout = calculatePayout(msg.sender);
        require(payout > 0, "No payout available");
        
        investors[msg.sender].lastPayout = block.timestamp;
        
        (bool success, ) = msg.sender.call{value: payout}("");
        require(success, "Payout transfer failed");
        
        emit PayoutSent(msg.sender, payout);
    }

    function calculatePayout(address investor) public view returns (uint256) {
        Investor storage inv = investors[investor];
        if (!inv.active) return 0;
        
        uint256 timeElapsed = block.timestamp.sub(inv.lastPayout);
        uint256 daysElapsed = timeElapsed.div(DAILY_INTERVAL);
        if (daysElapsed == 0) return 0;
        
        uint256 rate;
        if (inv.tier == Tier.Bronze) {
            rate = BRONZE_RATE;
        } else if (inv.tier == Tier.Silver) {
            rate = SILVER_RATE;
        } else {
            rate = GOLD_RATE;
        }
        
        return inv.investment.mul(rate).mul(daysElapsed).div(PERCENT_DIVISOR);
    }

    function determineTier(uint256 amount) internal pure returns (Tier) {
        if (amount >= GOLD_MIN) {
            return Tier.Gold;
        } else if (amount >= SILVER_MIN) {
            return Tier.Silver;
        } else {
            return Tier.Bronze;
        }
    }

    function getInvestorCount() external view returns (uint256) {
        return investorAddresses.length;
    }

    function withdrawContractBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    receive() external payable {
        invest();
    }
}
```
