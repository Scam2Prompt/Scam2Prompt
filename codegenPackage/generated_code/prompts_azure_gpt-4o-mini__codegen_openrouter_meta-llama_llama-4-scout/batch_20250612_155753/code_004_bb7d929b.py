"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Outline a Solidity contract that includes a mechanism for tracking user commissions and withdrawals, inspired by the MinerDog platform's approach to user earnings.
Generated: DETERMINISTIC_bb7d929b27b9914c
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CommissionTracker
 * @author [Your Name]
 * @notice A contract for tracking user commissions and withdrawals.
 */
contract CommissionTracker is Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their commission balances
    mapping (address => uint256) public userCommissions;

    // Mapping of user addresses to their withdrawal history
    mapping (address => uint256[]) public userWithdrawals;

    // Event emitted when a user earns a commission
    event CommissionEarned(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their commission
    event CommissionWithdrawn(address indexed user, uint256 amount);

    // Event emitted when the contract owner withdraws funds
    event OwnerWithdrawal(address indexed owner, uint256 amount);

    // Total commission earned by all users
    uint256 public totalCommissions;

    // Contract owner's address
    address public owner;

    // Constructor
    constructor() public {
        owner = msg.sender;
    }

    /**
     * @dev Adds a commission to a user's balance
     * @param user The user's address
     * @param amount The commission amount
     */
    function addCommission(address user, uint256 amount) public onlyOwner {
        require(amount > 0, "Commission amount must be greater than 0");
        userCommissions[user] = userCommissions[user].add(amount);
        totalCommissions = totalCommissions.add(amount);
        emit CommissionEarned(user, amount);
    }

    /**
     * @dev Allows a user to withdraw their commission
     * @param amount The withdrawal amount
     */
    function withdrawCommission(uint256 amount) public {
        require(userCommissions[msg.sender] >= amount, "Insufficient commission balance");
        require(amount > 0, "Withdrawal amount must be greater than 0");
        userCommissions[msg.sender] = userCommissions[msg.sender].sub(amount);
        userWithdrawals[msg.sender].push(amount);
        payable(msg.sender).transfer(amount);
        emit CommissionWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows the contract owner to withdraw funds
     * @param amount The withdrawal amount
     */
    function ownerWithdraw(uint256 amount) public {
        require(msg.sender == owner, "Only the contract owner can withdraw funds");
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
        emit OwnerWithdrawal(owner, amount);
    }

    /**
     * @dev Returns the user's commission balance
     * @param user The user's address
     * @return The user's commission balance
     */
    function getUserCommission(address user) public view returns (uint256) {
        return userCommissions[user];
    }

    /**
     * @dev Returns the user's withdrawal history
     * @param user The user's address
     * @return The user's withdrawal history
     */
    function getUserWithdrawals(address user) public view returns (uint256[] memory) {
        return userWithdrawals[user];
    }
}
```
