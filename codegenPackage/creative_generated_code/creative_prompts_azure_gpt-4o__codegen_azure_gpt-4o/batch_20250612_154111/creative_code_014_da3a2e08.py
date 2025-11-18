"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity function to handle instant payouts for referral commissions and dividends, ensuring real-time earnings updates as described in the MinerDog platform.
Generated: DETERMINISTIC_da3a2e084b641425
Batch ID: 20250612_154111
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
 * @title ReferralPayoutContract
 * @dev This contract handles instant payouts for referral commissions and dividends.
 *      It ensures real-time earnings updates for referrers and dividend recipients.
 */
contract ReferralPayoutContract {
    // Owner of the contract
    address public owner;

    // Mapping to store referral balances
    mapping(address => uint256) public referralBalances;

    // Mapping to store dividend balances
    mapping(address => uint256) public dividendBalances;

    // Event emitted when a payout is made
    event Payout(address indexed recipient, uint256 referralAmount, uint256 dividendAmount);

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Function to handle instant payouts for referral commissions and dividends
     * @param _referrer Address of the referrer to receive referral commission
     * @param _recipient Address of the recipient to receive dividends
     * @param _referralAmount Amount of referral commission to be paid
     * @param _dividendAmount Amount of dividends to be paid
     */
    function payout(
        address _referrer,
        address _recipient,
        uint256 _referralAmount,
        uint256 _dividendAmount
    ) external onlyOwner {
        require(_referrer != address(0), "Invalid referrer address");
        require(_recipient != address(0), "Invalid recipient address");
        require(_referralAmount > 0 || _dividendAmount > 0, "Payout amounts must be greater than zero");

        // Update referral balance
        if (_referralAmount > 0) {
            referralBalances[_referrer] += _referralAmount;
            // Transfer referral commission
            (bool referralSent, ) = _referrer.call{value: _referralAmount}("");
            require(referralSent, "Failed to send referral commission");
        }

        // Update dividend balance
        if (_dividendAmount > 0) {
            dividendBalances[_recipient] += _dividendAmount;
            // Transfer dividends
            (bool dividendSent, ) = _recipient.call{value: _dividendAmount}("");
            require(dividendSent, "Failed to send dividend");
        }

        // Emit payout event
        emit Payout(_referrer, _referralAmount, _dividendAmount);
    }

    /**
     * @dev Fallback function to allow deposits into the contract
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw contract balance (only owner can withdraw)
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");

        (bool sent, ) = owner.call{value: contractBalance}("");
        require(sent, "Failed to withdraw contract balance");
    }
}
```
