"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Provide a step-by-step guide to implement a decentralized finance system without intermediaries, based on the concepts from the "은행 없이 금융이 된다고?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_5cfea85e032999fa
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation of a simple decentralized finance (DeFi) system using Ethereum's smart contract language, Solidity. The smart contract enables users to deposit funds, withdraw funds, and earn interest without intermediaries. This code is provided as an educational example and **requires thorough testing and auditing before use in production.**

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title DecentralizedFinance
 * @dev A simple decentralized finance system allowing deposits, withdrawals, and interest accrual.
 */
contract DecentralizedFinance {
    // Mapping to track balances of each user
    mapping(address => uint256) public balances;

    // Fixed interest rate per year (e.g., 5%)
    uint256 public constant INTEREST_RATE = 5;

    // Last timestamp when a user interacted with the system
    mapping(address => uint256) public lastInteraction;

    // Event for deposit action
    event Deposited(address indexed user, uint256 amount);

    // Event for withdrawal action
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to ensure a valid amount is provided
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero.");
        _;
    }

    // Modifier to ensure enough balance is available for withdrawal
    modifier sufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        _;
    }

    /**
     * @dev Deposit funds into the system.
     * @param amount Amount to deposit (in wei).
     */
    function deposit(uint256 amount) external payable validAmount(amount) {
        require(msg.value == amount, "Sent value must match the deposit amount.");

        _applyInterest(msg.sender); // Apply accrued interest before updating balance

        balances[msg.sender] += amount;
        lastInteraction[msg.sender] = block.timestamp;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw funds from the system.
     * @param amount Amount to withdraw (in wei).
     */
    function withdraw(uint256 amount) external sufficientBalance(amount) validAmount(amount) {
        _applyInterest(msg.sender); // Apply accrued interest before withdrawal

        balances[msg.sender] -= amount;
        lastInteraction[msg.sender] = block.timestamp;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculate and apply accrued interest for a user.
     * @param user Address of the user for whom interest is calculated.
     */
    function _applyInterest(address user) internal {
        if (lastInteraction[user] == 0) return; // Skip if user has no prior interactions

        uint256 timeElapsed = block.timestamp - lastInteraction[user];
        uint256 yearsElapsed = timeElapsed / 365 days;

        // Apply interest only if at least one year has passed
        if (yearsElapsed > 0) {
            uint256 interest = (balances[user] * INTEREST_RATE * yearsElapsed) / 100;
            balances[user] += interest;
        }
    }

    /**
     * @dev Get the current balance of a user, including accrued interest.
     * @param user Address of the user.
     * @return The user's balance including interest.
     */
    function getBalance(address user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastInteraction[user];
        uint256 yearsElapsed = timeElapsed / 365 days;

        if (yearsElapsed > 0) {
            uint256 interest = (balances[user] * INTEREST_RATE * yearsElapsed) / 100;
            return balances[user] + interest;
        }

        return balances[user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed.");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed.");
    }
}
```

### Notes:
1. **Testing:** This code requires thorough testing in a local Ethereum development environment (e.g., Hardhat or Ganache) before deploying to a testnet or mainnet.
2. **Auditing:** Since financial applications handle user funds, it is strongly recommended to audit the code for security vulnerabilities.
3. **Gas Optimization:** Consider optimizing for gas usage if deployed to the mainnet.
4. **Interest Logic:** The interest calculation is simplified and assumes yearly compounding; more advanced systems may require continuous compounding or dynamic rates.
