"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Create a Solidity contract that tracks deposits and associates them with wallet addresses, ensuring compatibility with Coinbase Wallet and Ledger hardware wallets, as referenced in the DOG token presale.
Generated: DETERMINISTIC_52e4afdc0d575295
Batch ID: 20250612_153420
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
 * @title DepositTracker
 * @dev A Solidity contract to track deposits and associate them with wallet addresses.
 *      Compatible with Coinbase Wallet and Ledger hardware wallets.
 */
contract DepositTracker {
    // Mapping to store deposit amounts for each wallet address
    mapping(address => uint256) public deposits;

    // Event emitted when a deposit is made
    event DepositMade(address indexed wallet, uint256 amount);

    // Event emitted when a withdrawal is made
    event WithdrawalMade(address indexed wallet, uint256 amount);

    /**
     * @dev Allows users to deposit funds into the contract.
     *      The deposit amount is tracked against the sender's wallet address.
     *      This ensures compatibility with Coinbase Wallet and Ledger hardware wallets.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the deposit mapping for the sender's address
        deposits[msg.sender] += msg.value;

        // Emit the deposit event
        emit DepositMade(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their deposited funds.
     * @param amount The amount to withdraw (must be less than or equal to the deposited amount).
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "Insufficient balance");

        // Deduct the withdrawal amount from the sender's deposit
        deposits[msg.sender] -= amount;

        // Transfer the amount back to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit WithdrawalMade(msg.sender, amount);
    }

    /**
     * @dev Returns the deposit balance of a given wallet address.
     * @param wallet The address to query the deposit balance for.
     * @return The deposit balance of the wallet.
     */
    function getDepositBalance(address wallet) external view returns (uint256) {
        return deposits[wallet];
    }

    /**
     * @dev Fallback function to prevent accidental transfer of funds without calling the deposit function.
     *      Reverts any direct transfers to the contract.
     */
    fallback() external payable {
        revert("Direct transfers not allowed. Use deposit function.");
    }

    /**
     * @dev Receive function to prevent accidental transfer of funds without calling the deposit function.
     *      Reverts any direct transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed. Use deposit function.");
    }
}
```
