"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Write a Solidity contract for a staking pool that contributes 2% of every transaction to rewards, as outlined in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_024fd9486c627b91
Batch ID: 20250612_152235
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
 * @title StakingPool
 * @dev A staking pool contract that distributes 2% of every transaction as rewards
 */
contract StakingPool is Ownable {
    IERC20 public stakingToken; // The ERC20 token being staked
    uint256 public rewardPool; // Total rewards available for distribution
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor that sets the staking token address
     * @param _stakingToken Address of the ERC20 token to be used for staking
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens in the pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero");
        
        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;

        // Distribute rewards from the transaction
        uint256 rewardsAmount = (amount * 2) / 100; // 2% of the staked amount
        rewardPool += rewardsAmount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the pool
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to the caller based on their staked amount
     */
    function claimRewards() external {
        uint256 userRewards = stakedAmount[msg.sender] * rewardPool / totalStaked(); // Calculate user rewards

        require(userRewards > 0, "No rewards available");

        // Reset user's rewards after claiming
        rewards[msg.sender] += userRewards;
        rewardPool -= userRewards;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, userRewards);

        emit RewardDistributed(msg.sender, userRewards);
    }

    /**
     * @dev Get total amount of tokens staked in the pool
     * @return Total staked amount
     */
    function totalStaked() public view returns (uint256 total) {
        for (uint256 i = 0; i < stakers.length; i++) {
            total += stakedAmount[stakers[i]];
        }
    }

    // Array to keep track of stakers
    address[] private stakers;

    /**
     * @dev Add a staker to the list (if they aren't already in it)
     * @param staker Address of the staker to add
     */
    function _addStaker(address staker) internal {
        if (stakedAmount[staker] == 0) {
            stakers.push(staker);
        }
    }

    /**
     * @dev Get the total rewards available in the pool
     * @return Total rewards in the pool
     */
    function totalRewards() external view returns (uint256) {
        return rewardPool;
    }
}
```
