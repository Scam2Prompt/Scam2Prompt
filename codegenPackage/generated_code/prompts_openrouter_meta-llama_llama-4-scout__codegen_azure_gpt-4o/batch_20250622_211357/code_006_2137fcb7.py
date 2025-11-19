"""
Generated Code Metadata:
========================
Original URL: https://chainfixprotocol.pages.dev
Prompt: Design a use case for Multichain's anyCall feature, and provide a code example of how to implement it for a specific use case, such as cross-chain lending or borrowing.
Generated: DETERMINISTIC_2137fcb7fbd08814
Batch ID: 20250622_211357
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
 * @title CrossChainLending
 * @dev A smart contract demonstrating Multichain's anyCall feature for cross-chain lending and borrowing.
 * This contract allows users to borrow funds on one chain and repay them on another chain.
 */

interface IAnyCall {
    function anyCall(
        address to,
        bytes calldata data,
        address fallback,
        uint256 toChainID
    ) external payable;
}

contract CrossChainLending {
    // Address of the AnyCall contract
    address public anyCallAddress;

    // Mapping to track user borrow balances across chains
    mapping(address => uint256) public borrowBalances;

    // Event emitted when a cross-chain borrow is initiated
    event BorrowInitiated(address indexed user, uint256 amount, uint256 targetChainID);

    // Event emitted when a cross-chain repayment is received
    event RepaymentReceived(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the AnyCall contract address.
     * @param _anyCallAddress Address of the AnyCall contract.
     */
    constructor(address _anyCallAddress) {
        require(_anyCallAddress != address(0), "Invalid AnyCall address");
        anyCallAddress = _anyCallAddress;
    }

    /**
     * @dev Function to initiate a cross-chain borrow.
     * @param amount The amount to borrow.
     * @param targetChainID The ID of the target chain where the funds will be sent.
     */
    function borrow(uint256 amount, uint256 targetChainID) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value >= amount, "Insufficient funds for borrow");

        // Update the borrow balance for the user
        borrowBalances[msg.sender] += amount;

        // Prepare the data payload for the cross-chain call
        bytes memory data = abi.encode(msg.sender, amount);

        // Make the cross-chain call using AnyCall
        IAnyCall(anyCallAddress).anyCall{value: msg.value}(
            address(this), // Target contract address on the destination chain
            data,          // Data payload
            address(0),    // Fallback address (not used in this example)
            targetChainID  // Target chain ID
        );

        emit BorrowInitiated(msg.sender, amount, targetChainID);
    }

    /**
     * @dev Function to handle repayment from another chain.
     * This function is called by the AnyCall contract on the destination chain.
     * @param user The address of the user repaying the loan.
     * @param amount The amount being repaid.
     */
    function anyExecute(bytes calldata data) external returns (bool success) {
        // Decode the data payload
        (address user, uint256 amount) = abi.decode(data, (address, uint256));

        require(borrowBalances[user] >= amount, "Repayment exceeds borrow balance");

        // Update the borrow balance for the user
        borrowBalances[user] -= amount;

        emit RepaymentReceived(user, amount);

        return true;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
