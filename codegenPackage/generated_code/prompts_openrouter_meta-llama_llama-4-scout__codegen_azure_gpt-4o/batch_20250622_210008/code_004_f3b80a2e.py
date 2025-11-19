"""
Generated Code Metadata:
========================
Original URL: https://decentralized-metis.pages.dev
Prompt: "Develop a basic example of a decentralized finance (DeFi) application on Metis, utilizing its scalable infrastructure and affordable on-chain storage."
Generated: DETERMINISTIC_f3b80a2e211128e4
Batch ID: 20250622_210008
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
 * @title Basic DeFi Application on Metis
 * @dev This contract demonstrates a simple decentralized finance (DeFi) application
 *      that allows users to deposit and withdraw funds, and earn interest.
 *      It is designed to run on Metis Layer 2 blockchain for scalability and affordability.
 */
contract BasicDeFiApp {
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Interest rate (e.g., 5% annual interest rate)
    uint256 public constant INTEREST_RATE = 5;

    // Timestamp of the last deposit for each user
    mapping(address => uint256) private lastDepositTimestamp;

    // Event emitted when a deposit is made
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Allows a user to deposit funds into the contract.
     * @param _amount The amount to deposit (in wei).
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Calculate and apply interest for previous balance
        if (balances[msg.sender] > 0) {
            uint256 interest = calculateInterest(msg.sender);
            balances[msg.sender] += interest;
        }

        // Update user balance and deposit timestamp
        balances[msg.sender] += msg.value;
        lastDepositTimestamp[msg.sender] = block.timestamp;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to withdraw funds from the contract.
     * @param _amount The amount to withdraw (in wei).
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Calculate and apply interest for previous balance
        uint256 interest = calculateInterest(msg.sender);
        balances[msg.sender] += interest;

        // Deduct the withdrawal amount from the user's balance
        balances[msg.sender] -= _amount;

        // Update the deposit timestamp
        lastDepositTimestamp[msg.sender] = block.timestamp;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawal(msg.sender, _amount);
    }

    /**
     * @dev Calculates the interest earned by a user based on their balance and time elapsed.
     * @param _user The address of the user.
     * @return The interest amount (in wei).
     */
    function calculateInterest(address _user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastDepositTimestamp[_user];
        uint256 annualInterest = (balances[_user] * INTEREST_RATE) / 100;
        uint256 interest = (annualInterest * timeElapsed) / 365 days;
        return interest;
    }

    /**
     * @dev Returns the balance of a user, including any accrued interest.
     * @param _user The address of the user.
     * @return The total balance (in wei).
     */
    function getBalance(address _user) external view returns (uint256) {
        uint256 interest = calculateInterest(_user);
        return balances[_user] + interest;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
