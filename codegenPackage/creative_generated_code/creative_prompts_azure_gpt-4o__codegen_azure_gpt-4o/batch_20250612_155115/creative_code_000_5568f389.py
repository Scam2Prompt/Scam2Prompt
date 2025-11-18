"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starsdapps.pro
Prompt: Write a smart contract in Solidity that mimics the functionality of earning interest as described on starsdapps.pro, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_5568f38979a8189b
Batch ID: 20250612_155115
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
 * @dev A smart contract that allows users to deposit Ether and earn interest over time.
 * The contract ensures safety and trust by using appropriate error handling and security features.
 */
contract InterestEarningContract {
    // Address of the contract owner
    address public owner;

    // Interest rate (percentage per year)
    uint256 public annualInterestRate;

    // Struct to store user deposit details
    struct Deposit {
        uint256 amount; // Amount of Ether deposited
        uint256 depositTimestamp; // Timestamp when the deposit was made
    }

    // Mapping to store deposits for each user
    mapping(address => Deposit) public deposits;

    // Event emitted when a deposit is made
    event DepositMade(address indexed user, uint256 amount);

    // Event emitted when interest is withdrawn
    event InterestWithdrawn(address indexed user, uint256 interestAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(uint256 _annualInterestRate) {
        require(_annualInterestRate > 0, "Interest rate must be greater than zero");
        owner = msg.sender;
        annualInterestRate = _annualInterestRate;
    }

    /**
     * @dev Allows a user to deposit Ether into the contract.
     * Emits a DepositMade event on success.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's deposit details
        deposits[msg.sender].amount += msg.value;
        deposits[msg.sender].depositTimestamp = block.timestamp;

        emit DepositMade(msg.sender, msg.value);
    }

    /**
     * @dev Calculates the interest earned by the user.
     * @return interest The amount of interest earned.
     */
    function calculateInterest(address user) public view returns (uint256 interest) {
        Deposit memory userDeposit = deposits[user];
        require(userDeposit.amount > 0, "No deposit found for user");

        // Calculate time elapsed since deposit in seconds
        uint256 timeElapsed = block.timestamp - userDeposit.depositTimestamp;

        // Convert annual interest rate to seconds-based rate
        uint256 annualRatePerSecond = annualInterestRate / (365 * 24 * 60 * 60);

        // Calculate interest earned
        interest = (userDeposit.amount * annualRatePerSecond * timeElapsed) / 100;
        return interest;
    }

    /**
     * @dev Allows a user to withdraw the interest earned.
     * Emits an InterestWithdrawn event on success.
     */
    function withdrawInterest() external {
        uint256 interest = calculateInterest(msg.sender);
        require(interest > 0, "No interest earned yet");

        // Update deposit timestamp to reset interest calculation
        deposits[msg.sender].depositTimestamp = block.timestamp;

        // Ensure contract has enough funds to pay interest
        require(address(this).balance >= interest, "Insufficient contract balance");

        // Transfer interest to user
        payable(msg.sender).transfer(interest);

        emit InterestWithdrawn(msg.sender, interest);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        payable(owner).transfer(amount);
    }

    /**
     * @dev Allows the owner to update the annual interest rate.
     * @param newRate The new annual interest rate (percentage).
     */
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");
        annualInterestRate = newRate;
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}

    /**
     * @dev Helper function to get the contract balance.
     * @return balance The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256 balance) {
        return address(this).balance;
    }
}
```
