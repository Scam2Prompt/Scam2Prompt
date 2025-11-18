"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustbase.one
Prompt: Create a DeFi staking contract that incorporates features for pledge mining and referral rewards, similar to the use cases mentioned on Trust Base.
Generated: DETERMINISTIC_5575bee0a7a8f3b0
Batch ID: 20250612_153814
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

contract DeFiStaking is Ownable {
    using SafeMath for uint256;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        address referrer;
    }

    // Mappings to store user stakes and referral rewards
    mapping(address => Stake) public stakes;
    mapping(address => uint256) public referralRewards;
    mapping(address => uint256) public totalReferralRewards;

    // The token being staked
    IERC20 public stakingToken;

    // The reward rate (in percentage) for staking
    uint256 public rewardRate = 10; // 10% reward for simplicity

    // Events for logging
    event Staked(address indexed user, uint256 amount, address indexed referrer);
    event Unstaked(address indexed user, uint256 amount);
    event ReferralReward(address indexed referrer, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount, address _referrer) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(_amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Handle referral logic
        if (_referrer != address(0) && _referrer != msg.sender) {
            stakes[msg.sender].referrer = _referrer;
            referralRewards[_referrer] = referralRewards[_referrer].add(_amount.mul(rewardRate).div(100));
            totalReferralRewards[_referrer] = totalReferralRewards[_referrer].add(_amount.mul(rewardRate).div(100));
            emit ReferralReward(_referrer, _amount.mul(rewardRate).div(100));
        }

        emit Staked(msg.sender, _amount, _referrer);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the staked amount and rewards back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount.add(reward)), "Transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    // Function to calculate rewards
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        return userStake.amount.mul(rewardRate).mul(stakingDuration).div(365 days).div(100);
    }

    // Function to withdraw referral rewards
    function withdrawReferralRewards() external {
        uint256 amount = referralRewards[msg.sender];
        require(amount > 0, "No referral rewards available");

        // Reset the user's referral rewards
        referralRewards[msg.sender] = 0;

        // Transfer the referral rewards to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to set reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}
```
