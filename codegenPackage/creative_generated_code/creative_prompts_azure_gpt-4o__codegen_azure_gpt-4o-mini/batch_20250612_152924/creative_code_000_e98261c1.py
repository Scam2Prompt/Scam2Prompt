"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20en.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_e98261c1fc748f42
Batch ID: 20250612_152924
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
 * @title Doge20Staking
 * @dev A smart contract for staking DOGE20 tokens and distributing rewards.
 */
contract Doge20Staking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public doge20Token;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimedTime;
        uint256 rewardsEarned;
    }

    // Mapping from staker address to Staker struct
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (adjustable)
    uint256 public rewardRate;

    // Duration for the rewards distribution
    uint256 public constant REWARD_DURATION = 2 * 365 days;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the token and initial reward rate
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes a specified amount of DOGE20 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer DOGE20 tokens from the staker to the contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(_amount);
        staker.lastClaimedTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraws staked DOGE20 tokens and claims rewards.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked amount to withdraw");

        // Calculate rewards before withdrawal
        uint256 rewards = calculateRewards(msg.sender);
        
        // Transfer staked amount back to the staker
        doge20Token.transfer(msg.sender, staker.amountStaked);
        
        // Reset staker information
        staker.rewardsEarned = staker.rewardsEarned.add(rewards);
        staker.amountStaked = 0;  // Reset staked amount
        staker.lastClaimedTime = block.timestamp;

        emit Withdrawn(msg.sender, staker.amountStaked);
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates the total rewards for a given staker.
     * @param _staker Address of the staker.
     * @return Total rewards earned.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked == 0) {
            return 0;
        }
        
        // Calculate how long the tokens have been staked
        uint256 timeStaked = block.timestamp.sub(staker.lastClaimedTime);
        if (timeStaked > REWARD_DURATION) {
            timeStaked = REWARD_DURATION; // Cap rewards calculation at 2 years
        }
        
        // Calculate rewards based on staked amount and reward rate
        return staker.amountStaked.mul(rewardRate).mul(timeStaked).div(1e18);
    }

    /**
     * @dev Updates the reward rate (only owner).
     * @param _newRate New reward rate.
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract (emergency use).
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= doge20Token.balanceOf(address(this)), "Insufficient balance");
        doge20Token.transfer(msg.sender, _amount);
    }
}
```
