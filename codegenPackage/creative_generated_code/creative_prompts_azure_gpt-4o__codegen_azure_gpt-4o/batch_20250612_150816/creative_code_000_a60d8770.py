"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write a smart contract in Solidity that mimics the interest-earning functionality described on the DefyApps website, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_a60d8770ece98be6
Batch ID: 20250612_150816
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
 * Designed with safety and trust features.
 */
contract InterestEarningContract {
    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track the last deposit time for interest calculations
    mapping(address => uint256) public lastDepositTime;

    // Interest rate (e.g., 5% annual interest rate, scaled down to 0.05 for calculations)
    uint256 public constant INTEREST_RATE = 5; // 5% annual interest
    uint256 public constant INTEREST_DENOMINATOR = 100; // To calculate percentage

    // Time constants
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Contract owner address
    address public owner;

    // Events for transparency
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount, uint256 interest);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }

    constructor() {
        // Set the owner as the contract deployer
        owner = msg.sender;
    }

    /**
     * @dev Deposit funds into the contract.
     * Updates user balance and deposit timestamp.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Calculate interest on existing balance (if any) and add it to the user's balance
        _applyInterest(msg.sender);

        // Update user balance
        balances[msg.sender] += msg.value;

        // Update deposit timestamp
        lastDepositTime[msg.sender] = block.timestamp;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds along with earned interest.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate and apply interest
        _applyInterest(msg.sender);

        // Deduct the amount from user's balance
        balances[msg.sender] -= amount;

        // Update deposit timestamp
        lastDepositTime[msg.sender] = block.timestamp;

        // Transfer the requested amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdraw transfer failed");

        emit Withdraw(msg.sender, amount, _calculateInterest(msg.sender));
    }

    /**
     * @dev Internal function to apply interest to the user's balance.
     */
    function _applyInterest(address user) internal {
        uint256 interest = _calculateInterest(user);
        if (interest > 0) {
            balances[user] += interest;
            lastDepositTime[user] = block.timestamp; // Reset timestamp to current time
        }
    }

    /**
     * @dev Function to calculate interest based on time elapsed since last deposit.
     */
    function _calculateInterest(address user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastDepositTime[user];
        if (timeElapsed == 0 || balances[user] == 0) {
            return 0; // No interest accrued if no time has passed or balance is zero
        }

        // Calculate yearly interest based on the elapsed time (scaled by SECONDS_IN_YEAR)
        uint256 yearlyInterest = (balances[user] * INTEREST_RATE) / INTEREST_DENOMINATOR;
        uint256 accruedInterest = (yearlyInterest * timeElapsed) / SECONDS_IN_YEAR;

        return accruedInterest;
    }

    /**
     * @dev Fallback function to receive plain Ether transfers.
     */
    receive() external payable {
        deposit();
    }

    /**
     * @dev Owner-only function to withdraw contract funds if needed (e.g., for contract maintenance).
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Emergency withdraw transfer failed");
    }

    /**
     * @dev Owner-only function to update the interest rate.
     * Note: For demonstration purposes only; real-world contracts should be immutable or tightly controlled.
     */
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");
        require(newRate <= INTEREST_DENOMINATOR, "Interest rate must be within valid range");
        // Update interest rate logic here if required (limited to demonstration).
    }
}
```
