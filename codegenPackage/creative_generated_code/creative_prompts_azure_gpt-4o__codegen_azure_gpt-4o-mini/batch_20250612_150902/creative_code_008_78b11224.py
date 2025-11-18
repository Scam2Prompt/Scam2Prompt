"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Explain how to implement vested staking rewards in a cryptocurrency smart contract, similar to MoonBag's 25% vested staking mechanism.
Generated: DETERMINISTIC_78b112244099ed61
Batch ID: 20250612_150902
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title VestedStaking
 * @dev This contract implements a vested staking mechanism for rewards distribution.
 *      Users can stake their tokens and receive vested rewards over a specified duration.
 */
contract VestedStaking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Structure representing a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardPerTokenPaid;
        uint256 rewards;
        uint256 lastUpdateTime;
        uint256 vestingStart;
        uint256 vestingDuration;
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per token staked
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update the rewards for the caller
     */
    modifier updateReward(address account) {
        if (account != address(0)) {
            // Calculate the reward for the account
            Staker storage staker = stakers[account];
            staker.rewards = earned(account);
            staker.rewardPerTokenPaid = rewardPerToken();
            staker.lastUpdateTime = block.timestamp;
        }
        _;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        totalStaked = totalStaked.add(amount);
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.vestingStart = block.timestamp;
        staker.vestingDuration = 30 days; // Example vesting duration

        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked balance");

        totalStaked = totalStaked.sub(amount);
        staker.amountStaked = staker.amountStaked.sub(amount);

        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function getReward() external updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewards;

        require(reward > 0, "No rewards available");

        // Reset rewards after payout
        staker.rewards = 0;

        // Transfer rewards to the staker
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards earned by a user
     * @param account Address of the user
     * @return Reward amount earned by the user
     */
    function earned(address account) public view returns (uint256) {
        Staker storage staker = stakers[account];
        uint256 currentRewardPerToken = rewardPerToken();
        return staker.amountStaked
            .mul(currentRewardPerToken.sub(staker.rewardPerTokenPaid))
            .div(1e18)
            .add(staker.rewards);
    }

    /**
     * @dev Calculate the reward per token staked
     * @return Reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }
        return rewardRate.mul(block.timestamp.sub(stakers[msg.sender].lastUpdateTime)).div(totalStaked);
    }

    /**
     * @dev Function to retrieve staked amount for an address
     * @param account Address of the user
     * @return Staked amount
     */
    function stakedAmount(address account) external view returns (uint256) {
        return stakers[account].amountStaked;
    }
}
```
