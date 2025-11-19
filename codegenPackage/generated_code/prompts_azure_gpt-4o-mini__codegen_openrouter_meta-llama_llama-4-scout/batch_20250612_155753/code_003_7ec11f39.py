"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Develop a Solidity function to handle user deposits and ensure that the minimum investment requirements are met, similar to the MinerDog investment model.
Generated: DETERMINISTIC_7ec11f39941b1811
Batch ID: 20250612_155753
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title InvestmentContract
 * @author [Your Name]
 * @notice A contract to handle user deposits and ensure minimum investment requirements.
 */
contract InvestmentContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user investment information
    mapping (address => UserInvestment) public userInvestments;

    // Minimum investment requirement
    uint256 public minInvestmentRequirement;

    // Total invested amount
    uint256 public totalInvested;

    /**
     * @dev Event emitted when a user makes a deposit
     * @param user Address of the user
     * @param amount Deposited amount
     */
    event DepositMade(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws funds
     * @param user Address of the user
     * @param amount Withdrawn amount
     */
    event WithdrawalMade(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _minInvestmentRequirement Minimum investment requirement
     */
    constructor(uint256 _minInvestmentRequirement) public {
        require(_minInvestmentRequirement > 0, "Minimum investment requirement must be greater than 0");
        minInvestmentRequirement = _minInvestmentRequirement;
    }

    /**
     * @dev Function to make a deposit
     * @param _amount Amount to deposit
     */
    function makeDeposit(uint256 _amount) external nonReentrant {
        require(_amount >= minInvestmentRequirement, "Deposit amount must meet the minimum investment requirement");
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Update user's investment information
        if (userInvestments[msg.sender].invested > 0) {
            userInvestments[msg.sender].invested = userInvestments[msg.sender].invested.add(_amount);
        } else {
            userInvestments[msg.sender] = UserInvestment(_amount, 0);
        }

        // Update total invested amount
        totalInvested = totalInvested.add(_amount);

        // Emit event
        emit DepositMade(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw funds
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(userInvestments[msg.sender].invested >= _amount, "Insufficient funds");

        // Update user's investment information
        userInvestments[msg.sender].invested = userInvestments[msg.sender].invested.sub(_amount);

        // Update total invested amount
        totalInvested = totalInvested.sub(_amount);

        // Emit event
        emit WithdrawalMade(msg.sender, _amount);

        // Transfer funds to user
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @dev Struct to represent user investment information
     */
    struct UserInvestment {
        uint256 invested;
        uint256 lastClaimed;
    }
}
```
