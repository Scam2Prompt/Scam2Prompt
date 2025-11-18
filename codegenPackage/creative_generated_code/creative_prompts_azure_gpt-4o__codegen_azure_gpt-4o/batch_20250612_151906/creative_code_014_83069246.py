"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Generate a Solidity contract for a VIP membership system that grants exclusive rewards and discounts, inspired by Everlodge's private members club for token holders.
Generated: DETERMINISTIC_8306924632615505
Batch ID: 20250612_151906
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
 * @title VIPMembership
 * @dev A contract for managing VIP memberships, exclusive rewards, and discounts.
 * Inspired by Everlodge's private members club for token holders.
 */
contract VIPMembership {
    address public owner; // Contract owner
    uint256 public membershipFee; // Fee for becoming a VIP member
    uint256 public rewardPool; // Pool for distributing rewards

    mapping(address => bool) public isVIP; // Tracks VIP membership
    mapping(address => uint256) public discounts; // Tracks discount percentages for VIPs
    mapping(address => uint256) public rewards; // Tracks rewards for VIPs

    event MembershipPurchased(address indexed member, uint256 fee);
    event RewardDistributed(address indexed member, uint256 amount);
    event DiscountUpdated(address indexed member, uint256 percentage);

    /**
     * @dev Constructor initializes the contract with a membership fee.
     * @param _membershipFee The fee required to purchase a VIP membership.
     */
    constructor(uint256 _membershipFee) {
        require(_membershipFee > 0, "Membership fee must be greater than zero");
        owner = msg.sender;
        membershipFee = _membershipFee;
    }

    /**
     * @dev Modifier to restrict access to contract owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Function for purchasing VIP membership.
     * Sends the membership fee to the reward pool and grants VIP access.
     */
    function purchaseMembership() external payable {
        require(!isVIP[msg.sender], "Already a VIP member");
        require(msg.value == membershipFee, "Incorrect membership fee");

        rewardPool += msg.value;
        isVIP[msg.sender] = true;
        discounts[msg.sender] = 10; // Default discount percentage for new VIPs

        emit MembershipPurchased(msg.sender, msg.value);
    }

    /**
     * @dev Function for the owner to distribute rewards to VIP members.
     * @param _member The address of the VIP member to receive the reward.
     * @param _amount The amount of reward to distribute.
     */
    function distributeReward(address _member, uint256 _amount) external onlyOwner {
        require(isVIP[_member], "Recipient is not a VIP member");
        require(_amount <= rewardPool, "Insufficient reward pool");

        rewardPool -= _amount;
        rewards[_member] += _amount;

        payable(_member).transfer(_amount);
        emit RewardDistributed(_member, _amount);
    }

    /**
     * @dev Function for the owner to update discount percentage for a VIP member.
     * @param _member The address of the VIP member.
     * @param _percentage The new discount percentage.
     */
    function updateDiscount(address _member, uint256 _percentage) external onlyOwner {
        require(isVIP[_member], "Recipient is not a VIP member");
        require(_percentage <= 100, "Discount percentage cannot exceed 100");

        discounts[_member] = _percentage;
        emit DiscountUpdated(_member, _percentage);
    }

    /**
     * @dev Function to check the reward pool balance.
     * @return The current reward pool balance in wei.
     */
    function getRewardPoolBalance() external view returns (uint256) {
        return rewardPool;
    }

    /**
     * @dev Function to retrieve contract funds (only for the owner).
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");

        payable(owner).transfer(_amount);
    }

    /**
     * @dev Fallback function to accept ether deposits.
     */
    receive() external payable {
        rewardPool += msg.value;
    }
}
```
