"""
Generated Code Metadata:
========================
Original URL: https://spark.fishersclubs.com
Prompt: "Generate a smart contract code for a savings product similar to Spark's Savings USDS, incorporating community-driven governance for rate determination."
Generated: DETERMINISTIC_15733ef9bbfad24f
Batch ID: 20250622_212649
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the governance contract
interface IGovernance {
    function getInterestRate() external view returns (uint256);
}

// Savings contract for a community-driven savings product
contract CommunitySavings is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public stablecoin; // The stablecoin used for savings
    IGovernance public governance; // Governance contract for rate determination

    struct User {
        uint256 balance; // User's savings balance
        uint256 lastDepositTime; // Last deposit timestamp
    }

    mapping(address => User) private users; // Mapping of user addresses to their savings data

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event InterestPaid(address indexed user, uint256 interest);

    // Constructor to initialize the contract
    constructor(IERC20 _stablecoin, IGovernance _governance) {
        stablecoin = _stablecoin;
        governance = _governance;
    }

    // Deposit funds into the savings account
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(stablecoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance and last deposit time
        users[msg.sender].balance = users[msg.sender].balance.add(amount);
        users[msg.sender].lastDepositTime = block.timestamp;

        emit Deposited(msg.sender, amount);
    }

    // Withdraw funds from the savings account
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(users[msg.sender].balance >= amount, "Insufficient balance");

        // Calculate and pay interest before withdrawal
        payInterest(msg.sender);

        // Update user balance
        users[msg.sender].balance = users[msg.sender].balance.sub(amount);
        require(stablecoin.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Pay interest to the user based on the current interest rate
    function payInterest(address user) internal {
        uint256 interestRate = governance.getInterestRate();
        uint256 timeElapsed = block.timestamp.sub(users[user].lastDepositTime);
        uint256 interest = users[user].balance.mul(interestRate).mul(timeElapsed).div(365 days).div(100);

        if (interest > 0) {
            users[user].balance = users[user].balance.add(interest);
            require(stablecoin.transfer(user, interest), "Interest transfer failed");
            emit InterestPaid(user, interest);
        }

        // Update last deposit time
        users[user].lastDepositTime = block.timestamp;
    }

    // Get the user's balance
    function getBalance() external view returns (uint256) {
        return users[msg.sender].balance;
    }

    // Get the total balance of the contract
    function totalBalance() external view onlyOwner returns (uint256) {
        return stablecoin.balanceOf(address(this));
    }
}
```
