"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: Describe the process of wrapping FLR into WFLR and its implications for using it in EVM-compatible dapps.
Generated: DETERMINISTIC_e90ea5e40385d448
Batch ID: 20250612_162431
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
 * @title FLR to WFLR Wrapping Contract
 * @notice This contract allows users to wrap FLR (native token) into WFLR (ERC-20 wrapped version)
 *         and unwrap WFLR back to FLR. It is designed to enable the use of WFLR in EVM-compatible dApps.
 */
contract WFLR {
    // Mapping to store balances of WFLR for each address
    mapping(address => uint256) private balances;

    // Event emitted when FLR is wrapped into WFLR
    event Deposit(address indexed account, uint256 amount);

    // Event emitted when WFLR is unwrapped into FLR
    event Withdrawal(address indexed account, uint256 amount);

    /**
     * @notice Wrap FLR into WFLR
     * @dev The sender must send FLR to the contract via a payable transaction.
     *      The amount sent will be converted into WFLR and credited to the sender's balance.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Credit the sender's balance with the deposited amount
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @notice Unwrap WFLR back into FLR
     * @dev The sender must have sufficient WFLR balance to perform the withdrawal.
     * @param amount The amount of WFLR to unwrap into FLR.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient WFLR balance");

        // Deduct the amount from the sender's balance
        balances[msg.sender] -= amount;

        // Transfer FLR back to the sender
        payable(msg.sender).transfer(amount);

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @notice Get the WFLR balance of a specific address
     * @param account The address to query the balance for.
     * @return The WFLR balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Fallback function to reject direct FLR transfers without using the deposit method.
     */
    receive() external payable {
        revert("Direct FLR transfers are not allowed. Use the deposit method.");
    }
}
```

This contract implements wrapping native FLR tokens into WFLR (wrapped FLR) and unwrapping WFLR back into FLR. It enables developers to use WFLR in EVM-compatible dApps that require ERC-20 standard tokens.
