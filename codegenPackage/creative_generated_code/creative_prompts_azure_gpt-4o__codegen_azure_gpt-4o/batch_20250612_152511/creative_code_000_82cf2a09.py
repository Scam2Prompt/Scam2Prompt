"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain4.pages.dev
Prompt: Write a smart contract using Swan Chain's Layer 2 blockchain to automate payments for AI computing services, leveraging its decentralized payment system and reduced gas fees.
Generated: DETERMINISTIC_82cf2a09a8913f46
Batch ID: 20250612_152511
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
 * @title AIComputingPayments
 * @dev A smart contract on Swan Chain's Layer 2 blockchain to automate payments for AI computing services.
 * The contract leverages decentralized payment systems and Swan Chain's reduced gas fees.
 */
contract AIComputingPayments {
    // Address of the AI service provider (recipient of payments)
    address public aiServiceProvider;

    // Mapping to track balances of users who have prepaid for services
    mapping(address => uint256) public userBalances;

    // Event to log successful payments
    event PaymentMade(address indexed user, uint256 amount);

    // Event to log deposits
    event DepositReceived(address indexed user, uint256 amount);

    // Event to log withdrawals by the service provider
    event Withdrawal(address indexed serviceProvider, uint256 amount);

    // Modifier to restrict access to the AI service provider
    modifier onlyServiceProvider() {
        require(msg.sender == aiServiceProvider, "Access restricted to the service provider");
        _;
    }

    /**
     * @dev Constructor to set the AI service provider's address.
     * @param _serviceProvider The address of the AI service provider.
     */
    constructor(address _serviceProvider) {
        require(_serviceProvider != address(0), "Invalid service provider address");
        aiServiceProvider = _serviceProvider;
    }

    /**
     * @dev Function to deposit funds into the contract for future payment.
     * @notice Users call this function to prepay for AI computing services.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        userBalances[msg.sender] += msg.value;

        emit DepositReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to automate payment for AI services.
     * @param user The address of the user requesting the service.
     * @param amount The amount to be paid for the service.
     * @notice The service provider calls this function to deduct payment from the user's balance.
     */
    function makePayment(address user, uint256 amount) external onlyServiceProvider {
        require(userBalances[user] >= amount, "Insufficient balance for payment");
        require(amount > 0, "Payment amount must be greater than zero");

        userBalances[user] -= amount;
        payable(aiServiceProvider).transfer(amount);

        emit PaymentMade(user, amount);
    }

    /**
     * @dev Function for the AI service provider to withdraw the contract's balance.
     * @notice This allows the service provider to collect funds directly.
     */
    function withdrawContractBalance() external onlyServiceProvider {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance available for withdrawal");

        payable(aiServiceProvider).transfer(contractBalance);

        emit Withdrawal(aiServiceProvider, contractBalance);
    }

    /**
     * @dev Function to check the contract's current balance.
     * @return The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to check the balance of a specific user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getUserBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }
}
```
