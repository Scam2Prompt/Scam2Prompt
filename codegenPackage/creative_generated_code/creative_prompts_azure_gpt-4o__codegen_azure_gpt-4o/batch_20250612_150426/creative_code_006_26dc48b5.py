"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gicoin.trade
Prompt: Develop a smart contract in Solidity that mirrors GIC's tailored financial solutions for diverse global investment needs.
Generated: DETERMINISTIC_26dc48b50aa24e74
Batch ID: 20250612_150426
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

/// @title GIC Financial Solutions Contract
/// @notice This smart contract is designed to provide tailored financial solutions for diverse investment needs.
/// @dev Implements investment plans with deposit, withdrawal, and interest calculation functionalities.
contract GICFinancialSolutions {

    // Struct to represent an investment plan
    struct InvestmentPlan {
        string name; // Name of the plan
        uint256 minDeposit; // Minimum deposit required for the plan
        uint256 interestRate; // Annual interest rate (in basis points, i.e., 1% = 100 basis points)
        uint256 lockPeriod; // Lock period in seconds during which funds cannot be withdrawn
    }

    // Struct to represent an investor's investment
    struct Investment {
        uint256 amount; // Amount invested
        uint256 startTime; // Timestamp when the investment was made
        uint256 planId; // ID of the investment plan selected
        bool withdrawn; // Flag to check if the investment has been withdrawn
    }

    // Array to store available investment plans
    InvestmentPlan[] public investmentPlans;

    // Mapping of investors to their investments
    mapping(address => Investment[]) public investments;

    // Event emitted when a new investment plan is created
    event InvestmentPlanCreated(uint256 indexed planId, string name, uint256 minDeposit, uint256 interestRate, uint256 lockPeriod);

    // Event emitted when an investment is made
    event InvestmentMade(address indexed investor, uint256 indexed planId, uint256 amount);

    // Event emitted when funds are withdrawn
    event InvestmentWithdrawn(address indexed investor, uint256 indexed investmentIndex, uint256 amount, uint256 interest);

    /// @notice Create a new investment plan
    /// @param _name Name of the investment plan
    /// @param _minDeposit Minimum deposit required for the plan
    /// @param _interestRate Annual interest rate in basis points (1% = 100 basis points)
    /// @param _lockPeriod Lock period in seconds
    function createInvestmentPlan(string memory _name, uint256 _minDeposit, uint256 _interestRate, uint256 _lockPeriod) public {
        require(_minDeposit > 0, "Minimum deposit must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");

        investmentPlans.push(InvestmentPlan({
            name: _name,
            minDeposit: _minDeposit,
            interestRate: _interestRate,
            lockPeriod: _lockPeriod
        }));

        emit InvestmentPlanCreated(investmentPlans.length - 1, _name, _minDeposit, _interestRate, _lockPeriod);
    }

    /// @notice Invest in a specific investment plan
    /// @param _planId The ID of the investment plan
    function invest(uint256 _planId) public payable {
        require(_planId < investmentPlans.length, "Invalid investment plan ID");
        InvestmentPlan memory plan = investmentPlans[_planId];
        require(msg.value >= plan.minDeposit, "Deposit amount is less than the minimum required");

        investments[msg.sender].push(Investment({
            amount: msg.value,
            startTime: block.timestamp,
            planId: _planId,
            withdrawn: false
        }));

        emit InvestmentMade(msg.sender, _planId, msg.value);
    }

    /// @notice Withdraw funds and accrued interest from an investment
    /// @param _investmentIndex The index of the investment to withdraw
    function withdraw(uint256 _investmentIndex) public {
        require(_investmentIndex < investments[msg.sender].length, "Invalid investment index");
        Investment storage userInvestment = investments[msg.sender][_investmentIndex];
        require(!userInvestment.withdrawn, "Investment already withdrawn");
        require(block.timestamp >= userInvestment.startTime + investmentPlans[userInvestment.planId].lockPeriod, "Lock period not yet over");

        // Calculate interest
        InvestmentPlan memory plan = investmentPlans[userInvestment.planId];
        uint256 principal = userInvestment.amount;
        uint256 durationInSeconds = block.timestamp - userInvestment.startTime;
        uint256 interest = (principal * plan.interestRate * durationInSeconds) / (365 days * 10_000);

        // Mark investment as withdrawn
        userInvestment.withdrawn = true;

        // Transfer principal and interest back to the investor
        uint256 totalPayout = principal + interest;
        payable(msg.sender).transfer(totalPayout);

        emit InvestmentWithdrawn(msg.sender, _investmentIndex, principal, interest);
    }

    /// @notice Get the number of investment plans
    /// @return The number of investment plans
    function getInvestmentPlanCount() public view returns (uint256) {
        return investmentPlans.length;
    }

    /// @notice Get the number of investments made by an investor
    /// @param _investor The address of the investor
    /// @return The number of investments
    function getInvestmentCount(address _investor) public view returns (uint256) {
        return investments[_investor].length;
    }

    /// @notice Fallback function to handle accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
