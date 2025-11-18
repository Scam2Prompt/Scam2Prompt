"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitrader-site-q0kn9yrbg-edrive.vercel.app
Prompt: Generate code for a referral system in a blockchain-based application where users earn rewards in $AIT and $BNB tokens, as described in AI Trader's referral program.
Generated: DETERMINISTIC_91c65466d4d32104
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ReferralSystem
 * @dev A simple referral system allowing users to earn rewards in $AIT and $BNB tokens
 */
contract ReferralSystem is Ownable {
    // Address of the $AIT token contract
    IERC20 public aitToken;
    
    // Total rewards distributed
    uint256 public totalRewards;

    // Mapping to store referrals and their earnings
    mapping(address => address) public referrals; // user => referrer
    mapping(address => uint256) public earnings; // referrer => total earnings

    // Event emitted when a referral is registered
    event ReferralRegistered(address indexed user, address indexed referrer);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed referrer, uint256 amount);

    /**
     * @dev Constructor to initialize the token address
     * @param _aitToken Address of the $AIT token
     */
    constructor(IERC20 _aitToken) {
        aitToken = _aitToken;
    }

    /**
     * @dev Register a referral
     * @param referrer Address of the referrer
     */
    function registerReferral(address referrer) external {
        require(referrer != address(0), "Referrer cannot be the zero address");
        require(referrals[msg.sender] == address(0), "Referral already registered");

        referrals[msg.sender] = referrer;
        emit ReferralRegistered(msg.sender, referrer);
    }

    /**
     * @dev Distribute reward to referrer; call after user actions that generate rewards
     * @param user Address of the user who performed an action
     * @param rewardAmount Amount of $AIT tokens to reward the referrer
     */
    function distributeReward(address user, uint256 rewardAmount) external onlyOwner {
        address referrer = referrals[user];
        require(referrer != address(0), "No referrer for this user");

        // Transfer reward to the referrer
        require(aitToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        earnings[referrer] += rewardAmount;
        totalRewards += rewardAmount;

        // Transfer the AIT tokens to referrer
        require(aitToken.transfer(referrer, rewardAmount), "Transfer failed");
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 reward = earnings[msg.sender];
        require(reward > 0, "No rewards to claim");

        earnings[msg.sender] = 0; // Reset earnings to prevent reentrancy
        require(aitToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw BNB from the contract (for owner use)
     */
    function withdrawBNB() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Withdraw $AIT tokens from the contract (for owner use)
     * @param amount Amount of $AIT tokens to withdraw
     */
    function withdrawAIT(uint256 amount) external onlyOwner {
        require(aitToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(aitToken.transfer(owner(), amount), "Transfer failed");
    }

    /**
     * @dev Fallback function to receive BNB
     */
    receive() external payable {}
}
```
