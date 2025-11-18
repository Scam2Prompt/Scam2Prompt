"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_e98261c1fc748f42
Batch ID: 20250612_152827
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

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardClaimed(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with the DOGE20 token and reward rate.
     * @param _doge20Token The address of the DOGE20 token contract.
     * @param _rewardRate The reward rate per second for staking.
     */
    constructor(address _doge20Token, uint256 _rewardRate) {
        doge20Token = IERC20(_doge20Token);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens.
     * @param amount The amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastClaimedTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        
        require(rewards > 0, "No rewards to claim");
        require(doge20Token.balanceOf(address(this)) >= rewards, "Insufficient contract balance for rewards");

        staker.lastClaimedTime = block.timestamp;
        staker.rewardsEarned = staker.rewardsEarned.add(rewards);

        require(doge20Token.transfer(msg.sender, rewards), "Transfer failed");
        
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows users to unstake their tokens.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens to unstake");

        // First, claim any rewards before unstaking
        claimRewards();

        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0; // Reset staked amount
        totalStaked = totalStaked.sub(amountToUnstake);

        require(doge20Token.transfer(msg.sender, amountToUnstake), "Transfer failed");
        
        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Calculates the rewards for a staker.
     * @param stakerAddress The address of the staker.
     * @return The calculated rewards.
     */
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];

        if (staker.amountStaked == 0) {
            return 0;
        }

        uint256 timeStaked = block.timestamp.sub(staker.lastClaimedTime);
        uint256 rewards = staker.amountStaked.mul(rewardRate).mul(timeStaked).div(1e18);

        return rewards;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens accidentally sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
