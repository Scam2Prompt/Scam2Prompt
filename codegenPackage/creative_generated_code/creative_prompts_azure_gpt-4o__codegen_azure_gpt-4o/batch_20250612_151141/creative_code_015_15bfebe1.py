"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Solidity contract to implement the Crudo Protocol's referral program, including features for tracking referrals, calculating bonuses, and distributing rewards.
Generated: DETERMINISTIC_15bfebe13bf02f1b
Batch ID: 20250612_151141
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
 * @title CrudoReferralProgram
 * @dev A contract implementing the Crudo Protocol's referral program, allowing tracking of referrals,
 * calculating bonuses, and distributing rewards.
 */
contract CrudoReferralProgram {
    // Struct to hold referral information.
    struct Referral {
        uint256 totalReferrals;    // Total number of referrals made by this address.
        uint256 totalRewards;      // Total rewards accumulated by this address.
    }
    
    // Mapping to store referral data for each address.
    mapping(address => Referral) public referrals;

    // Mapping to track which referrer referred each address.
    mapping(address => address) public referrerOf;

    // Admin address for managing the program
    address public admin;

    // Event emitted when a new referral is recorded.
    event ReferralRecorded(address indexed referrer, address indexed referee);

    // Event emitted when rewards are distributed.
    event RewardsDistributed(address indexed referrer, uint256 rewardAmount);

    // Modifier to restrict access to admin-only functions.
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    // Constructor to initialize the admin address.
    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Function to record a referral.
     * @param _referrer The address of the referrer.
     * @param _referee The address of the referee.
     */
    function recordReferral(address _referrer, address _referee) external {
        require(_referrer != address(0), "Referrer cannot be the zero address");
        require(_referee != address(0), "Referee cannot be the zero address");
        require(referrerOf[_referee] == address(0), "Referee is already referred");

        // Record the referrer for the referee.
        referrerOf[_referee] = _referrer;

        // Update referral data.
        referrals[_referrer].totalReferrals++;

        emit ReferralRecorded(_referrer, _referee);
    }

    /**
     * @dev Function to distribute rewards to a referrer based on total referrals.
     * @param _referrer The address of the referrer.
     * @param _rewardAmount The amount of reward to distribute.
     */
    function distributeRewards(address _referrer, uint256 _rewardAmount) external onlyAdmin {
        require(_referrer != address(0), "Referrer cannot be the zero address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Update total rewards for the referrer.
        referrals[_referrer].totalRewards += _rewardAmount;

        emit RewardsDistributed(_referrer, _rewardAmount);

        // Transfer the reward (assumes contract holds sufficient balance).
        (bool sent, ) = _referrer.call{value: _rewardAmount}("");
        require(sent, "Failed to transfer reward");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether from the contract (admin-only).
     * @param _amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 _amount) external onlyAdmin {
        require(_amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient contract balance");

        (bool sent, ) = admin.call{value: _amount}("");
        require(sent, "Failed to withdraw Ether");
    }

    /**
     * @dev Function to get the referral statistics for an address.
     * @param _user The address to query.
     * @return totalReferrals Total referrals made by the user.
     * @return totalRewards Total rewards earned by the user.
     */
    function getReferralStats(address _user) external view returns (uint256 totalReferrals, uint256 totalRewards) {
        totalReferrals = referrals[_user].totalReferrals;
        totalRewards = referrals[_user].totalRewards;
    }
}
```
