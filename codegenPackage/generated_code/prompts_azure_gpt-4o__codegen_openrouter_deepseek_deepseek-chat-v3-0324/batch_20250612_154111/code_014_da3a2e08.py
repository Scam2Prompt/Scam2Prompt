"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity function to handle instant payouts for referral commissions and dividends, ensuring real-time earnings updates as described in the MinerDog platform.
Generated: DETERMINISTIC_da3a2e084b641425
Batch ID: 20250612_154111
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MinerDogPayouts is Ownable, ReentrancyGuard {
    // Struct to store user earnings information
    struct UserEarnings {
        uint256 referralCommission;
        uint256 dividends;
        uint256 lastPayoutTimestamp;
    }

    // Mapping to track user earnings
    mapping(address => UserEarnings) public userEarnings;

    // The token used for payouts
    IERC20 public payoutToken;

    // Events
    event ReferralCommissionPaid(address indexed referrer, address indexed referee, uint256 amount);
    event DividendsPaid(address indexed user, uint256 amount);
    event PayoutTokenUpdated(address indexed newToken);

    // Constructor
    constructor(address _payoutToken) {
        require(_payoutToken != address(0), "Invalid token address");
        payoutToken = IERC20(_payoutToken);
    }

    /**
     * @dev Update the payout token address
     * @param _newToken Address of the new payout token
     */
    function updatePayoutToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        payoutToken = IERC20(_newToken);
        emit PayoutTokenUpdated(_newToken);
    }

    /**
     * @dev Add referral commission to referrer's balance
     * @param _referrer Address of the referrer
     * @param _amount Amount of commission to add
     */
    function addReferralCommission(address _referrer, uint256 _amount) external onlyOwner {
        require(_referrer != address(0), "Invalid referrer address");
        require(_amount > 0, "Amount must be greater than 0");

        userEarnings[_referrer].referralCommission += _amount;
    }

    /**
     * @dev Add dividends to user's balance
     * @param _user Address of the user
     * @param _amount Amount of dividends to add
     */
    function addDividends(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than 0");

        userEarnings[_user].dividends += _amount;
    }

    /**
     * @dev Claim all pending earnings (referral commissions + dividends)
     */
    function claimEarnings() external nonReentrant {
        address user = msg.sender;
        UserEarnings storage earnings = userEarnings[user];

        uint256 totalAmount = earnings.referralCommission + earnings.dividends;
        require(totalAmount > 0, "No earnings to claim");

        // Reset balances before transfer to prevent reentrancy
        earnings.referralCommission = 0;
        earnings.dividends = 0;
        earnings.lastPayoutTimestamp = block.timestamp;

        // Transfer tokens to user
        require(payoutToken.transfer(user, totalAmount), "Transfer failed");

        emit ReferralCommissionPaid(address(0), user, earnings.referralCommission);
        emit DividendsPaid(user, earnings.dividends);
    }

    /**
     * @dev Get total claimable amount for a user
     * @param _user Address of the user
     * @return Total claimable amount
     */
    function getClaimableAmount(address _user) external view returns (uint256) {
        UserEarnings memory earnings = userEarnings[_user];
        return earnings.referralCommission + earnings.dividends;
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to this contract
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function recoverERC20(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(payoutToken), "Cannot withdraw payout token");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
