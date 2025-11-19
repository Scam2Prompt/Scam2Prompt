"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Develop a Solidity function to handle user deposits and ensure that the minimum investment requirements are met, similar to the MinerDog investment model.
Generated: DETERMINISTIC_7ec11f39941b1811
Batch ID: 20250612_155753
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

contract MinerDogInvestment {
    // State variable to hold the minimum investment requirement
    uint256 public constant MIN_INVESTMENT = 0.1 ether;

    // Mapping to track deposits of each user
    mapping(address => uint256) public userDeposits;

    // Event to log deposits
    event Deposit(address indexed user, uint256 amount);

    // Modifier to ensure that the sender has sent a sufficient amount
    modifier onlyValidInvestment(uint256 _amount) {
        require(_amount >= MIN_INVESTMENT, "Investment does not meet the minimum requirement.");
        _;
    }

    /**
     * @dev Function to handle user deposits.
     * @param _amount The amount of ether the user wishes to invest.
     */
    function deposit() external payable onlyValidInvestment(msg.value) {
        // Update the user's deposit balance
        userDeposits[msg.sender] += msg.value;

        // Emit a Deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw user deposits.
     * @param _amount The amount of ether the user wishes to withdraw.
     */
    function withdraw(uint256 _amount) external {
        // Ensure the user has sufficient balance to withdraw
        require(userDeposits[msg.sender] >= _amount, "Insufficient balance to withdraw.");

        // Update the user's deposit balance
        userDeposits[msg.sender] -= _amount;

        // Transfer the amount to the user
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed.");

        // Log the withdrawal event (optional)
        // emit Withdrawal(msg.sender, _amount);
    }

    /**
     * @dev Function to check the user's deposit balance.
     * @return The deposit balance of the user.
     */
    function getUserDeposit() external view returns (uint256) {
        return userDeposits[msg.sender];
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("Direct ether transfers not allowed. Use the deposit function.");
    }
}
```
