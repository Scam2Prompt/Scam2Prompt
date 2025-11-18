"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase1bdag.pages.dev
Prompt: Write a smart contract in Solidity that automates the referral bonus system for BDAG presale, ensuring accurate tracking and distribution of rewards.
Generated: DETERMINISTIC_321e197ac96f14e8
Batch ID: 20250612_152249
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
 * @title BDAGPresaleReferral
 * @dev Smart contract to automate referral bonus system for BDAG presale.
 */
contract BDAGPresaleReferral {
    // Struct to store referral information
    struct Referral {
        uint256 totalReferrals; // Total successful referrals
        uint256 totalReward;    // Total rewards earned by the referrer
    }

    // Mapping to store referral data (referrer -> Referral details)
    mapping(address => Referral) public referrals;

    // Mapping to track if an address has been referred
    mapping(address => bool) public hasBeenReferred;

    // Owner address
    address public owner;

    // Reward per successful referral (adjustable by owner)
    uint256 public referralReward;

    // Event emitted when a referral bonus is distributed
    event ReferralBonusDistributed(address indexed referrer, address indexed referee, uint256 reward);

    // Event emitted when the reward amount is updated
    event RewardUpdated(uint256 oldReward, uint256 newReward);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor to initialize owner and referral reward.
     * @param _referralReward Initial reward per successful referral.
     */
    constructor(uint256 _referralReward) {
        require(_referralReward > 0, "Reward must be greater than zero");
        owner = msg.sender;
        referralReward = _referralReward;
    }

    /**
     * @dev Function to handle a successful referral.
     * @param referrer Address of the referrer.
     * @param referee Address of the referee.
     */
    function handleReferral(address referrer, address referee) external {
        require(referrer != address(0), "Invalid referrer address");
        require(referee != address(0), "Invalid referee address");
        require(referrer != referee, "Referrer and referee cannot be the same");
        require(!hasBeenReferred[referee], "Referee has already been referred");

        // Mark the referee as referred
        hasBeenReferred[referee] = true;

        // Update referral data for the referrer
        referrals[referrer].totalReferrals += 1;
        referrals[referrer].totalReward += referralReward;

        // Emit event for referral bonus distribution
        emit ReferralBonusDistributed(referrer, referee, referralReward);
    }

    /**
     * @dev Function to update the reward per referral.
     * @param _newReward New reward amount per referral.
     */
    function updateReferralReward(uint256 _newReward) external onlyOwner {
        require(_newReward > 0, "Reward must be greater than zero");
        uint256 oldReward = referralReward;
        referralReward = _newReward;

        // Emit event for reward update
        emit RewardUpdated(oldReward, _newReward);
    }

    /**
     * @dev Function to retrieve referral details for a referrer.
     * @param referrer Address of the referrer.
     * @return totalReferrals Total successful referrals.
     * @return totalReward Total rewards earned by the referrer.
     */
    function getReferralDetails(address referrer) external view returns (uint256 totalReferrals, uint256 totalReward) {
        Referral memory ref = referrals[referrer];
        return (ref.totalReferrals, ref.totalReward);
    }

    /**
     * @dev Function to withdraw contract funds (if applicable).
     * Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the entire contract balance to the owner
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to accept ETH (if applicable).
     */
    receive() external payable {
        // Accept ETH payments for potential presale purchases
    }
}
```
