"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavosstg.wpenginepowered.com
Prompt: Write code to implement multi-factor authentication for a Braavos smart contract wallet, leveraging its account segmentation and daily withdrawal limit features.
Generated: DETERMINISTIC_379058754bc792cf
Batch ID: 20250612_150323
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MultiFactorAuthWallet is Ownable {
    // Define the structure for user accounts
    struct UserAccount {
        bool isActive;
        uint256 dailyWithdrawalLimit;
        uint256 withdrawnToday;
        uint256 lastWithdrawalDate;
    }

    // Mapping to store user accounts
    mapping(address => UserAccount) private userAccounts;

    // Event emitted on successful withdrawal
    event Withdrawal(address indexed user, uint256 amount);

    // Modifier to check if the user is active
    modifier onlyActiveUser() {
        require(userAccounts[msg.sender].isActive, "User is not active");
        _;
    }

    // Function to activate a user account with a withdrawal limit
    function activateUser(uint256 dailyLimit) external {
        require(!userAccounts[msg.sender].isActive, "User already active");
        userAccounts[msg.sender] = UserAccount({
            isActive: true,
            dailyWithdrawalLimit: dailyLimit,
            withdrawnToday: 0,
            lastWithdrawalDate: block.timestamp
        });
    }

    // Function to withdraw funds from the wallet
    function withdraw(IERC20 token, uint256 amount) external onlyActiveUser {
        UserAccount storage account = userAccounts[msg.sender];
        
        // Check if the withdrawal is within the daily limit
        require(canWithdrawToday(account), "Daily limit exceeded");
        require(amount <= account.dailyWithdrawalLimit, "Amount exceeds daily limit");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update withdrawal records
        account.withdrawnToday += amount;
        if (block.timestamp / 1 days != account.lastWithdrawalDate / 1 days) {
            account.withdrawnToday = amount; // Reset for new day
        }
        account.lastWithdrawalDate = block.timestamp;

        // Transfer tokens to the user
        token.transfer(msg.sender, amount);
        emit Withdrawal(msg.sender, amount);
    }

    // Function to check if the user can withdraw today
    function canWithdrawToday(UserAccount storage account) internal view returns (bool) {
        return account.withdrawnToday < account.dailyWithdrawalLimit ||
               (block.timestamp / 1 days != account.lastWithdrawalDate / 1 days);
    }

    // Function to deactivate a user account
    function deactivateUser() external onlyActiveUser {
        delete userAccounts[msg.sender];
    }

    // Function to get user account details
    function getUserAccountDetails() external view returns (UserAccount memory) {
        return userAccounts[msg.sender];
    }
}
```
