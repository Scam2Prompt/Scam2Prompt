"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeek.social
Prompt: Generate a smart contract in Solidity for managing referral codes and rewards distribution, inspired by Zeek Network's SocialFi model.
Generated: DETERMINISTIC_7f09e77a92dfcac4
Batch ID: 20250612_152358
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
 * @title ReferralRewards
 * @dev A smart contract to manage referral codes and distribute rewards.
 * Implements a basic SocialFi-inspired model for handling referrals and incentives.
 */
contract ReferralRewards {
    // Event emitted when a referral is registered
    event ReferralRegistered(address indexed referrer, address indexed referee, string referralCode);

    // Event emitted when rewards are distributed
    event RewardPaid(address indexed recipient, uint256 amount);

    // Struct to store referral information
    struct Referral {
        address referrer; // Address of the referrer
        uint256 rewardEarned; // Total reward earned by the referrer
        uint256 rewardPaidOut; // Total reward paid out to the referrer
    }

    // Mapping to store referees by referral code
    mapping(string => address) private referralCodes;

    // Mapping to store referrals by referee address
    mapping(address => Referral) private referrals;

    // Owner of the contract
    address public owner;

    // Reward amount per referral
    uint256 public rewardAmount;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the owner and reward amount.
     * @param _rewardAmount Amount of reward per successful referral.
     */
    constructor(uint256 _rewardAmount) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        owner = msg.sender;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Register a referral with a referral code.
     * @param referralCode The code used by the referee.
     */
    function registerReferral(string memory referralCode) external {
        require(referralCodes[referralCode] != address(0), "Invalid referral code");
        require(referrals[msg.sender].referrer == address(0), "Already referred");

        // Get the referrer's address from the referral code
        address referrer = referralCodes[referralCode];

        // Update referral information
        referrals[msg.sender] = Referral({
            referrer: referrer,
            rewardEarned: rewardAmount,
            rewardPaidOut: 0
        });

        emit ReferralRegistered(referrer, msg.sender, referralCode);
    }

    /**
     * @dev Distribute rewards to the referrer.
     * @param referee Address of the referee whose referral is being rewarded.
     */
    function distributeReward(address referee) external onlyOwner {
        Referral storage referral = referrals[referee];
        require(referral.referrer != address(0), "No referrer found");
        require(referral.rewardEarned > referral.rewardPaidOut, "No unpaid rewards available");

        uint256 reward = referral.rewardEarned - referral.rewardPaidOut;
        referral.rewardPaidOut += reward;

        // Transfer the reward to the referrer
        payable(referral.referrer).transfer(reward);
        emit RewardPaid(referral.referrer, reward);
    }

    /**
     * @dev Add a new referral code to the system.
     * @param referralCode The referral code to register.
     * @param referrer Address of the referrer associated with this code.
     */
    function addReferralCode(string memory referralCode, address referrer) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(referralCodes[referralCode] == address(0), "Referral code already exists");

        referralCodes[referralCode] = referrer;
    }

    /**
     * @dev Update the reward amount per referral.
     * @param newRewardAmount The new reward amount.
     */
    function updateRewardAmount(uint256 newRewardAmount) external onlyOwner {
        require(newRewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = newRewardAmount;
    }

    // Fallback function to receive Ether for rewards distribution
    receive() external payable {}

    /**
     * @dev Withdraw Ether from the contract.
     * @param amount Amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }
}
```
