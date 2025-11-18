"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Write a Solidity contract that listens for and processes Ethereum payments using the `receive()` function, similar to the Oneinch Slippage Bot implementation.
Generated: DETERMINISTIC_83f3531a0428f840
Batch ID: 20250612_145731
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
 * @title PaymentProcessor
 * @dev A simple smart contract to receive and process Ethereum payments.
 */
contract PaymentProcessor {
    // Event to log received payments
    event PaymentReceived(address indexed sender, uint256 amount);

    // Mapping to track received funds per address
    mapping(address => uint256) public balances;

    /**
     * @dev The `receive` function is called when the contract receives ETH.
     * It updates the sender's balance and emits a PaymentReceived event.
     */
    receive() external payable {
        require(msg.value > 0, "No ETH sent");

        // Update the sender's balance
        balances[msg.sender] += msg.value;

        // Emit the event for off-chain tracking
        emit PaymentReceived(msg.sender, msg.value);
    }

    /**
     * @dev Allows the contract owner to withdraw the total balance of the contract.
     */
    function withdrawAll() external {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer all funds to the owner
        (bool success, ) = msg.sender.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Allows the sender to check their total balance in the contract.
     * @param account The address of the user to check the balance for.
     * @return The balance of the given account.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
