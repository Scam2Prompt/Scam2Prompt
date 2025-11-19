"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Design a Solidity contract that implements a hold bonus feature, rewarding users for maintaining their investment without withdrawals, similar to MinerDog's model.
Generated: DETERMINISTIC_d95fd21e2430ca43
Batch ID: 20250612_155753
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

contract HoldBonus {
    // Using SafeMath to prevent overflow/underflow issues
    using SafeMath for uint256;

    // State variables
    struct UserInfo {
        uint256 investment;     // Amount invested by the user
        uint256 lastClaimed;    // Last timestamp when bonus was claimed
        uint256 bonusReward;     // Total bonus reward accumulated
    }

    mapping(address => UserInfo) public users; // Mapping of user addresses to their info

    uint256 public constant HOLD_PERIOD = 30 days; // Required hold period for bonus eligibility
    uint256 public constant BONUS_RATE = 10; // Bonus rate per month (10%)

    event InvestmentMade(address indexed user, uint256 amount);
    event BonusClaimed(address indexed user, uint256 amount);

    // Modifier to check if the user is eligible to claim bonuses
    modifier onlyEligibleForBonus(address user) {
        require(block.timestamp >= users[user].lastClaimed + HOLD_PERIOD, "Hold period not completed");
        _;
    }

    // Function to invest in the contract
    function invest() external payable {
        require(msg.value > 0, "Investment must be greater than zero");

        UserInfo storage user = users[msg.sender];

        // If user has existing investment, accumulate bonus rewards
        if (user.investment > 0) {
            user.bonusReward += calculateBonus(user.investment, user.lastClaimed);
        } 
        
        // Update user's investment and last claimed time
        user.investment += msg.value;
        user.lastClaimed = block.timestamp;

        emit InvestmentMade(msg.sender, msg.value);
    }

    // Function to calculate bonus based on the investment and last claimed time
    function calculateBonus(uint256 investment, uint256 lastClaimed) internal view returns (uint256) {
        uint256 monthsPassed = (block.timestamp - lastClaimed) / 30 days;
        return investment.mul(BONUS_RATE).mul(monthsPassed).div(100);
    }

    // Function to claim the accumulated bonus
    function claimBonus() external onlyEligibleForBonus(msg.sender) {
        UserInfo storage user = users[msg.sender];

        uint256 totalBonus = user.bonusReward + calculateBonus(user.investment, user.lastClaimed);
        require(totalBonus > 0, "No bonus to claim");

        // Reset the user's bonus reward and update last claimed timestamp
        user.bonusReward = 0;
        user.lastClaimed = block.timestamp;

        // Transfer the bonus to the user
        payable(msg.sender).transfer(totalBonus);

        emit BonusClaimed(msg.sender, totalBonus);
    }

    // Function to check the user's total balance (investment + bonuses)
    function totalBalance(address user) external view returns (uint256) {
        UserInfo storage userInfo = users[user];
        return userInfo.investment + userInfo.bonusReward + calculateBonus(userInfo.investment, userInfo.lastClaimed);
    }

    // Function to withdraw investment (not allowed in this model)
    function withdraw() external {
        revert("Withdrawals are not allowed in this model.");
    }

    // Fallback function to accept ether
    receive() external payable {
        invest();
    }
}

// Importing SafeMath library for arithmetic operations
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");

        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        return sub(a, b, "SafeMath: subtraction overflow");
    }

    function sub(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
        require(b <= a, errorMessage);
        uint256 c = a - b;

        return c;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");

        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        uint256 c = a / b;

        return c;
    }
}
```
