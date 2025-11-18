"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.v3-dashboard.com
Prompt: Write a Solidity contract that integrates with Aave V3 to automatically repay a loan when the health factor drops below a specified threshold.
Generated: DETERMINISTIC_b6ad86e9f87d88d2
Batch ID: 20250612_153854
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

// Import Aave V3 interfaces
import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IERC20.sol";

contract AutoRepayLoan {
    address public owner; // Owner of the contract
    IPool public immutable aavePool; // Aave Pool contract address
    uint256 public healthFactorThreshold; // Threshold to monitor health factor
    address public stableCoin; // Address of the stable coin used for repayment

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Events for monitoring contract activity
    event HealthFactorMonitored(uint256 healthFactor);
    event LoanRepaid(uint256 amount);

    // Constructor to initialize the contract with required parameters
    constructor(address _aavePool, uint256 _healthFactorThreshold, address _stableCoin) {
        require(_aavePool != address(0), "Invalid Aave Pool address");
        require(_stableCoin != address(0), "Invalid stable coin address");
        require(_healthFactorThreshold > 0, "Health factor must be greater than zero");

        owner = msg.sender;
        aavePool = IPool(_aavePool);
        healthFactorThreshold = _healthFactorThreshold;
        stableCoin = _stableCoin;
    }

    // Function to update the health factor threshold
    function updateHealthFactorThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0, "Health factor must be greater than zero");
        healthFactorThreshold = _newThreshold;
    }

    // Function to repay the loan when health factor is below the threshold
    function monitorAndRepayLoan(address user) external {
        // Retrieve Reserve Data for the user
        (, , , , , uint256 healthFactor) = aavePool.getUserAccountData(user);

        emit HealthFactorMonitored(healthFactor);

        // Check if health factor is below the threshold
        require(healthFactor < healthFactorThreshold * 1e18, "Health factor is above the threshold");

        // Calculate the repayment amount (repay partial or full debt)
        uint256 debtToRepay = getDebtBalance(user);

        // Approve the Aave Pool to use stable coin for repayment
        IERC20(stableCoin).approve(address(aavePool), debtToRepay);

        // Repay the debt
        aavePool.repay(stableCoin, debtToRepay, 2, user); // Mode 2: Stable Rate

        emit LoanRepaid(debtToRepay);
    }

    // Helper function to fetch total debt balance of the user
    function getDebtBalance(address user) public view returns (uint256) {
        (uint256 stableDebt, uint256 variableDebt) = aavePool.getUserDebtBalanceData(user, stableCoin);
        return stableDebt + variableDebt;
    }

    // Function for the owner to rescue ERC20 tokens accidentally sent to the contract
    function rescueTokens(address token, address to, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(to, amount), "Token transfer failed");
    }
}
```
