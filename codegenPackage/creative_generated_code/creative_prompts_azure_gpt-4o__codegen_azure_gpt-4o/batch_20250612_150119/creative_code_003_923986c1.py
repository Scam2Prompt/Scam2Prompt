"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Create a smart contract in Solidity for managing fixed-term deposits and payouts, inspired by the roadmap features mentioned on profitproinvest.com.
Generated: DETERMINISTIC_923986c1395d560f
Batch ID: 20250612_150119
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
 * @title FixedTermDeposit
 * @dev A smart contract to manage fixed-term deposits and payouts.
 * Inspired by the roadmap features of profitproinvest.com.
 */
contract FixedTermDeposit {

    // Struct to hold deposit information
    struct Deposit {
        uint256 amount;       // Amount of deposit
        uint256 startTime;    // Timestamp when the deposit was made
        uint256 duration;     // Duration for the fixed term (in seconds)
        uint256 interestRate; // Interest rate in percentage (e.g., 5 means 5%)
        bool paidOut;         // Flag to track if payout has been made
    }

    // Mapping to store deposits for each depositor
    mapping(address => Deposit[]) public deposits;

    // Owner of the contract
    address public owner;

    // Event emitted when a new deposit is created
    event DepositCreated(address indexed depositor, uint256 amount, uint256 duration, uint256 interestRate);

    // Event emitted when a payout is made
    event PayoutMade(address indexed depositor, uint256 amount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation");
        _;
    }

    /**
     * @dev Modifier to ensure the deposit exists and is valid.
     */
    modifier validDeposit(uint256 depositIndex) {
        require(depositIndex < deposits[msg.sender].length, "Invalid deposit index");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new fixed-term deposit.
     * @param _duration Duration of the deposit term in seconds.
     * @param _interestRate Interest rate percentage for the deposit.
     */
    function createDeposit(uint256 _duration, uint256 _interestRate) external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");

        // Add deposit details to the user's deposit list
        deposits[msg.sender].push(Deposit({
            amount: msg.value,
            startTime: block.timestamp,
            duration: _duration,
            interestRate: _interestRate,
            paidOut: false
        }));

        emit DepositCreated(msg.sender, msg.value, _duration, _interestRate);
    }

    /**
     * @dev Function to calculate the payout amount for a deposit.
     * @param depositIndex Index of the deposit in the user's deposit list.
     * @return The total payout amount including interest.
     */
    function calculatePayout(uint256 depositIndex) public view validDeposit(depositIndex) returns (uint256) {
        Deposit memory userDeposit = deposits[msg.sender][depositIndex];
        require(!userDeposit.paidOut, "Payout already made for this deposit");

        // Check if the deposit term has matured
        require(block.timestamp >= userDeposit.startTime + userDeposit.duration, "Deposit term has not matured yet");

        // Calculate interest
        uint256 interest = (userDeposit.amount * userDeposit.interestRate) / 100;

        // Return total payout (principal + interest)
        return userDeposit.amount + interest;
    }

    /**
     * @dev Function to withdraw the payout of a matured deposit.
     * @param depositIndex Index of the deposit in the user's deposit list.
     */
    function withdrawPayout(uint256 depositIndex) external validDeposit(depositIndex) {
        Deposit storage userDeposit = deposits[msg.sender][depositIndex];
        require(!userDeposit.paidOut, "Payout already made for this deposit");

        // Check if the deposit term has matured
        require(block.timestamp >= userDeposit.startTime + userDeposit.duration, "Deposit term has not matured yet");

        // Calculate payout amount
        uint256 payoutAmount = calculatePayout(depositIndex);

        // Mark the deposit as paid out
        userDeposit.paidOut = true;

        // Transfer payout to the depositor
        (bool success, ) = msg.sender.call{value: payoutAmount}("");
        require(success, "Payout transfer failed");

        emit PayoutMade(msg.sender, payoutAmount);
    }

    /**
     * @dev Function to allow the owner to withdraw contract balance.
     * @notice Restricted to owner only.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdraw transfer failed");
    }

    /**
     * @dev Fallback function to accept plain ether deposits.
     */
    receive() external payable {}
}
```
