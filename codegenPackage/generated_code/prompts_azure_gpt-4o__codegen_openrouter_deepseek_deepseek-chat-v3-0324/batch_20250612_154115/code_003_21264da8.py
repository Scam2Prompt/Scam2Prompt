"""
Generated Code Metadata:
========================
Original URL: https://orikod.com
Prompt: Create a Solidity smart contract optimized for Arbitrum AnyTrust chains, designed for micro-payment applications with low gas fees.
Generated: DETERMINISTIC_21264da885b45918
Batch ID: 20250612_154115
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
 * @title MicroPaymentContract
 * @dev A gas-optimized smart contract for micro-payments on Arbitrum AnyTrust chains
 */
contract MicroPaymentContract {
    // Struct to store payment details
    struct Payment {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        bool isWithdrawn;
    }

    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Mapping to store payments by ID
    mapping(bytes32 => Payment) private payments;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event PaymentCreated(
        bytes32 indexed paymentId,
        address indexed sender,
        address indexed recipient,
        uint256 amount
    );
    event PaymentWithdrawn(bytes32 indexed paymentId, address indexed recipient, uint256 amount);
    event BalanceWithdrawn(address indexed user, uint256 amount);

    // Modifier to check for zero address
    modifier notZeroAddress(address _address) {
        require(_address != address(0), "Invalid address: zero address");
        _;
    }

    /**
     * @dev Deposit funds into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Create a new payment
     * @param _recipient Address of the payment recipient
     * @param _amount Amount to be paid
     * @return paymentId Unique identifier for the payment
     */
    function createPayment(
        address _recipient,
        uint256 _amount
    ) external notZeroAddress(_recipient) returns (bytes32 paymentId) {
        require(_amount > 0, "Payment amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        paymentId = keccak256(abi.encodePacked(msg.sender, _recipient, _amount, block.timestamp));

        payments[paymentId] = Payment({
            sender: msg.sender,
            recipient: _recipient,
            amount: _amount,
            timestamp: block.timestamp,
            isWithdrawn: false
        });

        emit PaymentCreated(paymentId, msg.sender, _recipient, _amount);
        return paymentId;
    }

    /**
     * @dev Withdraw a payment
     * @param _paymentId ID of the payment to withdraw
     */
    function withdrawPayment(bytes32 _paymentId) external {
        Payment storage payment = payments[_paymentId];
        require(payment.recipient == msg.sender, "Not the payment recipient");
        require(!payment.isWithdrawn, "Payment already withdrawn");
        require(payment.amount > 0, "Invalid payment amount");

        payment.isWithdrawn = true;
        balances[msg.sender] += payment.amount;

        emit PaymentWithdrawn(_paymentId, msg.sender, payment.amount);
    }

    /**
     * @dev Withdraw balance from the contract
     * @param _amount Amount to withdraw
     */
    function withdrawBalance(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");

        emit BalanceWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Get user balance
     * @param _user Address of the user
     * @return balance Current balance of the user
     */
    function getBalance(address _user) external view returns (uint256 balance) {
        return balances[_user];
    }

    /**
     * @dev Get payment details
     * @param _paymentId ID of the payment
     * @return sender Address of the payment sender
     * @return recipient Address of the payment recipient
     * @return amount Payment amount
     * @return timestamp Payment creation timestamp
     * @return isWithdrawn Whether the payment has been withdrawn
     */
    function getPaymentDetails(
        bytes32 _paymentId
    )
        external
        view
        returns (
            address sender,
            address recipient,
            uint256 amount,
            uint256 timestamp,
            bool isWithdrawn
        )
    {
        Payment storage payment = payments[_paymentId];
        return (
            payment.sender,
            payment.recipient,
            payment.amount,
            payment.timestamp,
            payment.isWithdrawn
        );
    }
}
```
