"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Design a simple DeFi application (e.g., AMM, Perps, Lend) on Berachain, utilizing its validators and Proof-of-Liquidity consensus.
Generated: DETERMINISTIC_b11ef7c67145ce60
Batch ID: 20250622_205751
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
 * @title Simple DeFi Lending Application on Berachain
 * @dev This contract allows users to deposit and borrow assets using Berachain's Proof-of-Liquidity consensus.
 * Validators are incentivized to participate in the protocol by earning fees.
 */
contract DeFiLending {
    // Struct to store user balances
    struct UserBalance {
        uint256 deposit; // Amount deposited by the user
        uint256 borrow;  // Amount borrowed by the user
    }

    // Mapping to store balances of each user
    mapping(address => UserBalance) public balances;

    // Interest rate for borrowing (e.g., 5% annualized)
    uint256 public constant BORROW_INTEREST_RATE = 5;

    // Validator fee percentage (e.g., 1% of all transactions)
    uint256 public constant VALIDATOR_FEE_PERCENTAGE = 1;

    // Address of the validator (for fee distribution)
    address public validator;

    // Event declarations
    event Deposit(address indexed user, uint256 amount);
    event Borrow(address indexed user, uint256 amount);
    event Repay(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the validator address.
     * @param _validator Address of the validator.
     */
    constructor(address _validator) {
        require(_validator != address(0), "Validator address cannot be zero");
        validator = _validator;
    }

    /**
     * @dev Allows a user to deposit funds into the protocol.
     * @param amount Amount to deposit.
     */
    function deposit(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect deposit amount");

        // Update user balance
        balances[msg.sender].deposit += amount;

        // Emit deposit event
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Allows a user to borrow funds from the protocol.
     * @param amount Amount to borrow.
     */
    function borrow(uint256 amount) external {
        require(balances[msg.sender].deposit >= amount, "Insufficient collateral");

        // Calculate validator fee
        uint256 validatorFee = (amount * VALIDATOR_FEE_PERCENTAGE) / 100;

        // Update user balance
        balances[msg.sender].borrow += amount;

        // Transfer borrowed amount minus validator fee to the user
        payable(msg.sender).transfer(amount - validatorFee);

        // Transfer validator fee to the validator
        payable(validator).transfer(validatorFee);

        // Emit borrow event
        emit Borrow(msg.sender, amount);
    }

    /**
     * @dev Allows a user to repay borrowed funds.
     * @param amount Amount to repay.
     */
    function repay(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect repayment amount");
        require(balances[msg.sender].borrow >= amount, "Repayment exceeds borrowed amount");

        // Update user balance
        balances[msg.sender].borrow -= amount;

        // Emit repay event
        emit Repay(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their deposited funds.
     * @param amount Amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(balances[msg.sender].deposit >= amount, "Insufficient deposit balance");
        require(balances[msg.sender].borrow == 0, "Outstanding borrow must be repaid first");

        // Update user balance
        balances[msg.sender].deposit -= amount;

        // Transfer the withdrawn amount to the user
        payable(msg.sender).transfer(amount);

        // Emit withdraw event
        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
