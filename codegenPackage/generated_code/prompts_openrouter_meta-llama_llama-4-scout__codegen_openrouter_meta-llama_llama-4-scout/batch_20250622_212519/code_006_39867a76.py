"""
Generated Code Metadata:
========================
Original URL: https://starsdapps.pro
Prompt: "Create a simple example of a DeFi smart contract written in Solidity for educational purposes."
Generated: DETERMINISTIC_39867a76032e14c8
Batch ID: 20250622_212519
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

/**
 * @title Simple DeFi Smart Contract
 * @author [Your Name]
 * @notice A basic example of a DeFi smart contract for educational purposes.
 */
contract SimpleDeFiContract {
    // Mapping of user addresses to their respective balances
    mapping (address => uint256) public balances;

    // Event emitted when a user deposits funds
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws funds
    event Withdrawal(address indexed user, uint256 amount);

    // Event emitted when a user borrows funds
    event Borrow(address indexed user, uint256 amount);

    // Event emitted when a user repays a loan
    event Repay(address indexed user, uint256 amount);

    // Mapping of user addresses to their respective loan amounts
    mapping (address => uint256) public loans;

    // Interest rate for loans (in percent)
    uint256 public interestRate;

    /**
     * @dev Initializes the contract with an interest rate
     * @param _interestRate The interest rate for loans (in percent)
     */
    constructor(uint256 _interestRate) {
        interestRate = _interestRate;
    }

    /**
     * @dev Deposits funds into the contract
     * @param _amount The amount to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Update user's balance
        balances[msg.sender] += _amount;

        // Emit deposit event
        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraws funds from the contract
     * @param _amount The amount to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update user's balance
        balances[msg.sender] -= _amount;

        // Emit withdrawal event
        emit Withdrawal(msg.sender, _amount);

        // Transfer funds to user
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @dev Borrows funds from the contract
     * @param _amount The amount to borrow
     */
    function borrow(uint256 _amount) public {
        require(_amount > 0, "Borrow amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient collateral");

        // Calculate interest
        uint256 interest = (_amount * interestRate) / 100;

        // Update user's loan
        loans[msg.sender] += _amount + interest;

        // Emit borrow event
        emit Borrow(msg.sender, _amount);
    }

    /**
     * @dev Repays a loan
     * @param _amount The amount to repay
     */
    function repay(uint256 _amount) public {
        require(_amount > 0, "Repayment amount must be greater than zero");
        require(loans[msg.sender] > 0, "No loan to repay");

        // Update user's loan
        loans[msg.sender] -= _amount;

        // Emit repay event
        emit Repay(msg.sender, _amount);

        // Transfer funds to contract
        require(msg.sender.transfer(_amount), "Repayment failed");
    }

    /**
     * @dev Gets the user's balance
     * @return The user's balance
     */
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Gets the user's loan amount
     * @return The user's loan amount
     */
    function getLoan() public view returns (uint256) {
        return loans[msg.sender];
    }
}
```
