"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Write a Solidity contract for managing token rewards and referrals, inspired by the Nyan Heroes platform.
Generated: DETERMINISTIC_e21230011e2b56be
Batch ID: 20250612_151027
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
 * @title TokenRewardsAndReferrals
 * @dev A contract to manage token rewards and referral bonuses.
 */
contract TokenRewardsAndReferrals {
    // State variables
    address public owner; // Owner of the contract
    uint256 public rewardRate; // Reward rate for actions
    uint256 public referralBonus; // Referral bonus for referring others

    mapping(address => uint256) public balances; // Mapping to track user balances
    mapping(address => address) public referrals; // Mapping to track who referred whom

    // Events
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralAdded(address indexed referrer, address indexed referee);
    event RewardsTransferred(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner.");
        _;
    }

    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardRate The base reward rate for actions.
     * @param _referralBonus The bonus for successful referrals.
     */
    constructor(uint256 _rewardRate, uint256 _referralBonus) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        referralBonus = _referralBonus;
    }

    /**
     * @dev Function to set reward rate. Only owner can call this.
     * @param _rewardRate The new reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to set referral bonus. Only owner can call this.
     * @param _referralBonus The new referral bonus.
     */
    function setReferralBonus(uint256 _referralBonus) external onlyOwner {
        referralBonus = _referralBonus;
    }

    /**
     * @dev Function to add a referral relationship.
     * @param referee The address of the referee.
     * @param referrer The address of the referrer.
     */
    function addReferral(address referee, address referrer)
        external
        validAddress(referee)
        validAddress(referrer)
    {
        require(referrals[referee] == address(0), "Referral already exists.");
        require(referee != referrer, "Referee and referrer cannot be the same.");
        
        referrals[referee] = referrer;
        emit ReferralAdded(referrer, referee);

        // Add referral bonus for the referrer
        balances[referrer] += referralBonus;
    }

    /**
     * @dev Function to claim rewards for a user.
     */
    function claimReward() external {
        uint256 reward = rewardRate;
        require(reward > 0, "Reward rate is zero.");

        balances[msg.sender] += reward;
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to transfer rewards to an external account.
     * @param to The address to transfer rewards to.
     * @param amount The amount to transfer.
     */
    function transferRewards(address to, uint256 amount) external validAddress(to) {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit RewardsTransferred(to, amount);
    }

    /**
     * @dev Function to view balance of an account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
