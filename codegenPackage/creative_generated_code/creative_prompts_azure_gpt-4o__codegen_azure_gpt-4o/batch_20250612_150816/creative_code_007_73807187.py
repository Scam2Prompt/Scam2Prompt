"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Develop a Solidity smart contract that highlights earning interest securely, inspired by the features on the DefyApps platform.
Generated: DETERMINISTIC_7380718700c72095
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
 * @dev A smart contract that allows users to deposit funds, earn interest, and withdraw securely.
 * Inspired by DefyApps platform features.
 */
contract InterestEarningContract {
    // State variables
    address public owner; // Contract owner
    uint256 public interestRate; // Interest rate (as a percentage)
    uint256 public totalDeposits; // Total deposits in the contract

    struct Deposit {
        uint256 amount; // Amount deposited by the user
        uint256 timestamp; // Time of deposit
    }

    mapping(address => Deposit) public deposits; // Tracks deposits by address

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 interest);
    event InterestRateUpdated(uint256 oldRate, uint256 newRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract owner and default interest rate
    constructor(uint256 _initialInterestRate) {
        require(_initialInterestRate > 0, "Interest rate must be positive");
        owner = msg.sender;
        interestRate = _initialInterestRate;
    }

    /**
     * @dev Allows the owner to update the interest rate.
     * @param _newRate The new interest rate.
     */
    function updateInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Interest rate must be positive");
        emit InterestRateUpdated(interestRate, _newRate);
        interestRate = _newRate;
    }

    /**
     * @dev Allows users to deposit funds into the contract.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user's deposit and timestamp
        deposits[msg.sender].amount += msg.value;
        deposits[msg.sender].timestamp = block.timestamp;

        // Update total deposits in the contract
        totalDeposits += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Calculates earned interest for a user based on their deposit duration.
     * @param _user The address of the user.
     * @return The earned interest.
     */
    function calculateInterest(address _user) public view returns (uint256) {
        Deposit memory userDeposit = deposits[_user];
        require(userDeposit.amount > 0, "No deposit found for user");

        // Calculate interest based on deposit duration
        uint256 depositDuration = block.timestamp - userDeposit.timestamp;
        uint256 interest = (userDeposit.amount * interestRate * depositDuration) / (100 * 365 days);
        return interest;
    }

    /**
     * @dev Allows users to withdraw their deposits along with the earned interest.
     */
    function withdraw() external {
        Deposit memory userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No deposit found");

        // Calculate interest
        uint256 interest = calculateInterest(msg.sender);
        uint256 totalAmount = userDeposit.amount + interest;

        // Reset user's deposit data
        deposits[msg.sender].amount = 0;
        deposits[msg.sender].timestamp = 0;

        // Update total deposits in the contract
        totalDeposits -= userDeposit.amount;

        // Transfer funds to the user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, userDeposit.amount, interest);
    }

    /**
     * @dev Allows the owner to withdraw excess funds from the contract (excluding user deposits).
     * @param _amount The amount to withdraw.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= totalDeposits + _amount, "Insufficient excess funds");

        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Use deposit function to send funds");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Use deposit function to send funds");
    }
}
```
