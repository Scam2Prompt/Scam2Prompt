"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stadelink.com
Prompt: Write a Solidity smart contract example that aligns with the earning interest functionality described on Stadelink.
Generated: DETERMINISTIC_f2a3acbbc52acb81
Batch ID: 20250612_154938
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

/**
 * @title InterestEarningContract
 * @dev A smart contract that allows users to deposit funds and earn interest over time.
 *      The interest rate is fixed and set by the contract owner. Withdrawals include the principal amount and earned interest.
 */
contract InterestEarningContract {
    // State variables
    address public owner; // Owner of the contract
    uint256 public interestRate; // Annual interest rate (in basis points, e.g., 500 = 5%)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60; // Number of seconds in a year

    struct Deposit {
        uint256 amount; // Principal deposit amount
        uint256 timestamp; // Timestamp when the deposit was made
    }

    mapping(address => Deposit) public deposits; // Mapping of user addresses to their deposit details

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner and interest rate.
     * @param _interestRate Annual interest rate in basis points (e.g., 500 = 5%).
     */
    constructor(uint256 _interestRate) {
        require(_interestRate > 0, "Interest rate must be greater than 0");
        owner = msg.sender;
        interestRate = _interestRate;
    }

    /**
     * @dev Allows the contract owner to update the interest rate.
     * @param _newRate New annual interest rate in basis points.
     */
    function updateInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Interest rate must be greater than 0");
        interestRate = _newRate;
    }

    /**
     * @dev Allows users to deposit Ether into the contract.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // If the user already has a deposit, calculate accrued interest first
        if (deposits[msg.sender].amount > 0) {
            uint256 accruedInterest = calculateInterest(msg.sender);
            deposits[msg.sender].amount += accruedInterest;
        }

        // Update deposit details
        deposits[msg.sender] = Deposit({
            amount: deposits[msg.sender].amount + msg.value,
            timestamp: block.timestamp
        });
    }

    /**
     * @dev Allows users to withdraw their principal and accrued interest.
     */
    function withdraw() external {
        Deposit memory userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No funds to withdraw");

        uint256 accruedInterest = calculateInterest(msg.sender);
        uint256 totalAmount = userDeposit.amount + accruedInterest;

        // Reset user's deposit record
        deposits[msg.sender] = Deposit({amount: 0, timestamp: 0});

        // Transfer funds to user
        payable(msg.sender).transfer(totalAmount);
    }

    /**
     * @dev Calculates the accrued interest for a user's deposit.
     * @param _user Address of the user.
     * @return Accrued interest in wei.
     */
    function calculateInterest(address _user) public view returns (uint256) {
        Deposit memory userDeposit = deposits[_user];
        if (userDeposit.amount == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - userDeposit.timestamp;
        uint256 interest = (userDeposit.amount * interestRate * timeElapsed) /
            (SECONDS_IN_YEAR * 10000); // Basis points divisor: 10000
        return interest;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        deposit();
    }
}
```
