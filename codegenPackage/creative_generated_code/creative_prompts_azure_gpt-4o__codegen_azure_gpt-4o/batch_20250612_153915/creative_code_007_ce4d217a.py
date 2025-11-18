"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Recommend best practices for securing smart contracts on The Open Network and provide code examples.
Generated: DETERMINISTIC_ce4d217a68fadb50
Batch ID: 20250612_153915
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
 * @title SecureSmartContract
 * @dev Demonstrates best practices for securing smart contracts on The Open Network (TON).
 * NOTE: Always follow these practices when deploying contracts to TON or similar blockchain environments.
 */
contract SecureSmartContract {
    // State variables
    address private owner;
    mapping(address => uint256) private balances;

    // Events for transparency
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender; // Set the contract owner as the deployer
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: You are not the owner");
        _;
    }

    /**
     * @dev Deposit funds into the contract.
     * Emits a Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value; // Update user balance
        emit Deposit(msg.sender, msg.value); // Emit deposit event
    }

    /**
     * @dev Withdraw funds from the contract.
     * Emits a Withdrawal event.
     * Proper checks are implemented to prevent reentrancy attacks.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balance before transferring to prevent reentrancy attacks
        balances[msg.sender] -= amount;

        // Securely transfer funds to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed: Unable to send Ether");

        emit Withdrawal(msg.sender, amount); // Emit withdrawal event
    }

    /**
     * @dev Owner-only function to withdraw all funds from the contract.
     * Avoids locking funds in case of emergency.
     */
    function emergencyWithdrawAll() external onlyOwner {
        // Transfer remaining contract balance to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Emergency withdrawal failed");
    }

    /**
     * @dev Get the balance of the caller.
     * Returns the balance of the user's account in the contract.
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Prevent accidental Ether transfers to the contract by overriding the fallback function.
     */
    fallback() external payable {
        revert("Fallback function disabled");
    }

    /**
     * @dev Receive function allows secure deposits directly to the contract.
     */
    receive() external payable {
        require(msg.value > 0, "Received amount must be greater than zero");
        balances[msg.sender] += msg.value; // Update user balance
        emit Deposit(msg.sender, msg.value); // Emit deposit event
    }

    /**
     * @dev Change ownership to another address.
     * Accessible only by the current owner.
     * Ensures ownership transfer is intentional.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```

### Security Best Practices Implemented in the Code:
1. **Reentrancy Prevention:** Balance updates are performed before transferring funds to prevent reentrancy attacks.
2. **Access Control:** `onlyOwner` modifier ensures critical functions are restricted to the owner.
3. **Fallback and Receive Functions:** Proper handling of Ether transfers with `fallback` and `receive` to prevent accidental misuse.
4. **Event Logging:** Transparency is maintained by emitting events for deposits and withdrawals.
5. **Error Handling:** Custom error messages clarify failure causes.
6. **Ownership Transfer:** Ownership change is safeguarded with checks and restrictions.

Deploy and test the contract thoroughly before using it in a production environment.
