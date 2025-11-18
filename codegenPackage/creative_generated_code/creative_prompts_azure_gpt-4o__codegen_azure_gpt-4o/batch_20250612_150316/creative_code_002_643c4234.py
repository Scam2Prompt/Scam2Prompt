"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Implement a referral system in a smart contract where a portion of the entry fee is credited to the referrer’s balance, as described on BibbyDivs.com.
Generated: DETERMINISTIC_643c42340be2dd5b
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready smart contract written in Solidity for implementing a referral system:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ReferralSystem
 * @dev A simple referral system where a portion of the entry fee is credited to the referrer’s balance.
 */
contract ReferralSystem {
    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Percentage of entry fee that goes to the referrer (e.g., 10%)
    uint256 public constant REFERRAL_PERCENTAGE = 10;

    // Event emitted when a deposit is made
    event Deposit(address indexed user, address indexed referrer, uint256 amount, uint256 referrerReward);

    // Event emitted when a user withdraws funds
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Allows a user to deposit funds and optionally specify a referrer.
     * @param referrer Address of the referrer, or address(0) if there is no referrer.
     */
    function deposit(address referrer) external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        uint256 depositAmount = msg.value;

        // Calculate referral reward
        uint256 referrerReward = 0;
        if (referrer != address(0) && referrer != msg.sender) {
            referrerReward = (depositAmount * REFERRAL_PERCENTAGE) / 100;
            balances[referrer] += referrerReward; // Credit reward to referrer's balance
        }

        // Update sender's balance
        balances[msg.sender] += depositAmount - referrerReward;

        // Emit event
        emit Deposit(msg.sender, referrer, depositAmount, referrerReward);
    }

    /**
     * @dev Allows a user to withdraw their balance.
     */
    function withdraw() external {
        uint256 userBalance = balances[msg.sender];
        require(userBalance > 0, "Insufficient balance");

        // Reset user's balance before sending to avoid reentrancy attacks
        balances[msg.sender] = 0;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: userBalance}("");
        require(success, "Withdrawal failed");

        // Emit event
        emit Withdrawal(msg.sender, userBalance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not supported");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not supported");
    }
}
```

This smart contract is designed to handle deposits, calculate referral rewards, and manage user withdrawals securely while adhering to Solidity best practices.
