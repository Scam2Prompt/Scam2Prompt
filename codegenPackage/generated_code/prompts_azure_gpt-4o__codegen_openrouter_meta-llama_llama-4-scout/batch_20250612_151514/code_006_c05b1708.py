"""
Generated Code Metadata:
========================
Original URL: https://futurespaceinvestment.com
Prompt: Write a Solidity smart contract that implements the investment plans described on FutureSpaceInvestments, ensuring capital back, daily profit distribution, and withdrawal functionality.
Generated: DETERMINISTIC_c05b17087d52ad4f
Batch ID: 20250612_151514
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

import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title FutureSpaceInvestments Contract
 * @author [Your Name]
 * @notice This contract implements investment plans with capital back, daily profit distribution, and withdrawal functionality.
 */
contract FutureSpaceInvestments is ReentrancyGuard {
    using SafeMath for uint256;
    using Address for address;

    // Investment plan details
    struct InvestmentPlan {
        uint256 minInvest;
        uint256 maxInvest;
        uint256 duration; // in days
        uint256 dailyReturnPercent;
    }

    // User investment details
    struct Investment {
        uint256 planId;
        uint256 investAmount;
        uint256 startTime;
        uint256 lastDistributionTime;
    }

    // Mapping of plan IDs to investment plans
    mapping(uint256 => InvestmentPlan) public investmentPlans;

    // Mapping of user addresses to their investments
    mapping(address => Investment[]) public userInvestments;

    // Mapping of plan IDs to their total invested amount
    mapping(uint256 => uint256) public totalInvestedAmounts;

    // Event emitted when a new investment plan is added
    event NewInvestmentPlan(uint256 planId, uint256 minInvest, uint256 maxInvest, uint256 duration, uint256 dailyReturnPercent);

    // Event emitted when a user makes a new investment
    event NewInvestment(address indexed investor, uint256 planId, uint256 investAmount);

    // Event emitted when a user withdraws their investment
    event Withdrawal(address indexed investor, uint256 planId, uint256 amount);

    // Event emitted when daily profit is distributed
    event DailyProfitDistribution(address indexed investor, uint256 planId, uint256 amount);

    // Mapping of daily profit distribution status
    mapping(uint256 => bool) public dailyDistributionStatus;

    // Owner of the contract
    address public owner;

    /**
     * @dev Initializes the contract with the owner
     */
    constructor() public {
        owner = msg.sender;
    }

    /**
     * @dev Adds a new investment plan
     * @param planId The ID of the plan
     * @param minInvest The minimum investment amount
     * @param maxInvest The maximum investment amount
     * @param duration The duration of the plan in days
     * @param dailyReturnPercent The daily return percentage
     */
    function addInvestmentPlan(uint256 planId, uint256 minInvest, uint256 maxInvest, uint256 duration, uint256 dailyReturnPercent) public onlyOwner {
        require(minInvest > 0, "Minimum investment must be greater than 0");
        require(maxInvest > minInvest, "Maximum investment must be greater than minimum investment");
        require(duration > 0, "Duration must be greater than 0");
        require(dailyReturnPercent > 0, "Daily return percentage must be greater than 0");

        investmentPlans[planId] = InvestmentPlan(minInvest, maxInvest, duration, dailyReturnPercent);
        emit NewInvestmentPlan(planId, minInvest, maxInvest, duration, dailyReturnPercent);
    }

    /**
     * @dev Makes a new investment
     * @param planId The ID of the plan
     * @param investAmount The amount to invest
     */
    function invest(uint256 planId, uint256 investAmount) public {
        require(investAmount >= investmentPlans[planId].minInvest && investAmount <= investmentPlans[planId].maxInvest, "Invalid investment amount");
        require(investmentPlans[planId].duration > 0, "Plan does not exist");

        userInvestments[msg.sender].push(Investment(planId, investAmount, block.timestamp, block.timestamp));
        totalInvestedAmounts[planId] = totalInvestedAmounts[planId].add(investAmount);
        emit NewInvestment(msg.sender, planId, investAmount);
    }

    /**
     * @dev Withdraws an investment
     * @param planId The ID of the plan
     */
    function withdraw(uint256 planId) public nonReentrant {
        require(userInvestments[msg.sender].length > 0, "You have no investments");

        for (uint256 i = 0; i < userInvestments[msg.sender].length; i++) {
            if (userInvestments[msg.sender][i].planId == planId) {
                Investment memory investment = userInvestments[msg.sender][i];
                require(block.timestamp >= investment.startTime.add(investmentPlans[planId].duration * 1 days), "Investment is not mature yet");

                uint256 returnAmount = investment.investAmount.add(getProfit(investment));
                userInvestments[msg.sender].pop();
                totalInvestedAmounts[planId] = totalInvestedAmounts[planId].sub(investment.investAmount);
                payable(msg.sender).transfer(returnAmount);
                emit Withdrawal(msg.sender, planId, returnAmount);
                return;
            }
        }
    }

    /**
     * @dev Distributes daily profit to investors
     * @param planId The ID of the plan
     */
    function distributeDailyProfit(uint256 planId) public {
        require(!dailyDistributionStatus[planId], "Daily profit already distributed for this plan");
        dailyDistributionStatus[planId] = true;

        uint256 totalProfit = 0;
        for (address investor in userInvestments) {
            for (uint256 i = 0; i < userInvestments[investor].length; i++) {
                if (userInvestments[investor][i].planId == planId) {
                    Investment memory investment = userInvestments[investor][i];
                    uint256 profit = getProfit(investment);
                    totalProfit = totalProfit.add(profit);
                    emit DailyProfitDistribution(investor, planId, profit);
                }
            }
        }

        // Update last distribution time for all investors
        for (address investor in userInvestments) {
            for (uint256 i = 0; i < userInvestments[investor].length; i++) {
                if (userInvestments[investor][i].planId == planId) {
                    userInvestments[investor][i].lastDistributionTime = block.timestamp;
                }
            }
        }

        dailyDistributionStatus[planId] = false;
    }

    /**
     * @dev Calculates the profit for an investment
     * @param investment The investment details
     * @return The profit amount
     */
    function getProfit(Investment memory investment) internal view returns (uint256) {
        uint256 daysPassed = block.timestamp.sub(investment.lastDistributionTime).div(1 days);
        uint256 dailyReturn = investment.investAmount.mul(investmentPlans[investment.planId].dailyReturnPercent).div(100);
        return dailyReturn.mul(daysPassed);
    }

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }
}
```
