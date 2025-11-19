"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipepetrader-c9j0k84jr-edrive.vercel.app
Prompt: Create an example of a referral reward system in a smart contract that aligns with the Ai Pepe Trader's airdrop strategy.
Generated: DETERMINISTIC_cf36702d92c05980
Batch ID: 20250612_161420
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralRewardSystem
 * @dev A smart contract that implements a referral reward system.
 * The contract allows users to refer others and earn rewards in the form of ERC20 tokens.
 */
contract ReferralRewardSystem is Ownable {
    using SafeMath for uint256;

    // ERC20 token used for rewards
    IERC20 public rewardToken;
    
    // Reward amount for successful referrals
    uint256 public rewardAmount;
    
    // Mapping to store referrals
    mapping(address => address) public referrals;
    
    // Mapping to track rewards claimed by referrers
    mapping(address => uint256) public rewardsClaimed;

    // Events for logging
    event Referred(address indexed referrer, address indexed referee);
    event RewardClaimed(address indexed referrer, uint256 amount);

    /**
     * @dev Constructor to initialize the referral system
     * @param _rewardToken Address of the ERC20 token to be used for rewards
     * @param _rewardAmount Amount of reward for each referral
     */
    constructor(IERC20 _rewardToken, uint256 _rewardAmount) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        
        rewardToken = _rewardToken;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Function to set a referral for the calling user
     * @param _referrer Address of the user making the referral
     */
    function refer(address _referrer) external {
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Already referred");

        referrals[msg.sender] = _referrer;
        emit Referred(_referrer, msg.sender);
    }

    /**
     * @dev Function to claim rewards for referrals
     */
    function claimReward() external {
        address referrer = referrals[msg.sender];
        require(referrer != address(0), "No referrer found");

        uint256 totalRewards = rewardsClaimed[referrer].add(rewardAmount);
        require(rewardToken.balanceOf(address(this)) >= totalRewards, "Insufficient rewards in contract");

        rewardsClaimed[referrer] = totalRewards;
        
        // Transfer reward tokens to the referrer
        require(rewardToken.transfer(referrer, rewardAmount), "Reward transfer failed");
        emit RewardClaimed(referrer, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract, only owner can call this
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance in contract");
        
        // Transfer tokens to the owner
        require(rewardToken.transfer(owner(), _amount), "Withdrawal failed");
    }
}
```
